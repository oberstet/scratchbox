###############################################################################
##
##  Copyright 2013 Tavendo GmbH
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

GEPHI_SERVER_URL = "ws://ec2-54-242-250-189.compute-1.amazonaws.com:8080/workspace0"
GEPHI_TOPIC_URI = "http://informationsecurityanalytics.com/moirai/graph#"

import sys, json

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS, \
                               listenWS

from autobahn.wamp import WampServerFactory, \
                          WampServerProtocol



class GephiClientProtocol(WebSocketClientProtocol):

   def onOpen(self):
      print "connected to Gephi"

   def onMessage(self, msg, binary):
      if not binary:
         obj = json.loads(msg)
         self.factory.broker.dispatch(GEPHI_TOPIC_URI + "1", obj)


class GephiBridgeProtocol(WampServerProtocol):

   def onSessionOpen(self):
      ## register a URI and all URIs having the string as prefix as PubSub topic
      self.registerForPubSub(GEPHI_TOPIC_URI, True)


class GephiBridgeFactory(WampServerFactory):

   protocol = GephiBridgeProtocol

   def startFactory(self):
      WampServerFactory.startFactory(self)
      reactor.callLater(5, self.connectGephi)

   def connectGephi(self):
      wsClientFactory = WebSocketClientFactory(GEPHI_SERVER_URL)
      wsClientFactory.protocol = GephiClientProtocol
      wsClientFactory.broker = self
      connectWS(wsClientFactory)


if __name__ == '__main__':

   log.startLogging(sys.stdout)
   debug = len(sys.argv) > 1 and sys.argv[1] == 'debug'

   factory = GephiBridgeFactory("ws://localhost:9000", debugWamp = debug)
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()
