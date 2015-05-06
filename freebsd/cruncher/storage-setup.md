# Storage Configuration

With all of below configuraiton variants, the 24 external HDDs are configured as a software RAID-60. This provides extremely high data integrity and security.

This **Archive Storage Subsystem** is then used for:

* long-term archival of received flat-files
* database and system backups

Further, of the 12 internal Intel DC S3700 SATA SSDs, two are used in a software RAID-1 (mirror) formatted with Btrfs as primary system disk.

This **System Storage Subsystem** is used for:

* boot disk
* OS
* OS containers

*The storage configurations below differ in how we make use of the (remaining) 10 internal Intel DC S3700 SATA SSDs and the 8 Intel P3700 NVMe SSDs.*


## Storage Configuration A

In this variant, two independent PostgreSQL database clusters are run:

* Work Database
* Results Database

The **Work Database** completely runs from the 8 NVMes configured in a software RAID-0, formatted with XFS. The usable capacity is **16TB**.

The **Results Database** completeley runs from the 10 SSDs configured in a software RAID-10, formatted with XFS. The usable capacity is **4TB**.

Both database clusters run in **continuous archive mode**, archiving WAL segments to the **Archive Storage**.

The **Work Database** is used for big ETLs and analytical workloads. Only final results are copied over to the **Results Database**. All *presentation* front-ends fetch data from the **Results Database**.

Pros:

* likely the highest performance setup we can achieve
* clear separation in "work" and "results" datasets
* each database can be tuned to needs (performance vs availability)
* **Work Database** maintainance/downtime does not affect presentation frontends

Cons:

* two database clusters required database links / foreign tables to move data between
* small risk of small data loss on **Work Database**


## Storage Configuration B

In this variant, a single PostgreSQL database cluster is run.

The 10 internal SSDs are configured in a software RAID-10 formatted with XFS and hold the primary database cluster area (`PGDATA`).

2 NVMe SSDs are configured in a software RAID-1 formatted with XFS and hold the transaction logs of the database (WAL segments, `PGDATA/pg_xlog`).

The remaining 6 NVMe SSDs are configured in a software RAID-0 formatted with XFS and hold an additional **FAST Tablespace** (`PGDATA/pg_tblspc/fast`).


## Results Database

To create the storage area for **Results Database**:

```console
mdadm --create /dev/md123 --name result --level=10 --chunk=256 --raid-devices=10 /dev/sd[b-c] /dev/sd[e-l]
```

This creates a complex RAID-10.

Another variant would be to create a nested RAID:

```console
mdadm --create /dev/md230 --name result0 --level=1 --raid-devices=2 /dev/sd{b,c}
mdadm --create /dev/md231 --name result1 --level=1 --raid-devices=2 /dev/sd{e,f}
mdadm --create /dev/md232 --name result2 --level=1 --raid-devices=2 /dev/sd{g,h}
mdadm --create /dev/md233 --name result3 --level=1 --raid-devices=2 /dev/sd{i,j}
mdadm --create /dev/md234 --name result4 --level=1 --raid-devices=2 /dev/sd{k,l}
mdadm --create /dev/md235 --name result --level=0 --raid-devices=5 /dev/md23[0-4]
```

Check settings:

```console
for drive in {a..l}; do cat /sys/block/sd${drive}/queue/scheduler; done
for drive in {a..l}; do cat /sys/block/sd${drive}/device/queue_depth; done
for drive in {a..l}; do cat /sys/block/sd${drive}/queue/add_random; done
for drive in {a..l}; do cat /sys/block/sd${drive}/queue/rq_affinity; done
for drive in {a..l}; do cat /sys/block/sd${drive}/queue/nr_requests; done
```

Adjust settings:

