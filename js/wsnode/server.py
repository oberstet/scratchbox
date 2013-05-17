###############################################################################
##
##  Copyright 2011-2013 Tavendo GmbH
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

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

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
