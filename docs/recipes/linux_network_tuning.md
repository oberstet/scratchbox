# Linux Network Tuning

The Linux TCP/IP networking stack is quite capable and well configured out of the box. It also does some autotuning that often works pretty good (and for some parameters better than you can do manually).

That being said, for production use with significant network load or benchmarking and load testing, it needs some tuning.

In particular we want to run millions of concurrent TCP connections, sustain a high turnover rate of new and disappearing TCP connections, and get low latency on those.

Caveats.

> 1. You will need enough memory to reach those numbers.
> 2. We assume a dedicated server (no local user issues like security and other). 
> 3. I am no expert on this. This stuff should probably being considered experimental and base-level.
> 4. Don't call me if those settings break your machine - call your mom;)


## Large connection numbers

The following allows for 16 Mio. open TCP connections / open file descriptors and a deep TCP accept queue (8k connections).

Add the following to the end of `/etc/sysctl.conf` and do `sysctl -p` to immediately load the settings without reboot:

	net.core.somaxconn = 8192
	net.ipv4.tcp_max_orphans = 8192
	net.ipv4.tcp_max_syn_backlog = 8192
	net.core.netdev_max_backlog = 262144
	
	net.ipv4.ip_local_port_range = 1024 65535
	
	#net.ipv4.tcp_low_latency = 1
	#net.ipv4.tcp_window_scaling = 0
	#net.ipv4.tcp_syncookies = 0
	
	fs.file-max = 16777216
	fs.pipe-max-size = 134217728

Modify `/etc/security/limits.conf` for the following:

	# wildcard does not work for root, but for all other users
	*               soft     nofile           16777216
	*               hard     nofile           16777216
	# settings should also apply to root
	root            soft     nofile           16777216
	root            hard     nofile           16777216

and add the following line

	session required pam_limits.so

to *both* of these files at the end:

	/etc/pam.d/common-session
	/etc/pam.d/common-session-noninteractive

Reboot (or at least I don't know how to make it immediate without reboot).

After reboot, check that you actually got large (`16777216`) FD limit:

	ulimit -n

Probably also check that above `sysctl` settings actually are in place (`sysctl -a | grep ..` or such). I am paranoid.


## Linux tunables of interest

Linux has a insane number of kernel tunables. The following seem to be of particular interest to (TPC/IP) networking (list via `sysctl -a`):

	fs.file-max
	fs.pipe-max-size
	fs.file-nr
	net.core.somaxconn
	net.core.netdev_max_backlog
	net.ipv4.tcp_max_syn_backlog
	net.ipv4.tcp_max_orphans
	net.ipv4.ip_local_port_range
	net.core.optmem_max
	net.ipv4.tcp_mem
	net.core.rmem_default
	net.core.rmem_max
	net.ipv4.tcp_rmem
	net.core.wmem_default
	net.core.wmem_max
	net.ipv4.tcp_wmem
	net.ipv4.tcp_congestion_control
	net.ipv4.tcp_fastopen
	net.ipv4.tcp_low_latency
	net.ipv4.tcp_window_scaling


## Resources

The following are some resources I found useful:

  * [sysctl man page](http://linux.die.net/man/8/sysctl)
  * [IP networking tunables kernel docs](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt)
  * [TCP listen() Backlog](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/023/2333/2333s2.html)
  * [Linux Tuning](http://fasterdata.es.net/host-tuning/linux/)
  * [The USE Method: Linux Performance Checklist](http://dtrace.org/blogs/brendan/2012/03/07/the-use-method-linux-performance-checklist/)
  * [Linux TCP/IP tuning for scalability](http://www.lognormal.com/blog/2012/09/27/linux-tcpip-tuning/)
  * [Kernel tuning for the TCP stack](http://www.linuxinstruction.com/?q=node/15)
  * [Multi-queue network interfaces with SMP on Linux](https://greenhost.nl/2013/04/10/multi-queue-network-interfaces-with-smp-on-linux/)
  * [Improved Linux SMP Scaling: User-directed Processor Affinity](http://software.intel.com/en-us/articles/improved-linux-smp-scaling-user-directed-processor-affinity)
  * [Red Hat Enterprise Linux 6
Performance Tuning Guide](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/)
  * [What is the linux kernel parameter "TCP low-latency"?](http://www.linuxvox.com/2009/11/what-is-the-linux-kernel-parameter-tcp_low_latency/)
