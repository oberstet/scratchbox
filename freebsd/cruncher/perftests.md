# Background

## Storage Performance

### NVMe

The **cruncher** machine has eight [Intel P3700 2TB](http://www.intel.com/content/www/us/en/solid-state-drives/intel-ssd-dc-family-for-pcie.html) flash-memory PCIe cards with a total of 16TB fast flash-memory.

The Intel [specification](http://www.intel.com/content/dam/www/public/us/en/documents/product-specifications/ssd-dc-p3700-spec.pdf) list a number of performance metrics:

1. Sequential Read (Write) up to **2,800 MB/s** (2,000 MB/s)
2. Random 4KB Read (Write) up to **450,000 IOPS** (175,000 IOPS)
3. Random 4KB 70/30 Read-Write up to **265,000 IOPS**
4. Random 8KB Read (Write) **295,000 IOPS** (90,000 IOPS)

Our first goal is to verify these performance numbers on **cruncher** running FreeBSD and at the block device level (single NVMe device) using FIO, a storage performance testing tool.

The second goal is to determine how much of the above raw performance is available at the ZFS filesystem level when the latter are created on ZFS pool spanning one or multiple of the NVMe devices.

Our expectation would be to meet the Intel specification performance values up to 80%, and at least 50% at the filesystem level.

> Due to caching at the filesystem level, we need to be careful with the latter goal of 50% performance.

Our final goal would be to compare the performance of the PostgreSQL standard pgbench test on a database instance running from a NVMe backend pool compared to a pool on the internal Intel DC S3700 SSDs.

> **cruncher** has eight Intel P3700 2TB NVMe disks, twelve internal Intel DC S3700 800GB SSDs connected and 24 external Seagate ES.3 6TB harddrives.


#### Identifying hardware

[nvmecontrol](https://www.freebsd.org/cgi/man.cgi?query=nvmecontrol) is a FreeBSD system tool that allows to query and manage NVMe devices:

```console
root@s4l-zfs:~/oberstet # which nvmecontrol
/sbin/nvmecontrol
```

To list all devices:

```console
root@s4l-zfs:~/oberstet # nvmecontrol devlist
 nvme0: INTEL SSDPEDMD020T4
    nvme0ns1 (1907729MB)
 nvme1: INTEL SSDPEDMD020T4
    nvme1ns1 (1907729MB)
 nvme2: INTEL SSDPEDMD020T4
    nvme2ns1 (1907729MB)
 nvme3: INTEL SSDPEDMD020T4
    nvme3ns1 (1907729MB)
 nvme4: INTEL SSDPEDMD020T4
    nvme4ns1 (1907729MB)
 nvme5: INTEL SSDPEDMD020T4
    nvme5ns1 (1907729MB)
 nvme6: INTEL SSDPEDMD020T4
    nvme6ns1 (1907729MB)
 nvme7: INTEL SSDPEDMD020T4
    nvme7ns1 (1907729MB)
```

To query a controller:

```console
root@s4l-zfs:~/oberstet # nvmecontrol identify nvme0
Controller Capabilities/Features
================================
Vendor ID:                  8086
Subsystem Vendor ID:        8086
Serial Number:              CVFT4476002A2P0EGN
Model Number:               INTEL SSDPEDMD020T4
Firmware Version:           8DV10130
Recommended Arb Burst:      0
IEEE OUI Identifier:        e4 d2 5c
Multi-Interface Cap:        00
Max Data Transfer Size:     131072

Admin Command Set Attributes
============================
Security Send/Receive:       Not Supported
Format NVM:                  Supported
Firmware Activate/Download:  Supported
Abort Command Limit:         4
Async Event Request Limit:   4
Number of Firmware Slots:    1
Firmware Slot 1 Read-Only:   No
Per-Namespace SMART Log:     No
Error Log Page Entries:      64
Number of Power States:      1

NVM Command Set Attributes
==========================
Submission Queue Entry Size
  Max:                       64
  Min:                       64
Completion Queue Entry Size
  Max:                       16
  Min:                       16
Number of Namespaces:        1
Compare Command:             Not Supported
Write Uncorrectable Command: Supported
Dataset Management Command:  Supported
Volatile Write Cache:        Not Present
```

To get information on a namespace:

```console
root@s4l-zfs:~/oberstet # nvmecontrol identify nvme0ns1
Size (in LBAs):              3907029168 (3726M)
Capacity (in LBAs):          3907029168 (3726M)
Utilization (in LBAs):       3907029168 (3726M)
Thin Provisioning:           Not Supported
Number of LBA Formats:       7
Current LBA Format:          LBA Format #00
LBA Format #00: Data Size:   512  Metadata Size:     0
LBA Format #01: Data Size:   512  Metadata Size:     8
LBA Format #02: Data Size:   512  Metadata Size:    16
LBA Format #03: Data Size:  4096  Metadata Size:     0
LBA Format #04: Data Size:  4096  Metadata Size:     8
LBA Format #05: Data Size:  4096  Metadata Size:    64
LBA Format #06: Data Size:  4096  Metadata Size:   128
```

#### Performance measured using nvmecontrol

The `nvmecontrol` tool also allows to run performance tests. E.g. the FreeBSD manual contains this example

```console
root@s4l-zfs:~ # nvmecontrol perftest -n 32 -o read -s 512 -t 30 nvme0ns1
Threads: 32 Size:    512  READ Time:  30 IO/s:  151373 MB/s:   73
```

When running with a 4KB block size we get:

```console
root@s4l-zfs:~ # nvmecontrol perftest -n 32 -o read -s 4096 -t 30 nvme0ns1
Threads: 32 Size:   4096  READ Time:  30 IO/s:  152631 MB/s:  596
```

Here are results with increasing number of threads performing I/O requests:

```console
root@s4l-zfs:~ # nvmecontrol perftest -n 1 -o read -s 4096 -t 30 nvme0ns1
Threads:  1 Size:   4096  READ Time:  30 IO/s:   22785 MB/s:   89
root@s4l-zfs:~ # nvmecontrol perftest -n 2 -o read -s 4096 -t 30 nvme0ns1
Threads:  2 Size:   4096  READ Time:  30 IO/s:   44971 MB/s:  175
root@s4l-zfs:~ # nvmecontrol perftest -n 4 -o read -s 4096 -t 30 nvme0ns1
Threads:  4 Size:   4096  READ Time:  30 IO/s:   81305 MB/s:  317
root@s4l-zfs:~ # nvmecontrol perftest -n 8 -o read -s 4096 -t 30 nvme0ns1
Threads:  8 Size:   4096  READ Time:  30 IO/s:  124931 MB/s:  488
root@s4l-zfs:~ # nvmecontrol perftest -n 16 -o read -s 4096 -t 30 nvme0ns1
Threads: 16 Size:   4096  READ Time:  30 IO/s:  152883 MB/s:  597
root@s4l-zfs:~ # nvmecontrol perftest -n 32 -o read -s 4096 -t 30 nvme0ns1
Threads: 32 Size:   4096  READ Time:  30 IO/s:  152733 MB/s:  596
root@s4l-zfs:~ # nvmecontrol perftest -n 64 -o read -s 4096 -t 30 nvme0ns1
Threads: 64 Size:   4096  READ Time:  30 IO/s:  150085 MB/s:  586
root@s4l-zfs:~ # nvmecontrol perftest -n 128 -o read -s 4096 -t 30 nvme0ns1
Threads: 128 Size:   4096  READ Time:  30 IO/s:  149764 MB/s:  585
root@s4l-zfs:~ # 
```

The peak performance in IOPS is reached at 16 threads. The is far beyond the IO queue depth of 128 which the NVMe device has. The peak performance of 152,883 IOPS is also far less than the 450,000 IOPS Intel claims for the device - 34% of the claimed performance. Mmh.

Lets do a quick test using FIO and see what we can get there for a pure 4KB random read workload.

Using this control file

**Control File 1**

```
root@s4l-zfs:~/oberstet # cat control.fio 
[global]
thread=1
ioengine=posixaio
direct=1
time_based=1
randrepeat=0
refill_buffers=1
end_fsync=1
size=10G
runtime=30
ramp_time=0
bs=4k
rw=randread

[random-read-4k]
numjobs=4
iodepth=32
group_reporting
```

we get 

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=posixaio, iodepth=32
...
fio-2.1.9
Starting 4 threads
Jobs: 4 (f=4): [rrrr] [100.0% done] [391.7MB/0KB/0KB /s] [100K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=4): err= 0: pid=101124: Mon Mar 30 23:42:25 2015
  read : io=13109MB, bw=447424KB/s, iops=111855, runt= 30001msec
    slat (usec): min=0, max=224, avg=10.68, stdev= 8.51
    clat (usec): min=212, max=4915, avg=1043.01, stdev=336.08
     lat (usec): min=222, max=4922, avg=1053.70, stdev=335.64
    clat percentiles (usec):
     |  1.00th=[  422],  5.00th=[  502], 10.00th=[  580], 20.00th=[  740],
     | 30.00th=[  868], 40.00th=[  948], 50.00th=[ 1020], 60.00th=[ 1112],
     | 70.00th=[ 1224], 80.00th=[ 1336], 90.00th=[ 1480], 95.00th=[ 1592],
     | 99.00th=[ 1848], 99.50th=[ 1976], 99.90th=[ 2288], 99.95th=[ 2384],
     | 99.99th=[ 2832]
    bw (KB  /s): min=79152, max=139880, per=25.00%, avg=111868.58, stdev=12339.09
    lat (usec) : 250=0.01%, 500=4.79%, 750=15.67%, 1000=26.56%
    lat (msec) : 2=52.54%, 4=0.43%, 10=0.01%
  cpu          : usr=1.45%, sys=98.56%, ctx=3077, majf=0, minf=36
  IO depths    : 1=0.1%, 2=0.1%, 4=0.6%, 8=7.1%, 16=85.0%, 32=7.2%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=93.5%, 8=0.9%, 16=3.7%, 32=1.9%, 64=0.0%, >=64=0.0%
     issued    : total=r=3355790/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: io=13109MB, aggrb=447423KB/s, minb=447423KB/s, maxb=447423KB/s, mint=30001msec, maxt=30001msec
```

FIO measures 111,855 IOPS. nvmecontrol says 152,883 IOPS. And Intel says 450,000 IOPS. Mmmmh.

> Using the **posixaio* engine of FIO above was the fastest run of varying numjobs and iodepth.

Further, look at the CPU load! The AIO implementation in the FreeBSD Posix layer seems to incur some overhead.

Using the **sync** engine of FIO (fastest parameters) by setting `ioengine=sync` in the control file (and `iodepth=1`, since the sync engine will only produce one concurrent request per worker thread/process)

**Control File 2**

```
root@s4l-zfs:~/oberstet # cat control.fio 
[global]
thread=1
ioengine=sync
direct=1
time_based=1
randrepeat=0
refill_buffers=1
end_fsync=1
size=10G
runtime=30
ramp_time=0
bs=4k
rw=randread

[random-read-4k]
numjobs=32
iodepth=1
group_reporting
```

here is what we get:


```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 32 (f=32): [rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr] [100.0% done] [419.2MB/0KB/0KB /s] [107K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=32): err= 0: pid=101139: Mon Mar 30 23:47:53 2015
  read : io=12550MB, bw=428371KB/s, iops=107092, runt= 30001msec
    clat (usec): min=96, max=3394, avg=296.70, stdev=31.06
     lat (usec): min=96, max=3394, avg=296.76, stdev=31.07
    clat percentiles (usec):
     |  1.00th=[  247],  5.00th=[  258], 10.00th=[  262], 20.00th=[  270],
     | 30.00th=[  278], 40.00th=[  282], 50.00th=[  290], 60.00th=[  302],
     | 70.00th=[  314], 80.00th=[  326], 90.00th=[  334], 95.00th=[  346],
     | 99.00th=[  366], 99.50th=[  374], 99.90th=[  394], 99.95th=[  406],
     | 99.99th=[  474]
    bw (KB  /s): min=12088, max=14504, per=3.12%, avg=13374.60, stdev=943.67
    lat (usec) : 100=0.01%, 250=1.75%, 500=98.25%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%
  cpu          : usr=0.71%, sys=2.62%, ctx=3212977, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=3212893/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=12550MB, aggrb=428371KB/s, minb=428371KB/s, maxb=428371KB/s, mint=30001msec, maxt=30001msec

```

The CPU load is negliable, the latencies are very flat and with 107,092 IOPS the throughput is only marginally lower than using AIO.

**However, now we finally have arrived at 107k / 450k or roughly 24% of the datesheet performance. And this is at the block device level.**

Maybe we ask too much? Lets check the performance of one of the internal Intel DC S3700 SSDs. These 12 Intel DC S3700 SSDs are connected to a HBA (LSI SAS 3008) using the `msr` driver. 

```console
root@s4l-zfs:~/oberstet # camcontrol identify da11
pass11: <INTEL SSDSC2BA800G3 5DV10270> ATA-9 SATA 3.x device
pass11: 600.000MB/s transfers, Command Queueing Enabled

protocol              ATA/ATAPI-9 SATA 3.x
device model          INTEL SSDSC2BA800G3
firmware revision     5DV10270
serial number         BTTV449503TE800JGN
WWN                   55cd2e404b738727
cylinders             16383
heads                 16
sectors/track         63
sector size           logical 512, physical 4096, offset 0
LBA supported         268435455 sectors
LBA48 supported       1562824368 sectors
PIO supported         PIO4
DMA supported         WDMA2 UDMA6 
media RPM             non-rotating

Feature                      Support  Enabled   Value           Vendor
read ahead                     yes  yes
write cache                    yes  yes
flush cache                    yes  yes
overlap                        no
Tagged Command Queuing (TCQ)   no   no
Native Command Queuing (NCQ)   yes      32 tags
NCQ Queue Management           no
NCQ Streaming                  no
Receive & Send FPDMA Queued    no
SMART                          yes  yes
microcode download             yes  yes
security                       yes  no
power management               yes  yes
advanced power management      no   no
automatic acoustic management  no   no
media status notification      no   no
power-up in Standby            no   no
write-read-verify              no   no
unload                         yes  yes
general purpose logging        yes  yes
free-fall                      no   no
Data Set Management (DSM/TRIM) yes
DSM - max 512byte blocks       yes              6
DSM - deterministic read       yes              zeroed
Host Protected Area (HPA)      yes      no      1562824368/1562824368
HPA - Security                 no
root@s4l-zfs:~/oberstet # 
```

Here are FIO results using the exact same **Control File 1** as above:

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/da11 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=posixaio, iodepth=32
...
fio-2.1.9
Starting 4 threads
Jobs: 4 (f=4): [rrrr] [100.0% done] [295.2MB/0KB/0KB /s] [75.8K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=4): err= 0: pid=101134: Mon Mar 30 23:44:54 2015
  read : io=8602.3MB, bw=293605KB/s, iops=73401, runt= 30002msec
    slat (usec): min=0, max=1726.7K, avg=14.79, stdev=1203.15
    clat (usec): min=56, max=1727.7K, avg=1631.81, stdev=3729.51
     lat (usec): min=302, max=1727.7K, avg=1646.60, stdev=3917.54
    clat percentiles (usec):
     |  1.00th=[  604],  5.00th=[  708], 10.00th=[  796], 20.00th=[  996],
     | 30.00th=[ 1304], 40.00th=[ 1592], 50.00th=[ 1736], 60.00th=[ 1848],
     | 70.00th=[ 1944], 80.00th=[ 2064], 90.00th=[ 2224], 95.00th=[ 2384],
     | 99.00th=[ 2736], 99.50th=[ 2896], 99.90th=[ 3728], 99.95th=[ 4896],
     | 99.99th=[ 9152]
    bw (KB  /s): min=11004, max=88176, per=25.31%, avg=74297.00, stdev=8208.27
    lat (usec) : 100=0.01%, 250=0.01%, 500=0.19%, 750=7.12%, 1000=12.91%
    lat (msec) : 2=54.42%, 4=25.28%, 10=0.07%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 250=0.01%, 500=0.01%, 2000=0.01%
  cpu          : usr=1.50%, sys=97.68%, ctx=85166, majf=0, minf=19
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=1.4%, 16=85.3%, 32=13.3%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=91.5%, 8=4.3%, 16=3.7%, 32=0.5%, 64=0.0%, >=64=0.0%
     issued    : total=r=2202186/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: io=8602.3MB, aggrb=293605KB/s, minb=293605KB/s, maxb=293605KB/s, mint=30002msec, maxt=30002msec
```

And here are results for **Control File 2**

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/da11 control.fio
random-read-4k: (g=0): rw=read, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 32 (f=32): [RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR] [100.0% done] [258.6MB/0KB/0KB /s] [66.2K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=32): err= 0: pid=101028: Sun Mar 29 23:48:25 2015
  read : io=7873.7MB, bw=268745KB/s, iops=67186, runt= 30001msec
    clat (usec): min=142, max=1137.3K, avg=475.05, stdev=1195.30
     lat (usec): min=142, max=1137.3K, avg=475.13, stdev=1195.31
    clat percentiles (usec):
     |  1.00th=[  326],  5.00th=[  354], 10.00th=[  374], 20.00th=[  394],
     | 30.00th=[  410], 40.00th=[  426], 50.00th=[  446], 60.00th=[  466],
     | 70.00th=[  490], 80.00th=[  524], 90.00th=[  596], 95.00th=[  668],
     | 99.00th=[  804], 99.50th=[  868], 99.90th=[ 1432], 99.95th=[ 2672],
     | 99.99th=[17536]
    bw (KB  /s): min=  299, max= 9288, per=3.13%, avg=8411.83, stdev=1217.48
    lat (usec) : 250=0.01%, 500=72.90%, 750=25.08%, 1000=1.82%
    lat (msec) : 2=0.14%, 4=0.03%, 10=0.02%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 2000=0.01%
  cpu          : usr=0.42%, sys=5.41%, ctx=2001658, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=2015652/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=7873.7MB, aggrb=268744KB/s, minb=268744KB/s, maxb=268744KB/s, mint=30001msec, maxt=30001msec
```

With 67,186 IOPS measured using FIO, this compares quite well with the "up to 75,000 IOPS" that Intel [claims](http://www.intel.com/content/www/us/en/solid-state-drives/solid-state-drives-dc-s3700-series.html) for this device.

#### Summary

At the block device level, the FIO performance results for 4kB pure random reads
matches well with the numbers from the Intel datasheet - but only for the DC S3700, not the P3700.

**4kB Random Read**

|                  | Intel Datasheet | FIO Measurement |  Match |
|------------------|-----------------|-----------------|--------|
|  DC S3700        | 75,000          | 67,186          |  90%   |
|  P3700           | 450,000         | 107,092         |  24%   |

So from the datasheets the P3700 should be 6x as fast as the DC S3700, however FIO only shows a 59% speedup.

At this point, we might draw two preliminary conclusions:

1. The results indicate that there is a performance issue with the NVMe devices already at the block device or device driver level.
2. For the internal SSDs, we should verify the rest of the performance numbers (random writes, sequential reads, sequential writes), but chances results are similar close, and then we can continue testing at the ZFS level.

#### More numbers

##### Control File

```console
root@s4l-zfs:~/oberstet # cat control.fio 
[global]
thread=1
ioengine=sync
direct=1
time_based=1
randrepeat=0
refill_buffers=1
end_fsync=1
size=10G
runtime=30
ramp_time=0
numjobs=32
iodepth=1

[random-read-4k]
stonewall
bs=4k
rw=randread
group_reporting

[random-write-4k]
stonewall
bs=4k
rw=randwrite
group_reporting

[sequential-read-128k]
stonewall
bs=128k
rw=read
group_reporting
 
[sequential-write-128k]
stonewall
bs=128k
rw=write
group_reporting
```

##### Intel DC S3700

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/da11 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 128 threads
...
random-read-4k: (groupid=0, jobs=32): err= 0: pid=101193: Tue Mar 31 00:11:27 2015
  read : io=6654.5MB, bw=227129KB/s, iops=56782, runt= 30001msec
    clat (usec): min=128, max=84231, avg=558.91, stdev=411.86
     lat (usec): min=128, max=84232, avg=558.99, stdev=411.86
    clat percentiles (usec):
     |  1.00th=[  306],  5.00th=[  374], 10.00th=[  414], 20.00th=[  458],
     | 30.00th=[  494], 40.00th=[  524], 50.00th=[  548], 60.00th=[  572],
     | 70.00th=[  604], 80.00th=[  636], 90.00th=[  684], 95.00th=[  724],
     | 99.00th=[  820], 99.50th=[  876], 99.90th=[ 3184], 99.95th=[ 6496],
     | 99.99th=[18816]
    bw (KB  /s): min= 4472, max= 9128, per=3.13%, avg=7112.62, stdev=889.53
    lat (usec) : 250=0.03%, 500=32.03%, 750=64.70%, 1000=2.97%
    lat (msec) : 2=0.12%, 4=0.06%, 10=0.05%, 20=0.02%, 50=0.01%
    lat (msec) : 100=0.01%
  cpu          : usr=0.44%, sys=5.99%, ctx=1688677, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=1703525/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=32): err= 0: pid=100669: Tue Mar 31 00:11:27 2015
  write: io=4892.6MB, bw=166989KB/s, iops=41747, runt= 30002msec
    clat (usec): min=60, max=8627, avg=760.18, stdev=165.76
     lat (usec): min=60, max=8627, avg=760.33, stdev=165.76
    clat percentiles (usec):
     |  1.00th=[  596],  5.00th=[  620], 10.00th=[  628], 20.00th=[  644],
     | 30.00th=[  660], 40.00th=[  692], 50.00th=[  740], 60.00th=[  780],
     | 70.00th=[  828], 80.00th=[  868], 90.00th=[  932], 95.00th=[  972],
     | 99.00th=[ 1048], 99.50th=[ 1080], 99.90th=[ 1144], 99.95th=[ 1192],
     | 99.99th=[ 8256]
    bw (KB  /s): min= 4208, max= 6304, per=3.13%, avg=5227.60, stdev=709.58
    lat (usec) : 100=0.01%, 250=0.02%, 500=0.10%, 750=51.51%, 1000=45.26%
    lat (msec) : 2=3.08%, 10=0.03%
  cpu          : usr=0.64%, sys=3.80%, ctx=1252652, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=1252499/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=32): err= 0: pid=101204: Tue Mar 31 00:11:27 2015
  read : io=12587MB, bw=429489KB/s, iops=3355, runt= 30010msec
    clat (usec): min=466, max=30094, avg=9530.53, stdev=925.16
     lat (usec): min=466, max=30094, avg=9530.97, stdev=925.02
    clat percentiles (usec):
     |  1.00th=[ 8640],  5.00th=[ 8768], 10.00th=[ 8768], 20.00th=[ 8768],
     | 30.00th=[ 8896], 40.00th=[ 8896], 50.00th=[ 9024], 60.00th=[ 9024],
     | 70.00th=[10560], 80.00th=[10688], 90.00th=[10816], 95.00th=[10944],
     | 99.00th=[11072], 99.50th=[11200], 99.90th=[11456], 99.95th=[11584],
     | 99.99th=[26496]
    bw (KB  /s): min=11912, max=15905, per=3.13%, avg=13449.43, stdev=1184.52
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=64.48%, 20=35.48%, 50=0.02%
  cpu          : usr=0.06%, sys=0.87%, ctx=101655, majf=0, minf=928
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=100695/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=32): err= 0: pid=101312: Tue Mar 31 00:11:27 2015
  write: io=11148MB, bw=380379KB/s, iops=2971, runt= 30012msec
    clat (usec): min=435, max=21292, avg=10720.00, stdev=1156.17
     lat (usec): min=435, max=21305, avg=10720.38, stdev=1156.30
    clat percentiles (usec):
     |  1.00th=[ 9408],  5.00th=[ 9664], 10.00th=[ 9664], 20.00th=[ 9792],
     | 30.00th=[ 9792], 40.00th=[10176], 50.00th=[10944], 60.00th=[11200],
     | 70.00th=[11328], 80.00th=[11456], 90.00th=[11584], 95.00th=[11840],
     | 99.00th=[12096], 99.50th=[19584], 99.90th=[20864], 99.95th=[21120],
     | 99.99th=[21120]
    bw (KB  /s): min=10730, max=13568, per=3.13%, avg=11898.62, stdev=868.81
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=37.23%, 20=62.38%, 50=0.36%
  cpu          : usr=0.42%, sys=0.50%, ctx=89720, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=89187/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=6654.5MB, aggrb=227129KB/s, minb=227129KB/s, maxb=227129KB/s, mint=30001msec, maxt=30001msec

Run status group 1 (all jobs):
  WRITE: io=4892.6MB, aggrb=166988KB/s, minb=166988KB/s, maxb=166988KB/s, mint=30002msec, maxt=30002msec

Run status group 2 (all jobs):
   READ: io=12587MB, aggrb=429488KB/s, minb=429488KB/s, maxb=429488KB/s, mint=30010msec, maxt=30010msec

Run status group 3 (all jobs):
  WRITE: io=11148MB, aggrb=380379KB/s, minb=380379KB/s, maxb=380379KB/s, mint=30012msec, maxt=30012msec
```

##### Intel P3700

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 128 threads
...
random-read-4k: (groupid=0, jobs=32): err= 0: pid=101749: Tue Mar 31 00:21:15 2015
  read : io=11319MB, bw=386345KB/s, iops=96586, runt= 30001msec
    clat (usec): min=100, max=3696, avg=329.07, stdev=53.15
     lat (usec): min=100, max=3696, avg=329.14, stdev=53.16
    clat percentiles (usec):
     |  1.00th=[  247],  5.00th=[  258], 10.00th=[  266], 20.00th=[  274],
     | 30.00th=[  286], 40.00th=[  306], 50.00th=[  330], 60.00th=[  354],
     | 70.00th=[  366], 80.00th=[  382], 90.00th=[  398], 95.00th=[  410],
     | 99.00th=[  430], 99.50th=[  438], 99.90th=[  458], 99.95th=[  466],
     | 99.99th=[  498]
    bw (KB  /s): min=10496, max=14568, per=3.13%, avg=12101.09, stdev=1492.87
    lat (usec) : 250=1.66%, 500=98.33%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%
  cpu          : usr=0.62%, sys=2.66%, ctx=2897748, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=2897682/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=32): err= 0: pid=100420: Tue Mar 31 00:21:15 2015
  write: io=13581MB, bw=463530KB/s, iops=115882, runt= 30002msec
    clat (usec): min=25, max=13300, avg=272.68, stdev=92.18
     lat (usec): min=25, max=13300, avg=272.75, stdev=92.18
    clat percentiles (usec):
     |  1.00th=[  211],  5.00th=[  225], 10.00th=[  233], 20.00th=[  245],
     | 30.00th=[  253], 40.00th=[  262], 50.00th=[  270], 60.00th=[  278],
     | 70.00th=[  290], 80.00th=[  302], 90.00th=[  314], 95.00th=[  322],
     | 99.00th=[  338], 99.50th=[  346], 99.90th=[  366], 99.95th=[  382],
     | 99.99th=[ 5728]
    bw (KB  /s): min=12640, max=17360, per=3.13%, avg=14494.35, stdev=1116.49
    lat (usec) : 50=0.01%, 100=0.06%, 250=25.02%, 500=74.89%, 750=0.01%
    lat (usec) : 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%
  cpu          : usr=1.24%, sys=5.15%, ctx=3476760, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=3476704/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=32): err= 0: pid=100424: Tue Mar 31 00:21:15 2015
  read : io=17569MB, bw=599649KB/s, iops=4684, runt= 30002msec
    clat (usec): min=482, max=11166, avg=6826.35, stdev=175.27
     lat (usec): min=482, max=11167, avg=6826.54, stdev=175.28
    clat percentiles (usec):
     |  1.00th=[ 6496],  5.00th=[ 6688], 10.00th=[ 6752], 20.00th=[ 6752],
     | 30.00th=[ 6816], 40.00th=[ 6816], 50.00th=[ 6816], 60.00th=[ 6816],
     | 70.00th=[ 6880], 80.00th=[ 6880], 90.00th=[ 6944], 95.00th=[ 7008],
     | 99.00th=[ 7072], 99.50th=[ 7200], 99.90th=[ 8512], 99.95th=[ 8896],
     | 99.99th=[ 9408]
    bw (KB  /s): min=18213, max=20571, per=3.13%, avg=18753.19, stdev=169.59
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.03%, 10=99.95%, 20=0.01%
  cpu          : usr=0.09%, sys=0.67%, ctx=141495, majf=0, minf=928
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=140552/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=32): err= 0: pid=100677: Tue Mar 31 00:21:15 2015
  write: io=16223MB, bw=553690KB/s, iops=4325, runt= 30003msec
    clat (usec): min=171, max=17915, avg=7369.70, stdev=1163.40
     lat (usec): min=171, max=17915, avg=7369.80, stdev=1163.40
    clat percentiles (usec):
     |  1.00th=[ 4512],  5.00th=[ 4704], 10.00th=[ 4768], 20.00th=[ 7392],
     | 30.00th=[ 7520], 40.00th=[ 7712], 50.00th=[ 7776], 60.00th=[ 7840],
     | 70.00th=[ 7904], 80.00th=[ 8032], 90.00th=[ 8096], 95.00th=[ 8160],
     | 99.00th=[ 8256], 99.50th=[ 8384], 99.90th=[14144], 99.95th=[15040],
     | 99.99th=[16768]
    bw (KB  /s): min=15616, max=27483, per=3.13%, avg=17332.36, stdev=3001.24
    lat (usec) : 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.02%
    lat (msec) : 2=0.05%, 4=0.06%, 10=99.62%, 20=0.25%
  cpu          : usr=0.44%, sys=0.63%, ctx=130195, majf=0, minf=0
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=129784/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=11319MB, aggrb=386344KB/s, minb=386344KB/s, maxb=386344KB/s, mint=30001msec, maxt=30001msec

Run status group 1 (all jobs):
  WRITE: io=13581MB, aggrb=463529KB/s, minb=463529KB/s, maxb=463529KB/s, mint=30002msec, maxt=30002msec

Run status group 2 (all jobs):
   READ: io=17569MB, aggrb=599648KB/s, minb=599648KB/s, maxb=599648KB/s, mint=30002msec, maxt=30002msec

Run status group 3 (all jobs):
  WRITE: io=16223MB, aggrb=553689KB/s, minb=553689KB/s, maxb=553689KB/s, mint=30003msec, maxt=30003msec
```
