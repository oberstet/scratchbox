# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/posixbase.py#L449
# http://twistedmatrix.com/trac/browser/trunk/twisted/internet/interfaces.py#L895
# http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.AdoptedStreamServerEndpoint.html
# http://twistedmatrix.com/pipermail/twisted-commits/2012-March/034524.html
# http://twistedmatrix.com/documents/current/core/howto/endpoints.html


import choosereactor

from os import environ
from sys import argv, executable
from socket import AF_INET

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

def main(fd = None):
   root = File(".")
   factory = Site(root)

   if fd is None:
      # Create a new listening port and several other processes to help out.
      port = reactor.listenTCP(8080, factory)
      print port
      print dir(port)
      for i in range(3):
         reactor.spawnProcess(
            None, executable, [executable, __file__, str(port.fileno())],
            childFDs = {0: 0, 1: 1, 2: 2, port.fileno(): port.fileno()},
            env = environ)
   else:
      # Another process created the port, just start listening on it.
      port = reactor.adoptStreamPort(fd, AF_INET, factory)

   reactor.run()


if __name__ == '__main__':
   if len(argv) == 1:
      main()
   else:
      main(int(argv[1]))
