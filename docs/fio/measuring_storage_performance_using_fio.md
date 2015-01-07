# Introduction

[FIO](https://github.com/axboe/fio), the flexible I/O tester is an advanced storage performance test tool, written by Jens Axboe, a former employee of Oracle and FusionIO.

The tool is widely used in the industry, e.g. see [here](http://www.storagereview.com/fio_flexible_i_o_tester_synthetic_benchmark) for a longer article by [StorageReview](http://www.storagereview.com/), a storage reviewing and testing site.

The tool is open-source, available for all major Unix platforms, and also [available](http://www.bluestop.org/fio/) precompiled for Windows.

Resources:

* [FIO manpage](http://linux.die.net/man/1/fio)
* [FIO workload profiles examples](https://github.com/axboe/fio/tree/master/examples)
* [FIO output explained](https://tobert.github.io/post/2014-04-17-fio-output-explained.html)
* [FIO Grundlagen](http://www.thomas-krenn.com/de/wiki/Fio_Grundlagen)
* [FIO unter Windows nutzen](http://www.thomas-krenn.com/de/wiki/Fio_unter_Windows_nutzen)
* [Getting started with FIO](https://tobert.github.io/post/2014-04-28-getting-started-with-fio.html)

## Test System

The system we used for testing has the following hardware specification:

1. 1x Intel Xeon "Haswell" 3.4 GHz (E3-1240 v3)
2. 32GB ECC RAM
3. 2x [Intel DC3700](http://www.intel.com/content/www/us/en/solid-state-drives/solid-state-drives-dc-s3700-series.html) 200GB (SSDSC2BA200G3)
4. 4x [Seagate Constellation ES.3](http://www.seagate.com/de/de/internal-hard-drives/nas-drives/enterprise-capacity-3-5-hdd/) 2TB SAS (ST2000NM0023)
5. All drives in a [JBOD](http://en.wikipedia.org/wiki/Non-RAID_drive_architectures#JBOD) configuration (no hardware RAID controller) on ZFS RAIDs

The total price for above box is roughly **2.500 Euro** (2014/11).

> The Intel [datasheet](http://www.intel.com/content/dam/www/public/us/en/documents/product-specifications/ssd-dc-s3700-spec.pdf) for the exact SSD model used claims "up to" 16,500 random write IOPS at 8KB size with a IO queue depth of 32. We are going to see if we can get that from ZFS.


The software run on the box:

1. FreeBSD 10.1 Release (kernel recompiled)
2. ZFS
3. PostgreSQL 9.4 (compiled from vanilla sources)

To report on disks, use [camcontrol](https://www.freebsd.org/cgi/man.cgi?format=html&query=camcontrol%288%29):

```console
root@brummer2:/home/oberstet # camcontrol devlist
<SEAGATE ST2000NM0023 0004>        at scbus0 target 2 lun 0 (pass0,da0)
<SEAGATE ST2000NM0023 0004>        at scbus0 target 3 lun 0 (pass1,da1)
<SEAGATE ST2000NM0023 0004>        at scbus0 target 4 lun 0 (pass2,da2)
<SEAGATE ST2000NM0023 0004>        at scbus0 target 5 lun 0 (pass3,da3)
<INTEL SSDSC2BA200G3 5DV10270>     at scbus1 target 0 lun 0 (ada0,pass4)
<INTEL SSDSC2BA200G3 5DV10270>     at scbus2 target 0 lun 0 (ada1,pass5)
<AHCI SGPIO Enclosure 1.00 0001>   at scbus7 target 0 lun 0 (ses0,pass6)
```

And here is the CPU and memory:

```console
[oberstet@brummer1 ~]$ sysctl hw.realmem
hw.realmem: 34359738368
[oberstet@brummer1 ~]$ sysctl hw.model
hw.model: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
[oberstet@brummer1 ~]$
```

https://github.com/axboe/fio/tree/master/examples

# IO Modes

FIO has a number of workload modes:

* `read`: Sequential reads
* `write`: Sequential writes
* `randwrite`: Random writes
* `randread`: Random reads
* `rw`: Sequential mixed reads and writes
* `randrw`: Random mixed reads and writes


zfs create -o mountpoint=/test system/test
zfs set recordsize=8k system/test
zfs get recordsize,compression /test


zfs create -o mountpoint=/test2 tank/test2
zfs set recordsize=8k tank/test2
zfs set atime=off tank/test2
zfs get recordsize,atime,compression /test2


zfs create -o mountpoint=/test3 tank/test3
zfs set recordsize=128k tank/test3
zfs get recordsize,compression /test3


## Windows

`--ioengine=sync`
`--ioengine=windowsaio`


On FreeBSD, for asynchronous I/O, the [aio](https://www.freebsd.org/cgi/man.cgi?query=aio&sektion=4) kernel module has to be loaded:

```console
$ kldload aio
```

or add the following to `/boot/loader.conf`:

```
aio_load="YES"
```


Drop IO cache

echo 3 > /proc/sys/vm/drop_caches



FreeBSD:

Disable:

Intel Turbo Boost Technology => ON
Enhanced Intel SpeedStep Tech => OFF
Hyperthreading => OFF

http://www.ateamsystems.com/blog/Increase-FreeBSD-Performance-With-powerd
http://www.ateamsystems.com/tech-blog/increase-freebsd-performance-with-powerd/


powerd_enable="YES"
powerd_flags="-a hiadaptive"
performance_cpu_freq="HIGH"



https://calomel.org/freebsd_network_tuning.html

http://www.allanjude.com/bsd/zfs-advanced.html


vfs.zfs.vdev.max_pending
vfs.zfs.top_maxinflight
vfs.zfs.l2arc_write_max
vfs.zfs.l2arc_write_boost



sysctl vfs.zfs.l2arc_write_max=67108864
sysctl vfs.zfs.l2arc_write_boost=67108864
sysctl vfs.zfs.top_maxinflight=64


sysctl vfs.zfs.l2arc_write_max=16777216
sysctl vfs.zfs.l2arc_write_boost=16777216



sysctl vfs.zfs.l2arc_write_max=8388608
sysctl vfs.zfs.l2arc_write_boost=8388608
sysctl vfs.zfs.top_maxinflight=32


root@brummer2:~/fio # zfs get recordsize,atime,compression,dedup system/test
NAME         PROPERTY     VALUE     SOURCE
system/test  recordsize   8K        local
system/test  atime        off       local
system/test  compression  off       default



http://blog.vx.sk/uploads/conferences/EuroBSDcon2012/zfs-tuning-handout.pdf


# sysctl vfs.zfs
# sysctl kstat.zfs



## Test Vorgehen Windows

1. Install FIO for Windows


Display [zpool statistics](http://docs.oracle.com/cd/E19253-01/819-5461/gammt/index.html)

zpool iostat -v 1


https://wiki.postgresql.org/wiki/HP_ProLiant_DL380_G5_Tuning_Guide


# Smartctl

http://www.freebsddiary.org/smart.php
https://www.freebsd.org/cgi/man.cgi?query=smartctl&apropos=0&sektion=0&manpath=FreeBSD+10.1-RELEASE+and+Ports&arch=default&format=html


pkg install smartmontools


        /usr/local/sbin/smartctl -a /dev/ad0    for first ATA/SATA drive
        /usr/local/sbin/smartctl -a /dev/da0    for first SCSI drive
        /usr/local/sbin/smartctl -a /dev/ada0   for first SATA drive



To enable drive monitoring, you can use /usr/local/sbin/smartd.
A sample configuration file has been installed as
/usr/local/etc/smartd.conf.sample
Copy this file to /usr/local/etc/smartd.conf and edit appropriately

To have smartd start at boot
        echo 'smartd_enable="YES"' >> /etc/rc.conf



Enable SMART on a device:

```
smartctl /dev/ada0 -s on
```

```console
root@brummer2:/home/oberstet # smartctl /dev/ada0 -P show
smartctl 6.3 2014-07-26 r3976 [FreeBSD 10.1-RELEASE amd64] (local build)
Copyright (C) 2002-14, Bruce Allen, Christian Franke, www.smartmontools.org

Drive found in smartmontools Database.  Drive identity strings:
MODEL:              INTEL SSDSC2BA200G3
FIRMWARE:           5DV10270
match smartmontools Drive Database entry:
MODEL REGEXP:       INTEL SSDSC(1N|2B)[ABP](080|100|120|160|200|240|300|400|480|600|800)G[34]T?
FIRMWARE REGEXP:    .*
MODEL FAMILY:       Intel 730 and DC S3500/S3700 Series SSDs
ATTRIBUTE OPTIONS:  170 Available_Reservd_Space
                    171 Program_Fail_Count
                    172 Erase_Fail_Count
                    174 Unsafe_Shutdown_Count
                    175 Power_Loss_Cap_Test
                    183 SATA_Downshift_Count
                    190 Temperature_Case
                    192 Unsafe_Shutdown_Count
                    194 Temperature_Internal
                    199 CRC_Error_Count
                    225 Host_Writes_32MiB
                    226 Workld_Media_Wear_Indic
                    227 Workld_Host_Reads_Perc
                    228 Workload_Minutes
                    234 Thermal_Throttle
                    241 Host_Writes_32MiB
                    242 Host_Reads_32MiB
OTHER PRESETS:      Fixes LBA byte ordering in Ext. Comprehensive SMART error log (same as -F xerrorlba)
```


```console
root@brummer2:/home/oberstet # smartctl -a /dev/ada0
smartctl 6.3 2014-07-26 r3976 [FreeBSD 10.1-RELEASE amd64] (local build)
Copyright (C) 2002-14, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Intel 730 and DC S3500/S3700 Series SSDs
Device Model:     INTEL SSDSC2BA200G3
Serial Number:    BTTV441500T2200GGN
LU WWN Device Id: 5 5cd2e4 04b6f58ce
Firmware Version: 5DV10270
User Capacity:    200,049,647,616 bytes [200 GB]
Sector Sizes:     512 bytes logical, 4096 bytes physical
Rotation Rate:    Solid State Device
Form Factor:      2.5 inches
Device is:        In smartctl database [for details use: -P show]
ATA Version is:   ACS-2 T13/2015-D revision 3
SATA Version is:  SATA 2.6, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Wed Jan  7 13:08:51 2015 CET
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x00) Offline data collection activity
                                        was never started.
                                        Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0) The previous self-test routine completed
                                        without error or no self-test has ever
                                        been run.
Total time to complete Offline
data collection:                (    0) seconds.
Offline data collection
capabilities:                    (0x79) SMART execute Offline immediate.
                                        No Auto Offline data collection support.
                                        Suspend Offline collection upon new
                                        command.
                                        Offline surface scan supported.
                                        Self-test supported.
                                        Conveyance Self-test supported.
                                        Selective Self-test supported.
SMART capabilities:            (0x0003) Saves SMART data before entering
                                        power-saving mode.
                                        Supports SMART auto save timer.
Error logging capability:        (0x01) Error logging supported.
                                        General Purpose Logging supported.
Short self-test routine
recommended polling time:        (   1) minutes.
Extended self-test routine
recommended polling time:        (   2) minutes.
Conveyance self-test routine
recommended polling time:        (   2) minutes.
SCT capabilities:              (0x003d) SCT Status supported.
                                        SCT Error Recovery Control supported.
                                        SCT Feature Control supported.
                                        SCT Data Table supported.

SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0032   100   100   000    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   100   100   000    Old_age   Always       -       614
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       8
170 Available_Reservd_Space 0x0033   100   100   010    Pre-fail  Always       -       0
171 Program_Fail_Count      0x0032   100   100   000    Old_age   Always       -       0
172 Erase_Fail_Count        0x0032   100   100   000    Old_age   Always       -       0
174 Unsafe_Shutdown_Count   0x0032   100   100   000    Old_age   Always       -       2
175 Power_Loss_Cap_Test     0x0033   100   100   010    Pre-fail  Always       -       624 (3 5515)
183 SATA_Downshift_Count    0x0032   100   100   000    Old_age   Always       -       0
184 End-to-End_Error        0x0033   100   100   090    Pre-fail  Always       -       0
187 Reported_Uncorrect      0x0032   100   100   000    Old_age   Always       -       0
190 Temperature_Case        0x0022   076   075   000    Old_age   Always       -       24 (Min/Max 19/35)
192 Unsafe_Shutdown_Count   0x0032   100   100   000    Old_age   Always       -       2
194 Temperature_Internal    0x0022   100   100   000    Old_age   Always       -       33
197 Current_Pending_Sector  0x0032   100   100   000    Old_age   Always       -       0
199 CRC_Error_Count         0x003e   100   100   000    Old_age   Always       -       0
225 Host_Writes_32MiB       0x0032   100   100   000    Old_age   Always       -       103522
226 Workld_Media_Wear_Indic 0x0032   100   100   000    Old_age   Always       -       40
227 Workld_Host_Reads_Perc  0x0032   100   100   000    Old_age   Always       -       42
228 Workload_Minutes        0x0032   100   100   000    Old_age   Always       -       36859
232 Available_Reservd_Space 0x0033   100   100   010    Pre-fail  Always       -       0
233 Media_Wearout_Indicator 0x0032   100   100   000    Old_age   Always       -       0
234 Thermal_Throttle        0x0032   100   100   000    Old_age   Always       -       0/0
241 Host_Writes_32MiB       0x0032   100   100   000    Old_age   Always       -       103522
242 Host_Reads_32MiB        0x0032   100   100   000    Old_age   Always       -       76743

SMART Error Log Version: 1
No Errors Logged

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]

SMART Selective self-test log data structure revision number 1
 SPAN  MIN_LBA  MAX_LBA  CURRENT_TEST_STATUS
    1        0        0  Not_testing
    2        0        0  Not_testing
    3        0        0  Not_testing
    4        0        0  Not_testing
    5        0        0  Not_testing
Selective self-test flags (0x0):
  After scanning selected spans, do NOT read-scan remainder of disk.
If Selective self-test is pending on power-up, resume after 0 minute delay.

root@brummer2:/home/oberstet #
```



http://www.allanjude.com/bsd/zfs.html


# PostgreSQL

For each database within a PostgreSQL database cluster, create two ZFS filesystems

1. for data files
2. for log files

Set the ZFS recordsize on the FS for *data files* to 8KB. Leave the FS for *log files* at the default recordsize of 128KB. *You must do this before creating the PostgreSQL database!.


https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server
http://olavgg.com/post/62799347118/postgresql-9-3-on-zfs-with-lz4-compression-on



http://de.slideshare.net/markwkm/postgresql-portland-performance-practice-project-database-test-2-filesystem-characterization



http://blog.delphix.com/ahl/2014/openzfs-write-throttle/
http://blog.delphix.com/ahl/2014/tuning-openzfs-write-throttle/

root@brummer2:/home/oberstet # sysctl vfs.zfs | grep dirty
vfs.zfs.dirty_data_max: 3426535833
vfs.zfs.dirty_data_max_max: 4294967296
vfs.zfs.dirty_data_max_percent: 10
vfs.zfs.dirty_data_sync: 67108864
vfs.zfs.delay_min_dirty_percent: 60


https://pthree.org/2012/12/12/zfs-administration-part-vii-zpool-properties/

https://wiki.freebsd.org/ZFSTuningGuide

http://constantin.glez.de/blog/2011/02/frequently-asked-questions-about-flash-memory-ssds-and-zfs



# Root on ZFS

http://olavgg.com/post/62799347118/postgresql-9-3-on-zfs-with-lz4-compression-on

https://forums.freebsd.org/threads/freebsd-9-zfs-the-easy-way.31557/

