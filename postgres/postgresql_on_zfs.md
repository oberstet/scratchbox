https://www.kib.kiev.ua/kib/pgsql_perf_v2.0.pdf

http://linux.die.net/man/1/iozone

# ZIL on RAMdisk

Create a RAM disk

	mdconfig -a -s 2g -t malloc -o reserve -u 0

Check

	mdconfig -lv

Add as log device to pool

	zpool add system log /dev/md0

Check

	zpool status system

Remove log device

	zpool remove system /dev/md0

Destroy RAM disk

	mdconfig -d -u 0





### PGBench

http://de.slideshare.net/linuxpoet/introduction-to-pgbench

Prepare:

	su -l pgsql
	createdb pgbench
	pgbench -i -s 1000 pgbench

Run:

	pgbench    -c 16 -j 8 -T 60 pgbench


### System

http://www.brendangregg.com/USEmethod/use-freebsd.html


kldload hwpmc
pmcstat -n 100000000 -TS unhalted-cycles


### DWH

http://www.postgresql.org/docs/9.4/static/non-durability.html

### Raw Data Loading

http://stackoverflow.com/a/12207237/884770


### PG Processes

PostgreSQL has several [background processes](http://de.slideshare.net/EnterpriseDB/overviewutilityprocesses-finalaug222013).

E.g. the WAL writer process is responsible for writing and synching WAL records.


### Testing WAL

Use [pg_test_fsync](http://www.postgresql.org/docs/current/static/pgtestfsync.html) to test WAL performance.

Use [diskchecker](http://brad.livejournal.com/2116715.html) to test [WAL reliability](http://www.postgresql.org/docs/current/static/wal-reliability.html).


### Tuning WAL

http://www.postgresql.org/docs/9.4/static/non-durability.html
http://rhaas.blogspot.de/2012/03/tuning-sharedbuffers-and-walbuffers.html


### Disk Layout

The filesystem layout of a PostgreSQL cluster is described [here](http://www.postgresql.org/docs/current/static/storage-file-layout.html).

The WAL configuration is described:

* http://www.pgcon.org/2012/schedule/attachments/258_212_Internals%20Of%20PostgreSQL%20Wal.pdf
* http://www.postgresql.org/docs/current/static/wal-configuration.html
* http://www.postgresql.org/docs/current/static/runtime-config-wal.html


http://solarisinternals.com/wiki/index.php/ZFS_for_Databases#PostgreSQL_Considerations

ZFS tuning:

* http://www.solarisinternals.com/wiki/index.php/ZFS_Evil_Tuning_Guide


List SCSI devices

	camcontrol devlist

Get information on devices

	camcontrol identify ada0

or

	sdparm da0

Listing relevant ZFS system tunables:

	sysctl vfs.zfs

Listing all ZFS properties relevant:

	zfs list -o name,recordsize,logbias,primarycache,secondarycache,compression,dedup


### PG Configuration

Turn off [full page writes](http://www.postgresql.org/docs/9.4/static/runtime-config-wal.html#GUC-FULL-PAGE-WRITES). This isn't necessary on ZFS.

Possibly turn on [asynchronous commits](http://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT)


SET synchronous_commit = on


### Cluster Base

Create a new ZFS filesystem with default options mounted on the cluster base directory `$PGDATA`.

### Transaction Logs

Create a separate ZFS filesystem for `$PGDATA/pg_xlog`. This will contain the PostgreSQL transaction logs (WAL files) which are cluster-wide (not per database). Each WAL Segment contains Bocks of 8K and Segment size is 16M.


* `atime=off`
* `mountpoint=$PGDATA/pg_xlog`

Other relevant parameters should be left at their default values:

* `logbias=latency`
* `recordsize=128K`
* `compression=off`
* `dedup=off`
* `primarycache=all`
* `secondarycache=all`

### Databases

Create a separate ZFS filesystem for each database `$PGDATA/base/<database>`within the PostgreSQL database cluster

* `atime=off`
* `recordsize=8K`
* `logbias=throughput`

Other relevant parameters should be left at their default values:

* `compression=off`
* `dedup=off`
* `primarycache=all`
* `secondarycache=all`

### Temp Tablespace

PostgreSQL maintains a default temporary data area (e.g. for disk based sorts) under `$PGDATA/base/pgsql_tmp`.

* `atime=off`
* `recordsize=8K`
* `logbias=throughput`

