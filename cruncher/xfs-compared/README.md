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

* user: 3.5%
* system: 96.5%

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-md-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=11.2GiB/s,w=0KiB/s][r=2887k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=143097: Wed Jan 25 14:40:44 2017
   read: IOPS=2880k, BW=10.2GiB/s (11.8GB/s)(660GiB/60042msec)
  cpu          : usr=0.58%, sys=16.50%, ctx=173014130, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=172943424,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=10.2GiB/s (11.8GB/s), 10.2GiB/s-10.2GiB/s (11.8GB/s-11.8GB/s), io=660GiB (708GB), run=60042-60042msec

Disk stats (read/write):
    md1: ios=172699047/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=10808964/0, aggrmerge=0/0, aggrticks=1267392/0, aggrin_queue=1335648, aggrutil=100.00%
  nvme15n1: ios=10813464/0, merge=0/0, ticks=1266856/0, in_queue=1302112, util=100.00%
  nvme6n1: ios=10812756/0, merge=0/0, ticks=1270708/0, in_queue=1304924, util=100.00%
  nvme9n1: ios=10811863/0, merge=0/0, ticks=1274088/0, in_queue=1392044, util=100.00%
  nvme11n1: ios=10809962/0, merge=0/0, ticks=1269460/0, in_queue=1389376, util=100.00%
  nvme2n1: ios=10813030/0, merge=0/0, ticks=1268572/0, in_queue=1393992, util=100.00%
  nvme14n1: ios=10807324/0, merge=0/0, ticks=1262044/0, in_queue=1296956, util=100.00%
  nvme5n1: ios=10809891/0, merge=0/0, ticks=1276392/0, in_queue=1307896, util=100.00%
  nvme8n1: ios=10807743/0, merge=0/0, ticks=1272348/0, in_queue=1304380, util=100.00%
  nvme10n1: ios=10803385/0, merge=0/0, ticks=1279124/0, in_queue=1312712, util=100.00%
  nvme1n1: ios=10801628/0, merge=0/0, ticks=1256624/0, in_queue=1378312, util=100.00%
  nvme13n1: ios=10814900/0, merge=0/0, ticks=1259740/0, in_queue=1380972, util=100.00%
  nvme4n1: ios=10809390/0, merge=0/0, ticks=1270428/0, in_queue=1405368, util=100.00%
  nvme7n1: ios=10806474/0, merge=0/0, ticks=1265372/0, in_queue=1303728, util=100.00%
  nvme0n1: ios=10806302/0, merge=0/0, ticks=1260700/0, in_queue=1298000, util=100.00%
  nvme12n1: ios=10811902/0, merge=0/0, ticks=1257756/0, in_queue=1292164, util=100.00%
  nvme3n1: ios=10803410/0, merge=0/0, ticks=1268064/0, in_queue=1307440, util=100.00%
```

## ioengine=psync

* user: 3.3%
* system: 96.7%

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio xfs-md-nvmes-psync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=11.3GiB/s,w=0KiB/s][r=2952k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=141856: Wed Jan 25 14:38:51 2017
   read: IOPS=2946k, BW=11.3GiB/s (12.7GB/s)(675GiB/60039msec)
  cpu          : usr=0.55%, sys=16.56%, ctx=177055647, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=176899840,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=11.3GiB/s (12.7GB/s), 11.3GiB/s-11.3GiB/s (12.7GB/s-12.7GB/s), io=675GiB (725GB), run=60039-60039msec

Disk stats (read/write):
    md1: ios=176561933/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=11056240/0, aggrmerge=0/0, aggrticks=1334011/0, aggrin_queue=1408627, aggrutil=100.00%
  nvme15n1: ios=11055707/0, merge=0/0, ticks=1330132/0, in_queue=1364228, util=100.00%
  nvme6n1: ios=11055332/0, merge=0/0, ticks=1338104/0, in_queue=1371792, util=100.00%
  nvme9n1: ios=11053046/0, merge=0/0, ticks=1348328/0, in_queue=1492628, util=100.00%
  nvme11n1: ios=11056001/0, merge=0/0, ticks=1335772/0, in_queue=1481508, util=100.00%
  nvme2n1: ios=11052721/0, merge=0/0, ticks=1335964/0, in_queue=1470292, util=100.00%
  nvme14n1: ios=11053308/0, merge=0/0, ticks=1320064/0, in_queue=1356604, util=100.00%
  nvme5n1: ios=11057295/0, merge=0/0, ticks=1345752/0, in_queue=1383352, util=100.00%
  nvme8n1: ios=11055659/0, merge=0/0, ticks=1341524/0, in_queue=1376052, util=100.00%
  nvme10n1: ios=11058520/0, merge=0/0, ticks=1351304/0, in_queue=1386444, util=100.00%
  nvme1n1: ios=11058887/0, merge=0/0, ticks=1327880/0, in_queue=1453008, util=100.00%
  nvme13n1: ios=11051854/0, merge=0/0, ticks=1324848/0, in_queue=1458192, util=100.00%
  nvme4n1: ios=11053614/0, merge=0/0, ticks=1335016/0, in_queue=1484228, util=100.00%
  nvme7n1: ios=11060943/0, merge=0/0, ticks=1330780/0, in_queue=1368016, util=100.00%
  nvme0n1: ios=11060606/0, merge=0/0, ticks=1319916/0, in_queue=1356332, util=100.00%
  nvme12n1: ios=11054826/0, merge=0/0, ticks=1321720/0, in_queue=1360304, util=100.00%
  nvme3n1: ios=11061521/0, merge=0/0, ticks=1337084/0, in_queue=1375060, util=100.00%
```
