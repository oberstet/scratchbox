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

To query a controller:

```console
root@s4l-zfs:~/oberstet # nvmecontrol identify nvme0
Controller Capabilities/Features
================================
Vendor ID:                  8086
Subsystem Vendor ID:        8086
Serial Number:              CVFT4476002A2P0EGN
Model Number:               INTEL SSDPEDMD020T4
Firmware Version:           8DV10130
Recommended Arb Burst:      0
IEEE OUI Identifier:        e4 d2 5c
Multi-Interface Cap:        00
Max Data Transfer Size:     131072

Admin Command Set Attributes
============================
Security Send/Receive:       Not Supported
Format NVM:                  Supported
Firmware Activate/Download:  Supported
Abort Command Limit:         4
Async Event Request Limit:   4
Number of Firmware Slots:    1
Firmware Slot 1 Read-Only:   No
Per-Namespace SMART Log:     No
Error Log Page Entries:      64
Number of Power States:      1

NVM Command Set Attributes
==========================
Submission Queue Entry Size
  Max:                       64
  Min:                       64
Completion Queue Entry Size
  Max:                       16
  Min:                       16
Number of Namespaces:        1
Compare Command:             Not Supported
Write Uncorrectable Command: Supported
Dataset Management Command:  Supported
Volatile Write Cache:        Not Present
```

To get information on a namespace:

```console
root@s4l-zfs:~/oberstet # nvmecontrol identify nvme0ns1
Size (in LBAs):              3907029168 (3726M)
Capacity (in LBAs):          3907029168 (3726M)
Utilization (in LBAs):       3907029168 (3726M)
Thin Provisioning:           Not Supported
Number of LBA Formats:       7
Current LBA Format:          LBA Format #00
LBA Format #00: Data Size:   512  Metadata Size:     0
LBA Format #01: Data Size:   512  Metadata Size:     8
LBA Format #02: Data Size:   512  Metadata Size:    16
LBA Format #03: Data Size:  4096  Metadata Size:     0
LBA Format #04: Data Size:  4096  Metadata Size:     8
LBA Format #05: Data Size:  4096  Metadata Size:    64
LBA Format #06: Data Size:  4096  Metadata Size:   128
```