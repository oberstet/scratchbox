import sys

from twisted.internet import reactor
from twisted.python import log

from autobahn.websocket import WebSocketServerFactory, \
                               WebSocketServerProtocol, \
                               listenWS, \
                               HttpException

from autobahn.httpstatus import HTTP_STATUS_CODE_BAD_REQUEST


class EchoServerProtocol(WebSocketServerProtocol):

   def onConnect(self, connectionRequest):
      print connectionRequest
      print "Client connecting .."
      print "URL", connectionRequest.path
      print "Origin", connectionRequest.origin
      print "Protocols", connectionRequest.protocols

      if 'foo' in connectionRequest.protocols:
         ## accept WS, we will speak the 'foo' subprotocol
         return 'foo'
      else:
         raise HttpException(HTTP_STATUS_CODE_BAD_REQUEST[0],
                             "This server only speaks the 'foo' protocol")

   def onMessage(self, msg, binary):
      self.sendMessage(msg, binary)


if __name__ == '__main__':

   debug = True
   log.startLogging(sys.stdout)

   factory = WebSocketServerFactory("ws://127.0.0.1:9000",
                                    debug = debug)

   factory.protocol = EchoServerProtocol
   listenWS(factory)

   reactor.run()
