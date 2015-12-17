# cgroups

References:

* https://the.binbashtheory.com/control-resources-cgroups/
* http://packages.ubuntu.com/trusty/admin/cgroup-bin
* https://wiki.archlinux.org/index.php/Cgroups
* https://www.kernel.org/doc/Documentation/cgroups/
* http://blogs.rdoproject.org/7761/hands-on-linux-sandbox-with-namespaces-and-cgroups

Installing CLI tools:

```console
sudo apt-get install cgroup-bin
```

List cgroups subsystems:

```console
oberstet@bvr-sql18:~$ lssubsys
cpuset
cpu,cpuacct
memory
devices
freezer
net_cls,net_prio
blkio
perf_event
hugetlb
```

Check processes and cgroups:

```
ps -aeo pid,cgroup,command 
```

