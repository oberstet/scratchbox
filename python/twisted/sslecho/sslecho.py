from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):
   def connectionMade(self):
      print "connection made"

   def connectionLost(self, reason):
      print "connection lost"

   def dataReceived(self, data):
      print data
      self.transport.write(data)

factory = Factory()
factory.protocol = Echo

reactor.listenSSL(8090, factory, ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt'))
reactor.run()
