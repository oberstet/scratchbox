# XFS over individual NVMes

## Preparation

### Create

```console
sudo mkfs.xfs -f -K /dev/nvme0n1
sudo mkfs.xfs -f -K /dev/nvme1n1
sudo mkfs.xfs -f -K /dev/nvme2n1
sudo mkfs.xfs -f -K /dev/nvme3n1
sudo mkfs.xfs -f -K /dev/nvme4n1
sudo mkfs.xfs -f -K /dev/nvme5n1
sudo mkfs.xfs -f -K /dev/nvme6n1
sudo mkfs.xfs -f -K /dev/nvme7n1
sudo mkfs.xfs -f -K /dev/nvme8n1
sudo mkfs.xfs -f -K /dev/nvme9n1
sudo mkfs.xfs -f -K /dev/nvme10n1
sudo mkfs.xfs -f -K /dev/nvme11n1
sudo mkfs.xfs -f -K /dev/nvme12n1
sudo mkfs.xfs -f -K /dev/nvme13n1
sudo mkfs.xfs -f -K /dev/nvme14n1
sudo mkfs.xfs -f -K /dev/nvme15n1

sudo mkdir -p /mnt/data0
sudo mkdir -p /mnt/data1
sudo mkdir -p /mnt/data2
sudo mkdir -p /mnt/data3
sudo mkdir -p /mnt/data4
sudo mkdir -p /mnt/data5
sudo mkdir -p /mnt/data6
sudo mkdir -p /mnt/data7
sudo mkdir -p /mnt/data8
sudo mkdir -p /mnt/data9
sudo mkdir -p /mnt/data10
sudo mkdir -p /mnt/data11
sudo mkdir -p /mnt/data12
sudo mkdir -p /mnt/data13
sudo mkdir -p /mnt/data14
sudo mkdir -p /mnt/data15

sudo mount -t xfs -o noatime -o nobarrier /dev/nvme0n1 /mnt/data0
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme1n1 /mnt/data1
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme2n1 /mnt/data2
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme3n1 /mnt/data3
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme4n1 /mnt/data4
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme5n1 /mnt/data5
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme6n1 /mnt/data6
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme7n1 /mnt/data7
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme8n1 /mnt/data8
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme9n1 /mnt/data9
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme10n1 /mnt/data10
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme11n1 /mnt/data11
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme12n1 /mnt/data12
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme13n1 /mnt/data13
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme14n1 /mnt/data14
sudo mount -t xfs -o noatime -o nobarrier /dev/nvme15n1 /mnt/data15
```

### Destroy

```console
sudo umount -f /mnt/data0
sudo umount -f /mnt/data1
sudo umount -f /mnt/data2
sudo umount -f /mnt/data3
sudo umount -f /mnt/data4
sudo umount -f /mnt/data5
sudo umount -f /mnt/data6
sudo umount -f /mnt/data7
sudo umount -f /mnt/data8
sudo umount -f /mnt/data9
sudo umount -f /mnt/data10
sudo umount -f /mnt/data11
sudo umount -f /mnt/data12
sudo umount -f /mnt/data13
sudo umount -f /mnt/data14
sudo umount -f /mnt/data15

sudo rm -rf /mnt/data0
sudo rm -rf /mnt/data1
sudo rm -rf /mnt/data2
sudo rm -rf /mnt/data3
sudo rm -rf /mnt/data4
sudo rm -rf /mnt/data5
sudo rm -rf /mnt/data6
sudo rm -rf /mnt/data7
sudo rm -rf /mnt/data8
sudo rm -rf /mnt/data9
sudo rm -rf /mnt/data10
sudo rm -rf /mnt/data11
sudo rm -rf /mnt/data12
sudo rm -rf /mnt/data13
sudo rm -rf /mnt/data14
sudo rm -rf /mnt/data15

sudo dd if=/dev/zero of=/dev/nvme0n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme1n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme2n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme3n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme4n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme5n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme6n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme7n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme8n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme9n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme10n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme11n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme12n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme13n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme14n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme15n1 bs=4096 count=1000 conv=notrunc
```

## ioengine=sync

