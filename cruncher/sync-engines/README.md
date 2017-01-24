# What was tested

The following compares **random 4kB read IO** using different **synchronous IO engines**

* sync
* psync
* psync2
* psync2 + hipri

at different **IO concurrencies**

* 512
* 1024
* 2048

over 8 x Intel P3608 4TB NVMe (16 logical NVMes) as

* individual block devices
* made into a RAID-0 (striped at chunksize 8k) using Linux MD

and with the NVMe devices raw formatted using sector sizes of

* 512 bytes
* 4096 bytes

I am using this:

```
oberstet@svr-psql19:~$ uname -r
4.8.0-0.bpo.2-amd64
oberstet@svr-psql19:~$ /opt/fio/bin/fio --version
fio-2.17-17-g9cf1
```

The driver is [test.sh](test.sh) and the FIO control files are [individual-nvmes.fio](individual-nvmes.fio) and [md-nvmes.fio](md-nvmes.fio).


# Results

## 512 bytes sector size

### Concurrency 512, individual disks

* [individual-nvmes-sync-512](sector-size-512/individual-nvmes-sync-512.log): IOPS=3559k
* [individual-nvmes-psync-512](sector-size-512/individual-nvmes-psync-512.log): IOPS=3520k
* [individual-nvmes-pvsync-512](sector-size-512/individual-nvmes-pvsync-512.log): IOPS=3483k
* [individual-nvmes-pvsync2-512](sector-size-512/individual-nvmes-pvsync2-512.log): IOPS=3468k
* [individual-nvmes-pvsync2-hipri-512](sector-size-512/individual-nvmes-pvsync2-hipri-512.log): IOPS=1697k

### Concurrency 1024, individual disks

* [individual-nvmes-sync-1024](sector-size-512/individual-nvmes-sync-1024.log): IOPS=5147k
* [individual-nvmes-psync-1024](sector-size-512/individual-nvmes-psync-1024.log): IOPS=5214k
* [individual-nvmes-pvsync-1024](sector-size-512/individual-nvmes-pvsync-1024.log): IOPS=5213k
* [individual-nvmes-pvsync2-1024](sector-size-512/individual-nvmes-pvsync2-1024.log): IOPS=5145k
* [individual-nvmes-pvsync2-hipri-1024](sector-size-512/individual-nvmes-pvsync2-hipri-1024.log): IOPS=1702k

### Concurrency 2048, individual disks

* [individual-nvmes-sync-2048](sector-size-512/individual-nvmes-sync-2048.log): IOPS=6626k
* [individual-nvmes-psync-2048](sector-size-512/individual-nvmes-psync-2048.log): IOPS=6561k
* [individual-nvmes-pvsync-2048](sector-size-512/individual-nvmes-pvsync-2048.log): IOPS=6460k
* [individual-nvmes-pvsync2-2048](sector-size-512/individual-nvmes-pvsync2-2048.log): IOPS=6632k
* [individual-nvmes-pvsync2-hipri-2048](sector-size-512/individual-nvmes-pvsync2-hipri-2048.log): IOPS=1698k

### Concurrency 512, MD RAID-0

* [md-nvmes-sync-512](sector-size-512/md-nvmes-sync-512.log): IOPS=1890k
* [md-nvmes-psync-512](sector-size-512/md-nvmes-psync-512.log): IOPS=3248k
* [md-nvmes-pvsync-512](sector-size-512/md-nvmes-pvsync-512.log): IOPS=3083k
* [md-nvmes-pvsync2-512](sector-size-512/md-nvmes-pvsync2-512.log): IOPS=3251k
* [md-nvmes-pvsync2-hipri-512](sector-size-512/md-nvmes-pvsync2-hipri-512.log): IOPS=3266k

### Concurrency 1024, MD RAID-0

* [md-nvmes-sync-1024](sector-size-512/md-nvmes-sync-1024.log): IOPS=1489k
* [md-nvmes-psync-1024](sector-size-512/md-nvmes-psync-1024.log): IOPS=3977k
* [md-nvmes-pvsync-1024](sector-size-512/md-nvmes-pvsync-1024.log): IOPS=3997k
* [md-nvmes-pvsync2-1024](sector-size-512/md-nvmes-pvsync2-1024.log): IOPS=4026k
* [md-nvmes-pvsync2-hipri-1024](sector-size-512/md-nvmes-pvsync2-hipri-1024.log): IOPS=4016k

### Concurrency 2048, MD RAID-0

* [md-nvmes-sync-2048](sector-size-512/md-nvmes-sync-2048.log): IOPS=1469k
* [md-nvmes-psync-2048](sector-size-512/md-nvmes-psync-2048.log): IOPS=4137k
* [md-nvmes-pvsync-2048](sector-size-512/md-nvmes-pvsync-2048.log): IOPS=4165k
* [md-nvmes-pvsync2-2048](sector-size-512/md-nvmes-pvsync2-2048.log): IOPS=4206k
* [md-nvmes-pvsync2-hipri-2048](sector-size-512/md-nvmes-pvsync2-hipri-2048.log): IOPS=4204k


