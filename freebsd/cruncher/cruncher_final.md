http://www.ducea.com/2009/03/08/mdadm-cheat-sheet/

>>>>>>> cbd6a0e478e50ec7612847c8c916c7fe640bb8fd
>>>>>> r http://download.opensuse.org/repositories/benchmark/SLE_12/ opensuse:benchmark
zypper ar http://download.opensuse.org/repositories/server:/monitoring/SLE_12/ opensuse:server:monitoring
zypper ar http://download.opensuse.org/repositories/devel:/tools/SLE_12/ opensuse:devel:tools
zypper ar http://download.opensuse.org/repositories/devel:/tools:/scm/SLE_12/ opensuse:devel:tools:scm
zypper ref


bvr-sql18:~ # ln -svf /usr/lib/systemd/system/multi-user.target /usr/lib/systemd/system/default.target
‘/usr/lib/systemd/system/default.target’ -> ‘/usr/lib/systemd/system/multi-user.target’
bvr-sql18:~ # ll /usr/lib/systemd/system/default.target
lrwxrwxrwx 1 root root 41 Apr 16 16:11 /usr/lib/systemd/system/default.target -> /usr/lib/systemd/system/multi-user.target

bvr-sql18:~ # init 3
bvr-sql18:~ # ps -Af | grep X


mdadm --create /dev/md0 --chunk=256 --level=0 --raid-devices=4 /dev/nvme0n1 /dev/nvme1n1 /dev/nvme2n1 /dev/nvme3n1

mdadm --detail /dev/md0

mdadm --stop /dev/md0
mdadm --remove /dev/md0
mdadm --zero-superblock /dev/nvme0n1
 

mdadm --create /dev/md0 --chunk=256 --level=0 --raid-devices=8 \
   /dev/nvme0n1 \
   /dev/nvme1n1 \
   /dev/nvme2n1 \
   /dev/nvme3n1 \
   /dev/nvme4n1 \
   /dev/nvme5n1 \
   /dev/nvme6n1 \
   /dev/nvme7n1



bvr-sql18:~/scratchbox/freebsd/cruncher/results # cat /proc/mdstat
Personalities : [raid1] [raid0]
md0 : active raid0 nvme3n1[3] nvme2n1[2] nvme1n1[1] nvme0n1[0]
      7813533696 blocks super 1.2 256k chunks

md125 : active raid1 sda3[0] sdd3[1]
      759385920 blocks super 1.0 [2/2] [UU]
      bitmap: 2/6 pages [8KB], 65536KB chunk

md126 : active raid1 sdd1[1] sda1[0]
      1051584 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

md127 : active raid1 sda2[0] sdd2[1]
      20972416 blocks super 1.0 [2/2] [UU]
      bitmap: 0/1 pages [0KB], 65536KB chunk

unused devices: <none>

 cbd6a0e478e50ec7612847c8c916c7fe640bb8fd
