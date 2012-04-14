import sys

from twisted.enterprise import adbapi
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import threads

class Echo(Protocol):

   def connectionMade(self):
      print "connection made"
      self.send()

   def connectionLost(self, reason):
      print "connection lost"

   def dataReceived(self, data):
      print "received: ", len(data)

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

   factory = Factory()
   factory.protocol = Echo
   port = 8090

   if 'defer' in sys.argv:
      print "deferToThread"
      def foo():
         return 23
      d = threads.deferToThread(foo)
   else:
      print "no deferToThread"

   if 'ssl' in sys.argv:
      print "running SSL on", port
      reactor.listenSSL(port, factory, ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt'))
   else:
      print "running plain TCP on", port
      reactor.listenTCP(port, factory)

   reactor.run()
