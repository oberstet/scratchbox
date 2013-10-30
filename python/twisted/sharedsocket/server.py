###############################################################################
##
##  Copyright 2013 (C) Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import sys

## make sure we run a capable reactor
##
if 'bsd' in sys.platform or sys.platform.startswith('darwin'):
   from twisted.internet import kqreactor
   kqreactor.install()
elif sys.platform.startswith('linux'):
   from twisted.internet import epollreactor
   epollreactor.install()
elif sys.platform == 'win32':
   raise Exception("sorry, Twisted/Windows select/iocp reactors lack the necessary bits")
else:
   raise Exception("hey man, what are you using?")


import sys, os
from os import environ
from sys import argv, executable
from socket import AF_INET

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web import resource


class Simple(resource.Resource):
   isLeaf = True
   def render_GET(self, request):
      self.cnt += 1
      return "<html>Hello, world! [Twisted Web]</html>"


def main(fd = None):
   log.startLogging(sys.stdout)
   print "Using Twisted reactor class %s" % str(reactor.__class__)

   if True:
      root = File(".")
   else:
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


if __name__ == '__main__':
   if len(argv) == 1:
      main()
   else:
      main(int(argv[1]))
