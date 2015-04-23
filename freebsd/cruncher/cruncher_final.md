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


# mdadm

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

