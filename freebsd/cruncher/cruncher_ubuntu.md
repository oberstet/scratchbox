# Cruncher / Ubuntu

## Multi-queue Block Device Layer

* https://www.thomas-krenn.com/en/wiki/Linux_Multi-Queue_Block_IO_Queueing_Mechanism_%28blk-mq%29
* http://bjorling.me/blkmq-slides.pdf
* https://lwn.net/Articles/552904/
* http://kernel.dk/systor13-final18.pdf
* http://www.phoronix.com/scan.php?page=news_item&px=MTUxNDQ
* http://www.phoronix.com/scan.php?page=news_item&px=linux-4.1-block-core-blk-mq
* http://ubuntuhandbook.org/index.php/2015/06/upgrade-kernel-4-1-ubuntu-linux-mint/
* http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.1-unstable/

## Kernel Versions

* RHEL 7.1            => Linux kernel 3.10.0-229
* SLES 12             => Linux kernel 3.12.39-47.1
* Ubuntu 14.04.2 LTS  => Linux kernel 3.16
* **Ubuntu 15.04        => Linux kernel 3.19.3**
* Ubuntu 15.10        => October 2015 (Linux kernel 4.1.x)
* Ubuntu 16.04 LTS    => April 2016

## Null Block Device

* [Null Block Device](https://www.kernel.org/doc/Documentation/block/null_blk.txt)
* `/dev/nullb0`
* `/sys/block/nullb0/...`

## DMIDecode

* http://www.nongnu.org/dmidecode/
* http://linux.die.net/man/8/dmidecode

Get serial numbers of DIMMs:

```console
dmidecode -t 17
```

# Storage

## Storage Setup

```
sudo mdadm --create /dev/md2 --chunk=8 --level=0 --raid-devices=8 \
   /dev/nvme0n1 \
   /dev/nvme1n1 \
   /dev/nvme2n1 \
   /dev/nvme3n1 \
   /dev/nvme4n1 \
   /dev/nvme5n1 \
   /dev/nvme6n1 \
   /dev/nvme7n1


sudo mdadm --create /dev/md3 --chunk=8 --level=10 --raid-devices=10 \
    /dev/sdb \
    /dev/sdd \
    /dev/sde \
    /dev/sdf \
    /dev/sdg \
    /dev/sdh \
    /dev/sdi \
    /dev/sdag \
    /dev/sdah \
    /dev/sdai


sudo mdadm --create /dev/md240 --level=6 --raid-devices=6 /dev/sd[m-r]


http://unix.stackexchange.com/questions/129497/difference-between-uuid-from-blkid-and-mdadm


System:

/dev/sda
/dev/sdc


Internal (10 x 800GB):

/dev/sdb 
/dev/sdd 
/dev/sde 
/dev/sdf 
/dev/sdg 
/dev/sdh 
/dev/sdi 
/dev/sdag
/dev/sdah
/dev/sdai


JBOD (24 x 6TB):

/dev/sdj
/dev/sdk
/dev/sdl
/dev/sdm
/dev/sdn
/dev/sdo

/dev/sdp
/dev/sdq
/dev/sdr
/dev/sds
/dev/sdt
/dev/sdu

/dev/sdv
/dev/sdw
/dev/sdx
/dev/sdy
/dev/sdz
/dev/sdaa

/dev/sdab
/dev/sdac
/dev/sdad
/dev/sdae
/dev/sdaf
```

# PostgresXL

The repo [here](http://git.postgresql.org/gitweb/?p=postgres-xl.git;a=summary) has recent developments - eg it's based on PG 9.5 already. It's the bleeding edge though.

Clone the repo:

```
cd ~/scm/3rdparty
git clone http://git.postgresql.org/git/postgres-xl.git
```

This will take a **long** time (we have to use HTTP, since native Git protocol is blocked by firewall).
