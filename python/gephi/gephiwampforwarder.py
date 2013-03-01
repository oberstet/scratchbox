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

WAMP_SERVER_URL = "ws://localhost:9000"
GEPHI_SERVER_URL = "ws://ec2-54-242-250-189.compute-1.amazonaws.com:8080/workspace0"
GEPHI_TOPIC_URI = "http://informationsecurityanalytics.com/moirai/graph#"


import sys, json

from twisted.python import log
from twisted.internet import reactor

from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS

from autobahn.wamp import WampClientFactory, \
                          WampClientProtocol



class GephiClientProtocol(WebSocketClientProtocol):

   def onOpen(self):
      print "connected to Gephi"

   def onMessage(self, msg, binary):
      if not binary:
         obj = json.loads(msg)
         self.factory.forwarder.publish(GEPHI_TOPIC_URI + "1", obj)


class GephiForwardingProtocol(WampClientProtocol):

   def onSessionOpen(self):
      print "connected to WAMP server"
      factory = WebSocketClientFactory(GEPHI_SERVER_URL)
      factory.protocol = GephiClientProtocol
      factory.forwarder = self
      connectWS(factory)



if __name__ == '__main__':

   log.startLogging(sys.stdout)
   debug = len(sys.argv) > 1 and sys.argv[1] == 'debug'

   factory = WampClientFactory(WAMP_SERVER_URL, debugWamp = debug)
   factory.protocol = GephiForwardingProtocol

   connectWS(factory)

   reactor.run()
