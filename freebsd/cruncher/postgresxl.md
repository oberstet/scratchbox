# PostgresXL

## Installation

The repo [here](http://git.postgresql.org/gitweb/?p=postgres-xl.git;a=summary) has recent developments - eg it's based on PG 9.5 already. It's the bleeding edge though.

Clone the repo:

```
cd ~/scm/3rdparty
git clone http://git.postgresql.org/git/postgres-xl.git
```

This will take a **long** time (we have to use HTTP, since native Git protocol is blocked by firewall).

Install requirements:

```
sudo apt-get install -y openssl libssl-dev
sudo apt-get install -y build-essential
sudo apt-get install -y libreadline6 libreadline6-dev
sudo apt-get install -y flex bison
```

### Building

Build it:

```
export CFLAGS="-O3 -march=native -mtune=native"
./configure --prefix=/opt/pgxl
make -j8
sudo make install
cd contrib/pgxc_ctl
make
sudo make install
```

PostgresXL now is installed in `/opt/pgxl`.

Expand the PATH (do this here, because of the way that `pgxc_ctl` works):

```console
postgres@bvr-sql18:~$ cat /etc/environment 
PATH="/opt/pgxl/bin:/opt/crossbar/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
```

### GTM Proxy Patch

```console
oberstet@bvr-sql18:~/scm/3rdparty/postgres-xl$ git diff
diff --git a/src/include/gtm/gtm_proxy.h b/src/include/gtm/gtm_proxy.h
index 068d59e..fa20648 100644
--- a/src/include/gtm/gtm_proxy.h
+++ b/src/include/gtm/gtm_proxy.h
@@ -61,7 +61,7 @@ typedef struct GTMProxy_Connections
 } GTMProxy_Connections;

 #define ERRORDATA_STACK_SIZE  20
-#define GTM_PROXY_MAX_CONNECTIONS      1024
+#define GTM_PROXY_MAX_CONNECTIONS      4096

 typedef struct GTMProxy_ThreadInfo
 {
```

## Storage Setup

Install the XFS filesystem utilities:

```
sudo apt-get install -y xfsprogs
```

Check existing array:

```
sudo mdadm --detail /dev/md2
```

Stop and destroy existing array:

```
sudo mdadm --stop /dev/md2
sudo mdadm --remove /dev/md2
sudo mdadm --zero-superblock /dev/nvme0n1
sudo mdadm --zero-superblock /dev/nvme1n1
sudo mdadm --zero-superblock /dev/nvme2n1
sudo mdadm --zero-superblock /dev/nvme3n1
sudo mdadm --zero-superblock /dev/nvme4n1
sudo mdadm --zero-superblock /dev/nvme5n1
sudo mdadm --zero-superblock /dev/nvme6n1
sudo mdadm --zero-superblock /dev/nvme7n1
sudo dd if=/dev/zero of=/dev/nvme0n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme1n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme2n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme3n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme4n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme5n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme6n1 bs=4096 count=1000
sudo dd if=/dev/zero of=/dev/nvme7n1 bs=4096 count=1000
```

We now partition each of the eight 2TB NVMes into eight partitions:

```
(echo g; echo p; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
echo w;) | sudo fdisk /dev/nvme0n1
```

and then create a filesystem on each partition:

```
sudo mkdir -p /data/pgxl/node1/shard1
sudo mkfs.xfs -f /dev/nvme0n1p1
sudo mount -o defaults,noatime,discard,nobarrier /dev/nvme0n1p1 /data/pgxl/node1/shard1
```


There is a Python script `postgresxl.py` to automate this.

We will end up with 64 shards:

```console
oberstet@bvr-sql18:~$ mount | grep nvme
/dev/nvme0n1p1 on /data/pgxl/node1/shard1 type xfs (rw,noatime,attr2,discard,nobarrier,inode64,noquota)
/dev/nvme0n1p2 on /data/pgxl/node1/shard2 type xfs (rw,noatime,attr2,discard,nobarrier,inode64,noquota)
/dev/nvme0n1p3 on /data/pgxl/node1/shard3 type xfs (rw,noatime,attr2,discard,nobarrier,inode64,noquota)
...
rw,noatime,attr2,discard,nobarrier,inode64,noquota)
/dev/nvme7n1p7 on /data/pgxl/node8/shard7 type xfs (rw,noatime,attr2,discard,nobarrier,inode64,noquota)
/dev/nvme7n1p8 on /data/pgxl/node8/shard8 type xfs (rw,noatime,attr2,discard,nobarrier,inode64,noquota)
```

Change the owner of the root data directory:

```
sudo chown -R postgres:postgres /data/pgxl/
```

## Cluster Setup

Postgres-XL comes with a special tool [pgxc_ctl](http://postgres-x2.github.io/presentation_docs/2014-05-07_pgxc_ctl_Primer/Pgxc_ctlprimer.pdf) which is used to create, manage and monitor a PG-XL cluster.

The tool uses SSH connections to connect to nodes and setup/control stuff there. Therefor, you will need password-less SSH login for the PG-XL (usually `postgres`) user working.

Further, the tool may open multiple SSH connections in parallel. By default, many SSH daemons are configured to deny too many parallel SSH connection attempts ("ssh_exchange_identification: Connection closed by remote host"). See [here](http://unix.stackexchange.com/questions/136693/maxstartups-and-maxsessions-configurations-parameter-for-ssh-connections). You likely will need to increase the limits:

```
sudo echo "MaxStartups 256" >> /etc/ssh/sshd_config
sudo service sshd restart
```

Create a PostgresXL service user

```
sudo adduser postgres
```

To prepare an default configuration

```
pgxc_ctl prepare
vim ~/pgxc_ctl/pgxc_ctl.conf
```
 
The configurations we tested can be found at `GIT/user/oberstet/pgxl/pgxc_ctl-8x.conf` and so on. To use one of these configs, copy over the config

```
cp ~/scm/parcit/RA/user/oberstet/pgxl/pgxc_ctl-8x.conf
```

Now initialize the cluster:

```
pgxc_ctl init all | tee pgxl_init.log
```

The tool can also work interactively:

```
postgres@bvr-sql18:~$ pgxc_ctl
/bin/bash
Installing pgxc_ctl_bash script as /home/postgres/pgxc_ctl/pgxc_ctl_bash.
Installing pgxc_ctl_bash script as /home/postgres/pgxc_ctl/pgxc_ctl_bash.
Reading configuration using /home/postgres/pgxc_ctl/pgxc_ctl_bash --home /home/postgres/pgxc_ctl --configuration /home/postgres/pgxc_ctl/pgxc_ctl.conf
Finished to read configuration.
   ******** PGXC_CTL START ***************

Current directory: /home/postgres/pgxc_ctl
PGXC monitor all
Running: gtm master
Running: coordinator master coord1
Running: datanode master node1shard1
Running: datanode master node1shard2
Running: datanode master node2shard1
Running: datanode master node2shard2
Running: datanode master node3shard1
Running: datanode master node3shard2
Running: datanode master node4shard1
Running: datanode master node4shard2
Running: datanode master node5shard1
Running: datanode master node5shard2
Running: datanode master node6shard1
Running: datanode master node6shard2
Running: datanode master node7shard1
Running: datanode master node7shard2
Running: datanode master node8shard1
Running: datanode master node8shard2
PGXC
```

Login as DB superuser at the coordinator and do some stuff

```
postgres@bvr-sql18:~$ psql
psql (PGXL 9.5alpha1, based on PG 9.5alpha1 (Postgres-XL 9.5alpha1))
Type "help" for help.

postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD '123456';
ALTER ROLE
postgres=# create database test1;
CREATE DATABASE
postgres=# \q
```

## Fixing after setup

Here is a dirty quick trick to expand the PG config after the cluster has already been setup:

```
find /data/pgxl/ -type f -name "postgresql.conf" -exec sh -c 'echo "max_connections = 8192" >> {}' \;
find /data/pgxl/node* -type f -name "postgresql.conf" -exec sh -c 'echo "max_prepared_transactions = 8192" >> {}' \;
```

# Assessment

| Variant | Accel. WHERE | Accel. JOIN | Accel. GROUP BY | Accel. DML | Transparent | Vanilla PG | "No unknown unknowns" |
|---------|--------------|-------------|-----------------|------------|-------------|------------|--------|
| PostgreSQL 9.5 + SQL Balancer | yes | yes | yes | yes | no | yes | yes |
| PostgreSQL 9.6 ([here](https://www.pgcon.org/2015/schedule/attachments/374_Parallel%20Seq%20Scan.pdf)) | yes | no | no | no | yes | yes | yes |
| Postgres-XL 9.5 | yes | yes | yes | yes | yes | no | no |
| CitusDB | ? | ? | ? | ? | ? | no | no |