## 4096 bytes sector size

### Concurrency 512, individual disks

* [individual-nvmes-sync-512](sector-size-4096/individual-nvmes-sync-512.log): IOPS=6767k
* [individual-nvmes-psync-512](sector-size-4096/individual-nvmes-psync-512.log): IOPS=6839k
* [individual-nvmes-pvsync-512](sector-size-4096/individual-nvmes-pvsync-512.log): IOPS=6490k
* [individual-nvmes-pvsync2-512](sector-size-4096/individual-nvmes-pvsync2-512.log): IOPS=6597k
* [individual-nvmes-pvsync2-hipri-512](sector-size-4096/individual-nvmes-pvsync2-hipri-512.log): IOPS=9486k

### Concurrency 1024, individual disks

* [individual-nvmes-sync-1024](sector-size-4096/individual-nvmes-sync-1024.log): IOPS=9165k
* [individual-nvmes-psync-1024](sector-size-4096/individual-nvmes-psync-1024.log): IOPS=9410k
* [individual-nvmes-pvsync-1024](sector-size-4096/individual-nvmes-pvsync-1024.log): IOPS=9382k
* [individual-nvmes-pvsync2-1024](sector-size-4096/individual-nvmes-pvsync2-1024.log): IOPS=9424k
* [individual-nvmes-pvsync2-hipri-1024](sector-size-4096/individual-nvmes-pvsync2-hipri-1024.log): IOPS=9435k

### Concurrency 2048, individual disks

* [individual-nvmes-sync-2048](sector-size-4096/individual-nvmes-sync-2048.log): IOPS=9296k
* [individual-nvmes-psync-2048](sector-size-4096/individual-nvmes-psync-2048.log): IOPS=9335k
* [individual-nvmes-pvsync-2048](sector-size-4096/individual-nvmes-pvsync-2048.log): IOPS=9331k
* [individual-nvmes-pvsync2-2048](sector-size-4096/individual-nvmes-pvsync2-2048.log): IOPS=9282k
* [individual-nvmes-pvsync2-hipri-2048](sector-size-4096/individual-nvmes-pvsync2-hipri-2048.log): IOPS=9330k

### Concurrency 512, MD RAID-0

* [md-nvmes-sync-512](sector-size-4096/md-nvmes-sync-512.log): IOPS=1649k
* [md-nvmes-psync-512](sector-size-4096/md-nvmes-psync-512.log): IOPS=4167k
* [md-nvmes-pvsync-512](sector-size-4096/md-nvmes-pvsync-512.log): IOPS=4174k
* [md-nvmes-pvsync2-512](sector-size-4096/md-nvmes-pvsync2-512.log): IOPS=4217k
* [md-nvmes-pvsync2-hipri-512](sector-size-4096/md-nvmes-pvsync2-hipri-512.log): IOPS=4215k

### Concurrency 1024, MD RAID-0

* [md-nvmes-sync-1024](sector-size-4096/md-nvmes-sync-1024.log): IOPS=1619k
* [md-nvmes-psync-1024](sector-size-4096/md-nvmes-psync-1024.log): IOPS=4289k
* [md-nvmes-pvsync-1024](sector-size-4096/md-nvmes-pvsync-1024.log): IOPS=4287k
* [md-nvmes-pvsync2-1024](sector-size-4096/md-nvmes-pvsync2-1024.log): IOPS=4339k
* [md-nvmes-pvsync2-hipri-1024](sector-size-4096/md-nvmes-pvsync2-hipri-1024.log): IOPS=4338k

### Concurrency 2048, MD RAID-0

* [md-nvmes-sync-2048](sector-size-4096/md-nvmes-sync-2048.log): IOPS=1608k
* [md-nvmes-psync-2048](sector-size-4096/md-nvmes-psync-2048.log): IOPS=4285k
* [md-nvmes-pvsync-2048](sector-size-4096/md-nvmes-pvsync-2048.log): IOPS=4336k
* [md-nvmes-pvsync2-2048](sector-size-4096/md-nvmes-pvsync2-2048.log): IOPS=4356k
* [md-nvmes-pvsync2-hipri-2048](sector-size-4096/md-nvmes-pvsync2-hipri-2048.log): IOPS=4353k


# TODO

* [x] low-level reformat NVMe devices to 4k sector size using isdct and retest
* [ ] test at XFS level (1 FS over 1 MD, and 16 XFSs over 16 individual NVMes)
* [x] rerun Linux perf on above tests
* [x] double check PG 9.6 (still) uses lseek/read/write
* [ ] write to PG hackers about this stuff and [this thread](https://www.postgresql.org/message-id/flat/CABUevEzZ%3DCGdmwSZwW9oNuf4pQZMExk33jcNO7rseqrAgKzj5Q%40mail.gmail.com#CABUevEzZ=CGdmwSZwW9oNuf4pQZMExk33jcNO7rseqrAgKzj5Q@mail.gmail.com)

# Questions

* [x] why is the difference between engines largish for MD, but not individual disks?
* [ ] what is that **hipri** thing anyways?
