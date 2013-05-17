import sys

from twisted.internet import reactor
from twisted.python import log

from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS


class EchoClientProtocol(WebSocketClientProtocol):

   def onConnect(self, connectionResponse):
      print "Connected to server."
      print "Protocol", connectionResponse.protocol

   def sendHello(self):
      self.sendMessage("Hello, world!")

   def onOpen(self):
      self.sendHello()

   def onMessage(self, msg, binary):
      print "Got echo: " + msg
      reactor.callLater(1, self.sendHello)

   def onClose(self, wasClean, code, reason):
      print "Connection closed."
      print "wasClean", wasClean
      print "code", code
      print "reason", reason
      reactor.stop()


if __name__ == '__main__':

   debug = True
   log.startLogging(sys.stdout)

   factory = WebSocketClientFactory("ws://127.0.0.1:9000/wsecho",
                                    origin = "example.com",
                                    protocols = ["foo", "bar"],
                                    debug = debug)
   factory.protocol = EchoClientProtocol
   connectWS(factory)

   reactor.run()
