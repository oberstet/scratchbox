# Linux / P3700 Block Device

## Control File

```console
extern107:~/oberstet # cat control3.fio 
[global]
thread=1
ioengine=sync
direct=1
time_based=1
randrepeat=0
norandommap
refill_buffers=1
end_fsync=1
runtime=600
ramp_time=60
numjobs=64
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

## Results

```console
extern107:~/oberstet # fio --filename /dev/nvme7n1 control3.fio 
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.13
Starting 256 threads
Jobs: 64 (f=64): [_(192),W(64)] [4.0% done] [0KB/1933MB/0KB /s] [0/15.5K/0 iops] [eta 17h:23m:08s]     ]
random-read-4k: (groupid=0, jobs=64): err= 0: pid=14962: Wed Apr  1 10:44:10 2015
  read : io=1814.7GB, bw=3096.1MB/s, iops=792803, runt=600002msec
    clat (usec): min=6, max=4279.6K, avg=78.44, stdev=1520.88
     lat (usec): min=6, max=4279.6K, avg=78.50, stdev=1520.88
    clat percentiles (usec):
     |  1.00th=[   18],  5.00th=[   27], 10.00th=[   33], 20.00th=[   41],
     | 30.00th=[   47], 40.00th=[   52], 50.00th=[   58], 60.00th=[   64],
     | 70.00th=[   71], 80.00th=[   83], 90.00th=[  122], 95.00th=[  177],
     | 99.00th=[  350], 99.50th=[  426], 99.90th=[  748], 99.95th=[ 1032],
     | 99.99th=[ 3952]
    bw (KB  /s): min=    0, max=269128, per=1.59%, avg=50463.71, stdev=17660.66
    lat (usec) : 10=0.02%, 20=1.26%, 50=33.51%, 100=51.34%, 250=11.61%
    lat (usec) : 500=1.97%, 750=0.20%, 1000=0.05%
    lat (msec) : 2=0.03%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : >=2000=0.01%
  cpu          : usr=2.27%, sys=11.03%, ctx=522973824, majf=0, minf=28356
  IO depths    : 1=110.1%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=475683588/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=64): err= 0: pid=15027: Wed Apr  1 10:44:10 2015
  write: io=979.10GB, bw=1672.5MB/s, iops=428155, runt=600002msec
    clat (usec): min=7, max=223970, avg=146.98, stdev=200.12
     lat (usec): min=7, max=223970, avg=147.07, stdev=200.12
    clat percentiles (usec):
     |  1.00th=[   15],  5.00th=[   26], 10.00th=[   36], 20.00th=[   55],
     | 30.00th=[   78], 40.00th=[  107], 50.00th=[  141], 60.00th=[  169],
     | 70.00th=[  189], 80.00th=[  209], 90.00th=[  245], 95.00th=[  290],
     | 99.00th=[  470], 99.50th=[  588], 99.90th=[ 1224], 99.95th=[ 2064],
     | 99.99th=[12224]
    bw (KB  /s): min=    0, max=39816, per=1.56%, avg=26743.17, stdev=1992.14
    lat (usec) : 10=0.01%, 20=2.45%, 50=14.89%, 100=20.34%, 250=53.11%
    lat (usec) : 500=8.38%, 750=0.58%, 1000=0.12%
    lat (msec) : 2=0.08%, 4=0.03%, 10=0.01%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 250=0.01%
  cpu          : usr=2.31%, sys=4.66%, ctx=281226324, majf=0, minf=14265
  IO depths    : 1=109.5%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=256894208/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=64): err= 0: pid=15142: Wed Apr  1 10:44:10 2015
  read : io=1427.2GB, bw=2435.7MB/s, iops=19484, runt=600004msec
    clat (usec): min=139, max=10623, avg=3282.51, stdev=1580.24
     lat (usec): min=139, max=10623, avg=3282.67, stdev=1580.25
    clat percentiles (usec):
     |  1.00th=[  684],  5.00th=[ 1020], 10.00th=[ 1304], 20.00th=[ 1768],
     | 30.00th=[ 2160], 40.00th=[ 2608], 50.00th=[ 3120], 60.00th=[ 3600],
     | 70.00th=[ 4128], 80.00th=[ 4768], 90.00th=[ 5600], 95.00th=[ 6048],
     | 99.00th=[ 6688], 99.50th=[ 6880], 99.90th=[ 7456], 99.95th=[ 7712],
     | 99.99th=[ 8384]
    bw (KB  /s): min=    2, max=51968, per=1.56%, avg=38975.74, stdev=4440.38
    lat (usec) : 250=0.01%, 500=0.20%, 750=1.31%, 1000=3.19%
    lat (msec) : 2=21.03%, 4=41.40%, 10=32.87%, 20=0.01%
  cpu          : usr=0.11%, sys=1.10%, ctx=12747653, majf=0, minf=23314
  IO depths    : 1=109.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=11691026/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=64): err= 0: pid=15233: Wed Apr  1 10:44:10 2015
  write: io=1132.1GB, bw=1933.6MB/s, iops=15468, runt=600007msec
    clat (usec): min=54, max=27286, avg=4095.23, stdev=3278.33
     lat (usec): min=54, max=27286, avg=4095.47, stdev=3278.32
    clat percentiles (usec):
     |  1.00th=[   71],  5.00th=[   92], 10.00th=[  126], 20.00th=[  474],
     | 30.00th=[ 1176], 40.00th=[ 2384], 50.00th=[ 3920], 60.00th=[ 5408],
     | 70.00th=[ 6560], 80.00th=[ 7328], 90.00th=[ 8256], 95.00th=[ 9024],
     | 99.00th=[10816], 99.50th=[12352], 99.90th=[19072], 99.95th=[20608],
     | 99.99th=[22144]
    bw (KB  /s): min=    2, max=33536, per=1.56%, avg=30940.76, stdev=1011.21
    lat (usec) : 100=6.45%, 250=8.81%, 500=5.21%, 750=3.97%, 1000=3.44%
    lat (msec) : 2=9.27%, 4=13.39%, 10=47.59%, 20=1.81%, 50=0.07%
  cpu          : usr=1.21%, sys=0.41%, ctx=10212277, majf=0, minf=27808
  IO depths    : 1=110.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=9281312/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=1814.7GB, aggrb=3096.1MB/s, minb=3096.1MB/s, maxb=3096.1MB/s, mint=600002msec, maxt=600002msec

Run status group 1 (all jobs):
  WRITE: io=979.10GB, aggrb=1672.5MB/s, minb=1672.5MB/s, maxb=1672.5MB/s, mint=600002msec, maxt=600002msec

Run status group 2 (all jobs):
   READ: io=1427.2GB, aggrb=2435.7MB/s, minb=2435.7MB/s, maxb=2435.7MB/s, mint=600004msec, maxt=600004msec

Run status group 3 (all jobs):
  WRITE: io=1132.1GB, aggrb=1933.6MB/s, minb=1933.6MB/s, maxb=1933.6MB/s, mint=600007msec, maxt=600007msec

Disk stats (read/write):
  nvme7n1: ios=536373720/291424691, merge=0/0, ticks=78033148/81038384, in_queue=165009804, util=100.00%
```
