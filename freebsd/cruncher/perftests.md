# Background

## Storage Performance

### NVMe

The **cruncher** machine has eight [Intel P3700 2TB](http://www.intel.com/content/www/us/en/solid-state-drives/intel-ssd-dc-family-for-pcie.html) flash-memory PCIe cards with a total of 16TB fast flash-memory.

The Intel [specification](http://www.intel.com/content/dam/www/public/us/en/documents/product-specifications/ssd-dc-p3700-spec.pdf) list a number of performance metrics:

1. Sequential Read (Write) up to 2,800 MB/s (2,000 MB/s)
2. Random 4KB Read (Write) up to 450,000 IOPS (175,000 IOPS)
3. Random 4KB 70/30 Read-Write up to 265,000 IOPS
4. Random 8KB Read (Write) 295,000 IOPS (90,000 IOPS)

Our first goal is to verify these performance numbers on **cruncher** running FreeBSD and at the block device level (single NVMe device) using FIO, a storage performance testing tool.

The second goal is to determine how much of the above raw performance is available at the ZFS filesystem level when the latter are created on ZFS pool spanning one or multiple of the NVMe devices.

Our expectation would be to meet the Intel specification performance values up to 80%, and at least 50% at the filesystem level.

> Due to caching at the filesystem level, we need to be careful with the latter goal of 50% performance.

Our final goal would be to compare the performance of the PostgreSQL standard pgbench test on a database instance running from a NVMe backend pool compared to a pool on the internal Intel DC S3700 SSDs.

> **cruncher** has eight Intel P3700 2TB NVMe disks, twelve internal Intel DC S3700 800GB SSDs connected and 24 external Seagate ES.3 6TB harddrives.


#### Identifying hardware

[nvmecontrol](https://www.freebsd.org/cgi/man.cgi?query=nvmecontrol) is a FreeBSD system tool that allows to query and manage NVMe devices:

```console
root@s4l-zfs:~/oberstet # which nvmecontrol
/sbin/nvmecontrol
```

To list all devices:

```console
root@s4l-zfs:~/oberstet # nvmecontrol devlist
 nvme0: INTEL SSDPEDMD020T4
    nvme0ns1 (1907729MB)
 nvme1: INTEL SSDPEDMD020T4
    nvme1ns1 (1907729MB)
 nvme2: INTEL SSDPEDMD020T4
    nvme2ns1 (1907729MB)
 nvme3: INTEL SSDPEDMD020T4
    nvme3ns1 (1907729MB)
 nvme4: INTEL SSDPEDMD020T4
    nvme4ns1 (1907729MB)
 nvme5: INTEL SSDPEDMD020T4
    nvme5ns1 (1907729MB)
 nvme6: INTEL SSDPEDMD020T4
    nvme6ns1 (1907729MB)
 nvme7: INTEL SSDPEDMD020T4
    nvme7ns1 (1907729MB)
```
