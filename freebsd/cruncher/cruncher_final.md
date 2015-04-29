# Introduction

The box runs **SuSE Linux Enterprise Server 12** - see [here](https://www.suse.com/documentation/sles-12/) for documentation.

# Todo

* [x] Anlegen von Unix Nutzern
* [ ] Performance Optimierung auf XFS Ebene
* [ ] Aufsetzen PostgreSQL, R, PL/R, MADlib
* [ ] Transferieren der Basistabellen
* [ ] Entwicklung Workload Scheduler
* [ ] Performance Optimierung auf DB Ebene
* [ ] erste Queries mit Produktivdaten
* [ ] Prüfung tragfähiger Ansätze
* [ ] Anlegen aller Nutzern

# Storage Testing

FIO result parser in Python

Test schedule defined in Python:

- vary IO engine between aio and sync
- vary IO queue depth
- vary number of workers (threads)
- vary between sequential and random IO
- vary between 4kB, 8kB and 128kB block size

Spawn FIO executable with parameters set

Receive and parse FIO result output in Python

Save results and generate plots


- hardware block device
- XFS on hardware block device
- mdadm on hardware block device
- XFS on mdadm software block device

- 1
- 2, 4, 8 disks as RAID-0
- 2, 4, 8 disks as RAID-10


# Storage Layout

## Run one database cluster

The reason is to make optimal use of the large amount of RAM. When running multiple PostgreSQL database clusters, the available physical RAM needs to be split up and dedicated to the individual PostgreSQL database clusters.

## Run one (main) database

The reason is that - different from other DBMSs - PostgreSQL requires the use of usual database link mechanisms to cross databases even when those reside in the same PostgreSQL database cluster.

## Use schemas to organize the data-warehouse

As an organizational tool, PostgreSQL database schemes are used for:

* different layers within the DWH
* user scratch areas

Other categories might be added.

## Use tablespaces to expose storage hardware

The three storage subsystems of the hardware have different characteristics regarding performance and reliability.

We expose all three storage subsystem at the application level via PostgreSQL tablespaces.

The tablespaces are:

* standard
* fast
* archive

The *standard* tablespace runs on top of a RAID-10 mdadm software RAID over 10 Intel DC S3700 SAS SSDs with 800GB capacity each. The tablespace has a usable capacity of **4TB**.

The *fast* tablespace runs on top of a RAID-0 mdadm software RAID over 8 Intel P3700 NVMe SSDs with 2TB capacity each. This tablespace has a usable capacity of **16TB**.

The *archive* tablespace runs on top of a RAID-6 mdadm software RAID over 6 Seagate Constellation ES.3 disks and LVM managed volumes over 4 sets of disks. This tablespace has a usable capacity of 4 x 4 x 6TB = **96TB** minus use for other purposes (flat-files, backups, ..).

## Alternative Tablespace Design

Have each NVMe exposed as a single XFS filesystem to hold *fast* tablespaces *fast0* - *fast7*.

Put table partitions over *fast0* - *fast7* in a round-robin fashion.

# System Tuning

Kernel tuning for PostgreSQL is decribed [here](http://www.postgresql.org/docs/9.4/static/kernel-resources.html).

Some useful information might also be found in tuning guides for Oracle on Linux: see [here](http://www.puschitz.com/TuningLinuxForOracle.shtml), [here](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Tuning_and_Optimizing_Red_Hat_Enterprise_Linux_for_Oracle_9i_and_10g_Databases/chap-Oracle_9i_and_10g_Tuning_Guide-Setting_Shared_Memory.html) and [here](http://www.puschitz.com/TuningLinuxForOracle.shtml).

## Maximum number of open FDs

Add the following to the end of `/etc/sysctl.conf` and do `sysctl -p`:

```
fs.file-max = 16777216
fs.pipe-max-size = 134217728
```

Modify `/etc/security/limits.conf` for the following

```
# wildcard does not work for root, but for all other users
*               soft     nofile           1048576
*               hard     nofile           1048576
# settings should also apply to root
root            soft     nofile           1048576
root            hard     nofile           1048576
```

and add the following line

```
session required pam_limits.so
```

to both of these files at the end:

```
/etc/pam.d/common-session
/etc/pam.d/common-session-noninteractive
```

You [have to re-login](http://unix.stackexchange.com/a/108605/52500) for the PAM limits to take effect. Check that you actually got large (1048576) FD limit:

```
ulimit -n
```

## AIO

Add the following to the end of `/etc/sysctl.conf` and do `sysctl -p`:

```
# maximum I/O size for asynchronous I/Os
#fs.aio-max-size = 1048576

# maximum number of allowable concurrent requests
fs.aio-max-nr = 1048576
```

## SysV IPC

To list the current limits:

```console
bvr-sql18:~ # ipcs -l

------ Nachrichtenbeschränkungen --------
maximale systemweite Warteschlangen = 32768
maximale Größe der Nachricht (Bytes) = 65536
normale maximale Größe der Warteschlange (Bytes) = 65536

------ Gemeinsamer Speicher: Grenzen --------
Maximale Anzahl an Segmenten = 4096
Maximale Segmentgröße (KBytes) = 18014398509481983
Maximaler gesamter gemeinsamer Speicher (KBytes) = 18014398509480960
minimale Segmentgröße (Bytes) = 1

------ Semaphorengrenzen --------
maximale Anzahl von Feldern = 1024
maximale Semaphoren pro Feld = 250
maximale systemweite Semaphoren = 256000
maximale Operationen pro Semaphorenaufruf = 32
maximaler Semaphorenwert = 32767
```

## IO Scheduler

The recommended IO schedulers for database workloads is `deadline` for fast devices (normal SSDs) and `noop` for very fast devices with deep IO queues (NVMe disks). For slow magnetic disks, the `cfq` scheduler should work fine.

Check current settings on block devices (`/dev/sdm` is a magnetic disk, `/dev/sdb` is a fast SSD, and `/dev/nvme01n1` is a very fast NVMe SSD):

```console
bvr-sql18:~ # cat /sys/block/sdm/queue/scheduler
noop deadline [cfq] 
bvr-sql18:~ # cat /sys/block/sdb/queue/scheduler
noop [deadline] cfq 
bvr-sql18:~ # cat /sys/block/nvme0n1/queue/scheduler
none
bvr-sql18:~ # cat /sys/block/md100/queue/scheduler
none
```

**As can be seen, SLES 12 has automatically set the best IO scheduler depending on device type`.

To check which disks were automatically detected as slow, magnetic, rotational disks by the kernel:

```console
bvr-sql18:~ # grep . /sys/block/sd?/queue/rotational
/sys/block/sda/queue/rotational:0
/sys/block/sdb/queue/rotational:0
/sys/block/sdc/queue/rotational:0
/sys/block/sdd/queue/rotational:0
/sys/block/sde/queue/rotational:0
/sys/block/sdf/queue/rotational:0
/sys/block/sdg/queue/rotational:0
/sys/block/sdh/queue/rotational:0
/sys/block/sdi/queue/rotational:0
/sys/block/sdj/queue/rotational:0
/sys/block/sdk/queue/rotational:0
/sys/block/sdl/queue/rotational:0
/sys/block/sdm/queue/rotational:1
/sys/block/sdn/queue/rotational:1
/sys/block/sdo/queue/rotational:1
/sys/block/sdp/queue/rotational:1
/sys/block/sdq/queue/rotational:1
/sys/block/sdr/queue/rotational:1
/sys/block/sds/queue/rotational:1
/sys/block/sdt/queue/rotational:1
/sys/block/sdu/queue/rotational:1
/sys/block/sdv/queue/rotational:1
/sys/block/sdw/queue/rotational:1
/sys/block/sdx/queue/rotational:1
/sys/block/sdy/queue/rotational:1
/sys/block/sdz/queue/rotational:1
```

## Network

Add the following to the end of `/etc/sysctl.conf` and do `sysctl -p`:

```
net.core.somaxconn = 8192
net.ipv4.tcp_max_orphans = 8192
net.ipv4.tcp_max_syn_backlog = 8192
net.core.netdev_max_backlog = 262144
net.ipv4.ip_local_port_range = 1024 65535
```


# SSH

## Reverse SSH Tunnel

### SSH

On `bvr-sql18`, execute the following to establish the reverse SSH tunnel to `jumper.tavendo.de`:

```console
sudo ssh -fN -R 2222:localhost:22 ec2-user@jumper.tavendo.de
```

Note that above command will properly daemonize the SSH tunnel.

You now can login via the jump host:

```console
ssh -t ec2-user@jumper.tavendo.de "ssh -p 2222 oberstet@localhost"
```

### PostgreSQL

On **Test PC**, execute the following:

```console
ssh -fN -R 5432:localhost:5432 ec2-user@jumper.tavendo.de
```

On **Jumper**, check if the tunnel is listening there:

```console
[ec2-user@ip-172-31-11-121 ~]$ sudo netstat -plnt | grep ':5432'
tcp        0      0 127.0.0.1:5432              0.0.0.0:*                   LISTEN      1966/sshd           
tcp        0      0 ::1:5432                    :::*                        LISTEN      1966/sshd           
```

On **Your PC**, establish a 2nd (forward) tunnel:

```console
ssh -fN -L 5432:localhost:5432 ec2-user@jumper.tavendo.de
```

You now can connect to PostgreSQL on the **Test PC** from **Your PC** by connecting to `localhost:5432`.

> If you have a locally running PostgreSQL already listening on port 5432, you can bind to a different local port like this: ```ssh -fN -L 5434:localhost:5432 ec2-user@jumper.tavendo.de```. This will bind to local port **5434**.


## SSHFS

To mount a remote directory over SSH:

```console
sudo mkdir /mnt/bvr
sudo sshfs -o allow_other -o IdentityFile=~/.ssh/id_rsa \
   ec2-user@jumper.tavendo.de:/home/ec2-user /mnt/bvr
```

To unmount

```console
sudo fusermount -u /mnt/bvr
```

## SSHFS over reverse tunnel

To mount a directory over SSHFS via an intermediary jump host, first establish a (forward) SSH tunnel:

```console
ssh -fN -L 2222:localhost:2222 ec2-user@jumper.tavendo.de
```

and then mount

```console
sudo sshfs -o allow_other -o IdentityFile=~/.ssh/id_rsa \
   -p 2222 oberstet@localhost:/home/oberstet /mnt/bvr
```

# Zypper

## Listing installed packages

```console
zypper search -i
```

or

```console
rpm -qa
```

## Listing repositories

```console
zypper lr -u
```

## Searching for packages

```console
zypper se postgres
```

## Adding a repository

```console
zypper ar http://download.opensuse.org/repositories/server:/database:/postgresql/SLE_12/ opensuse:server:database:postgresql
zypper ref
```

https://en.opensuse.org/images/1/17/Zypper-cheat-sheet-1.pdf
https://en.opensuse.org/images/3/30/Zypper-cheat-sheet-2.pdf


# Storage Performance

The following storage configurations are tested both at **block device** level and at **filesystem level** (XFS and ext4).

- single DC S3700
- 2/4/8 x DC S3700 under mdadm RAID-0
- 2/4/8 x DC S3700 under mdadm RAID-10
- single P3700
- 2/4/8 x P3700 under mdadm RAID-0
- 2/4/8 x P3700 under mdadm RAID-10

# Disks

Listing disks

```console
fdisk -l
```

or

```console
lsblk -io KNAME,TYPE,SIZE,MODEL | grep ST6000
```

Erasing a partition table:

```console
dd if=/dev/zero of=/dev/sdg bs=512 count=1 conv=notrunc
```

# mdadm

Documentation:

* [mdadm man page](http://linux.die.net/man/8/mdadm)
* [mdadm Wiki](https://raid.wiki.kernel.org/index.php/RAID_setup)

## Creating an array

Create a RAID-0 over all NVMe SSDs:

```console
mdadm --create /dev/md0 --chunk=256 --level=0 --raid-devices=8 \
   /dev/nvme0n1 \
   /dev/nvme1n1 \
   /dev/nvme2n1 \
   /dev/nvme3n1 \
   /dev/nvme4n1 \
   /dev/nvme5n1 \
   /dev/nvme6n1 \
   /dev/nvme7n1
```

## Get array information

Listing mdadm arrays:

```console
bvr-sql18:~ # cat /proc/mdstat
Personalities : [raid1] [raid0]
md0 : active raid0 nvme7n1[7] nvme6n1[6] nvme5n1[5] nvme4n1[4] nvme3n1[3] nvme2n1[2] nvme1n1[1] nvme0n1[0]
      15627067392 blocks super 1.2 256k chunks

md125 : active raid1 sda3[0] sdd3[1]
      759385920 blocks super 1.0 [2/2] [UU]
      bitmap: 0/6 pages [0KB], 65536KB chunk

md126 : active raid1 sdd1[1] sda1[0]
      1051584 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

md127 : active raid1 sda2[0] sdd2[1]
      20972416 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

unused devices: <none>
```

Getting details of an array:

```console
bvr-sql18:~ # mdadm --detail /dev/md0
/dev/md0:
        Version : 1.2
  Creation Time : Thu Apr 16 19:31:34 2015
     Raid Level : raid0
     Array Size : 15627067392 (14903.13 GiB 16002.12 GB)
   Raid Devices : 8
  Total Devices : 8
    Persistence : Superblock is persistent

    Update Time : Thu Apr 16 19:31:34 2015
          State : clean
 Active Devices : 8
Working Devices : 8
 Failed Devices : 0
  Spare Devices : 0

     Chunk Size : 256K

           Name : bvr-sql18:0  (local to host bvr-sql18)
           UUID : 7280eb72:929d263f:4604a091:3fe38c91
         Events : 0

    Number   Major   Minor   RaidDevice State
       0     259        0        0      active sync   /dev/nvme0n1
       1     259        1        1      active sync   /dev/nvme1n1
       2     259        2        2      active sync   /dev/nvme2n1
       3     259        3        3      active sync   /dev/nvme3n1
       4     259        4        4      active sync   /dev/nvme4n1
       5     259        5        5      active sync   /dev/nvme5n1
       6     259        6        6      active sync   /dev/nvme6n1
       7     259        7        7      active sync   /dev/nvme7n1
```



## Destroying an array

Destroy the array:

```console
mdadm --stop /dev/md0
mdadm --remove /dev/md0
mdadm --zero-superblock /dev/nvme0n1
mdadm --zero-superblock /dev/nvme1n1
mdadm --zero-superblock /dev/nvme2n1
mdadm --zero-superblock /dev/nvme3n1
mdadm --zero-superblock /dev/nvme4n1
mdadm --zero-superblock /dev/nvme5n1
mdadm --zero-superblock /dev/nvme6n1
mdadm --zero-superblock /dev/nvme7n1
```

Pointers:

* [mdadm cheatsheet](http://www.ducea.com/2009/03/08/mdadm-cheat-sheet/
)

# XFS

/dev/md0 on /data1 type xfs (rw,noatime,attr2,inode64,logbsize=256k,sunit=512,swidth=4096,noquota)

# Git

Configure Git (obviously, adjust for your name and email):

```console
git config --global user.name "Tobias Oberstein"
git config --global user.email "tobias.oberstein@tavendo.de"
git config --global push.default simple
git config --global --bool pull.rebase true
```

To clone the BVR Git repository in your Unix home:

```console
oberstet@bvr-sql18:~/scm> git clone http://bvr-git10.bvr-ext.de/Bonobo.Git.Server/RA.git bvr
Klone nach 'bvr'...
Username for 'http://bvr-git10.bvr-ext.de': re_oberstein
Password for 'http://re_oberstein@bvr-git10.bvr-ext.de': 
remote: Counting objects: 26783, done.

remote: Compressing objects: 100% (24065/24065), done.
remote: Total 26783 (delta 17054), reused 2836 (delta 1762)
Empfange Objekte: 100% (26783/26783), 22.93 MiB | 2.73 MiB/s, Fertig.
Löse Unterschiede auf: 100% (17054/17054), Fertig.
Prüfe Konnektivität... Fertig.
oberstet@bvr-sql18:~/scm> 
oberstet@bvr-sql18:~/scm> cd bvr/
oberstet@bvr-sql18:~/scm/bvr> git status
Auf Branch master
Ihr Branch ist auf dem selben Stand wie 'origin/master'.
nichts zu committen, Arbeitsverzeichnis unverändert
oberstet@bvr-sql18:~/scm/bvr> git remote -v
origin	http://bvr-git10.bvr-ext.de/Bonobo.Git.Server/RA.git (fetch)
origin	http://bvr-git10.bvr-ext.de/Bonobo.Git.Server/RA.git (push)
oberstet@bvr-sql18:~/scm/bvr> 
```

After this, change into the repository and run:

```console
git config credential.helper store
```

This way Git will remember your login and password. The password is saved in `$HOME/.git-credentials`. Make sure this file is properly protected with permissions:

```console
oberstet@bvr-sql18:~/scm/bvr/user/oberstet> ls -la ~/.git*
-rw-r--r-- 1 oberstet users 116 21. Apr 12:31 /home/oberstet/.gitconfig
-rw------- 1 oberstet users 120 21. Apr 16:11 /home/oberstet/.git-credentials
```


# Network Statistics

There are lots of options to get network bandwidth statistics. One of them is using [iftop](http://www.ex-parrot.com/pdw/iftop/). To install:

```console
zypper install iftop
```

And then run `iftop`.


# Actual Storage Setup

Two of the internal SSD disks are holding a RAID-1 mdadm mirror for boot and system:

```console
bvr-sql18:~ # fdisk -l /dev/sda

Disk /dev/sda: 745.2 GiB, 800166076416 bytes, 1562824368 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x000642b3

Device     Boot    Start        End    Sectors   Size Id Type
/dev/sda1  *        2048    2105343    2103296     1G fd Linux raid autodetect
/dev/sda2        2105344   44050431   41945088    20G fd Linux raid autodetect
/dev/sda3       44050432 1562822655 1518772224 724.2G fd Linux raid autodetect

bvr-sql18:~ # fdisk -l /dev/sdd

Disk /dev/sdd: 745.2 GiB, 800166076416 bytes, 1562824368 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x000df23b

Device     Boot    Start        End    Sectors   Size Id Type
/dev/sdd1  *        2048    2105343    2103296     1G fd Linux raid autodetect
/dev/sdd2        2105344   44050431   41945088    20G fd Linux raid autodetect
/dev/sdd3       44050432 1562822655 1518772224 724.2G fd Linux raid autodetect
```

Here are the md arrays over the partitions:

```console
bvr-sql18:~ # mdadm --detail /dev/md125
/dev/md125:
        Version : 1.0
  Creation Time : Wed Apr  8 10:34:59 2015
     Raid Level : raid1
     Array Size : 759385920 (724.21 GiB 777.61 GB)
  Used Dev Size : 759385920 (724.21 GiB 777.61 GB)
   Raid Devices : 2
  Total Devices : 2
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Thu Apr 23 11:38:29 2015
          State : active
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
  Spare Devices : 0

           Name : any:root
           UUID : 67221fe1:b542bd90:5f716fd9:f80f8014
         Events : 600

    Number   Major   Minor   RaidDevice State
       0       8        3        0      active sync   /dev/sda3
       1       8       51        1      active sync   /dev/sdd3
bvr-sql18:~ # mdadm --detail /dev/md126
/dev/md126:
        Version : 1.0
  Creation Time : Wed Apr  8 10:34:58 2015
     Raid Level : raid1
     Array Size : 1051584 (1027.11 MiB 1076.82 MB)
  Used Dev Size : 1051584 (1027.11 MiB 1076.82 MB)
   Raid Devices : 2
  Total Devices : 2
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Tue Apr 21 16:53:27 2015
          State : active
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
  Spare Devices : 0

           Name : any:boot
           UUID : abd31c3e:314d868e:a76a42b2:6025b230
         Events : 50

    Number   Major   Minor   RaidDevice State
       0       8        1        0      active sync   /dev/sda1
       1       8       49        1      active sync   /dev/sdd1
bvr-sql18:~ # mdadm --detail /dev/md127
/dev/md127:
        Version : 1.0
  Creation Time : Wed Apr  8 10:34:59 2015
     Raid Level : raid1
     Array Size : 20972416 (20.00 GiB 21.48 GB)
  Used Dev Size : 20972416 (20.00 GiB 21.48 GB)
   Raid Devices : 2
  Total Devices : 2
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Thu Apr 16 14:43:56 2015
          State : active
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
  Spare Devices : 0

           Name : any:swap
           UUID : e726ac5a:34f5c549:534b092c:91913311
         Events : 27

    Number   Major   Minor   RaidDevice State
       0       8        2        0      active sync   /dev/sda2
       1       8       50        1      active sync   /dev/sdd2
```

# Install Proxy Certificate

Auf Notebook:

```console
cat Schreibtisch/BVR/BVRGateway.cer
openssl x509 -in Schreibtisch/BVR/BVRGateway.cer -text -noout
scp Schreibtisch/BVR/BVRGateway.cer ec2-user@jumper.tavendo.de:/home/ec2-user
```

Auf Jumper:

```console
scp -P 2222 BVRGateway.cer root@localhost:/root
```

Auf SQL18:

```console
cp BVRGateway.cer /etc/pki/trust/anchors/
/usr/sbin/update-ca-certificates
```

Test:

```console
wget https://pypi.python.org
```

Links:

* https://blog.hqcodeshop.fi/archives/157-Installing-own-CA-root-certificate-into-openSUSE.html


# Python

Install prerequisites:

```console
zypper in python-devel libopenssl-devel libbz2-devel readline-devel sqlite3-devel ncurses-devel
```

Build:

```console
CPPFLAGS="-I/usr/include/ncurses/" ./configure --prefix=/opt/python2
CPPFLAGS="-I/usr/include/ncurses/" make
sudo make install
```

Pip:

```console
wget https://bootstrap.pypa.io/get-pip.py
sudo /opt/python2/bin/python get-pip.py
```

Test:

```console
sudo /opt/python2/bin/pip install glances
```

# Install SLES12 SDK

`sudo yast` and:

* => Software => Software Repositories
* => Select "Add", then "Extensions and Modules from Registration Server ..."
* => Choose "SUSE Linux Enterprise Software Development Kit 12 x86_6"

Walk through the rest of the dialogs.


# PostgreSQL Tuning

```
shared_buffers = 512MB
work_mem = 64MB
maintenance_work_mem = 1024MB
full_page_writes = off
wal_buffers = 16MB
checkpoint_segments = 64
checkpoint_completion_target = 0.9
random_page_cost = 2.0
cpu_tuple_cost = 0.05                   
autovacuum_vacuum_scale_factor = 0.05
autovacuum_analyze_scale_factor = 0.2
```



* http://www.cybertec.at/bypassing-the-transaction-log/
* http://www.cybertec.at/pg_resetxlog-when-hope-depends-on-luck/

# Sortme



>>>>>>> cbd6a0e478e50ec7612847c8c916c7fe640bb8fd
>>>>>> r http://download.opensuse.org/repositories/benchmark/SLE_12/ opensuse:benchmark
zypper ar http://download.opensuse.org/repositories/server:/monitoring/SLE_12/ opensuse:server:monitoring
zypper ar http://download.opensuse.org/repositories/devel:/tools/SLE_12/ opensuse:devel:tools
zypper ar http://download.opensuse.org/repositories/devel:/tools:/scm/SLE_12/ opensuse:devel:tools:scm
zypper ref


bvr-sql18:~ # ln -svf /usr/lib/systemd/system/multi-user.target /usr/lib/systemd/system/default.target
‘/usr/lib/systemd/system/default.target’ -> ‘/usr/lib/systemd/system/multi-user.target’
bvr-sql18:~ # ll /usr/lib/systemd/system/default.target
lrwxrwxrwx 1 root root 41 Apr 16 16:11 /usr/lib/systemd/system/default.target -> /usr/lib/systemd/system/multi-user.target

bvr-sql18:~ # init 3
bvr-sql18:~ # ps -Af | grep X


mdadm --create /dev/md0 --chunk=256 --level=0 --raid-devices=4 /dev/nvme0n1 /dev/nvme1n1 /dev/nvme2n1 /dev/nvme3n1

mdadm --detail /dev/md0

 





http://linux.die.net/man/8/mkfs.xfs
https://erikugel.wordpress.com/2010/04/11/setting-up-linux-with-raid-faster-slackware-with-mdadm-and-xfs/
https://www.mythtv.org/wiki/Optimizing_Performance#Optimizing_XFS_on_RAID_Arrays


mkfs.xfs -d sunit=512,swidth=4096 /dev/md0


mount -o noatime,nodiratime,logbufs=8


mount -o remount,sunit=512,swidth=3072

/bin/mount -t xfs -o noatime /dev/md0 /mnt





bvr-sql18:/home/oberstet # zypper search -iv | grep "opensuse:"
i | fio                                  | package     | 2.2.6-34.1                   | x86_64 | opensuse:benchmark
i | git                                  | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | git-core                             | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | git-email                            | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | git-gui                              | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | git-web                              | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | gitk                                 | package     | 2.3.5-241.2                  | x86_64 | opensuse:devel:tools:scm
i | htop                                 | package     | 1.0.3-1.1                    | x86_64 | opensuse:server:monitoring
i | perl-Net-SMTP-SSL                    | package     | 1.02-27.1                    | noarch | opensuse:devel:tools:scm



---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20150417 BVR-SQL18"
AAAAB3NzaC1yc2EAAAABJQAAAQEAi989X/st3U2eOsKa7KkpgeQQeHuWklYfPZPr
zTtGl9rSKMXQZ8LnEjjM7Jb2wD5X/qjCRJH1V8UHiYTAAB140aolAcJaVRCGN3P1
YCo5uDEpr2aktr9g5wePFtrJrISw+g49y8bSLDP00nDjNLHkPw1BskGEBH0jTyKn
wkB+r3vcWPzCFU3w4/Bhf39DIuKvpXQc9HfotscQ0GnHrAqwyW3vgiefgtN8qcQF
7O6ZWfCxlVvnUpKNRkBuDglT3C+9vzxp8n0m8Q7OdMzOCs1bgBQE+NEaUil7bb70
YERamugq34TGsqwd1bwxoXbywLTpoLJvCbyRFvK88HNwpPEcqw==
---- END SSH2 PUBLIC KEY ----


bvr-sql18:~ # mkfs.xfs -d sunit=512,swidth=4096 /dev/md0
meta-data=/dev/md0               isize=256    agcount=32, agsize=122086464 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=0        finobt=0
data     =                       bsize=4096   blocks=3906766848, imaxpct=5
         =                       sunit=64     swidth=512 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=0
log      =internal log           bsize=4096   blocks=521728, version=2
         =                       sectsz=512   sunit=64 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0

