import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File


if __name__ == '__main__':

   log.startLogging(sys.stdout)
   root = File(".")
   site = Site(root)
   site.log = lambda _: None
   reactor.listenTCP(8090, site)
   reactor.run()
