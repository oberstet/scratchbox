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


## Work Database

To create the storage area for **Work Database**:

```console
mdadm --create /dev/md220 --name work --level=0 --raid-devices=8 /dev/nvme[0-7]n1
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
