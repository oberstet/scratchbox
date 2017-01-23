# FIO on ramdisk

## Xeon E3 machine

Here is testing IO performance on a small Xeon E3 machine running a stock FreeBSD 10.1 kernel:

```console
root@brummer2:/home/oberstet # uname -a
FreeBSD brummer2 10.1-RELEASE-p6 FreeBSD 10.1-RELEASE-p6 #0: Tue Feb 24 19:00:21 UTC 2015     root@amd64-builder.daemonology.net:/usr/obj/usr/src/sys/GENERIC  amd64
root@brummer2:/home/oberstet # sysctl hw.physmem
hw.physmem: 34265112576
root@brummer2:/home/oberstet # sysctl hw.model
hw.model: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
root@brummer2:/home/oberstet # sysctl hw.physmem
hw.physmem: 34265112576
``` 

Create a 1GB ramdisk:

```console
root@brummer2:/home/oberstet # mdconfig -a -t swap -s 1g
md0
root@brummer2:/home/oberstet # dd if=/dev/zero of=/dev/md0 bs=1m count=1k
1024+0 records in
1024+0 records out
1073741824 bytes transferred in 0.271545 secs (3954192288 bytes/sec)
```

Using `randomio` to verify single-threaded performance:

```console
root@brummer2:/home/oberstet # randomio /dev/md0 1 0 0 4096 2
  total |  read:         latency (ms)       |  write:        latency (ms)
   iops |   iops   min    avg    max   sdev |   iops   min    avg    max   sdev
--------+-----------------------------------+----------------------------------
194061.8 |194061.8   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
193431.6 |193431.6   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
192262.1 |192262.1   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
193017.6 |193017.6   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
192865.5 |192865.5   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
^C
```

Checking multi-threaded performance:


```console
root@brummer2:/home/oberstet # randomio /dev/md0 20 0.5 0 4096 2
  total |  read:         latency (ms)       |  write:        latency (ms)
   iops |   iops   min    avg    max   sdev |   iops   min    avg    max   sdev
--------+-----------------------------------+----------------------------------
551761.2 |276048.8   0.0    0.0    0.1    0.0 |275712.5   0.0    0.0    0.1    0.0
553759.3 |276719.4   0.0    0.0    0.1    0.0 |277039.9   0.0    0.0    0.1    0.0
552447.6 |276812.7   0.0    0.0    0.1    0.0 |275634.9   0.0    0.0    0.1    0.0
553411.7 |276757.3   0.0    0.0    0.1    0.0 |276654.4   0.0    0.0    0.1    0.0
552220.9 |276528.5   0.0    0.0    0.1    0.0 |275692.4   0.0    0.0    0.1    0.0
^C
```

Checking performance using FIO:

