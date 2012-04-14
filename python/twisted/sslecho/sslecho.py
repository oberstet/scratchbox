from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):

   def connectionMade(self):
      print "connection made"
      self.sendServerStatus()

   def connectionLost(self, reason):
      print "connection lost"

   def dataReceived(self, data):
      print data
      self.transport.write(data)

   def sendHtml(self, html):
      raw = html.encode("utf-8")
      response  = "HTTP/1.1 200 OK\x0d\x0a"
      response += "Content-Type: text/html; charset=UTF-8\x0d\x0a"
      response += "Content-Length: %d\x0d\x0a" % len(raw)
      response += "\x0d\x0a"
      response += raw
      self.transport.write(response)

   def sendServerStatus(self):
      html = """
<!DOCTYPE html>
<html>
   <body>
      <h1>Foobar</h1>
   </body>
</html>
"""
      self.sendHtml(html)

factory = Factory()
factory.protocol = Echo

reactor.listenSSL(8090, factory, ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt'))
reactor.run()
