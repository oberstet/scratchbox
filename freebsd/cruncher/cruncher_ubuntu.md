# Cruncher / Ubuntu

## systemd

```console
oberstet@bvr-sql18:~$ ls -la /etc/systemd/system
insgesamt 68
drwxr-xr-x 13 root root 4096 Dez  9 10:46 .
drwxr-xr-x  5 root root 4096 Nov  3 14:30 ..
-rw-r--r--  1 root root  307 Nov 13 01:43 crossbar.service
drwxr-xr-x  2 root root 4096 Aug 18 17:03 default.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:03 getty.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:12 graphical.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:12 halt.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:12 kexec.target.wants
-rw-r--r--  1 root root  318 Nov 18 16:51 livemon.service
drwxr-xr-x  2 root root 4096 Nov 26 12:06 multi-user.target.wants
lrwxrwxrwx  1 root root   47 Aug 18 17:12 plymouth-log.service -> /lib/systemd/system/plymouth-read-write.service
lrwxrwxrwx  1 root root   41 Aug 18 17:12 plymouth.service -> /lib/systemd/system/plymouth-quit.service
-rw-r--r--  1 root root  497 Nov 16 15:22 postgresql.service
drwxr-xr-x  2 root root 4096 Aug 18 17:12 poweroff.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:12 reboot.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:07 shutdown.target.wants
drwxr-xr-x  2 root root 4096 Aug 18 17:12 sockets.target.wants
-rw-r--r--  1 root root  422 Dez  9 10:46 sqlbalancer.service
lrwxrwxrwx  1 root root   31 Aug 18 17:12 sshd.service -> /lib/systemd/system/ssh.service
drwxr-xr-x  2 root root 4096 Aug 18 17:12 sysinit.target.wants
lrwxrwxrwx  1 root root   35 Aug 18 17:03 syslog.service -> /lib/systemd/system/rsyslog.service
oberstet@bvr-sql18:~$ ls -la /lib/systemd/system/ssh.service
-rw-r--r-- 1 root root 344 Mär 23  2015 /lib/systemd/system/ssh.service
oberstet@bvr-sql18:~$ cat /lib/systemd/system/ssh.service
[Unit]
Description=OpenBSD Secure Shell server
After=network.target auditd.service
ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

[Service]
EnvironmentFile=-/etc/default/ssh
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
Alias=sshd.service
oberstet@bvr-sql18:~$ cat /etc/systemd/system/crossbar.service
[Unit]
Description=ADR Crossbar.io
After=network.target

[Service]
Type=simple
User=crossbar
Group=crossbar
StandardInput=null
StandardOutput=journal
StandardError=journal
ExecStart=/opt/crossbar/bin/crossbar start --cbdir=/var/crossbar/node/.crossbar
Restart=on-abort

[Install]
WantedBy=multi-user.target
oberstet@bvr-sql18:~$
```


## Networking

List network interface cards and logical interface names:

```console
oberstet@bvr-sql18:~$ sudo lshw -class network
  *-network:0
       description: Ethernet interface
       product: Ethernet Controller 10-Gigabit X540-AT2
       vendor: Intel Corporation
       physical id: 0
       bus info: pci@0000:01:00.0
       logical name: eth0
       version: 01
       serial: c4:54:44:92:73:d2
       size: 1Gbit/s
       capacity: 1Gbit/s
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi msix pciexpress bus_master cap_list rom ethernet physical tp 100bt-fd 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=ixgbe driverversion=4.0.1-k duplex=full firmware=0x80000314 ip=10.200.1.67 latency=0 link=yes multicast=yes port=twisted pair speed=1Gbit/s
       resources: irq:24 memory:aaa00000-aabfffff ioport:4020(size=32) memory:aac04000-aac07fff memory:90000000-9007ffff memory:90100000-901fffff memory:90200000-902fffff
  *-network:1 DISABLED
       description: Ethernet interface
       product: Ethernet Controller 10-Gigabit X540-AT2
       vendor: Intel Corporation
       physical id: 0.1
       bus info: pci@0000:01:00.1
       logical name: eth1
       version: 01
       serial: c4:54:44:92:73:d3
       capacity: 1Gbit/s
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi msix pciexpress bus_master cap_list rom ethernet physical tp 100bt-fd 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=ixgbe driverversion=4.0.1-k firmware=0x80000314 latency=0 link=no multicast=yes port=twisted pair
       resources: irq:184 memory:aa800000-aa9fffff ioport:4000(size=32) memory:aac00000-aac03fff memory:90080000-900fffff memory:90300000-903fffff memory:90400000-904fffff
  *-network:0 DISABLED
       description: Ethernet interface
       product: 82599ES 10-Gigabit SFI/SFP+ Network Connection
       vendor: Intel Corporation
       physical id: 0
       bus info: pci@0000:02:00.0
       logical name: p11p1
       version: 01
       serial: 0c:c4:7a:1e:a9:6a
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi msix pciexpress vpd bus_master cap_list rom ethernet physical fibre
       configuration: autonegotiation=off broadcast=yes driver=ixgbe driverversion=4.0.1-k firmware=0x80000208 latency=0 link=no multicast=yes
       resources: irq:297 memory:90500000-9057ffff ioport:3020(size=32) memory:90600000-90603fff memory:abb80000-abbfffff memory:90604000-90703fff memory:90704000-90803fff
  *-network:1 DISABLED
       description: Ethernet interface
       product: 82599ES 10-Gigabit SFI/SFP+ Network Connection
       vendor: Intel Corporation
       physical id: 0.1
       bus info: pci@0000:02:00.1
       logical name: p11p2
       version: 01
       serial: 0c:c4:7a:1e:a9:6b
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi msix pciexpress vpd bus_master cap_list rom ethernet physical fibre
       configuration: autonegotiation=off broadcast=yes driver=ixgbe driverversion=4.0.1-k firmware=0x80000208 latency=0 link=no multicast=yes
       resources: irq:474 memory:90580000-905fffff ioport:3000(size=32) memory:90804000-90807fff memory:abb00000-abb7ffff memory:90808000-90907fff memory:90908000-90a07fff
oberstet@bvr-sql18:~$
```

