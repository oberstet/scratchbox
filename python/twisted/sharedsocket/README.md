## Test Setup

The host is a Intel Core i7 (quad core, HT enabled, 3.4GHz) with 12GB RAM running Ubuntu 12.04 LTS 64 bit.

Linux is running directly on hardware (no virtualization!).

Linux TCP networking is tuned as in the following.

Add the following to the end of `/etc/sysctl.conf` and do `sysctl -p`:

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

Further system level tuning:

Modify `/etc/security/limits.conf` for the following

	# wildcard does not work for root, but for all other users
	*               soft     nofile           1048576
	*               hard     nofile           1048576
	# settings should also apply to root
	root            soft     nofile           1048576
	root            hard     nofile           1048576

and add the following line

	session required pam_limits.so

to both of these files at the end:

	/etc/pam.d/common-session
	/etc/pam.d/common-session-noninteractive

Reboot.

Check that you get large (`1048576`) FD limit:

	ulimit -n

Probably also check that above `sysctl` settings actually are in place (`sysctl -a | grep ..` or such).

[PyPy](http://pypy.org/) is from

	cd $HOME/tarballs
	wget https://bitbucket.org/pypy/pypy/downloads/pypy-2.1-linux64.tar.bz2
    cd $HOME
	tar xvjf pypy-2.1-linux64.tar.bz2

and using stock Twisted 13.1 release:

	cd $HOME/tarballs
	wget https://pypi.python.org/packages/source/T/Twisted/Twisted-13.1.0.tar.bz2
	cd $HOME/build
	tar xvjf ../Twisted-13.1.0.tar.bz2
	cd Twisted-13.1.0
	$HOME/pypy-2.1/bin/pypy setup.py install


Nginx is setup and run (on port 80) like this

	sudo apt-get install nginx
	sudo service nginx start
	sudo su
	echo "<html>Hello, world! [Nginx      ]</html>" > /usr/share/nginx/www/index.html

The `index.html` file size is exactly the same for Nginx and Twisted Web.

> I have no clue at all if the default Nginx is already tuned or what. If anybody has any hints on how to make it fly higher, please let me know!


For HTTP load testing, we use [weighttp](http://redmine.lighttpd.net/projects/weighttp/wiki), which uses [libev](http://software.schmorp.de/pkg/libev.html) for scalable processing based on `epoll()` and can generate stable and scalable concurrent load on SMP systems.

Note that a lot of tools suck for the stuff we do here, e.g. HTTPerf uses `select()`, not `epoll` and will fail badly. It also sucks regarding generating concurrent load. Read more [here](http://gwan.com/en_apachebench_httperf.html).

Hence:

	sudo apt-get install libev-dev
	cd $HOME/build
	git clone git://git.lighttpd.net/weighttp
	cd weighttp
	./waf configure
	sudo ./waf install

For easy load inspection (broken down by process and thread):

	sudo apt-get install htop


## Testing


	cd
	$HOME/pypy-2.1/bin/pypy server.py

With Keep-alive:

	weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"
	weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1/"

Without Keep-alive.

	weighttp -n 100000 -c 500 -t 4 "http://127.0.0.1:8080/"
	weighttp -n 100000 -c 500 -t 4 "http://127.0.0.1/"

## Appendix

### Linux sysctl vars of interest

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


### Resources

  * http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
  * http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
  * http://twistedmatrix.com/trac/browser/trunk/twisted/internet/posixbase.py#L449
  * http://twistedmatrix.com/trac/browser/trunk/twisted/internet/interfaces.py#L895
  * http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
  * http://twistedmatrix.com/pipermail/twisted-commits/2012-March/034524.html
  * http://twistedmatrix.com/documents/current/core/howto/endpoints.html
  * http://terraltech.com/how-to-test-your-websites-performance/
  * http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/023/2333/2333s2.html
  * http://fasterdata.es.net/host-tuning/linux/
  * http://www.lognormal.com/blog/2012/09/27/linux-tcpip-tuning/
  * http://www.linuxinstruction.com/?q=node/15
  * https://www.varnish-cache.org/lists/pipermail/varnish-misc/2008-April/016139.html
  * https://github.com/rfk/threading2
  * https://greenhost.nl/2013/04/10/multi-queue-network-interfaces-with-smp-on-linux/
  * http://software.intel.com/en-us/articles/improved-linux-smp-scaling-user-directed-processor-affinity
  * https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/
  * http://www.linuxvox.com/2009/11/what-is-the-linux-kernel-parameter-tcp_low_latency/