```console
root@brummer2:/home/oberstet # cat control.fio 
[global]
thread=1
ioengine=sync
direct=1
time_based=1
randrepeat=0
norandommap
refill_buffers=1
end_fsync=1
runtime=60
ramp_time=10
numjobs=8
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
root@brummer2:/home/oberstet # fio --filename /dev/md0 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 8 (f=8): [________________________WWWWWWWW] [100.0% done] [0KB/7354MB/0KB /s] [0/58.9K/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=8): err= 0: pid=100981: Thu Apr  2 11:40:13 2015
  read : io=126363MB, bw=2106.2MB/s, iops=539139, runt= 60001msec
    clat (usec): min=3, max=70, avg=13.73, stdev= 5.47
     lat (usec): min=3, max=70, avg=13.77, stdev= 5.47
    clat percentiles (usec):
     |  1.00th=[    4],  5.00th=[    6], 10.00th=[    7], 20.00th=[    8],
     | 30.00th=[   10], 40.00th=[   12], 50.00th=[   14], 60.00th=[   15],
     | 70.00th=[   17], 80.00th=[   19], 90.00th=[   21], 95.00th=[   23],
     | 99.00th=[   27], 99.50th=[   28], 99.90th=[   31], 99.95th=[   32],
     | 99.99th=[   35]
    bw (KB  /s): min=    1, max=272656, per=12.39%, avg=267098.46, stdev=25744.54
    lat (usec) : 4=0.01%, 10=27.45%, 20=56.24%, 50=16.31%, 100=0.01%
  cpu          : usr=9.04%, sys=21.13%, ctx=37714147, majf=0, minf=8
  IO depths    : 1=116.6%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=32348901/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=8): err= 0: pid=100989: Thu Apr  2 11:40:13 2015
  write: io=123158MB, bw=2052.7MB/s, iops=525466, runt= 60001msec
    clat (usec): min=4, max=85, avg=13.48, stdev= 5.26
     lat (usec): min=4, max=85, avg=13.52, stdev= 5.26
    clat percentiles (usec):
     |  1.00th=[    5],  5.00th=[    6], 10.00th=[    7], 20.00th=[    8],
     | 30.00th=[   10], 40.00th=[   12], 50.00th=[   13], 60.00th=[   15],
     | 70.00th=[   16], 80.00th=[   18], 90.00th=[   21], 95.00th=[   23],
     | 99.00th=[   26], 99.50th=[   28], 99.90th=[   31], 99.95th=[   32],
     | 99.99th=[   35]
    bw (KB  /s): min=    1, max=265888, per=12.38%, avg=260260.70, stdev=25318.57
    lat (usec) : 10=28.61%, 20=57.27%, 50=14.12%, 100=0.01%
  cpu          : usr=13.61%, sys=20.93%, ctx=36792156, majf=0, minf=0
  IO depths    : 1=116.7%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=31528530/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=8): err= 0: pid=100997: Thu Apr  2 11:40:13 2015
  read : io=459247MB, bw=7653.2MB/s, iops=61231, runt= 60001msec
    clat (usec): min=102, max=165, avg=129.98, stdev= 0.80
     lat (usec): min=102, max=165, avg=130.01, stdev= 0.80
    clat percentiles (usec):
     |  1.00th=[  129],  5.00th=[  129], 10.00th=[  129], 20.00th=[  129],
     | 30.00th=[  131], 40.00th=[  131], 50.00th=[  131], 60.00th=[  131],
     | 70.00th=[  131], 80.00th=[  131], 90.00th=[  131], 95.00th=[  131],
     | 99.00th=[  133], 99.50th=[  133], 99.90th=[  135], 99.95th=[  135],
     | 99.99th=[  139]
    bw (KB  /s): min=294656, max=983808, per=12.42%, avg=973727.43, stdev=64352.98
    lat (usec) : 250=100.00%
  cpu          : usr=0.87%, sys=3.13%, ctx=4285299, majf=0, minf=232
  IO depths    : 1=116.6%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=3673976/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=8): err= 0: pid=101005: Thu Apr  2 11:40:13 2015
  write: io=443046MB, bw=7383.1MB/s, iops=59071, runt= 60001msec
    clat (usec): min=53, max=208, avg=115.27, stdev= 2.36
     lat (usec): min=53, max=209, avg=115.32, stdev= 2.36
    clat percentiles (usec):
     |  1.00th=[  112],  5.00th=[  112], 10.00th=[  112], 20.00th=[  113],
     | 30.00th=[  113], 40.00th=[  114], 50.00th=[  115], 60.00th=[  116],
     | 70.00th=[  117], 80.00th=[  118], 90.00th=[  118], 95.00th=[  119],
     | 99.00th=[  120], 99.50th=[  120], 99.90th=[  121], 99.95th=[  123],
     | 99.99th=[  137]
    bw (KB  /s): min=  139, max=960512, per=12.39%, avg=936601.73, stdev=90340.49
    lat (usec) : 100=0.01%, 250=100.00%
  cpu          : usr=17.69%, sys=3.43%, ctx=4129396, majf=0, minf=0
  IO depths    : 1=116.5%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=3544368/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=126363MB, aggrb=2106.2MB/s, minb=2106.2MB/s, maxb=2106.2MB/s, mint=60001msec, maxt=60001msec

Run status group 1 (all jobs):
  WRITE: io=123158MB, aggrb=2052.7MB/s, minb=2052.7MB/s, maxb=2052.7MB/s, mint=60001msec, maxt=60001msec

Run status group 2 (all jobs):
   READ: io=459247MB, aggrb=7653.2MB/s, minb=7653.2MB/s, maxb=7653.2MB/s, mint=60001msec, maxt=60001msec

Run status group 3 (all jobs):
  WRITE: io=443046MB, aggrb=7383.1MB/s, minb=7383.1MB/s, maxb=7383.1MB/s, mint=60001msec, maxt=60001msec
root@brummer2:/home/oberstet # 
```

