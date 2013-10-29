# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/posixbase.py#L449
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/interfaces.py#L895
# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://twistedmatrix.com/pipermail/twisted-commits/2012-March/034524.html
# http://twistedmatrix.com/documents/current/core/howto/endpoints.html

# curl -s "http://192.168.56.101:8080/?[1-100000]" > /dev/null


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

      for i in range(3):
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


if __name__ == '__main__':
   if len(argv) == 1:
      main()
   else:
      main(int(argv[1]))
