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
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 32 -o read -s 512 -t 30 nvme0ns1
Threads: 32 Size:    512  READ Time:  30 IO/s:   95797 MB/s:   46
```

When running with a 4KB block size we get:

```console
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 32 -o read -s 4096 -t 30 nvme0ns1
Threads: 32 Size:   4096  READ Time:  30 IO/s:  126968 MB/s:  495
```

Interestingly, the numbers for 4KB are higher than for 512 bytes requests.

Here are results with increasing number of threads performing I/O requests:

```console
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 1 -o read -s 4096 -t 30 nvme0ns1
Threads:  1 Size:   4096  READ Time:  30 IO/s:   22565 MB/s:   88
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 2 -o read -s 4096 -t 30 nvme0ns1
Threads:  2 Size:   4096  READ Time:  30 IO/s:   43968 MB/s:  171
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 4 -o read -s 4096 -t 30 nvme0ns1
Threads:  4 Size:   4096  READ Time:  30 IO/s:   78263 MB/s:  305
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 8 -o read -s 4096 -t 30 nvme0ns1
Threads:  8 Size:   4096  READ Time:  30 IO/s:  122422 MB/s:  478
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 16 -o read -s 4096 -t 30 nvme0ns1
Threads: 16 Size:   4096  READ Time:  30 IO/s:  128345 MB/s:  501
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 32 -o read -s 4096 -t 30 nvme0ns1
Threads: 32 Size:   4096  READ Time:  30 IO/s:  126968 MB/s:  495
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 48 -o read -s 4096 -t 30 nvme0ns1
Threads: 48 Size:   4096  READ Time:  30 IO/s:  125945 MB/s:  491
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 64 -o read -s 4096 -t 30 nvme0ns1
Threads: 64 Size:   4096  READ Time:  30 IO/s:  125385 MB/s:  489
root@s4l-zfs:~/oberstet # nvmecontrol perftest -n 96 -o read -s 4096 -t 30 nvme0ns1
Threads: 96 Size:   4096  READ Time:  30 IO/s:   94188 MB/s:  367
```

The peak performance in IOPS is reached at 16 threads. The is far beyond the IO queue depth of 128 which the NVMe device has. The peak performance of 128,345 IOPS is also far less than the 450,000 IOPS Intel claims for the device - 28% of the claimed performance. Mmh.

Lets do a quick test using FIO and see what we can get there for a pure 4KB random read workload.

Using this control file

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
rw=read

[random-read-4k]
numjobs=4
iodepth=32
group_reporting
```

we get 

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control.fio
random-read-4k: (g=0): rw=read, bs=4K-4K/4K-4K/4K-4K, ioengine=posixaio, iodepth=32
...
fio-2.1.9
Starting 4 threads
Jobs: 4 (f=4): [RRRR] [100.0% done] [327.5MB/0KB/0KB /s] [83.8K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=4): err= 0: pid=101035: Sun Mar 29 23:37:56 2015
  read : io=10216MB, bw=348685KB/s, iops=87171, runt= 30002msec
    slat (usec): min=1, max=253, avg=13.38, stdev=10.00
    clat (usec): min=223, max=5266, avg=1362.70, stdev=445.07
     lat (usec): min=249, max=5320, avg=1376.09, stdev=443.27
    clat percentiles (usec):
     |  1.00th=[  524],  5.00th=[  612], 10.00th=[  700], 20.00th=[  932],
     | 30.00th=[ 1112], 40.00th=[ 1272], 50.00th=[ 1416], 60.00th=[ 1528],
     | 70.00th=[ 1624], 80.00th=[ 1720], 90.00th=[ 1912], 95.00th=[ 2064],
     | 99.00th=[ 2352], 99.50th=[ 2480], 99.90th=[ 2832], 99.95th=[ 2960],
     | 99.99th=[ 3344]
    bw (KB  /s): min=63600, max=104496, per=25.05%, avg=87341.55, stdev=9264.77
    lat (usec) : 250=0.01%, 500=0.51%, 750=11.62%, 1000=11.05%
    lat (msec) : 2=69.72%, 4=7.10%, 10=0.01%
  cpu          : usr=1.22%, sys=98.70%, ctx=15029, majf=0, minf=80
  IO depths    : 1=0.1%, 2=0.1%, 4=0.6%, 8=3.9%, 16=85.6%, 32=9.9%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=92.1%, 8=2.8%, 16=4.1%, 32=1.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=2615310/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: io=10216MB, aggrb=348684KB/s, minb=348684KB/s, maxb=348684KB/s, mint=30002msec, maxt=30002msec
```

FIO measures 84,647 IOPS. nvmecontrol says 128,345 IOPS. And Intel says 450,000 IOPS. Mmmmh.

> Using the **posixaio* engine of FIO above was the fastest run of varying numjobs and iodepth.

Further, look at the CPU load. The AIO implementation in the FreeBSD Posix layer seems to incur some overhead.

Here is what we get using the **sync** engine of FIO (fastest parameters) by setting `ioengine=sync` in the control file:

```console
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control.fio
random-read-4k: (g=0): rw=read, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 32 (f=32): [RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR] [100.0% done] [342.4MB/0KB/0KB /s] [87.7K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=32): err= 0: pid=101033: Sun Mar 29 23:41:04 2015
  read : io=8900.2MB, bw=303780KB/s, iops=75945, runt= 30001msec
    clat (usec): min=60, max=3515, avg=420.06, stdev=60.56
     lat (usec): min=60, max=3515, avg=420.15, stdev=60.57
    clat percentiles (usec):
     |  1.00th=[  318],  5.00th=[  342], 10.00th=[  354], 20.00th=[  366],
     | 30.00th=[  378], 40.00th=[  398], 50.00th=[  418], 60.00th=[  438],
     | 70.00th=[  454], 80.00th=[  474], 90.00th=[  490], 95.00th=[  506],
     | 99.00th=[  540], 99.50th=[  556], 99.90th=[  636], 99.95th=[  724],
     | 99.99th=[ 1320]
    bw (KB  /s): min= 8160, max=11232, per=3.12%, avg=9475.23, stdev=846.42
    lat (usec) : 100=0.01%, 250=0.05%, 500=93.62%, 750=6.29%, 1000=0.02%
    lat (msec) : 2=0.01%, 4=0.01%
  cpu          : usr=0.52%, sys=2.92%, ctx=2278909, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=2278428/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=8900.2MB, aggrb=303780KB/s, minb=303780KB/s, maxb=303780KB/s, mint=30001msec, maxt=30001msec
```

The CPU load is negliable, the latencies are very flat and with 79,945 IOPS the throughput is only marginally less than using AIO.

However, now we finally have arrived at 80k / 450k or roughly 18% of the datesheet performance. And this is at the filesystem level.

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

Here are FIO results using the exact same control file as above:


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

|                  | Intel Datasheet | FIO Measurement |  Match |
|------------------|-----------------|-----------------|--------|
|  DC S3700        | 75,000          | 67,186          |  90%   |
|  P3700           | 450,000         | 75,945          |  17%   |

The results indicate that there is a performance issue with the NVMe devices already at the block device or device driver level.

For the internal SSDs, we can continue testing at the ZFS level after we have verified the rest of the datasheet numbers at the block device level.