Delete the ramdisk:

```console
mdconfig -d -u 0 
```

## 48 core big machine

```console
root@s4l-zfs:~ # mdconfig -a -t swap -s 1g
md0
root@s4l-zfs:~ # dd if=/dev/zero of=/dev/md0 bs=1m count=1k
1024+0 records in
1024+0 records out
1073741824 bytes transferred in 2.394976 secs (448330951 bytes/sec)
```

```console
root@s4l-zfs:~ # mdconfig -a -t swap -s 1g
md0
root@s4l-zfs:~ # dd if=/dev/zero of=/dev/md0 bs=1m count=1k
1024+0 records in
1024+0 records out
1073741824 bytes transferred in 2.317714 secs (463276243 bytes/sec)
root@s4l-zfs:~ # randomio /dev/md0 1 0 0 4096 2
  total |  read:         latency (ms)       |  write:        latency (ms)
   iops |   iops   min    avg    max   sdev |   iops   min    avg    max   sdev
--------+-----------------------------------+----------------------------------
58594.8 |58594.8   0.0    0.0    0.1    0.0 |    0.0   inf    nan    0.0    nan
70131.1 |70131.1   0.0    0.0    0.2    0.0 |    0.0   inf    nan    0.0    nan
76805.0 |76805.0   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
77839.5 |77839.5   0.0    0.0    0.1    0.0 |    0.0   inf    nan    0.0    nan
79377.3 |79377.3   0.0    0.0    0.0    0.0 |    0.0   inf    nan    0.0    nan
^C
root@s4l-zfs:~ # randomio /dev/md0 20 0.5 0 4096 2
  total |  read:         latency (ms)       |  write:        latency (ms)
   iops |   iops   min    avg    max   sdev |   iops   min    avg    max   sdev
--------+-----------------------------------+----------------------------------
47768.7 |23966.3   0.0    0.4    1.2    0.2 |23802.4   0.0    0.4    1.3    0.2
46538.1 |23266.8   0.0    0.4    1.3    0.2 |23271.3   0.0    0.4    1.4    0.2
45982.2 |22976.7   0.0    0.4    1.4    0.2 |23005.4   0.0    0.4    1.4    0.2
45744.5 |22953.2   0.0    0.4    1.4    0.2 |22791.3   0.0    0.4    1.4    0.2
45858.3 |22969.6   0.0    0.4    1.3    0.2 |22888.6   0.0    0.4    1.4    0.2
45567.9 |22911.9   0.0    0.4    1.4    0.2 |22656.0   0.0    0.4    1.3    0.2
^C
root@s4l-zfs:~ # cat control.fio 
[global]
thread=1
ioengine=sync
direct=1
time_based=1
randrepeat=0
norandommap
refill_buffers=1
end_fsync=1
runtime=60
ramp_time=10
numjobs=8
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
root@s4l-zfs:~ # fio --filename /dev/md0 control.fio
random-read-4k: (g=0): rw=randread, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
random-write-4k: (g=1): rw=randwrite, bs=4K-4K/4K-4K/4K-4K, ioengine=sync, iodepth=1
...
sequential-read-128k: (g=2): rw=read, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
sequential-write-128k: (g=3): rw=write, bs=128K-128K/128K-128K/128K-128K, ioengine=sync, iodepth=1
...
fio-2.1.9
Starting 32 threads
Jobs: 8 (f=8): [________________________WWWWWWWW] [100.0% done] [0KB/1269MB/0KB /s] [0/10.2K/0 iops] [eta 00m:00s]
random-read-4k: (groupid=0, jobs=8): err= 0: pid=101259: Thu Apr  2 15:42:36 2015
  read : io=54494MB, bw=930022KB/s, iops=232505, runt= 60001msec
    clat (usec): min=4, max=941, avg=33.04, stdev=14.87
     lat (usec): min=4, max=942, avg=33.10, stdev=14.87
    clat percentiles (usec):
     |  1.00th=[    8],  5.00th=[   11], 10.00th=[   14], 20.00th=[   18],
     | 30.00th=[   23], 40.00th=[   28], 50.00th=[   32], 60.00th=[   37],
     | 70.00th=[   41], 80.00th=[   46], 90.00th=[   53], 95.00th=[   58],
     | 99.00th=[   69], 99.50th=[   73], 99.90th=[   83], 99.95th=[   89],
     | 99.99th=[  114]
    bw (KB  /s): min=    5, max=129072, per=12.42%, avg=115519.67, stdev=10076.13
    lat (usec) : 10=2.28%, 20=19.71%, 50=63.40%, 100=14.58%, 250=0.03%
    lat (usec) : 500=0.01%, 750=0.01%, 1000=0.01%
  cpu          : usr=5.14%, sys=18.92%, ctx=16144006, majf=0, minf=8
  IO depths    : 1=115.7%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=13950567/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=8): err= 0: pid=101268: Thu Apr  2 15:42:36 2015
  write: io=30770MB, bw=525138KB/s, iops=131284, runt= 60001msec
    clat (usec): min=5, max=924, avg=58.04, stdev=38.65
     lat (usec): min=5, max=924, avg=58.10, stdev=38.65
    clat percentiles (usec):
     |  1.00th=[   12],  5.00th=[   17], 10.00th=[   21], 20.00th=[   29],
     | 30.00th=[   37], 40.00th=[   44], 50.00th=[   52], 60.00th=[   59],
     | 70.00th=[   67], 80.00th=[   77], 90.00th=[   92], 95.00th=[  122],
     | 99.00th=[  217], 99.50th=[  249], 99.90th=[  330], 99.95th=[  358],
     | 99.99th=[  422]
    bw (KB  /s): min=    0, max=82880, per=12.41%, avg=65157.55, stdev=12249.54
    lat (usec) : 10=0.49%, 20=7.89%, 50=38.07%, 100=45.76%, 250=7.29%
    lat (usec) : 500=0.49%, 750=0.01%, 1000=0.01%
  cpu          : usr=6.11%, sys=15.31%, ctx=9438074, majf=0, minf=0
  IO depths    : 1=119.8%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=7877203/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=8): err= 0: pid=101276: Thu Apr  2 15:42:36 2015
  read : io=149347MB, bw=2489.7MB/s, iops=19912, runt= 60001msec
    clat (usec): min=22, max=1459, avg=399.82, stdev=55.45
     lat (usec): min=22, max=1459, avg=399.92, stdev=55.45
    clat percentiles (usec):
     |  1.00th=[  290],  5.00th=[  306], 10.00th=[  330], 20.00th=[  358],
     | 30.00th=[  374], 40.00th=[  390], 50.00th=[  398], 60.00th=[  410],
     | 70.00th=[  422], 80.00th=[  438], 90.00th=[  470], 95.00th=[  502],
     | 99.00th=[  548], 99.50th=[  572], 99.90th=[  612], 99.95th=[  628],
     | 99.99th=[  668]
    bw (KB  /s): min=   41, max=374528, per=12.37%, avg=315284.12, stdev=36739.59
    lat (usec) : 50=0.01%, 100=0.01%, 250=0.05%, 500=94.87%, 750=5.07%
    lat (usec) : 1000=0.01%
    lat (msec) : 2=0.01%
  cpu          : usr=0.94%, sys=9.23%, ctx=1384963, majf=0, minf=232
  IO depths    : 1=115.9%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=1194773/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=8): err= 0: pid=101284: Thu Apr  2 15:42:36 2015
  write: io=78460MB, bw=1307.7MB/s, iops=10461, runt= 60001msec
    clat (usec): min=464, max=1191, avg=708.23, stdev=48.15
     lat (usec): min=464, max=1191, avg=708.38, stdev=48.15
    clat percentiles (usec):
     |  1.00th=[  636],  5.00th=[  652], 10.00th=[  660], 20.00th=[  676],
     | 30.00th=[  684], 40.00th=[  692], 50.00th=[  700], 60.00th=[  708],
     | 70.00th=[  716], 80.00th=[  732], 90.00th=[  772], 95.00th=[  812],
     | 99.00th=[  868], 99.50th=[  900], 99.90th=[  956], 99.95th=[  980],
     | 99.99th=[ 1032]
    bw (KB  /s): min=   35, max=171520, per=12.40%, avg=166095.31, stdev=16074.70
    lat (usec) : 500=0.02%, 750=86.24%, 1000=13.72%
    lat (msec) : 2=0.02%
  cpu          : usr=8.89%, sys=4.03%, ctx=730557, majf=0, minf=0
  IO depths    : 1=116.4%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=627680/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=54494MB, aggrb=930022KB/s, minb=930022KB/s, maxb=930022KB/s, mint=60001msec, maxt=60001msec

Run status group 1 (all jobs):
  WRITE: io=30770MB, aggrb=525138KB/s, minb=525138KB/s, maxb=525138KB/s, mint=60001msec, maxt=60001msec

Run status group 2 (all jobs):
   READ: io=149347MB, aggrb=2489.7MB/s, minb=2489.7MB/s, maxb=2489.7MB/s, mint=60001msec, maxt=60001msec

Run status group 3 (all jobs):
  WRITE: io=78460MB, aggrb=1307.7MB/s, minb=1307.7MB/s, maxb=1307.7MB/s, mint=60001msec, maxt=60001msec
```

