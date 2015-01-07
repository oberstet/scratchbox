

Using default IO engine with 1 worker and IO depth 1:

```
[rnd-write]
rw=randwrite
size=10G
thread=1
filename=/test/test.fio
ioengine=sync
direct=1
numjobs=1
iodepth=1
group_reporting
bs=8k
runtime=600
time_based=1
ramp_time=30
```

**1 Worker:**

```
rnd-write: (g=0): rw=randwrite, bs=8K-8K/8K-8K/8K-8K, ioengine=sync, iodepth=1
fio-2.1.9
Starting 1 thread
Jobs: 1 (f=1): [w] [100.0% done] [0KB/68569KB/0KB /s] [0/8571/0 iops] [eta 00m:00s]m:08s]
rnd-write: (groupid=0, jobs=1): err= 0: pid=101076: Wed Jan  7 11:51:25 2015
  write: io=49171MB, bw=83825KB/s, iops=10478, runt=600673msec
    clat (usec): min=6, max=3078.3K, avg=94.52, stdev=8716.24
     lat (usec): min=6, max=3078.3K, avg=94.59, stdev=8716.24
    clat percentiles (usec):
     |  1.00th=[    8],  5.00th=[    9], 10.00th=[    9], 20.00th=[    9],
     | 30.00th=[   10], 40.00th=[   10], 50.00th=[   10], 60.00th=[   11],
     | 70.00th=[   14], 80.00th=[   16], 90.00th=[   16], 95.00th=[   17],
     | 99.00th=[   18], 99.50th=[   19], 99.90th=[   41], 99.95th=[  532],
     | 99.99th=[61696]
    bw (KB  /s): min=    0, max=196000, per=100.00%, avg=86447.97, stdev=25890.95
    lat (usec) : 10=24.75%, 20=74.95%, 50=0.20%, 100=0.01%, 250=0.01%
    lat (usec) : 500=0.02%, 750=0.05%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2000=0.01%, >=2000=0.01%
  cpu          : usr=0.83%, sys=13.65%, ctx=13857, majf=0, minf=0
  IO depths    : 1=105.9%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=6293900/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: io=49171MB, aggrb=83824KB/s, minb=83824KB/s, maxb=83824KB/s, mint=600673msec, maxt=600673msec
```

**4 Workers:**

```
rnd-write: (g=0): rw=randwrite, bs=8K-8K/8K-8K/8K-8K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 4 threads
Jobs: 4 (f=4): [wwww] [84.6% done] [0KB/0KB/0KB /s] [0/0/0 iops] [eta 01m:37s]
Jobs: 4 (f=4): [wwww] [83.6% done] [0KB/68752KB/0KB /s] [0/8594/0 iops] [eta 02m:04s]
rnd-write: (groupid=0, jobs=4): err= 0: pid=101078: Wed Jan  7 12:05:35 2015
  write: io=35544MB, bw=60581KB/s, iops=7572, runt=600803msec
    clat (usec): min=5, max=3085.4K, avg=526.72, stdev=23801.87
     lat (usec): min=5, max=3085.4K, avg=526.82, stdev=23802.00
    clat percentiles (usec):
     |  1.00th=[   10],  5.00th=[   12], 10.00th=[   13], 20.00th=[   14],
     | 30.00th=[   14], 40.00th=[   15], 50.00th=[   15], 60.00th=[   15],
     | 70.00th=[   16], 80.00th=[   17], 90.00th=[   18], 95.00th=[   19],
     | 99.00th=[   22], 99.50th=[   23], 99.90th=[  668], 99.95th=[54016],
     | 99.99th=[1155072]
    bw (KB  /s): min=    0, max=80763, per=26.66%, avg=16148.43, stdev=8988.14
    lat (usec) : 10=0.53%, 20=95.13%, 50=4.22%, 100=0.01%, 250=0.01%
    lat (usec) : 500=0.01%, 750=0.03%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
    lat (msec) : 100=0.01%, 500=0.01%, 750=0.01%, 1000=0.02%, 2000=0.02%
    lat (msec) : >=2000=0.01%
  cpu          : usr=0.20%, sys=3.17%, ctx=9707, majf=0, minf=0
  IO depths    : 1=107.5%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=4549657/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: io=35544MB, aggrb=60581KB/s, minb=60581KB/s, maxb=60581KB/s, mint=600803msec, maxt=600803msec
```


