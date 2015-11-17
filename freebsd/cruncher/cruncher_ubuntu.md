# Cruncher / Ubuntu

## Samba

Install stuff:

```
sudo apt-get install samba
sudo apt-get install smbclient
```

Edit smbd config (only the delta to default is shown):

```
sudo vim /etc/samba/smb.conf
```

with

```
[global]
   workgroup = PARCIT
   security = user

[incoming]
   comment = ADR Incoming
   path = /files/rawdata/incoming
   browsable = yes
   guest ok = yes
   read only = no
   create mask = 0755
```

Adjust owner:

```
sudo chown -R nobody:nogroup /files/rawdata/incoming/
```

Restart smbd

```
sudo service smbd restart
```

List exported shares:

```
smbclient -L localhost
```

* https://help.ubuntu.com/lts/serverguide/samba-fileserver.html
* https://help.ubuntu.com/community/Samba/SambaServerGuide
* https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!

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

## IPMI

### Installation

To install

```
sudo apt-get install -y ipmitool
```

and add the following to `/etc/modules`

```
ipmi_devintf
ipmi_msghandler
ipmi_poweroff
ipmi_si
ipmi_watchdog
```

To manually load the kernel modules

```
sudo modprobe ipmi_devintf
sudo modprobe ipmi_msghandler
sudo modprobe ipmi_poweroff
sudo modprobe ipmi_si
sudo modprobe ipmi_watchdog
```

### Usage

See [here](http://www.openfusion.net/linux/ipmi_on_centos):

```
sudo ipmitool mc info
sudo ipmitool sdr
sudo ipmitool sensor
sudo ipmitool sel list
```

## DMIDecode

* http://www.nongnu.org/dmidecode/
* http://linux.die.net/man/8/dmidecode

Get serial numbers of DIMMs:

```console
dmidecode -t 17
```

# Various

## Interrupt Balancer Log Spam

The IRQ balancer is spamming the system log:

```
Sep 24 12:54:37 bvr-sql18 /usr/sbin/irqbalance: irq 75 affinity_hint subset empty
```

To silence these log messages, add the following line to `/etc/default/irqbalance`:

    OPTIONS="--hintpolicy=ignore"
    
and restart the service

    sudo service irqbalance restart


# Storage

## XFS and PostgreSQL

* http://de.slideshare.net/fuzzycz/postgresql-on-ext4-xfs-btrfs-and-zfs => Slide 49

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

# Memory Errors

* https://www.kernel.org/doc/Documentation/edac.txt
* http://lambda-diode.com/opinion/ecc-memory

```
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.129731] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.129740] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: cc00014000010092
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.129747] EDAC sbridge MC1: TSC 0
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.129749] EDAC sbridge MC1: ADDR 2007e9ea100 EDAC sbridge MC1: MISC 4430b486
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.129754] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085682 SOCKET 2 APIC 40
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130058] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130059] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130060] EDAC sbridge MC1: TSC 0
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130060] EDAC sbridge MC1: ADDR 2007eaaa100 EDAC sbridge MC1: MISC 54444486
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130063] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085682 SOCKET 2 APIC 40
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130483] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130485] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130485] EDAC sbridge MC1: TSC 0
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130486] EDAC sbridge MC1: ADDR 2007ebea100 EDAC sbridge MC1: MISC 546ed686
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.130487] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085682 SOCKET 2 APIC 40
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.131312] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.131313] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.131314] EDAC sbridge MC1: TSC 0
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.131314] EDAC sbridge MC1: ADDR 2007e6aa100 EDAC sbridge MC1: MISC 444e0286
Sep 24 11:08:02 bvr-sql18 kernel: [1281891.131315] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085682 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.272849] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.272854] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.272856] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.272857] EDAC sbridge MC1: ADDR 2007dcaa100 EDAC sbridge MC1: MISC 5412be86
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.272861] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273092] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273095] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: cc00008000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273097] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273098] EDAC sbridge MC1: ADDR 2007fcee100 EDAC sbridge MC1: MISC 454441686
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273102] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273782] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273784] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273786] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273787] EDAC sbridge MC1: ADDR 2007f7aa100 EDAC sbridge MC1: MISC 45466c086
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273791] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273982] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273985] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: cc00008000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273986] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273988] EDAC sbridge MC1: ADDR 2007f22e100 EDAC sbridge MC1: MISC 454122a86
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.273991] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274245] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274247] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274249] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274251] EDAC sbridge MC1: ADDR 2007f8ea100 EDAC sbridge MC1: MISC 4541c0e86
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274254] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274697] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274700] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274702] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274703] EDAC sbridge MC1: ADDR 2007f56e100 EDAC sbridge MC1: MISC 454584486
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.274707] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.425642] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.425646] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.425649] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.425653] EDAC sbridge MC1: ADDR 2007deaa100 EDAC sbridge MC1: MISC 442a2486
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.425657] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426276] EDAC sbridge MC1: HANDLING MCE MEMORY ERROR
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426278] EDAC sbridge MC1: CPU 24: Machine Check Event: 0 Bank 7: 8c00004000010092
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426280] EDAC sbridge MC1: TSC 0
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426282] EDAC sbridge MC1: ADDR 2007dfaa100 EDAC sbridge MC1: MISC 5408d286
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426285] EDAC sbridge MC1: PROCESSOR 0:306e7 TIME 1443085683 SOCKET 2 APIC 40
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.426347] CMCI storm detected: switching to poll mode
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931578] EDAC MC1: 5 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007e9ea offset:0x100 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931598] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007eaaa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931611] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007ebea offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931622] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007e6aa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931633] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007dcaa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931645] EDAC MC1: 2 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007fcee offset:0x100 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931656] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007f7aa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931667] EDAC MC1: 2 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007f22e offset:0x100 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931678] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007f8ea offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931689] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007f56e offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931700] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007deaa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
Sep 24 11:08:03 bvr-sql18 kernel: [1281891.931731] EDAC MC1: 1 CE memory read error on CPU_SrcID#2_Channel#2_DIMM#0 (channel:2 slot:0 page:0x2007dfaa offset:0x100 grain:32 syndrome:0x0 -  area:DRAM err_code:0001:0092 socket:2 channel_mask:2 rank:0)
```