Here with `numjobs = 64`:

```console
random-read-4k: (groupid=0, jobs=64): err= 0: pid=101293: Thu Apr  2 15:48:07 2015
  read : io=15182MB, bw=259097KB/s, iops=64774, runt= 60002msec
    clat (usec): min=8, max=5012, avg=983.32, stdev=645.24
     lat (usec): min=8, max=5012, avg=983.43, stdev=645.24
    clat percentiles (usec):
     |  1.00th=[   36],  5.00th=[  115], 10.00th=[  201], 20.00th=[  378],
     | 30.00th=[  556], 40.00th=[  732], 50.00th=[  908], 60.00th=[ 1080],
     | 70.00th=[ 1256], 80.00th=[ 1480], 90.00th=[ 1960], 95.00th=[ 2256],
     | 99.00th=[ 2640], 99.50th=[ 2736], 99.90th=[ 3024], 99.95th=[ 3184],
     | 99.99th=[ 4016]
    bw (KB  /s): min=    0, max= 5752, per=1.55%, avg=4024.58, stdev=1172.06
    lat (usec) : 10=0.01%, 20=0.33%, 50=1.26%, 100=2.66%, 250=8.48%
    lat (usec) : 500=14.21%, 750=14.28%, 1000=14.26%
    lat (msec) : 2=35.33%, 4=9.18%, 10=0.01%
  cpu          : usr=0.53%, sys=2.83%, ctx=4742067, majf=0, minf=64
  IO depths    : 1=122.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=3886578/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
random-write-4k: (groupid=1, jobs=64): err= 0: pid=101737: Thu Apr  2 15:48:07 2015
  write: io=10380MB, bw=177140KB/s, iops=44284, runt= 60002msec
    clat (usec): min=11, max=5308, avg=1434.61, stdev=825.13
     lat (usec): min=11, max=5308, avg=1434.70, stdev=825.13
    clat percentiles (usec):
     |  1.00th=[   52],  5.00th=[  177], 10.00th=[  314], 20.00th=[  588],
     | 30.00th=[  868], 40.00th=[ 1144], 50.00th=[ 1416], 60.00th=[ 1704],
     | 70.00th=[ 1976], 80.00th=[ 2256], 90.00th=[ 2544], 95.00th=[ 2736],
     | 99.00th=[ 3056], 99.50th=[ 3184], 99.90th=[ 3472], 99.95th=[ 3728],
     | 99.99th=[ 4384]
    bw (KB  /s): min=    0, max= 3105, per=1.55%, avg=2746.54, stdev=265.30
    lat (usec) : 20=0.19%, 50=0.75%, 100=1.49%, 250=5.34%, 500=8.96%
    lat (usec) : 750=9.06%, 1000=9.05%
    lat (msec) : 2=36.02%, 4=29.11%, 10=0.03%
  cpu          : usr=0.89%, sys=2.47%, ctx=3098858, majf=0, minf=0
  IO depths    : 1=116.6%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=2657185/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-read-128k: (groupid=2, jobs=64): err= 0: pid=101346: Thu Apr  2 15:48:07 2015
  read : io=119516MB, bw=1991.7MB/s, iops=15932, runt= 60010msec
    clat (usec): min=62, max=9741, avg=4012.66, stdev=162.76
     lat (usec): min=62, max=9741, avg=4012.87, stdev=162.77
    clat percentiles (usec):
     |  1.00th=[ 3632],  5.00th=[ 3728], 10.00th=[ 3792], 20.00th=[ 3888],
     | 30.00th=[ 3920], 40.00th=[ 3984], 50.00th=[ 4016], 60.00th=[ 4048],
     | 70.00th=[ 4128], 80.00th=[ 4128], 90.00th=[ 4192], 95.00th=[ 4256],
     | 99.00th=[ 4384], 99.50th=[ 4384], 99.90th=[ 4448], 99.95th=[ 4512],
     | 99.99th=[ 4576]
    bw (KB  /s): min=   12, max=34099, per=1.55%, avg=31634.45, stdev=2973.01
    lat (usec) : 100=0.01%, 250=0.01%, 500=0.01%
    lat (msec) : 2=0.01%, 4=45.96%, 10=54.04%
  cpu          : usr=0.16%, sys=1.58%, ctx=1120717, majf=0, minf=1856
  IO depths    : 1=116.7%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=956130/w=0/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1
sequential-write-128k: (groupid=3, jobs=64): err= 0: pid=100605: Thu Apr  2 15:48:07 2015
  write: io=80806MB, bw=1346.7MB/s, iops=10772, runt= 60006msec
    clat (usec): min=2914, max=6312, avg=5879.89, stdev=79.48
     lat (usec): min=2915, max=6312, avg=5880.09, stdev=79.48
    clat percentiles (usec):
     |  1.00th=[ 5728],  5.00th=[ 5728], 10.00th=[ 5792], 20.00th=[ 5792],
     | 30.00th=[ 5856], 40.00th=[ 5856], 50.00th=[ 5856], 60.00th=[ 5920],
     | 70.00th=[ 5920], 80.00th=[ 5920], 90.00th=[ 5984], 95.00th=[ 5984],
     | 99.00th=[ 6048], 99.50th=[ 6112], 99.90th=[ 6112], 99.95th=[ 6176],
     | 99.99th=[ 6240]
    bw (KB  /s): min=   12, max=21972, per=1.55%, avg=21387.19, stdev=1968.92
    lat (msec) : 4=0.01%, 10=100.00%
  cpu          : usr=1.24%, sys=0.57%, ctx=758008, majf=0, minf=0
  IO depths    : 1=117.1%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=0/w=646444/d=0, short=r=0/w=0/d=0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: io=15182MB, aggrb=259096KB/s, minb=259096KB/s, maxb=259096KB/s, mint=60002msec, maxt=60002msec

Run status group 1 (all jobs):
  WRITE: io=10380MB, aggrb=177139KB/s, minb=177139KB/s, maxb=177139KB/s, mint=60002msec, maxt=60002msec

Run status group 2 (all jobs):
   READ: io=119516MB, aggrb=1991.7MB/s, minb=1991.7MB/s, maxb=1991.7MB/s, mint=60010msec, maxt=60010msec

Run status group 3 (all jobs):
  WRITE: io=80806MB, aggrb=1346.7MB/s, minb=1346.7MB/s, maxb=1346.7MB/s, mint=60006msec, maxt=60006msec
```
