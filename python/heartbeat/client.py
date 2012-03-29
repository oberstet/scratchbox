###############################################################################
##
##  Copyright 2011,2012 Tavendo GmbH
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

import sys, os
from twisted.python import log
from twisted.internet import reactor
from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS

from autobahn.wamp import WampClientFactory, WampClientProtocol
from autobahn.util import utcnow, parseutc, newid

import datetime

# use WAMP base class, even though we won't use WAMP features
# but only plain WS Ping/Pong.
# reason: be able to test against our WS server on the net.
# which only wants to speak WAMP .. ha.

#class HeartbeatClientProtocol(WebSocketClientProtocol):
class HeartbeatClientProtocol(WampClientProtocol):

   BEAT_SIZE = 100
   BEATS_PER_SEC = 5

   def sendBeat(self):
      id = newid()
      payload = os.urandom(HeartbeatClientProtocol.BEAT_SIZE)
      self.beats[id] = datetime.datetime.utcnow()
      self.sendPing(id + payload)
      print "Sent heartbeat: " + id, self.beatsize
      reactor.callLater(1./float(HeartbeatClientProtocol.BEATS_PER_SEC), self.sendBeat)

   def onOpen(self):
      self.beats = {}
      self.beatsize = 100
      self.sendBeat()

   def onPong(self, payload):
      id = payload[:16]
      l = len(payload) - 16
      now = datetime.datetime.utcnow()

      if self.beats.has_key(id):
         rtt_ms = (now - self.beats[id]).total_seconds() * 1000.
         print "Got heartbeat: " + id, l, rtt_ms



if __name__ == '__main__':

   if len(sys.argv) < 2:
      print "Need the WebSocket server address, i.e. ws://localhost:9000"
      sys.exit(1)

   log.startLogging(sys.stdout)

   debug = False

   #factory = WebSocketClientFactory(sys.argv[1], debug = True, debugCodePaths = True)
   factory = WampClientFactory(sys.argv[1],
                               debug = debug,
                               debugCodePaths = True,
                               debugWamp = debug)
   factory.protocol = HeartbeatClientProtocol
   connectWS(factory)

   reactor.run()