```console
for drive in {a..l}; do echo noop > /sys/block/sd${drive}/queue/scheduler; done
for drive in {a..l}; do echo 32 > /sys/block/sd${drive}/device/queue_depth; done
for drive in {a..l}; do echo 0 > /sys/block/sd${drive}/queue/add_random; done
for drive in {a..l}; do echo 1 > /sys/block/sd${drive}/queue/rq_affinity; done
```

To make these settings permanent, add above to `/etc/rc.d/boot.local`.


## Work Database

To create the storage area for **Work Database**:

```console
mdadm --create /dev/md124 --name work --level=0 --raid-devices=8 /dev/nvme[0-7]n1
```

Check settings:

```console
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/scheduler; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/add_random; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/rq_affinity; done
for drive in {0..7}; do cat /sys/block/nvme${drive}n1/queue/nr_requests; done
```

Adjust settings:

```console
for drive in {0..7}; do echo none > /sys/block/nvme${drive}n1/queue/scheduler; done
for drive in {0..7}; do echo 0 > /sys/block/nvme${drive}n1/queue/add_random; done
for drive in {0..7}; do echo 1 > /sys/block/nvme${drive}n1/queue/rq_affinity; done
```

To make these settings permanent, add above to `/etc/rc.d/boot.local`.


## Archive