* user: 7.2%
* system: 70.2%

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-individual-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
randread-md-nvmes: Laying out IO file(s) (16 file(s) / 30720MiB)
Jobs: 909 (f=6916): [f(2),_(1),f(3),_(2),f(2),_(1),f(4),_(2),f(3),_(1),f(1),_(2),f(4),_(1),f(1),_(1),f(2),_(21),f(1),_(3),f(2),_(2),f(3),_(3),f(2),_(2),f(7),_(1),f(7),_(1),f(3),_(2),f(14),_(1),f(10),_(1),f(1),_(1),f(12),_(1),f(1),_(1),f(6),E(1),f(8),_(1),f(13),_(1),f(1),_(2),f(2),_(1),f(15),_(1),f(13),_(1),f(25),_(1),f(8),_(1),f(8),_(1),f(21),_(1),f(40),_(1),f(2),_(1),f(1),_(1),f(1),_(1),f(22),E(1),f(24),_(2),f(54),_(1),f(3),_(1),f(5),_(1),f(2),E(1),f(15),E(1),f(8),_(1),f(19),E(1),f(17),_(1),f(39),_(1),E(1),f(26),_(2),f(5),_(1),f(3),_(1),f(5),_(1),f(12),_(1),f(11),_(1),f(3),_(1),f(15),_(1),f(2),_(1),f(37),_(1),f(5),_(1),f(1),E(1),f(21),_(1),E(1),f(1),_(1),f(35),_(1),f(10),E(1),f(9),E(1),f(51),_(1),f(30),_(1),f(19),_(1),f(8),_(1),f(3),_(2),f(17),E(1),f(26),_(1),f(6),E(1),f(2),_(1),f(5),_(1),f(5),_(1),f(53),_(1),f(8),_(1),f(2),_(1),f(15),_(1),f(1)][100.0%][r=17.1GiB/s,w=0KiB/s][r=4698k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=130292: Wed Jan 25 13:55:38 2017
   read: IOPS=5398k, BW=20.7GiB/s (22.2GB/s)(618GiB/30013msec)
  cpu          : usr=1.09%, sys=10.83%, ctx=162085422, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=162001984,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=20.7GiB/s (22.2GB/s), 20.7GiB/s-20.7GiB/s (22.2GB/s-22.2GB/s), io=618GiB (664GB), run=30013-30013msec

Disk stats (read/write):
  nvme0n1: ios=10084364/2, merge=0/0, ticks=1461824/0, in_queue=1487560, util=97.37%
  nvme1n1: ios=10125252/2, merge=0/0, ticks=1475724/0, in_queue=1554036, util=97.79%
  nvme2n1: ios=10125252/2, merge=0/0, ticks=1478120/0, in_queue=1553752, util=98.00%
  nvme3n1: ios=10125252/2, merge=0/0, ticks=1483480/0, in_queue=1512492, util=97.45%
  nvme4n1: ios=10125252/2, merge=0/0, ticks=1478436/0, in_queue=1570904, util=98.35%
  nvme5n1: ios=10125252/2, merge=0/0, ticks=1488180/0, in_queue=1511276, util=97.67%
  nvme6n1: ios=10125252/2, merge=0/0, ticks=1478556/0, in_queue=1500324, util=97.50%
  nvme7n1: ios=10125252/2, merge=0/0, ticks=1482556/0, in_queue=1507456, util=97.61%
  nvme8n1: ios=10125252/2, merge=0/0, ticks=1477272/0, in_queue=1500404, util=97.79%
  nvme9n1: ios=10125252/2, merge=0/0, ticks=1495128/0, in_queue=1573660, util=98.64%
  nvme10n1: ios=10125252/2, merge=0/0, ticks=1498012/0, in_queue=1519564, util=97.78%
  nvme11n1: ios=10125252/2, merge=0/0, ticks=1491676/0, in_queue=1576788, util=98.94%
  nvme12n1: ios=10125252/3, merge=0/3, ticks=1470408/0, in_queue=1496076, util=98.09%
  nvme13n1: ios=10125252/3, merge=0/3, ticks=1479360/0, in_queue=1545588, util=98.78%
  nvme14n1: ios=10124228/3, merge=0/3, ticks=1470920/0, in_queue=1499048, util=98.48%
  nvme15n1: ios=10124228/3, merge=0/3, ticks=1486372/0, in_queue=1513316, util=98.16%
```

## ioengine=psync

* user: 7.0%
* system: 69.0%

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-individual-nvmes-psync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 218 (f=684): [_(1),f(1),_(3),f(1),E(1),_(1),f(1),_(1),f(3),_(2),E(2),f(3),E(1),_(1),f(1),_(3),f(1),E(1),f(1),_(1),f(1),_(1),f(4),_(6),f(2),_(9),E(1),_(4),f(1),_(1),f(1),_(7),f(1),_(4),f(1),_(5),f(1),_(2),f(2),_(1),f(2),_(3),f(1),_(1),f(1),_(4),f(2),_(14),f(1),_(2),f(1),_(7),f(1),_(5),f(1),_(3),f(2),_(3),f(2),_(1),f(1),_(1),f(1),_(1),f(1),_(1),f(1),_(1),f(1),_(1),f(2),_(1),f(1),_(2),f(2),_(3),f(1),_(1),f(1),_(3),f(1),_(4),f(1),_(2),f(2),_(1),f(1),_(5),f(1),_(2),E(1),_(1),f(2),_(1),f(3),_(1),f(1),_(2),f(1),_(1),f(1),_(1),f(8),_(1),f(1),_(1),f(1),_(1),f(2),_(1),f(3),_(4),f(1),_(2),f(1),_(5),f(2),_(4),f(1),_(3),f(2),_(3),f(1),_(1),f(1),_(2),f(1),_(1),f(1),E(1),f(2),_(8),f(1),_(4),f(1),_(4),f(3),_(3),f(1),_(1),E(1),_(3),f(1),_(1),f(2),_(2),f(1),_(2),f(1),_(6),f(2),_(3),f(2),_(1),f(2),_(6),f(1),_(1),f(1),_(2),f(1),_(3),f(1),_(2),f(1),_(1),f(1),_(3),f(2),_(2),f(1),_(2),f(1),_(1),f(2),E(1),f(1),_(1),f(1),_(3),f(1),_(1),f(1),_(2),f(1),_(2),f(1),_(2),f(1),_(2),f(3),_(3),E(1),_(2),f(1),_(2),f(1),E(1),_(1),f(1),_(2),f(1),_(1),f(2),_(8),f(1),_(4),f(1),_(5),E(1),_(1),f(1),_(1),E(1),f(1),_(2),f(1),_(1),f(1),_(1),f(1),_(5),f(2),_(1),E(1),_(4),f(2),_(6),f(2),_(11),f(2),_(1),f(1),_(1),f(2),_(1),f(1),E(2),_(7),f(1),_(2),f(2),_(3),E(1),f(1),_(4),E(1),_(4),f(1),_(2),f(3),_(1),f(2),_(1),f(2),_(1),f(1),_(2),f(2),_(2),E(1),_(3),f(1),_(2),f(1),_(3),f(1),_(1),f(1),_(4),f(1),E(1),_(6),f(1),_(1),f(1),_(1),f(1),_(4),f(1),_(3),f(1),_(3),f(3),_(3),f(1),_(2),E(1),_(6),f(1),_(1),f(1),_(3),E(1),f(2),_(1),f(1),_(2),f(1),_(3),f(1),_(1),f(1),_(8),E(1),f(1),_(4),f(1),_(16),f(1),_(4),E(1),_(2),f(1),_(4),f(1),_(1),f(1),_(5),E(2),f(1),E(1),_(1),f(1),_(1),f(1),_(1),f(1),_(9),f(1),E(1),_(3),E(1),_(1),f(1),_(4),f(1),_(5),f(1),_(5),E(1),_(1),f(1),_(13),E(1),_(1),f(1),_(2),f(1),_(4),E(1),_(10),E(1),_(3),f(1),_(5),f(1),_(2),f(1),_(6),E(1),f(1),_(9),E(1),_(4),E(2),_(3),E(1),_(1),E(1),f(1),_(2),E(2),_(4),E(1),_(1),E(1),_(3),E(2),_(5),E(1),_(1),E(1),_(3),E(1),_(13),f(1),_(93),E(1),_(1),E(1),_(18),E(1),_(26),E(1),_(26),E(1),_(15),E(1),_(2),E(2),_(17)][100.0%][r=15.5GiB/s,w=0KiB/s][r=4038k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=137154: Wed Jan 25 14:22:05 2017
   read: IOPS=5409k, BW=20.7GiB/s (22.2GB/s)(1238GiB/60014msec)
  cpu          : usr=1.09%, sys=10.86%, ctx=324740143, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=324615616,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=20.7GiB/s (22.2GB/s), 20.7GiB/s-20.7GiB/s (22.2GB/s-22.2GB/s), io=1238GiB (1330GB), run=60014-60014msec

Disk stats (read/write):
  nvme0n1: ios=20283973/0, merge=0/0, ticks=2944440/0, in_queue=2993232, util=99.64%
  nvme1n1: ios=20284091/0, merge=0/0, ticks=2958828/0, in_queue=3105884, util=100.00%
  nvme2n1: ios=20284108/0, merge=0/0, ticks=2985532/0, in_queue=3134772, util=100.00%
  nvme3n1: ios=20284101/0, merge=0/0, ticks=2988768/0, in_queue=3039024, util=99.73%
  nvme4n1: ios=20288604/0, merge=0/0, ticks=2987864/0, in_queue=3167240, util=99.97%
  nvme5n1: ios=20288604/0, merge=0/0, ticks=3005712/0, in_queue=3060012, util=99.58%
  nvme6n1: ios=20288604/0, merge=0/0, ticks=2990216/0, in_queue=3034524, util=99.42%
  nvme7n1: ios=20288604/0, merge=0/0, ticks=2985652/0, in_queue=3041164, util=99.66%
  nvme8n1: ios=20288604/0, merge=0/0, ticks=2982556/0, in_queue=3031004, util=99.68%
  nvme9n1: ios=20288604/0, merge=0/0, ticks=2993648/0, in_queue=3148092, util=100.00%
  nvme10n1: ios=20288604/0, merge=0/0, ticks=3018588/0, in_queue=3066644, util=99.70%
  nvme11n1: ios=20288604/0, merge=0/0, ticks=2990604/0, in_queue=3157444, util=100.00%
  nvme12n1: ios=20288604/0, merge=0/0, ticks=2946948/0, in_queue=2992364, util=99.94%
  nvme13n1: ios=20288604/0, merge=0/0, ticks=2963624/0, in_queue=3102588, util=100.00%
  nvme14n1: ios=20287580/0, merge=0/0, ticks=2960516/0, in_queue=3007456, util=99.91%
  nvme15n1: ios=20287580/0, merge=0/0, ticks=2973260/0, in_queue=3034380, util=100.00%
```

# XFS over MD

## Preparation

### Create

```console
sudo mdadm --create /dev/md1 \
  --chunk=8 \
  --level=0 \
  --raid-devices=16 \
  /dev/nvme0n1 \
  /dev/nvme1n1 \
  /dev/nvme2n1 \
  /dev/nvme3n1 \
  /dev/nvme4n1 \
  /dev/nvme5n1 \
  /dev/nvme6n1 \
  /dev/nvme7n1 \
  /dev/nvme8n1 \
  /dev/nvme9n1 \
  /dev/nvme10n1 \
  /dev/nvme11n1 \
  /dev/nvme12n1 \
  /dev/nvme13n1 \
  /dev/nvme14n1 \
  /dev/nvme15n1

sudo mkfs.xfs -f -K /dev/md1

sudo mkdir -p /mnt/data
sudo mount -t xfs -o noatime -o nobarrier /dev/md1 /mnt/data
```

### Destroy

```console
sudo umount -f /mnt/data
sudo rm -rf /mnt/data

sudo mdadm --stop /dev/md1

sudo mdadm --zero-superblock /dev/nvme0n1
sudo mdadm --zero-superblock /dev/nvme1n1
sudo mdadm --zero-superblock /dev/nvme2n1
sudo mdadm --zero-superblock /dev/nvme3n1
sudo mdadm --zero-superblock /dev/nvme4n1
sudo mdadm --zero-superblock /dev/nvme5n1
sudo mdadm --zero-superblock /dev/nvme6n1
sudo mdadm --zero-superblock /dev/nvme7n1
sudo mdadm --zero-superblock /dev/nvme8n1
sudo mdadm --zero-superblock /dev/nvme9n1
sudo mdadm --zero-superblock /dev/nvme10n1
sudo mdadm --zero-superblock /dev/nvme11n1
sudo mdadm --zero-superblock /dev/nvme12n1
sudo mdadm --zero-superblock /dev/nvme13n1
sudo mdadm --zero-superblock /dev/nvme14n1
sudo mdadm --zero-superblock /dev/nvme15n1

sudo dd if=/dev/zero of=/dev/nvme0n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme1n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme2n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme3n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme4n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme5n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme6n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme7n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme8n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme9n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme10n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme11n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme12n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme13n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme14n1 bs=4096 count=1000 conv=notrunc
sudo dd if=/dev/zero of=/dev/nvme15n1 bs=4096 count=1000 conv=notrunc
```


## ioengine=sync

* user: %
* system: %

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-md-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
randread-md-nvmes: Laying out IO file(s) (1 file(s) / 30720MiB)
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=10.8GiB/s,w=0KiB/s][r=2802k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=126172: Wed Jan 25 13:28:38 2017
   read: IOPS=2790k, BW=10.7GiB/s (11.5GB/s)(320GiB/30055msec)
  cpu          : usr=0.54%, sys=16.57%, ctx=83925701, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=83856256,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=10.7GiB/s (11.5GB/s), 10.7GiB/s-10.7GiB/s (11.5GB/s-11.5GB/s), io=320GiB (343GB), run=30055-30055msec

Disk stats (read/write):
    md1: ios=83487876/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=5241016/0, aggrmerge=0/0, aggrticks=602417/0, aggrin_queue=631630, aggrutil=100.00%
  nvme15n1: ios=5241792/0, merge=0/0, ticks=605236/0, in_queue=620568, util=100.00%
  nvme6n1: ios=5237340/0, merge=0/0, ticks=600988/0, in_queue=616300, util=100.00%
  nvme9n1: ios=5240508/0, merge=0/0, ticks=603920/0, in_queue=651944, util=100.00%
  nvme11n1: ios=5243099/0, merge=0/0, ticks=609252/0, in_queue=667892, util=100.00%
  nvme2n1: ios=5239941/0, merge=0/0, ticks=600368/0, in_queue=652348, util=100.00%
  nvme14n1: ios=5241849/0, merge=0/0, ticks=599476/0, in_queue=613908, util=100.00%
  nvme5n1: ios=5241983/0, merge=0/0, ticks=604812/0, in_queue=618460, util=100.00%
  nvme8n1: ios=5238803/0, merge=0/0, ticks=602536/0, in_queue=618860, util=100.00%
  nvme10n1: ios=5237541/0, merge=0/0, ticks=604248/0, in_queue=619348, util=100.00%
  nvme1n1: ios=5245675/0, merge=0/0, ticks=600920/0, in_queue=653516, util=100.00%
  nvme13n1: ios=5242526/0, merge=0/0, ticks=598364/0, in_queue=648596, util=100.00%
  nvme4n1: ios=5239735/0, merge=0/0, ticks=600044/0, in_queue=655164, util=100.00%
  nvme7n1: ios=5241613/0, merge=0/0, ticks=605536/0, in_queue=621932, util=100.00%
  nvme0n1: ios=5243492/0, merge=0/0, ticks=595352/0, in_queue=611380, util=100.00%
  nvme12n1: ios=5237618/0, merge=0/0, ticks=604612/0, in_queue=616196, util=100.00%
  nvme3n1: ios=5242741/0, merge=0/0, ticks=603020/0, in_queue=619668, util=100.00%
```

## ioengine=psync

* user: %
* system: %

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-md-nvmes-psync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=10.9GiB/s,w=0KiB/s][r=2842k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=127476: Wed Jan 25 13:31:08 2017
   read: IOPS=2830k, BW=10.9GiB/s (11.6GB/s)(324GiB/30036msec)
  cpu          : usr=0.52%, sys=16.59%, ctx=85084174, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=85009664,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=10.9GiB/s (11.6GB/s), 10.9GiB/s-10.9GiB/s (11.6GB/s-11.6GB/s), io=324GiB (348GB), run=30036-30036msec

Disk stats (read/write):
    md1: ios=84568651/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=5313104/0, aggrmerge=0/0, aggrticks=622202/0, aggrin_queue=653534, aggrutil=100.00%
  nvme15n1: ios=5313352/0, merge=0/0, ticks=618496/0, in_queue=634004, util=100.00%
  nvme6n1: ios=5311908/0, merge=0/0, ticks=622952/0, in_queue=638404, util=100.00%
  nvme9n1: ios=5312879/0, merge=0/0, ticks=628548/0, in_queue=684116, util=100.00%
  nvme11n1: ios=5312275/0, merge=0/0, ticks=623672/0, in_queue=680976, util=100.00%
  nvme2n1: ios=5309485/0, merge=0/0, ticks=624416/0, in_queue=680408, util=100.00%
  nvme14n1: ios=5313963/0, merge=0/0, ticks=617492/0, in_queue=633020, util=100.00%
  nvme5n1: ios=5309183/0, merge=0/0, ticks=626120/0, in_queue=638892, util=100.00%
  nvme8n1: ios=5311896/0, merge=0/0, ticks=627840/0, in_queue=642136, util=100.00%
  nvme10n1: ios=5313984/0, merge=0/0, ticks=629168/0, in_queue=643884, util=100.00%
  nvme1n1: ios=5313044/0, merge=0/0, ticks=616332/0, in_queue=674092, util=100.00%
  nvme13n1: ios=5315159/0, merge=0/0, ticks=619672/0, in_queue=675616, util=100.00%
  nvme4n1: ios=5311828/0, merge=0/0, ticks=622312/0, in_queue=685520, util=100.00%
  nvme7n1: ios=5315150/0, merge=0/0, ticks=620752/0, in_queue=638996, util=100.00%
  nvme0n1: ios=5314921/0, merge=0/0, ticks=615984/0, in_queue=632400, util=100.00%
  nvme12n1: ios=5316256/0, merge=0/0, ticks=617796/0, in_queue=633860, util=100.00%
  nvme3n1: ios=5314381/0, merge=0/0, ticks=623684/0, in_queue=640220, util=100.00%
```
