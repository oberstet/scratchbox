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

Here are the disks:

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

And here is the CPU:

```console
root@brummer2:/home/oberstet # sysctl hw.model
hw.model: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
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
zfs get recordsize,compression /test2


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

or add the following to `/etc/rc.conf`:

```
aio_load="YES"
```


## Test Vorgehen Windows

1. Install FIO for Windows


Display [zpool statistics](http://docs.oracle.com/cd/E19253-01/819-5461/gammt/index.html)

zpool iostat -v 1


https://wiki.postgresql.org/wiki/HP_ProLiant_DL380_G5_Tuning_Guide
