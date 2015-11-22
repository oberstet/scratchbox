# Cruncher / Ubuntu

## Samba

Install stuff:

```
sudo apt-get install samba
sudo apt-get install smbclient
```

Edit smbd config (only the delta to default is shown):

```
sudo vim /etc/samba/smb.conf
```

with

```
[global]
   workgroup = PARCIT
   security = user

[incoming]
   comment = ADR Incoming
   path = /files/rawdata/incoming
   browsable = yes
   guest ok = yes
   read only = no
   create mask = 0755
```

Adjust owner:

```
sudo chown -R nobody:nogroup /files/rawdata/incoming/
```

Restart smbd

```
sudo service smbd restart
```

List exported shares:

```
smbclient -L localhost
```

* https://help.ubuntu.com/lts/serverguide/samba-fileserver.html
* https://help.ubuntu.com/community/Samba/SambaServerGuide
* https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!

## Multi-queue Block Device Layer

* https://www.thomas-krenn.com/en/wiki/Linux_Multi-Queue_Block_IO_Queueing_Mechanism_%28blk-mq%29
* http://bjorling.me/blkmq-slides.pdf
* https://lwn.net/Articles/552904/
* http://kernel.dk/systor13-final18.pdf
* http://www.phoronix.com/scan.php?page=news_item&px=MTUxNDQ
* http://www.phoronix.com/scan.php?page=news_item&px=linux-4.1-block-core-blk-mq
* http://ubuntuhandbook.org/index.php/2015/06/upgrade-kernel-4-1-ubuntu-linux-mint/
* http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.1-unstable/

## Kernel Versions

* RHEL 7.1            => Linux kernel 3.10.0-229
* SLES 12             => Linux kernel 3.12.39-47.1
* Ubuntu 14.04.2 LTS  => Linux kernel 3.16
* **Ubuntu 15.04        => Linux kernel 3.19.3**
* Ubuntu 15.10        => October 2015 (Linux kernel 4.1.x)
* Ubuntu 16.04 LTS    => April 2016

## Null Block Device

