import sys
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File


if __name__ == '__main__':

   log.startLogging(sys.stdout)

   webdir = File(".")
   webdir.contentTypes['.svg'] = 'image/svg+xml'

   website = Site(webdir)
   reactor.listenTCP(8080, website)
   reactor.run()
