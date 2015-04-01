# FreeBSD / P3700 Block Device

## Control File

```console
root@s4l-zfs:~/oberstet # cat control4.fio 
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
root@s4l-zfs:~/oberstet # fio --filename=/dev/nvd7 control4.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 256 threads
...
random-read-4k: (groupid=0, jobs=64): err= 0: pid=100423: Wed Apr  1 14:52:18 2015
  read : io=237902MB, bw=406018KB/s, iops=101504, runt=600002msec
    clat (usec): min=33, max=400858, avg=628.75, stdev=653.69
     lat (usec): min=34, max=400858, avg=628.81, stdev=653.69
    clat percentiles (usec):
     |  1.00th=[  430],  5.00th=[  470], 10.00th=[  494], 20.00th=[  532],
     | 30.00th=[  556], 40.00th=[  580], 50.00th=[  604], 60.00th=[  636],
     | 70.00th=[  668], 80.00th=[  716], 90.00th=[  780], 95.00th=[  836],
     | 99.00th=[ 1032], 99.50th=[ 1208], 99.90th=[ 1592], 99.95th=[ 1832],
     | 99.99th=[ 3184]
    bw (KB  /s): min=    0, max= 8288, per=1.56%, avg=6345.81, stdev=603.61
    lat (usec) : 50=0.01%, 100=0.01%, 250=0.01%, 500=11.13%, 750=74.56%
    lat (usec) : 1000=13.11%
    lat (msec) : 2=1.15%, 4=0.04%, 10=0.01%, 50=0.01%, 500=0.01%
  cpu          : usr=0.32%, sys=1.29%, ctx=66943539, majf=0, minf=64
  IO depths    : 1=109.9%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=60902872/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=64): err= 0: pid=101902: Wed Apr  1 14:52:18 2015
  write: io=265841MB, bw=453700KB/s, iops=113425, runt=600002msec
    clat (usec): min=20, max=37032, avg=561.37, stdev=174.14
     lat (usec): min=20, max=37032, avg=561.44, stdev=174.14
    clat percentiles (usec):
     |  1.00th=[  390],  5.00th=[  418], 10.00th=[  438], 20.00th=[  466],
     | 30.00th=[  498], 40.00th=[  532], 50.00th=[  548], 60.00th=[  564],
     | 70.00th=[  588], 80.00th=[  644], 90.00th=[  716], 95.00th=[  764],
     | 99.00th=[  828], 99.50th=[  844], 99.90th=[  884], 99.95th=[  908],
     | 99.99th=[10432]
    bw (KB  /s): min=    0, max= 9424, per=1.56%, avg=7087.51, stdev=1115.63
    lat (usec) : 50=0.01%, 100=0.01%, 250=0.01%, 500=30.15%, 750=63.25%
    lat (usec) : 1000=6.56%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
  cpu          : usr=0.56%, sys=1.98%, ctx=74266818, majf=0, minf=0
  IO depths    : 1=109.1%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=68055278/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=64): err= 0: pid=101854: Wed Apr  1 14:52:18 2015
  read : io=440529MB, bw=751823KB/s, iops=5873, runt=600010msec
    clat (usec): min=268, max=20805, avg=10892.52, stdev=1464.72
     lat (usec): min=268, max=20806, avg=10892.77, stdev=1464.74
    clat percentiles (usec):
     |  1.00th=[ 5984],  5.00th=[ 8160], 10.00th=[ 9408], 20.00th=[10048],
     | 30.00th=[10432], 40.00th=[10688], 50.00th=[10944], 60.00th=[11200],
     | 70.00th=[11456], 80.00th=[11840], 90.00th=[12352], 95.00th=[12992],
     | 99.00th=[14528], 99.50th=[14912], 99.90th=[15936], 99.95th=[16512],
     | 99.99th=[18304]
    bw (KB  /s): min=    2, max=14671, per=1.56%, avg=11748.79, stdev=1040.09
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=17.87%, 20=82.12%, 50=0.01%
  cpu          : usr=0.06%, sys=0.41%, ctx=3805722, majf=0, minf=1856
  IO depths    : 1=107.8%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=3524228/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=64): err= 0: pid=101851: Wed Apr  1 14:52:18 2015
  write: io=347954MB, bw=593832KB/s, iops=4639, runt=600009msec
    clat (usec): min=276, max=27372, avg=13764.13, stdev=707.03
     lat (usec): min=276, max=27372, avg=13764.24, stdev=707.02
    clat percentiles (usec):
     |  1.00th=[12608],  5.00th=[12992], 10.00th=[13120], 20.00th=[13248],
     | 30.00th=[13376], 40.00th=[13504], 50.00th=[13632], 60.00th=[13760],
     | 70.00th=[14016], 80.00th=[14400], 90.00th=[14656], 95.00th=[14912],
     | 99.00th=[15296], 99.50th=[15424], 99.90th=[18048], 99.95th=[19584],
     | 99.99th=[21888]
    bw (KB  /s): min=    2, max= 9788, per=1.56%, avg=9279.97, stdev=434.70
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.14%, 20=99.81%, 50=0.04%
  cpu          : usr=0.28%, sys=0.35%, ctx=3113061, majf=0, minf=0
  IO depths    : 1=111.8%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=2783631/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=237902MB, aggrb=406017KB/s, minb=406017KB/s, maxb=406017KB/s, mint=600002msec, maxt=600002msec

Run status group 1 (all jobs):
  WRITE: io=265841MB, aggrb=453700KB/s, minb=453700KB/s, maxb=453700KB/s, mint=600002msec, maxt=600002msec

Run status group 2 (all jobs):
   READ: io=440529MB, aggrb=751822KB/s, minb=751822KB/s, maxb=751822KB/s, mint=600010msec, maxt=600010msec

Run status group 3 (all jobs):
  WRITE: io=347954MB, aggrb=593832KB/s, minb=593832KB/s, maxb=593832KB/s, mint=600009msec, maxt=600009msec
```

# FreeBSD / DC S3700

## Control File

Same as above.

## Results

```console
```