Get info on IPMI:

```console
oberstet@bvr-sql18:~$ sudo ipmitool lan print
Set in Progress         : Set Complete
Auth Type Support       : NONE MD2 MD5 PASSWORD OEM
Auth Type Enable        : Callback : NONE MD2 MD5 PASSWORD OEM
                        : User     : NONE MD2 MD5 PASSWORD OEM
                        : Operator : NONE MD2 MD5 PASSWORD OEM
                        : Admin    : NONE MD2 MD5 PASSWORD OEM
                        : OEM      :
IP Address Source       : Static Address
IP Address              : 10.200.1.71
Subnet Mask             : 255.255.255.0
MAC Address             : c4:54:44:61:5f:99
SNMP Community String   : Quanta
IP Header               : TTL=0x40 Flags=0x40 Precedence=0x00 TOS=0x10
BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled
Gratituous ARP Intrvl   : 0.0 seconds
Default Gateway IP      : 10.200.1.1
Default Gateway MAC     : 00:00:00:00:00:00
Backup Gateway IP       : 0.0.0.0
Backup Gateway MAC      : 00:00:00:00:00:00
802.1q VLAN ID          : Disabled
802.1q VLAN Priority    : 0
RMCP+ Cipher Suites     : 0,1,2,3,6,7,8,11,12
Cipher Suite Priv Max   : caaaXXaaaXXaaXX
                        :     X=Cipher Suite Unused
                        :     c=CALLBACK
                        :     u=USER
                        :     o=OPERATOR
                        :     a=ADMIN
                        :     O=OEM
oberstet@bvr-sql18:~$
```

## Samba

### Using network shares

List network share on a machine:

```console
oberstet@bvr-sql18:~$ smbclient -U toob -L 10.200.1.110
Enter toob's password:
Domain=[PARCIT] OS=[Windows 5.0] Server=[Windows 2000 LAN Manager]

        Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       Remote IPC
        ETC$            Disk      Remote Administration
        C$              Disk      Remote Administration
        parcit_dfs_extern$ Disk
        parcit_dfs_mazars$ Disk
        parcit_dfs_backup$ Disk
        parcit_dfs_gemeinsam$ Disk
        parcit_dfs_entwicklung$ Disk
        parcit_dfs_privat$ Disk
        parcit_dfs_temp$ Disk
        vol_cifs_parcit_rating$ Disk
        parcit_dfs_rating$ Disk
        vol_cifs_parcit_rating_rohdaten$ Disk
        Rating_Rohdaten Disk
Connection to 10.200.1.110 failed (Error NT_STATUS_IO_DEVICE_ERROR)
NetBIOS over TCP disabled -- no workgroup available
```

### Providing network shares

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


## Uninterruptible Sleep

A process blocked in a system call is in uninterruptible sleep and does not receive signals.

http://unix.stackexchange.com/a/5648

ps -fl -u postgres