The **Archive** storage subsystem is a 4U external JBOD with 24 [Seagate 6TB SAS (ST6000NM0014)](http://www.seagate.com/de/de/internal-hard-drives/nas-drives/enterprise-capacity-3-5-hdd/) magnetic disks.


### Reliability

The disks are designed for 24h operation in data-centers and have

* MTBF 2 Mio. hours
* AFR: 0,44 %
* UBER: 1 sector in every 10^15 bits read

The probability that at least 1 drive fails completely within 1 year is thus 1 - (1 - 0.0044)^24 = 10%.


### Disk Identification

The disks of the **Archive** subsystem are:

```console
bvr-sql18:~ # lsblk -io KNAME,TYPE,SIZE,MODEL | grep ST6000
sdm     disk    5,5T ST6000NM0014    
sdn     disk    5,5T ST6000NM0014    
sdo     disk    5,5T ST6000NM0014    
sdp     disk    5,5T ST6000NM0014    
sdq     disk    5,5T ST6000NM0014    
sdr     disk    5,5T ST6000NM0014    
sds     disk    5,5T ST6000NM0014    
sdt     disk    5,5T ST6000NM0014    
sdu     disk    5,5T ST6000NM0014    
sdv     disk    5,5T ST6000NM0014    
sdw     disk    5,5T ST6000NM0014    
sdx     disk    5,5T ST6000NM0014    
sdy     disk    5,5T ST6000NM0014    
sdz     disk    5,5T ST6000NM0014    
sdaa    disk    5,5T ST6000NM0014    
sdab    disk    5,5T ST6000NM0014    
sdac    disk    5,5T ST6000NM0014    
sdad    disk    5,5T ST6000NM0014    
sdae    disk    5,5T ST6000NM0014    
sdaf    disk    5,5T ST6000NM0014    
sdag    disk    5,5T ST6000NM0014    
sdah    disk    5,5T ST6000NM0014    
sdai    disk    5,5T ST6000NM0014    
sdaj    disk    5,5T ST6000NM0014    
```

To check their RAID status:

```console
bvr-sql18:~ # mdadm -E /dev/sd[m-z] /dev/sda[a-j]
mdadm: No md superblock detected on /dev/sdm.
mdadm: No md superblock detected on /dev/sdn.
mdadm: No md superblock detected on /dev/sdo.
mdadm: No md superblock detected on /dev/sdp.
mdadm: No md superblock detected on /dev/sdq.
mdadm: No md superblock detected on /dev/sdr.

mdadm: No md superblock detected on /dev/sds.
mdadm: No md superblock detected on /dev/sdt.
mdadm: No md superblock detected on /dev/sdu.
mdadm: No md superblock detected on /dev/sdv.
mdadm: No md superblock detected on /dev/sdw.
mdadm: No md superblock detected on /dev/sdx.

mdadm: No md superblock detected on /dev/sdy.
mdadm: No md superblock detected on /dev/sdz.
mdadm: No md superblock detected on /dev/sdaa.
mdadm: No md superblock detected on /dev/sdab.
mdadm: No md superblock detected on /dev/sdac.
mdadm: No md superblock detected on /dev/sdad.

mdadm: No md superblock detected on /dev/sdae.
mdadm: No md superblock detected on /dev/sdaf.
mdadm: No md superblock detected on /dev/sdag.
mdadm: No md superblock detected on /dev/sdah.
mdadm: No md superblock detected on /dev/sdai.
mdadm: No md superblock detected on /dev/sdaj.
```

### Delete Array


mdadm --misc --zero-superblock /dev/sd[m-z] /dev/sda[a-j]

### Entrpoy Source

By default, block devices are used as an entropy source (this is done by `/usr/sbin/haveged` which is running). Disable that:

```console
for drive in {m..z}; do echo 0 > /sys/block/sd${drive}/queue/add_random; done
for drive in {a..j}; do echo 0 > /sys/block/sda${drive}/queue/add_random; done
```

### IO Scheduler

Check current IO scheduer (should be `cfq`):

```console
for drive in {m..z}; do cat /sys/block/sd${drive}/queue/scheduler; done
for drive in {a..j}; do cat /sys/block/sda${drive}/queue/scheduler; done
```

Set IO scheduler to `cfq`:

```console
for drive in {m..z}; do echo cfq > /sys/block/sd${drive}/queue/scheduler; done
for drive in {a..j}; do echo cfq > /sys/block/sda${drive}/queue/scheduler; done
```


### Queue Depth

Check current queue depth setting (should be 32):

```console
for drive in {m..z}; do cat /sys/block/sd${drive}/device/queue_depth; done
for drive in {a..j}; do cat /sys/block/sda${drive}/device/queue_depth; done
```

Set queue depth to 32:

```console
for drive in {m..z}; do echo 32 > /sys/block/sd${drive}/device/queue_depth; done
for drive in {a..j}; do echo 32 > /sys/block/sda${drive}/device/queue_depth; done
```


### Creating the array

We will create a RAID-60 software RAID setup using the nesting feature of `mdadm'.

First, create the 4 RAID-6 set with 6 disks each:

```console
mdadm --create /dev/md240 --name archive0 --level=6 --raid-devices=6 /dev/sd[m-r]
mdadm --create /dev/md241 --name archive1 --level=6 --raid-devices=6 /dev/sd[s-x]
mdadm --create /dev/md242 --name archive2 --level=6 --raid-devices=6 /dev/sd[y-z] /dev/sda[a-d]
mdadm --create /dev/md243 --name archive3 --level=6 --raid-devices=6 /dev/sda[e-j]
```

Now create the RAID-0 from above RAID-6 sets:

```console
mdadm --create /dev/md244 --name archive --level=0 --raid-devices=4 /dev/md24[0-3]
```

Then create the XFS filesystem on top:

```console
mkfs.xfs /dev/md244
```

noatime,nodiratime,errors=remount-ro


#### Resources

* https://raid.wiki.kernel.org/index.php/RAID_setup
* https://www.suse.com/documentation/sles10/stor_admin/data/raidmdadmr6.html
* https://www.suse.com/documentation/sles10/stor_admin/data/raidmdadmr10nest.html


## PostgreSQL

PGDATA
PGDATA/pg_xlog
PGDATA/base/pgsql_tmp

Temporary files (for operations such as sorting more data than can fit in memory) are created within PGDATA/base/pgsql_tmp, or within a pgsql_tmp subdirectory of a tablespace directory if a tablespace other than pg_default is specified for them. 


http://www.postgresql.org/docs/9.4/static/storage-file-layout.html

https://lwn.net/Articles/590214/


##

To check the on-disk size of PostgreSQL tables:

```sql
SELECT
    relname,
    pg_relation_filepath(oid) filepath,
    round(relpages::numeric*8192./1024./1024./1024.,1) gbytes
FROM
    pg_class
WHERE
    relname LIKE 'tbl_%_201212'
ORDER BY
    3 DESC
;
```

Note that PostgreSQL may store data for a single table in multiple files. E.g.

```
relname                     filepath            gbytes
-------------------------------------------------------------
tbl_pk_konto_kkv_201212     base/20444/80072    5.2
```

is stored in multiple files:

```console
$ pwd
/usr/local/pgsql/data
$ ls -la base/20444/80072*
-rw-------  1 pgsql  pgsql  1073741824 Apr 10 15:42 base/20444/80072
-rw-------  1 pgsql  pgsql  1073741824 Apr 10 15:43 base/20444/80072.1
-rw-------  1 pgsql  pgsql  1073741824 Apr 10 15:43 base/20444/80072.2
-rw-------  1 pgsql  pgsql  1073741824 Apr 10 15:44 base/20444/80072.3
-rw-------  1 pgsql  pgsql  1073741824 Apr 10 15:45 base/20444/80072.4
-rw-------  1 pgsql  pgsql   264060928 Apr 13 13:42 base/20444/80072.5
-rw-------  1 pgsql  pgsql     1400832 Apr 10 15:35 base/20444/80072_fsm
```

# Final Configuration

```console
bvr-sql18:~ # cat /etc/mdadm.conf
DEVICE containers partitions
ARRAY /dev/md/boot UUID=abd31c3e:314d868e:a76a42b2:6025b230
ARRAY /dev/md/root UUID=67221fe1:b542bd90:5f716fd9:f80f8014
ARRAY /dev/md/swap UUID=e726ac5a:34f5c549:534b092c:91913311
ARRAY /dev/md/work  metadata=1.2 UUID=f13a126b:791cb459:f9bf3f82:8c097359 name=bvr-sql18:work
ARRAY /dev/md/result  metadata=1.2 UUID=a4fe6ef1:73fa5f1c:208333bd:83d74343 name=bvr-sql18:result
ARRAY /dev/md/archive2  metadata=1.2 UUID=e9f51cea:ce6a492f:e592ccd2:9bdc7e6d name=bvr-sql18:archive2
ARRAY /dev/md/archive3  metadata=1.2 UUID=adbebc87:5016ce48:afd53e25:2358ec19 name=bvr-sql18:archive3
ARRAY /dev/md/archive1  metadata=1.2 UUID=69c90acd:6e7b1849:19f42f3a:bccc60c1 name=bvr-sql18:archive1
ARRAY /dev/md/archive0  metadata=1.2 UUID=5c2dad3a:5663346e:e3a5f304:7676615c name=bvr-sql18:archive0
ARRAY /dev/md/archive  metadata=1.2 UUID=1676a04e:49b84715:1bae00c5:f08e5d70 name=bvr-sql18:archive
bvr-sql18:~ # cat /proc/mdstat
Personalities : [raid1] [raid0] [raid10] [raid6] [raid5] [raid4]
md243 : active raid6 sdaj[5] sdai[4] sdah[3] sdag[2] sdaf[1] sdae[0]
      23441565696 blocks super 1.2 level 6, 512k chunk, algorithm 2 [6/6] [UUUUUU]
      bitmap: 0/44 pages [0KB], 65536KB chunk

md242 : active raid6 sdad[5] sdac[4] sdab[3] sdaa[2] sdz[1] sdy[0]
      23441565696 blocks super 1.2 level 6, 512k chunk, algorithm 2 [6/6] [UUUUUU]
      bitmap: 0/44 pages [0KB], 65536KB chunk

md241 : active raid6 sdx[5] sdw[4] sdv[3] sdu[2] sdt[1] sds[0]
      23441565696 blocks super 1.2 level 6, 512k chunk, algorithm 2 [6/6] [UUUUUU]
      bitmap: 0/44 pages [0KB], 65536KB chunk

md121 : active raid0 md243[3] md242[2] md241[1] md240[0]
      93765738496 blocks super 1.2 512k chunks

md240 : active raid6 sdr[5] sdq[4] sdp[3] sdo[2] sdn[1] sdm[0]
      23441565696 blocks super 1.2 level 6, 512k chunk, algorithm 2 [6/6] [UUUUUU]
      bitmap: 0/44 pages [0KB], 65536KB chunk

md123 : active raid10 sdh[5] sdl[9] sdk[7] sdj[8] sdi[6] sdg[4] sdb[0] sdc[1] sde[2] sdf[3]
      3906405120 blocks super 1.2 256K chunks 2 near-copies [10/10] [UUUUUUUUUU]
      bitmap: 1/30 pages [4KB], 65536KB chunk

md124 : active raid0 nvme7n1[7] nvme6n1[6] nvme5n1[5] nvme4n1[4] nvme3n1[3] nvme2n1[2] nvme1n1[1] nvme0n1[0]
      15627067392 blocks super 1.2 512k chunks

md125 : active raid1 sdd2[1] sda2[0]
      20972416 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

md126 : active raid1 sda1[0] sdd1[1]
      1051584 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

md127 : active raid1 sdd3[1] sda3[0]
      759385920 blocks super 1.0 [2/2] [UU]
      bitmap: 0/6 pages [0KB], 65536KB chunk

unused devices: <none>
bvr-sql18:~ # mdadm --detail /dev/md/work
/dev/md/work:
        Version : 1.2
  Creation Time : Tue Apr 28 13:41:06 2015
     Raid Level : raid0
     Array Size : 15627067392 (14903.13 GiB 16002.12 GB)
   Raid Devices : 8
  Total Devices : 8
    Persistence : Superblock is persistent

    Update Time : Tue Apr 28 13:41:06 2015
          State : clean
 Active Devices : 8
Working Devices : 8
 Failed Devices : 0
  Spare Devices : 0

     Chunk Size : 512K

           Name : bvr-sql18:work  (local to host bvr-sql18)
           UUID : f13a126b:791cb459:f9bf3f82:8c097359
         Events : 0

    Number   Major   Minor   RaidDevice State
       0     259        0        0      active sync   /dev/nvme0n1
       1     259        1        1      active sync   /dev/nvme1n1
       2     259        2        2      active sync   /dev/nvme2n1
       3     259        3        3      active sync   /dev/nvme3n1
       4     259        4        4      active sync   /dev/nvme4n1
       5     259        5        5      active sync   /dev/nvme5n1
       6     259        6        6      active sync   /dev/nvme6n1
       7     259        7        7      active sync   /dev/nvme7n1
bvr-sql18:~ # mdadm --detail /dev/md/result
/dev/md/result:
        Version : 1.2
  Creation Time : Wed Apr 29 16:17:10 2015
     Raid Level : raid10
     Array Size : 3906405120 (3725.44 GiB 4000.16 GB)
  Used Dev Size : 781281024 (745.09 GiB 800.03 GB)
   Raid Devices : 10
  Total Devices : 10
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Thu Apr 30 15:54:11 2015
          State : active
 Active Devices : 10
Working Devices : 10
 Failed Devices : 0
  Spare Devices : 0

         Layout : near=2
     Chunk Size : 256K

           Name : bvr-sql18:result  (local to host bvr-sql18)
           UUID : a4fe6ef1:73fa5f1c:208333bd:83d74343
         Events : 3400

    Number   Major   Minor   RaidDevice State
       0       8       16        0      active sync set-A   /dev/sdb
       1       8       32        1      active sync set-B   /dev/sdc
       2       8       64        2      active sync set-A   /dev/sde
       3       8       80        3      active sync set-B   /dev/sdf
       4       8       96        4      active sync set-A   /dev/sdg
       5       8      112        5      active sync set-B   /dev/sdh
       6       8      128        6      active sync set-A   /dev/sdi
       7       8      160        7      active sync set-B   /dev/sdk
       8       8      144        8      active sync set-A   /dev/sdj
       9       8      176        9      active sync set-B   /dev/sdl
bvr-sql18:~ # mdadm --detail /dev/md/archive
/dev/md/archive:
        Version : 1.2
  Creation Time : Tue Apr 28 13:10:46 2015
     Raid Level : raid0
     Array Size : 93765738496 (89421.98 GiB 96016.12 GB)
   Raid Devices : 4
  Total Devices : 4
    Persistence : Superblock is persistent

    Update Time : Tue Apr 28 13:10:46 2015
          State : clean
 Active Devices : 4
Working Devices : 4
 Failed Devices : 0
  Spare Devices : 0

     Chunk Size : 512K

           Name : bvr-sql18:archive  (local to host bvr-sql18)
           UUID : 1676a04e:49b84715:1bae00c5:f08e5d70
         Events : 0

    Number   Major   Minor   RaidDevice State
       0       9      240        0      active sync   /dev/md240
       1       9      241        1      active sync   /dev/md241
       2       9      242        2      active sync   /dev/md242
       3       9      243        3      active sync   /dev/md243
bvr-sql18:~ # mdadm --detail /dev/md/archive0
mdadm: cannot open /dev/md/archive0: No such file or directory
bvr-sql18:~ # mdadm --detail /dev/md/archive1
mdadm: cannot open /dev/md/archive1: No such file or directory
bvr-sql18:~ # mdadm --detail /dev/md240
/dev/md240:
        Version : 1.2
  Creation Time : Tue May  5 10:47:56 2015
     Raid Level : raid6
     Array Size : 23441565696 (22355.62 GiB 24004.16 GB)
  Used Dev Size : 5860391424 (5588.90 GiB 6001.04 GB)
   Raid Devices : 6
  Total Devices : 6
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Wed May  6 12:30:27 2015
          State : active
 Active Devices : 6
Working Devices : 6
 Failed Devices : 0
  Spare Devices : 0

         Layout : left-symmetric
     Chunk Size : 512K

           Name : bvr-sql18:archive0  (local to host bvr-sql18)
           UUID : 5c2dad3a:5663346e:e3a5f304:7676615c
         Events : 18784

    Number   Major   Minor   RaidDevice State
       0       8      192        0      active sync   /dev/sdm
       1       8      208        1      active sync   /dev/sdn
       2       8      224        2      active sync   /dev/sdo
       3       8      240        3      active sync   /dev/sdp
       4      65        0        4      active sync   /dev/sdq
       5      65       16        5      active sync   /dev/sdr
bvr-sql18:~ # mdadm --detail /dev/md241
/dev/md241:
        Version : 1.2
  Creation Time : Tue May  5 10:48:01 2015
     Raid Level : raid6
     Array Size : 23441565696 (22355.62 GiB 24004.16 GB)
  Used Dev Size : 5860391424 (5588.90 GiB 6001.04 GB)
   Raid Devices : 6
  Total Devices : 6
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Wed May  6 12:39:45 2015
          State : active
 Active Devices : 6
Working Devices : 6
 Failed Devices : 0
  Spare Devices : 0

         Layout : left-symmetric
     Chunk Size : 512K

           Name : bvr-sql18:archive1  (local to host bvr-sql18)
           UUID : 69c90acd:6e7b1849:19f42f3a:bccc60c1
         Events : 18896

    Number   Major   Minor   RaidDevice State
       0      65       32        0      active sync   /dev/sds
       1      65       48        1      active sync   /dev/sdt
       2      65       64        2      active sync   /dev/sdu
       3      65       80        3      active sync   /dev/sdv
       4      65       96        4      active sync   /dev/sdw
       5      65      112        5      active sync   /dev/sdx
bvr-sql18:~ # mdadm --detail /dev/md242
/dev/md242:
        Version : 1.2
  Creation Time : Tue May  5 10:48:09 2015
     Raid Level : raid6
     Array Size : 23441565696 (22355.62 GiB 24004.16 GB)
  Used Dev Size : 5860391424 (5588.90 GiB 6001.04 GB)
   Raid Devices : 6
  Total Devices : 6
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Wed May  6 12:58:11 2015
          State : active
 Active Devices : 6
Working Devices : 6
 Failed Devices : 0
  Spare Devices : 0

         Layout : left-symmetric
     Chunk Size : 512K

           Name : bvr-sql18:archive2  (local to host bvr-sql18)
           UUID : e9f51cea:ce6a492f:e592ccd2:9bdc7e6d
         Events : 19120

    Number   Major   Minor   RaidDevice State
       0      65      128        0      active sync   /dev/sdy
       1      65      144        1      active sync   /dev/sdz
       2      65      160        2      active sync   /dev/sdaa
       3      65      176        3      active sync   /dev/sdab
       4      65      192        4      active sync   /dev/sdac
       5      65      208        5      active sync   /dev/sdad
bvr-sql18:~ # mdadm --detail /dev/md243
/dev/md243:
        Version : 1.2
  Creation Time : Tue May  5 10:48:15 2015
     Raid Level : raid6
     Array Size : 23441565696 (22355.62 GiB 24004.16 GB)
  Used Dev Size : 5860391424 (5588.90 GiB 6001.04 GB)
   Raid Devices : 6
  Total Devices : 6
    Persistence : Superblock is persistent

  Intent Bitmap : Internal

    Update Time : Wed May  6 13:06:36 2015
          State : active
 Active Devices : 6
Working Devices : 6
 Failed Devices : 0
  Spare Devices : 0

         Layout : left-symmetric
     Chunk Size : 512K

           Name : bvr-sql18:archive3  (local to host bvr-sql18)
           UUID : adbebc87:5016ce48:afd53e25:2358ec19
         Events : 19222

    Number   Major   Minor   RaidDevice State
       0      65      224        0      active sync   /dev/sdae
       1      65      240        1      active sync   /dev/sdaf
       2      66        0        2      active sync   /dev/sdag
       3      66       16        3      active sync   /dev/sdah
       4      66       32        4      active sync   /dev/sdai
       5      66       48        5      active sync   /dev/sdaj
bvr-sql18:~ #
```

and

```console
bvr-sql18:~ # cat /etc/fstab
UUID=90ce80d6-c110-4148-9aa6-cd2896b49469 swap swap defaults 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 / btrfs defaults 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /home btrfs subvol=@/home 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /opt btrfs subvol=@/opt 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /srv btrfs subvol=@/srv 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /tmp btrfs subvol=@/tmp 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /usr/local btrfs subvol=@/usr/local 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/crash btrfs subvol=@/var/crash 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/lib/mailman btrfs subvol=@/var/lib/mailman 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/lib/named btrfs subvol=@/var/lib/named 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/lib/pgsql btrfs subvol=@/var/lib/pgsql 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/log btrfs subvol=@/var/log 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/opt btrfs subvol=@/var/opt 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/spool btrfs subvol=@/var/spool 0 0
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /var/tmp btrfs subvol=@/var/tmp 0 0
UUID=bafc16b7-74c0-4d54-9976-eeb349c6fb62 /boot ext4 acl,user_xattr 1 2
UUID=1a6b8cd8-3bfd-440e-bf9e-539199d38e50 /.snapshots btrfs subvol=@/.snapshots 0 0

UUID=116f1cc2-74d2-44a7-b4e2-e8196bc86d82 /data/work xfs noatime,nodiratime 0 0
```

