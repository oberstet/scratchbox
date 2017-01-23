TMPL_PARTITION = r"""
(echo g; echo p; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
    echo n; echo; echo; echo +488378385; \
echo w;) | sudo fdisk {device}
"""

import subprocess

def setup():
    for i in range(8):

        # force unmount and remove all mountpoints
        for j in range(8):
            mountpoint = "/data/pgxl/node{}/shard{}".format(i + 1, j + 1)
            subprocess.call("umount -f {}".format(mountpoint), shell=True)
            subprocess.call("rm -rf {}".format(mountpoint), shell=True)
        subprocess.call("rm -rf /data/pgxl/node{}".format(i + 1), shell=True)

        # partition node storage
        device = "/dev/nvme{}n1".format(i)
        subprocess.call(TMPL_PARTITION.format(device=device), shell=True)

        # create filesystems and mountpoints
        for j in range(8):
            partition = "/dev/nvme{}n1p{}".format(i, j + 1)
            mountpoint = "/data/pgxl/node{}/shard{}".format(i + 1, j + 1)

            # create filesystem
            # http://blog.tsunanet.net/2011/08/mkfsxfs-raid10-optimal-performance.html
            subprocess.call("mkfs.xfs -f {}".format(partition), shell=True)

            # create mountpoint and mount filesystem
            subprocess.call("mkdir -p {}".format(mountpoint), shell=True)
            subprocess.call("sudo mount -o defaults,noatime,discard,nobarrier {} {}".format(partition, mountpoint), shell=True)

setup()
