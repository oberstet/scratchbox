# Scaling Twisted Web

**Too long to read? Go directly to the [RESULTS](https://github.com/oberstet/scratchbox/raw/master/python/twisted/sharedsocket/results.pdf).**

This is the first part of a series of experiments in preparation for a system design with Autobahn/Twisted that allows to:

 * scale-up on multicore
 * scale-out on cluster (LAN)
 * federate (WAN)

The first part here is about scaling up Twisted Web on multicore.

A Twisted Web based server is demonstrated that consists of a master process that creates a TCP listening socket, and then spawns multiple background worker processes that then *directly* accept incoming TCP connections and process HTTP requests.

The testing was done using PyPy 2.1 and Twisted 13.1, both stock release versions.

We compare the performance to Nginx.

Test results are [here](https://github.com/oberstet/scratchbox/raw/master/python/twisted/sharedsocket/results.pdf) with detailed test setup description and test logs further below.

I encourage anybody interested to repeat and verify the testing. Personally, I find the results quite encouraging. But seeing is believing;)

There is no bottleneck, and this design should in principle scale linearly with the number of available cores. The credits for the approach go to [Jean-Paul Calderone](http://as.ynchrono.us/). Thanks again Jean-Paul for another incredible helpful [answer](http://stackoverflow.com/a/10088578/884770). Any bugs, issues and mistakes here are my own;)

> Note that is neither expected and nor the goal to beat Nginx (at it's own game) here. That would be obviously folly. Though I have ideas to close the gap even further.
> 

## Test Setup

The host is a Intel Core i7 (4 real cores, HT enabled, 3.4GHz) with 12GB RAM running Ubuntu 12.04 LTS 64 bit.

Linux is running directly on hardware (no virtualization!).

Linux TCP networking is tuned as in the following. This (or similar) is *required*, since we are really pushing the system.

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

Reboot (or at least I don't know how to make it immediate without reboot).

Check that you actually got large (`1048576`) FD limit:

	ulimit -n

Probably also check that above `sysctl` settings actually are in place (`sysctl -a | grep ..` or such). I am paranoid.

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
	sudo chmod 666 /usr/share/nginx/www/index.html

> I have no clue at all if the default Nginx is already tuned or what. If anybody has any hints on how to make it fly higher, please let me know!


For HTTP load testing, we use [weighttp](http://redmine.lighttpd.net/projects/weighttp/wiki), which uses [libev](http://software.schmorp.de/pkg/libev.html) for scalable processing based on `epoll()` and can generate stable and scalable concurrent load on SMP systems.

Note that a lot of tools suck for the stuff we do here, e.g. HTTPerf uses `select()`, not `epoll` and will fail badly. It also sucks regarding generating (massive) concurrent load. Read more [here](http://gwan.com/en_apachebench_httperf.html).

Hence:

	sudo apt-get install libev-dev
	cd $HOME/build
	git clone git://git.lighttpd.net/weighttp
	cd weighttp
	./waf configure
	sudo ./waf install

For easy load inspection (broken down by process and thread):

	sudo apt-get install htop


## Testing and Result Logs

Notes:

  * for the Twisted/PyPy, make sure you run the load client a couple of times to allow the JITting to warmup on the hotpaths
  * for Nginx: the examples are run with reduced concurrency (1000) versus Twisted/PyPy (4000), since Nginx will bailout giving me TCP connection resets (104). Further tuning is needed here.

### Twisted Web 1a (10000 bytes payload, `Fixed` resource)

Server:

	$ ~/pypy-2.1/bin/pypy server.py --silence --resource fixed --payload 10000

Load:

	$ weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 1000 concurrent requests, 250000 total requests
	spawning thread #2: 1000 concurrent requests, 250000 total requests
	spawning thread #3: 1000 concurrent requests, 250000 total requests
	spawning thread #4: 1000 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 19 sec, 726 millisec and 699 microsec, 50692 req/s, 501531 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 10131000000 bytes total, 131000000 bytes http, 10000000000 bytes data


### Twisted 1b (10000 bytes payload, `static.File` resource)

Server:

	~/pypy-2.1/bin/pypy server.py --silence --resource file --payload 10000

Load:

	$ weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 1000 concurrent requests, 250000 total requests
	spawning thread #2: 1000 concurrent requests, 250000 total requests
	spawning thread #3: 1000 concurrent requests, 250000 total requests
	spawning thread #4: 1000 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 57 sec, 704 millisec and 696 microsec, 17329 req/s, 172602 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 10199000000 bytes total, 199000000 bytes http, 10000000000 bytes data


### Nginx 1

Server: started from system (see Test Setup), but add payload to `index.html`:

	python -c "import sys; sys.stdout.write('*'*10000)" > /usr/share/nginx/www/index.html
	wc -c /usr/share/nginx/www/index.html

Load:

	$ weighttp -n 1000000 -c 1000 -t 4 -k "http://127.0.0.1/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 250 concurrent requests, 250000 total requests
	spawning thread #2: 250 concurrent requests, 250000 total requests
	spawning thread #3: 250 concurrent requests, 250000 total requests
	spawning thread #4: 250 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 12 sec, 156 millisec and 126 microsec, 82263 req/s, 820859 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 10217951280 bytes total, 217951280 bytes http, 10000000000 bytes data


### Twisted 2a (40 bytes payload, `Fixed` resource)

Server:

	$ ~/pypy-2.1/bin/pypy server.py --silence --resource fixed --payload 40

Load:

	$ weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 1000 concurrent requests, 250000 total requests
	spawning thread #2: 1000 concurrent requests, 250000 total requests
	spawning thread #3: 1000 concurrent requests, 250000 total requests
	spawning thread #4: 1000 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 16 sec, 21 millisec and 887 microsec, 62414 req/s, 10239 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 168000000 bytes total, 128000000 bytes http, 40000000 bytes data


### Twisted 2b (40 bytes payload, `static.File` resource)

Server:

	$ ~/pypy-2.1/bin/pypy server.py --silence --payload 40

Load:

	$ weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 1000 concurrent requests, 250000 total requests
	spawning thread #2: 1000 concurrent requests, 250000 total requests
	spawning thread #3: 1000 concurrent requests, 250000 total requests
	spawning thread #4: 1000 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 45 sec, 867 millisec and 552 microsec, 21801 req/s, 5024 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 236000000 bytes total, 196000000 bytes http, 40000000 bytes data
	oberstet@corei7-ubuntu:~/scm/scratchbox/python/twisted/sharedsocket$ 


### Nginx 2 (40 bytes payload)

Server: started from system (see Test Setup), but add payload to `index.html`:

	python -c "import sys; sys.stdout.write('*'*40)" > /usr/share/nginx/www/index.html
	wc -c /usr/share/nginx/www/index.html

Load:

	$ weighttp -n 1000000 -c 1000 -t 4 -k "http://127.0.0.1/"
	weighttp - a lightweight and simple webserver benchmarking tool

	starting benchmark...
	spawning thread #1: 250 concurrent requests, 250000 total requests
	spawning thread #2: 250 concurrent requests, 250000 total requests
	spawning thread #3: 250 concurrent requests, 250000 total requests
	spawning thread #4: 250 concurrent requests, 250000 total requests
	progress:  10% done
	progress:  20% done
	progress:  30% done
	progress:  40% done
	progress:  50% done
	progress:  60% done
	progress:  70% done
	progress:  80% done
	progress:  90% done
	progress: 100% done

	finished in 11 sec, 575 millisec and 954 microsec, 86385 req/s, 21508 kbyte/s
	requests: 1000000 total, 1000000 started, 1000000 done, 1000000 succeeded, 0 failed, 0 errored
	status codes: 1000000 2xx, 0 3xx, 0 4xx, 0 5xx
	traffic: 254951105 bytes total, 214951105 bytes http, 40000000 bytes data


## Appendix

### Pystone

For comparison of the host system used for testing to other systems:

CPython:

	$ python -m test.pystone
	Pystone(1.1) time for 50000 passes = 0.47
	This machine benchmarks at 106383 pystones/second

PyPy:

	~/pypy-2.1/bin/pypy -m test.pystone
	Traceback (most recent call last):
	  File "app_main.py", line 72, in run_toplevel
	IOError: [Errno 2] No such file or directory: 'se-m'



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
