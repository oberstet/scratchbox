# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/posixbase.py#L449
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/interfaces.py#L895
# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://twistedmatrix.com/pipermail/twisted-commits/2012-March/034524.html
# http://twistedmatrix.com/documents/current/core/howto/endpoints.html

# curl -s "http://192.168.56.101:8080/?[1-100000]" > /dev/null

# http://terraltech.com/how-to-test-your-websites-performance/
# sudo apt-get install httperf

# http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/023/2333/2333s2.html
# http://fasterdata.es.net/host-tuning/linux/
# http://www.lognormal.com/blog/2012/09/27/linux-tcpip-tuning/

# http://www.linuxinstruction.com/?q=node/15
## https://www.varnish-cache.org/lists/pipermail/varnish-misc/2008-April/016139.html
# https://github.com/rfk/threading2

# https://greenhost.nl/2013/04/10/multi-queue-network-interfaces-with-smp-on-linux/
# http://software.intel.com/en-us/articles/improved-linux-smp-scaling-user-directed-processor-affinity
# https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/

# oberstet@ubuntu1204-1:~$ cat /proc/sys/net/core/somaxconn
# 128
# oberstet@ubuntu1204-1:~$ cat /proc/sys/net/ipv4/tcp_max_syn_backlog
# 2048

# http://www.linuxvox.com/2009/11/what-is-the-linux-kernel-parameter-tcp_low_latency/

LINUX_SYSCTL_VARS = [
   'fs.file-max',
   'fs.pipe-max-size',
   'fs.file-nr',

   'net.core.somaxconn',
   'net.core.netdev_max_backlog',
   'net.ipv4.tcp_max_syn_backlog',
   'net.ipv4.tcp_max_orphans',

   'net.ipv4.ip_local_port_range',

   'net.core.optmem_max',
   'net.ipv4.tcp_mem',

   'net.core.rmem_default',
   'net.core.rmem_max',
   'net.ipv4.tcp_rmem',

   'net.core.wmem_default',
   'net.core.wmem_max',
   'net.ipv4.tcp_wmem',

   'net.ipv4.tcp_congestion_control',
   'net.ipv4.tcp_fastopen',
   #'net.ipv4.tcp_fastopen_key',
   'net.ipv4.tcp_low_latency',

   'net.ipv4.tcp_window_scaling'
] 

## Add the following to the end of /etc/sysctl.conf and do "sysctl -p"
##
LINUX_SYSCTL_CONF = """
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
"""

## Modify /etc/security/limits.conf for the following
##
LINUX_LIMITS_CONF = """
# wildcard does not work for root, but for all other users
*               soft     nofile           1048576
*               hard     nofile           1048576
# settings should also apply to root
root            soft     nofile           1048576
root            hard     nofile           1048576
"""

### Add the following line to both (!) of these files at the end:
##
## session required pam_limits.so
##
## /etc/pam.d/common-session
## /etc/pam.d/common-session-noninteractive



# httperf --server 127.0.0.1 --port 8080 --num-conns 100000 --rate 10000

# http://gwan.com/en_apachebench_httperf.html


# sudo apt-get install htop


# http://redmine.lighttpd.net/projects/weighttp/wiki
#
# sudo apt-get install libev-dev
# git clone git://git.lighttpd.net/weighttp
# cd weighttp
# ./waf configure
# sudo ./waf install

# weighttp -n 1000000 -c 4000 -t 4 -k "http://127.0.0.1:8080/"


import choosereactor

import sys, os
from os import environ
from sys import argv, executable
from socket import AF_INET

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web import server, resource


class Simple(resource.Resource):
   isLeaf = True
   def render_GET(self, request):
      self.cnt += 1
      return ""
      print self.ident
      return "<html>Hello, world!</html>"


def main(fd = None):
   log.startLogging(sys.stdout)
   print "Using Twisted reactor class %s" % str(reactor.__class__)

   root = File(".")
   root = Simple()
   root.cnt = 0
   factory = Site(root)
   factory.log = lambda _: None # disable any logging

   if fd is None:
      root.ident = "master", os.getpid(), os.getppid()
      print root.ident, "started"

      # Create a new listening port and several other processes to help out.
      port = reactor.listenTCP(8080, factory, backlog = 10000)

      ## we only want to accept on workers, not master:
      ## http://twistedmatrix.com/documents/current/api/twisted.internet.abstract.FileDescriptor.html#stopReading
      port.stopReading()

      for i in range(4):
         reactor.spawnProcess(
            None, executable, [executable, __file__, str(port.fileno())],
            childFDs = {0: 0, 1: 1, 2: 2, port.fileno(): port.fileno()},
            env = environ)
   else:
      root.ident = "worker", os.getpid(), os.getppid()
      print root.ident, "started"
      # Another process created the port, just start listening on it.
      port = reactor.adoptStreamPort(fd, AF_INET, factory)

   def stat():
      print root.ident, root.cnt
      reactor.callLater(5, stat)

   stat()

   reactor.run()


def configInfo():
   for var in LINUX_SYSCTL_VARS:
      fn = '/proc/sys/' + var.replace('.', '/')
      val = open(fn).read().strip()
      print var, val
   print "FD ulimit:"
   os.system('ulimit -n')

if __name__ == '__main__':
   if len(argv) == 1:
      configInfo()
      main()
   else:
      main(int(argv[1]))