http://blog.notreally.org/2008/02/10/tricks-to-diagnose-processes-blocked-on-strong-io-in-linux/
http://bencane.com/2012/08/06/troubleshooting-high-io-wait-in-linux/

ps aux | grep " D"


https://danielmiessler.com/study/lsof/


sudo lsof -a /data/adr/

sudo lsof -u postgres /data/adr/


## Building R

http://www.r-bloggers.com/installing-r-on-ubuntu/

sudo apt-get install build-essential gfortran libreadline6 libreadline6-dev
sudo apt-get install xorg-dev

cd ~/tarballs
wget https://cran.r-project.org/src/base/R-3/R-3.2.2.tar.gz

cd ~/build
tar xvf ../tarballs/R-3.2.2.tar.gz
cd R-3.2.2
export CFLAGS="-O3 -march=native -mtune=native"
export CXXFLAGS="-O3 -march=native -mtune=native"
export FFLAGS="-O3 -march=native -mtune=native"
export F90FLAGS="-O3 -march=native -mtune=native"
#./configure --enable-R-shlib --with-x=no --prefix=/opt/R322
./configure --enable-R-shlib --prefix=/opt/R322


## Sortme

sudo umount -f /data/pgxl/node1/shard1
sudo umount -f /data/pgxl/node1/shard2
sudo umount -f /data/pgxl/node1/shard3
sudo umount -f /data/pgxl/node1/shard4
sudo umount -f /data/pgxl/node2/shard1
sudo umount -f /data/pgxl/node2/shard2
sudo umount -f /data/pgxl/node2/shard3
sudo umount -f /data/pgxl/node2/shard4
sudo umount -f /data/pgxl/node3/shard1
sudo umount -f /data/pgxl/node3/shard2
sudo umount -f /data/pgxl/node3/shard3
sudo umount -f /data/pgxl/node3/shard4
sudo umount -f /data/pgxl/node4/shard1
sudo umount -f /data/pgxl/node4/shard2
sudo umount -f /data/pgxl/node4/shard3
sudo umount -f /data/pgxl/node4/shard4
sudo umount -f /data/pgxl/node5/shard1
sudo umount -f /data/pgxl/node5/shard2
sudo umount -f /data/pgxl/node5/shard3
sudo umount -f /data/pgxl/node5/shard4
sudo umount -f /data/pgxl/node6/shard1
sudo umount -f /data/pgxl/node6/shard2
sudo umount -f /data/pgxl/node6/shard3
sudo umount -f /data/pgxl/node6/shard4
sudo umount -f /data/pgxl/node7/shard1
sudo umount -f /data/pgxl/node7/shard2
sudo umount -f /data/pgxl/node7/shard3
sudo umount -f /data/pgxl/node7/shard4
sudo umount -f /data/pgxl/node8/shard1
sudo umount -f /data/pgxl/node8/shard2
sudo umount -f /data/pgxl/node8/shard3
sudo umount -f /data/pgxl/node8/shard4


sudo mdadm --zero-superblock /dev/nvme0n1
sudo mdadm --zero-superblock /dev/nvme1n1
sudo mdadm --zero-superblock /dev/nvme2n1
sudo mdadm --zero-superblock /dev/nvme3n1
sudo mdadm --zero-superblock /dev/nvme4n1
sudo mdadm --zero-superblock /dev/nvme5n1
sudo mdadm --zero-superblock /dev/nvme6n1
sudo mdadm --zero-superblock /dev/nvme7n1

sudo dd if=/dev/zero of=/dev/nvme0n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme1n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme2n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme3n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme4n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme5n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme6n1 bs=4096 count=10000
sudo dd if=/dev/zero of=/dev/nvme7n1 bs=4096 count=10000

# http://askubuntu.com/questions/42266/what-is-the-recommended-way-to-empty-a-ssd

sudo blkdiscard /dev/nvme0n1
sudo blkdiscard /dev/nvme1n1
sudo blkdiscard /dev/nvme2n1
sudo blkdiscard /dev/nvme3n1
sudo blkdiscard /dev/nvme4n1
sudo blkdiscard /dev/nvme5n1
sudo blkdiscard /dev/nvme6n1
sudo blkdiscard /dev/nvme7n1

# FINAL CREATED:

sudo umount -f /data/adr
sudo dd if=/dev/zero of=/dev/md2 bs=4096 count=10000
sudo partprobe
sudo mkfs.xfs -f -K -L pg_adr /dev/md2
sudo mkdir -p /data/adr
sudo mount -o defaults,noatime,discard,nobarrier /dev/md2 /data/adr
sudo chown -R postgres:postgres /data/adr
sudo chmod 700 /data/adr
