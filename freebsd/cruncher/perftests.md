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
filename=/dev/nvd0
ioengine=posixaio
#ioengine=sync
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
root@s4l-zfs:~/oberstet # fio control.fio
random-read-4k: (g=0): rw=read, bs=4K-4K/4K-4K/4K-4K, ioengine=posixaio, iodepth=32
...
fio-2.1.9
Starting 4 threads
Jobs: 4 (f=4): [RRRR] [100.0% done] [330.3MB/0KB/0KB /s] [84.6K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=4): err= 0: pid=102081: Sun Mar 29 23:02:25 2015
  read : io=9920.3MB, bw=338589KB/s, iops=84647, runt= 30002msec
    slat (usec): min=1, max=285, avg=11.76, stdev= 7.76
    clat (usec): min=261, max=4989, avg=1431.39, stdev=430.32
     lat (usec): min=271, max=5015, avg=1443.15, stdev=427.03
    clat percentiles (usec):
     |  1.00th=[  572],  5.00th=[  692], 10.00th=[  796], 20.00th=[  980],
     | 30.00th=[ 1160], 40.00th=[ 1400], 50.00th=[ 1528], 60.00th=[ 1608],
     | 70.00th=[ 1704], 80.00th=[ 1800], 90.00th=[ 1944], 95.00th=[ 2064],
     | 99.00th=[ 2256], 99.50th=[ 2320], 99.90th=[ 2544], 99.95th=[ 2704],
     | 99.99th=[ 3568]
    bw (KB  /s): min=58024, max=91504, per=25.01%, avg=84686.41, stdev=3869.77
    lat (usec) : 500=0.13%, 750=7.42%, 1000=13.74%
    lat (msec) : 2=71.29%, 4=7.42%, 10=0.01%
  cpu          : usr=1.14%, sys=98.80%, ctx=11430, majf=0, minf=33
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=1.6%, 16=87.7%, 32=10.5%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=91.5%, 8=3.2%, 16=4.8%, 32=0.5%, 64=0.0%, >=64=0.0%
     issued    : total=r=2539587/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=32

Run status group 0 (all jobs):
   READ: io=9920.3MB, aggrb=338589KB/s, minb=338589KB/s, maxb=338589KB/s, mint=30002msec, maxt=30002msec
```

FIO measures 84,647 IOPS. nvmecontrol says 128,345 IOPS. And Intel says 450,000 IOPS. Mmmmh.

> Using the **posixaio* engine of FIO above was the fastest run of varying numjobs and iodepth.

Here is what we get using the **sync** engine of FIO (fastest parameters):

```console
root@s4l-zfs:~/oberstet # fio control.fio
random-read-4k: (g=0): rw=read, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 32 (f=32): [RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR] [100.0% done] [307.6MB/0KB/0KB /s] [78.8K/0/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=32): err= 0: pid=100457: Sun Mar 29 23:16:20 2015
  read : io=9182.9MB, bw=313429KB/s, iops=78357, runt= 30001msec
    clat (usec): min=33, max=4039, avg=406.86, stdev=132.64
     lat (usec): min=33, max=4039, avg=406.96, stdev=132.65
    clat percentiles (usec):
     |  1.00th=[  163],  5.00th=[  247], 10.00th=[  286], 20.00th=[  326],
     | 30.00th=[  358], 40.00th=[  382], 50.00th=[  406], 60.00th=[  426],
     | 70.00th=[  446], 80.00th=[  474], 90.00th=[  506], 95.00th=[  540],
     | 99.00th=[  812], 99.50th=[ 1004], 99.90th=[ 1608], 99.95th=[ 2768],
     | 99.99th=[ 3312]
    bw (KB  /s): min= 8024, max=12880, per=3.13%, avg=9804.22, stdev=1227.31
    lat (usec) : 50=0.01%, 100=0.10%, 250=5.24%, 500=83.24%, 750=10.11%
    lat (usec) : 1000=0.79%
    lat (msec) : 2=0.44%, 4=0.07%, 10=0.01%
  cpu          : usr=0.60%, sys=3.88%, ctx=2351228, majf=0, minf=32
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=2350797/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=9182.9MB, aggrb=313429KB/s, minb=313429KB/s, maxb=313429KB/s, mint=30001msec, maxt=30001msec
```
