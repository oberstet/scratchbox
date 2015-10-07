# Login

Login to the server using `postgres` - **not** as `oberstet` and then `sudo su -l postgres`.

> The reason for this is the way that `pgxc_ctl` works: it open SSH connections to the target nodes (in this case the machine itself), and to make that work without passwords, it has to work using public-private key auth. and using SSH agent. And SSH agent forwarding does break when doing `sudo su`.

# Prepare

You are now in the HOME of `postgres`: `/home/postgres`.

You will need `pgxc_ctl` and have a proper `pgxc_ctl.conf`:

```
postgres@bvr-sql18:~$ which pgxc_ctl
/opt/pgxl/bin/pgxc_ctl
postgres@bvr-sql18:~$ ls -la ./pgxc_ctl/pgxc_ctl.conf
-rw-rw-r-- 1 postgres postgres 6178 Okt  6 09:34 ./pgxc_ctl/pgxc_ctl.conf
postgres@bvr-sql18:~$
```

First check if a cluster is running. Start `pgxc_ctl` and enter `monitor all`:

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
Running: gtm proxy gtm_proxy1
Running: coordinator master coord1
Running: datanode master node1shard1
Running: datanode master node1shard2
Running: datanode master node1shard3
Running: datanode master node1shard4
Running: datanode master node2shard1
Running: datanode master node2shard2
Running: datanode master node2shard3
Running: datanode master node2shard4
Running: datanode master node3shard1
Running: datanode master node3shard2
Running: datanode master node3shard3
Running: datanode master node3shard4
Running: datanode master node4shard1
Running: datanode master node4shard2
Running: datanode master node4shard3
Running: datanode master node4shard4
Running: datanode master node5shard1
Running: datanode master node5shard2
Running: datanode master node5shard3
Running: datanode master node5shard4
Running: datanode master node6shard1
Running: datanode master node6shard2
Running: datanode master node6shard3
Running: datanode master node6shard4
Running: datanode master node7shard1
Running: datanode master node7shard2
Running: datanode master node7shard3
Running: datanode master node7shard4
Running: datanode master node8shard1
Running: datanode master node8shard2
Running: datanode master node8shard3
Running: datanode master node8shard4
PGXC
```

To stop the running cluster, enter `stop all`.

This will take a while! Be patient and do not interrupt the process. When the command has finished, do `monitor all` again.

Then exit `pgxc_ctl` and recheck that XL has shut down completely and no processes are running any more:

```
ps -Af | grep postgres | wc -l
```

or 

```
pgrep postgres | wc -l
```

This is important. Something, `pgxc_ctl` fails to stop everything. Can be a little tricky.

Now scratch the data directories of all XL parts:

```
make destroy
```

This will do:

```
postgres@bvr-sql18:~$ cat Makefile
destroy:
        rm -rf /data/pgxl/coord1/
        rm -rf /data/pgxl/gtm1/
        rm -rf /data/pgxl/gtm_proxy1/
        rm -rf /data/pgxl/node1/shard1/*
        rm -rf /data/pgxl/node1/shard2/*
        rm -rf /data/pgxl/node1/shard3/*
        rm -rf /data/pgxl/node1/shard4/*
        rm -rf /data/pgxl/node1/shard5/*
        rm -rf /data/pgxl/node1/shard6/*
        rm -rf /data/pgxl/node1/shard7/*
        rm -rf /data/pgxl/node1/shard8/*
        rm -rf /data/pgxl/node2/shard1/*
        rm -rf /data/pgxl/node2/shard2/*
        rm -rf /data/pgxl/node2/shard3/*
        rm -rf /data/pgxl/node2/shard4/*
        rm -rf /data/pgxl/node2/shard5/*
        rm -rf /data/pgxl/node2/shard6/*
        rm -rf /data/pgxl/node2/shard7/*
        rm -rf /data/pgxl/node2/shard8/*
        rm -rf /data/pgxl/node3/shard1/*
        rm -rf /data/pgxl/node3/shard2/*
        rm -rf /data/pgxl/node3/shard3/*
        rm -rf /data/pgxl/node3/shard4/*
        rm -rf /data/pgxl/node3/shard5/*
        rm -rf /data/pgxl/node3/shard6/*
        rm -rf /data/pgxl/node3/shard7/*
        rm -rf /data/pgxl/node3/shard8/*
        rm -rf /data/pgxl/node4/shard1/*
        rm -rf /data/pgxl/node4/shard2/*
        rm -rf /data/pgxl/node4/shard3/*
        rm -rf /data/pgxl/node4/shard4/*
        rm -rf /data/pgxl/node4/shard5/*
        rm -rf /data/pgxl/node4/shard6/*
        rm -rf /data/pgxl/node4/shard7/*
        rm -rf /data/pgxl/node4/shard8/*
        rm -rf /data/pgxl/node5/shard1/*
        rm -rf /data/pgxl/node5/shard2/*
        rm -rf /data/pgxl/node5/shard3/*
        rm -rf /data/pgxl/node5/shard4/*
        rm -rf /data/pgxl/node5/shard5/*
        rm -rf /data/pgxl/node5/shard6/*
        rm -rf /data/pgxl/node5/shard7/*
        rm -rf /data/pgxl/node5/shard8/*
        rm -rf /data/pgxl/node6/shard1/*
        rm -rf /data/pgxl/node6/shard2/*
        rm -rf /data/pgxl/node6/shard3/*
        rm -rf /data/pgxl/node6/shard4/*
        rm -rf /data/pgxl/node6/shard5/*
        rm -rf /data/pgxl/node6/shard6/*
        rm -rf /data/pgxl/node6/shard7/*
        rm -rf /data/pgxl/node6/shard8/*
        rm -rf /data/pgxl/node7/shard1/*
        rm -rf /data/pgxl/node7/shard2/*
        rm -rf /data/pgxl/node7/shard3/*
        rm -rf /data/pgxl/node7/shard4/*
        rm -rf /data/pgxl/node7/shard5/*
        rm -rf /data/pgxl/node7/shard6/*
        rm -rf /data/pgxl/node7/shard7/*
        rm -rf /data/pgxl/node7/shard8/*
        rm -rf /data/pgxl/node8/shard1/*
        rm -rf /data/pgxl/node8/shard2/*
        rm -rf /data/pgxl/node8/shard3/*
        rm -rf /data/pgxl/node8/shard4/*
        rm -rf /data/pgxl/node8/shard5/*
        rm -rf /data/pgxl/node8/shard6/*
        rm -rf /data/pgxl/node8/shard7/*
        rm -rf /data/pgxl/node8/shard8/*
```

# Setup

Make sure you have the desired cluster config in `./pgxc_ctl/pgxc_ctl.conf`.

For 32 nodes, here is what I used:

* [here](https://github.com/oberstet/scratchbox/blob/master/freebsd/cruncher/pgxl/pgxc_ctl-32x-proxy.conf)
* in the parcit repo under `users/oberstet/pgxl/pgxc_ctl-32x-proxy.conf`

Getting this config right can be tricky.

The start `pgxc_ctl` and enter `init all`.

This will take a while.

Then start the cluster: `start all`.

Check that the cluster has fully started (`monitor all`). If some parts haven't started, you may retry. Otherwise debug by looking into the logs of the respective cluster parts.


# Init

Run `psql` to change the superuser password and create the test database:

```
ALTER USER postgres WITH ENCRYPTED PASSWORD '123456';
CREATE DATABASE test1;
```

You should now be able to connect from desktop pgadmin.


# Test

The test script is

* [here](https://github.com/oberstet/scratchbox/blob/master/freebsd/cruncher/pgxl/test2.sql)
* in the parcit repo under `users/oberstet/pgxl/test2.sql`
