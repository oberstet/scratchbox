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

I am using this:

```
oberstet@svr-psql19:~$ uname -r
4.8.0-0.bpo.2-amd64
oberstet@svr-psql19:~$ /opt/fio/bin/fio --version
fio-2.17-17-g9cf1
```

The driver is [test.sh](test.sh) and the FIO control files are [individual-nvmes.fio](individual-nvmes.fio) and [md-nvmes.fio](md-nvmes.fio).


# Results

## Concurrency 512, individual disks

* individual-nvmes-sync-512: IOPS=3559k
* individual-nvmes-psync-512: IOPS=3520k
* individual-nvmes-pvsync-512: IOPS=3483k
* individual-nvmes-pvsync2-512: IOPS=3468k
* individual-nvmes-pvsync2-hipri-512: IOPS=1697k

## Concurrency 1024, individual disks

* individual-nvmes-sync-1024: IOPS=5147k
* individual-nvmes-psync-1024: IOPS=5214k
* individual-nvmes-pvsync-1024: IOPS=5213k
* individual-nvmes-pvsync2-1024: IOPS=5145k
* individual-nvmes-pvsync2-hipri-1024: IOPS=1702k

## Concurrency 2048, individual disks

* individual-nvmes-sync-2048: IOPS=6626k
* individual-nvmes-psync-2048: IOPS=6561k
* individual-nvmes-pvsync-2048: IOPS=6460k
* individual-nvmes-pvsync2-2048: IOPS=6632k
* individual-nvmes-pvsync2-hipri-2048: IOPS=1698k

## Concurrency 512, MD RAID-0

* md-nvmes-sync-512: IOPS=1890k
* md-nvmes-psync-512: IOPS=3248k
* md-nvmes-pvsync-512: IOPS=3083k
* md-nvmes-pvsync2-512: IOPS=3251k
* md-nvmes-pvsync2-hipri-512: IOPS=3266k

## Concurrency 1024, MD RAID-0

* md-nvmes-sync-1024: IOPS=1489k
* md-nvmes-psync-1024: IOPS=3977k
* md-nvmes-pvsync-1024: IOPS=3997k
* md-nvmes-pvsync2-1024: IOPS=4026k
* md-nvmes-pvsync2-hipri-1024: IOPS=4016k

## Concurrency 2048, MD RAID-0

* md-nvmes-sync-2048: IOPS=1469k
* md-nvmes-psync-2048: IOPS=4137k
* md-nvmes-pvsync-2048: IOPS=4165k
* md-nvmes-pvsync2-2048: IOPS=4206k
* md-nvmes-pvsync2-hipri-2048: IOPS=4204k

## Details

* [individual-nvmes-sync-1024](individual-nvmes-sync-1024.log)
* [individual-nvmes-sync-2048](individual-nvmes-sync-2048.log)
* [individual-nvmes-psync-512](individual-nvmes-psync-512.log)
* [individual-nvmes-psync-1024](individual-nvmes-psync-1024.log)
* [individual-nvmes-psync-2048](individual-nvmes-psync-2048.log)
* [individual-nvmes-pvsync-512](individual-nvmes-pvsync-512.log)
* [individual-nvmes-pvsync-1024](individual-nvmes-pvsync-1024.log)
* [individual-nvmes-pvsync-2048](individual-nvmes-pvsync-2048.log)
* [individual-nvmes-pvsync2-512](individual-nvmes-pvsync2-512.log)
* [individual-nvmes-pvsync2-1024](individual-nvmes-pvsync2-1024.log)
* [individual-nvmes-pvsync2-2048](individual-nvmes-pvsync2-2048.log)
* [individual-nvmes-pvsync2-hipri-1024](individual-nvmes-pvsync2-hipri-1024.log)
* [individual-nvmes-pvsync2-hipri-2048](individual-nvmes-pvsync2-hipri-2048.log)
* [individual-nvmes-pvsync2-hipri-512](individual-nvmes-pvsync2-hipri-512.log)
* [md-nvmes-sync-512](md-nvmes-sync-512.log)
* [md-nvmes-sync-1024](md-nvmes-sync-1024.log)
* [md-nvmes-sync-2048](md-nvmes-sync-2048.log)
* [md-nvmes-psync-512](md-nvmes-psync-512.log)
* [md-nvmes-psync-1024](md-nvmes-psync-1024.log)
* [md-nvmes-psync-2048](md-nvmes-psync-2048.log)
* [md-nvmes-pvsync-512](md-nvmes-pvsync-512.log)
* [md-nvmes-pvsync-1024](md-nvmes-pvsync-1024.log)
* [md-nvmes-pvsync-2048](md-nvmes-pvsync-2048.log)
* [md-nvmes-pvsync2-512](md-nvmes-pvsync2-512.log)
* [md-nvmes-pvsync2-1024](md-nvmes-pvsync2-1024.log)
* [md-nvmes-pvsync2-2048](md-nvmes-pvsync2-2048.log)
* [md-nvmes-pvsync2-hipri-512](md-nvmes-pvsync2-hipri-512.log)
* [md-nvmes-pvsync2-hipri-1024](md-nvmes-pvsync2-hipri-1024.log)
* [md-nvmes-pvsync2-hipri-2048](md-nvmes-pvsync2-hipri-2048.log)

# TODO

* low-level reformat NVMe devices to 4k sector size using isdct and retest
* test at XFS level (1 FS over 1 MD, and 16 XFSs over 16 individual NVMes)
* write to PG hackers about this stuff and [this thread](https://www.postgresql.org/message-id/flat/CABUevEzZ%3DCGdmwSZwW9oNuf4pQZMExk33jcNO7rseqrAgKzj5Q%40mail.gmail.com#CABUevEzZ=CGdmwSZwW9oNuf4pQZMExk33jcNO7rseqrAgKzj5Q@mail.gmail.com)