* [Null Block Device](https://www.kernel.org/doc/Documentation/block/null_blk.txt)
* `/dev/nullb0`
* `/sys/block/nullb0/...`

## IPMI

### Installation

To install

```
sudo apt-get install -y ipmitool
```

and add the following to `/etc/modules`

```
ipmi_devintf
ipmi_msghandler
ipmi_poweroff
ipmi_si
ipmi_watchdog
```

To manually load the kernel modules

```
sudo modprobe ipmi_devintf
sudo modprobe ipmi_msghandler
sudo modprobe ipmi_poweroff
sudo modprobe ipmi_si
sudo modprobe ipmi_watchdog
```

### Usage

See [here](http://www.openfusion.net/linux/ipmi_on_centos):

```
sudo ipmitool mc info
sudo ipmitool sdr
sudo ipmitool sensor
sudo ipmitool sel list
```

## DMIDecode

* http://www.nongnu.org/dmidecode/
* http://linux.die.net/man/8/dmidecode

Get serial numbers of DIMMs:

```console
dmidecode -t 17
```

# Various

## Interrupt Balancer Log Spam

The IRQ balancer is spamming the system log:

```
Sep 24 12:54:37 bvr-sql18 /usr/sbin/irqbalance: irq 75 affinity_hint subset empty
```

To silence these log messages, add the following line to `/etc/default/irqbalance`:

    OPTIONS="--hintpolicy=ignore"
    
and restart the service

    sudo service irqbalance restart


# Storage

## XFS and PostgreSQL

* http://de.slideshare.net/fuzzycz/postgresql-on-ext4-xfs-btrfs-and-zfs => Slide 49

## Storage Setup

```
sudo mdadm --create /dev/md2 --chunk=8 --level=0 --raid-devices=8 \
   /dev/nvme0n1 \
   /dev/nvme1n1 \
   /dev/nvme2n1 \
   /dev/nvme3n1 \
   /dev/nvme4n1 \
   /dev/nvme5n1 \
   /dev/nvme6n1 \
   /dev/nvme7n1


sudo mdadm --create /dev/md3 --chunk=8 --level=10 --raid-devices=10 \
    /dev/sdb \
    /dev/sdd \
    /dev/sde \
    /dev/sdf \
    /dev/sdg \
    /dev/sdh \
    /dev/sdi \
    /dev/sdag \
    /dev/sdah \
    /dev/sdai


sudo mdadm --create /dev/md240 --level=6 --raid-devices=6 /dev/sd[m-r]


http://unix.stackexchange.com/questions/129497/difference-between-uuid-from-blkid-and-mdadm


System:

/dev/sda
/dev/sdc


Internal (10 x 800GB):

/dev/sdb 
/dev/sdd 
/dev/sde 
/dev/sdf 
/dev/sdg 
/dev/sdh 
/dev/sdi 
/dev/sdag
/dev/sdah
/dev/sdai


JBOD (24 x 6TB):

/dev/sdj
/dev/sdk
/dev/sdl
/dev/sdm
/dev/sdn
/dev/sdo

/dev/sdp
/dev/sdq
/dev/sdr
/dev/sds
/dev/sdt
/dev/sdu

/dev/sdv
/dev/sdw
/dev/sdx
/dev/sdy
/dev/sdz
/dev/sdaa

/dev/sdab
/dev/sdac
/dev/sdad
/dev/sdae
/dev/sdaf
```

# Memory Errors

* https://www.kernel.org/doc/Documentation/edac.txt
* http://lambda-diode.com/opinion/ecc-memory


# PostgreSQL Backup

## Backup at filesystem Level

Install parallel compressor:

```
sudo apt-get install pbzip2
```

Shutdown the database:

```console
pg_ctl stop -m fast
```

Tar up the backup in parallel mode:

```console
oberstet@bvr-sql18:~$ time sudo tar cf /result/backup/backup_data_20151121.tar.bz2 --use-compress-prog=pbzip2 /data
tar: Entferne führende „/“ von Elementnamen

real    167m18.408s
user    7003m37.036s
sys     461m41.076s
```

This produces a single backup archive file:

```console
postgres@bvr-sql18:/result/backup$ ls -la
insgesamt 696759660
drwx------ 3 postgres postgres           56 Nov 21 12:39 .
drwxr-xr-x 3 root     root               19 Nov  7 14:19 ..
drwxrwxr-x 3 postgres postgres           93 Nov 21 12:26 backup_1
-rw-r--r-- 1 root     root     713481886989 Nov 21 15:26 backup_data_20151121.tar.bz2
```

Untar the backup in parallel mode:

```console
postgres@bvr-sql18:~$ cd / 
postgres@bvr-sql18:/$ time tar xf /result/backup/backup_data_20151121.tar.bz2 --use-compress-prog=pbzip2
real    131m50.738s
user    2101m25.756s
sys     689m39.092s
```

## Backup at database level

> "Thanks to synchronized snapshots shared among the backends managed by the jobs, the dump is taken consistently ensuring that all the jobs share the same data view"

Backup ADR database in parallel mode

```console
time pg_dump -Fd -f /result/backup/backup_adr_20151121 -j 16 adr
```

Backup postgres database

```
pg_dump -Fc -f /result/backup/backup_postgres_20151121.bak postgres
```

Backup cluster global stuff

```
pg_dumpall -g -f /result/backup/backup_20151121.bak
```

### Log

Backup (16 workers):

```
postgres@bvr-sql18:/result/backup$ time pg_dump -Fd -f /result/backup/backup_adr_20151121 -j 16 adr

real    52m42.936s
user    743m45.272s
sys     19m10.504s
```

Check the archive:

```console
postgres@bvr-sql18:/data/adr/pg_log$ ll /result/backup/
insgesamt 148
drwx------ 3 postgres postgres    93 Nov 21 12:25 ./
drwxr-xr-x 3 root     root        19 Nov  7 14:19 ../
-rw-rw-r-- 1 postgres postgres  5770 Nov 21 12:25 backup_20151121.bak
drwx------ 2 postgres postgres 86016 Nov 21 12:15 backup_adr_20151121/
-rw-rw-r-- 1 postgres postgres  2270 Nov 21 12:24 backup_postgres_20151121.bak
postgres@bvr-sql18:/result/backup/backup_1$ pg_restore -l backup_adr_20151121/ | wc -l
11631
```

# pgtune

Due to [this](https://github.com/gregs1104/pgtune/issues/15) issue, we are using a [patched](https://github.com/gregs1104/pgtune/pull/16) version.


# Intel SSDs

## Intel SSD Data Center Tool

* [Download](https://downloadcenter.intel.com/download/23931/Intel-Solid-State-Drive-Data-Center-Tool)
* [Manual](https://downloadmirror.intel.com/23931/eng/Intel_SSD_Data_Center_Tool_2_3_x_User_Guide_331961-005.pdf)

## Installation

To install:

```console
sudo apt-get install alien dpkg-dev debhelper build-essential
cd /tmp
wget https://downloadmirror.intel.com/23931/eng/DataCenterTool_2_3_1_Linux.zip
unzip DataCenterTool_2_3_1_Linux.zip
sudo alien isdct-2.3.1.400-14.x86_64.rpm
sudo dpkg -i isdct_2.3.1.400-15_amd64.deb
```

This provides:

```
oberstet@bvr-sql18:~$ which isdct
/usr/bin/isdct
oberstet@bvr-sql18:~$ isdct version
- Version Information -
Name: Intel(R) Data Center Tool
Version: 2.3.1
Description: Interact and configure Intel SSDs.


oberstet@bvr-sql18:~$
```

List all Intel SSDs:

```
oberstet@bvr-sql18:~$ sudo isdct show -intelssd | grep ProductFamily
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC S3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
ProductFamily: Intel SSD DC P3700 Series
```

Check for updates:

```console
oberstet@bvr-sql18:~$ sudo isdct show -intelssd | grep Update
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
FirmwareUpdateAvailable: The selected Intel SSD contains current firmware as of this tool release.
```

Show all info for SSD #19

```
sudo isdct show -a -intelssd 19
```

## NVMe Tuning

The Noop I/O scheduler implements a simple first-in first-out (FIFO) scheduling algorithm. Merging of requests happens at the generic block layer, but is a simple last-hit cache. If a system is CPU-bound and the storage is fast, this can be the best I/O scheduler to use.

```
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/scheduler; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/add_random; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/rq_affinity; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/nr_requests; done
```

produces

```console
oberstet@bvr-sql18:~$ for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/scheduler; done
none
none
none
none
none
none
none
none
oberstet@bvr-sql18:~$ for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/add_random; done
0
0
0
0
0
0
0
0
oberstet@bvr-sql18:~$ for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/rq_affinity; done
1
1
1
1
1
1
1
1
oberstet@bvr-sql18:~$ for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/nr_requests; done
1023
1023
1023
1023
1023
1023
1023
1023
oberstet@bvr-sql18:~$
```

## SSD Tuning

Show relevant tuning parameters

```
cat /sys/block/sdd/queue/scheduler
cat /sys/block/sdd/device/queue_depth
cat /sys/block/sdd/queue/add_random
cat /sys/block/sdd/queue/rq_affinity
cat /sys/block/sdd/queue/nr_requests
cat /sys/block/sdd/queue/nomerges
```

Unoptimized default values:

```console
oberstet@bvr-sql18:~$ cat /sys/block/sdd/queue/scheduler
noop [deadline] cfq
oberstet@bvr-sql18:~$ cat /sys/block/sdd/device/queue_depth
32
oberstet@bvr-sql18:~$ cat /sys/block/sdd/queue/add_random
0
oberstet@bvr-sql18:~$ cat /sys/block/sdd/queue/rq_affinity
1
oberstet@bvr-sql18:~$ cat /sys/block/sdd/queue/nr_requests
128
oberstet@bvr-sql18:~$ cat /sys/block/sdd/queue/nomerges
0
oberstet@bvr-sql18:~$
```

## Making changes permanent

If you want to make sure this remains disabled after reboots, you can add the command above to `/etc/rc.local`

```
vim /etc/rc.local
##Add this above "exit 0"##

echo 0 > /sys/block/sda/queue/add_random
exit 0
```

Save the file then make sure the file is executable

```
chmod +x /etc/rc.local
```

## Trim and Erase

An SSD can be notified that a data range isn't needed anymore at different levels:

1. hardware driver
2. block device
3. filesystem

### Hardware Driver Level

Pages can be trimmer using the Intel Datacenter SSD tool (see the [manual](https://downloadmirror.intel.com/23931/eng/Intel_SSD_Data_Center_Tool_2_3_x_User_Guide_331961-005.pdf)):

```
isdct -intelssd 19 delete
```

For SATA devices, this will issue an "ATA Secure Erase" if supported, or Sanitize erase if supported. For NVMe devices, this will issue an NVMe Format command with SecureEraseSetting = 2.

Hence, above command should be equivalent to

```
isdct -intelssd 19 start Function=nvmeformat SecureEraseSetting=2
```

However, the latter command allows more control via `SecureEraseSetting`:

* 0: No secure erase
* 1: User data erase
* 2: Crypto erase

### Block Device Driver Level

**WARNING: DO NOT DO THIS IF THERE IS DATA ON YOUR DISK!**

Blocks can be trimmed at the block device level using [blkdiscard](http://man7.org/linux/man-pages/man8/blkdiscard.8.html)

```
sudo blkdiscard /dev//dev/nvme0n1
```

### Filesystem Level

See [here](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/main-fs.html#idp4653632).

*Discard unused blocks*

Batch discard and online discard operations are features of mounted file systems that discard blocks which are not in use by the file system. These operations are useful for both solid-state drives and thinly-provisioned storage.

Batch discard operations are run explicitly by the user with the fstrim command. This command discards all unused blocks in a file system that match the user's criteria. Both operation types are supported for use with the XFS and ext4 file systems in Red Hat Enterprise Linux 6.2 and later as long as the block device underlying the file system supports physical discard operations. Physical discard operations are supported if the value of /sys/block/device/queue/discard_max_bytes is not zero.

Online discard operations are specified at mount time with the -o discard option (either in /etc/fstab or as part of the mount command), and run in realtime without user intervention. Online discard operations only discard blocks that are transitioning from used to free. Online discard operations are supported on ext4 file systems in Red Hat Enterprise Linux 6.2 and later, and on XFS file systems in Red Hat Enterprise Linux 6.4 and later.

Red Hat recommends batch discard operations unless the system's workload is such that batch discard is not feasible, or online discard operations are necessary to maintain performance.

```console
oberstet@bvr-sql18:~$ for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/discard_max_bytes; done
2199023255040
2199023255040
2199023255040
2199023255040
2199023255040
2199023255040
2199023255040
2199023255040
```


## Mounting

Get persistent UUID for block device:

```
sudo blkid -s UUID -o value /dev/md2
```

Add fstab entry

```
sudo echo "UUID=`blkid -s UUID -o value /dev/md2` /data/adr xfs defaults,noatime,discard,nobarrier 0 0" >> /etc/fstab 
```
