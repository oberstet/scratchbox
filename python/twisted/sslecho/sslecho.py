from twisted.enterprise import adbapi

from twisted.python import usage

from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

from twisted.application import service, internet
from twisted.application.service import Application, MultiService


from twisted.web.server import Site
from twisted.web.static import File


DBFILE = "foobar.dat"


def CreatePool():
   return adbapi.ConnectionPool('sqlite3',
                                DBFILE,
                                check_same_thread = False # http://twistedmatrix.com/trac/ticket/3629
                                )


class Echo(Protocol):

   def connectionMade(self):
      print "connection made"
      self.send()

   def connectionLost(self, reason):
      print "connection lost"

   def dataReceived(self, data):
      print "received: ", data
      #self.transport.write(data)

   def send(self):
      html = """<!DOCTYPE html><html><body><h1>Foobar</h1></body></html>"""
      raw = html.encode("utf-8")
      response  = "HTTP/1.1 200 OK\x0d\x0a"
      response += "Content-Type: text/html; charset=UTF-8\x0d\x0a"
      response += "Content-Length: %d\x0d\x0a" % len(raw)
      response += "\x0d\x0a"
      response += raw
      self.transport.write(response)





if __name__ == "__main__":
   pool = CreatePool()
   if True:
      factory = Factory()
      factory.protocol = Echo
   else:
      root = File(".")
      factory = Site(root)
   reactor.listenSSL(8090, factory, ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt'))
   reactor.run()


class SslEchoService(MultiService):

   def startService(self):

      pool = CreatePool()

      if False:
         factory = Factory()
         factory.protocol = Echo
      else:
         root = File(".")
         factory = Site(root)

      #hub_websocket_sslcontext = tlsctx.TlsContextFactory(cfg["hub-websocket-tlskey-pem"], cfg["hub-websocket-tlscert-pem"])
      context = ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt')

      service = internet.SSLServer(8090, factory, context)
      service.setServiceParent(self)

      MultiService.startService(self)


class Options(usage.Options):
   pass


def makeService(options):
   from twisted.internet import reactor
   reactor.suggestThreadPoolSize(30)
   return SslEchoService()
