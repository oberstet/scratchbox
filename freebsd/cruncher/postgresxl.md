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

Build it:

```
export CFLAGS="-O3 -march=native -mtune=native"
#./configure --with-openssl --prefix=/opt/pgxl # FIXME: does not work
./configure --prefix=/opt/pgxl
make -j8
sudo make install
cd contrib/pgxc_ctl
make
sudo make install
```

PostgresXL now is installed in `/opt/pgxl`.

Expand PATH:

```
echo "export PATH=/opt/pgxl/bin:${PATH}" >> ~/.profile
source ~/.profile
```

Create a PostgresXL service user and prepare a config:

```
sudo adduser postgres
pgxc_ctl prepare
vim ~/pgxc_ctl/pgxc_ctl.conf
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
