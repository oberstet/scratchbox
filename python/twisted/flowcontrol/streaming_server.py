###############################################################################
##
##  Copyright 2011 Tavendo GmbH
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

import hashlib

from twisted.internet import reactor

import autobahn
from autobahn.utf8validator import Utf8Validator
from autobahn.xormasker import XorMaskerNull

from autobahn.websocket import WebSocketServerFactory, \
                               WebSocketServerProtocol, \
                               listenWS

from streaming_client import BATCH_SIZE
COMPUTE_HASH = True


class StreamingHashServerProtocol(WebSocketServerProtocol):
   """
   Streaming WebSockets server that computes a running SHA-256 for data
   received. It will respond every BATCH_SIZE bytes with the digest
   up to that point. It can receive messages of unlimited number of frames
   and frames of unlimited length (actually, up to 2^63, which is the
   WebSockets protocol imposed limit on frame size). Digest is reset upon
   new message.
   """

   def onMessageBegin(self, opcode):
      WebSocketServerProtocol.onMessageBegin(self, opcode)
      if COMPUTE_HASH:
         self.sha256 = hashlib.sha256()
      else:
         self.sha256 = None
      self.count = 0
      self.received = 0
      self.next = BATCH_SIZE

   def onMessageFrameBegin(self, length, reserved):
      WebSocketServerProtocol.onMessageFrameBegin(self, length, reserved)

   def onMessageFrameData(self, data):
      length = len(data)
      self.received += length

      ## when the data received exceeds the next BATCH_SIZE ..
      if self.received >= self.next:

         ## update digest up to batch size
         rest = length - (self.received - self.next)
         if self.sha256:
            self.sha256.update(data[:rest])

         ## send digest
         if self.sha256:
            digest = self.sha256.hexdigest()
         else:
            digest = '???'
         self.sendMessage(digest)
         print "Sent digest for batch %d : %s" % (self.count, digest)

         ## advance to next batch
         self.next += BATCH_SIZE
         self.count += 1

         ## .. and update the digest for the rest
         if self.sha256:
            self.sha256.update(data[rest:])
      else:
         ## otherwise we just update the digest for received data
         if self.sha256:
            self.sha256.update(data)

   def onMessageFrameEnd(self):
      pass

   def onMessageEnd(self):
      pass


if __name__ == '__main__':
   print "Using Twisted reactor class %s" % str(reactor.__class__)
   print "Using UTF8 Validator class %s" % str(Utf8Validator)
   print "Using XOR Masker classes %s" % str(XorMaskerNull)
   print "Using JSON processor module '%s'" % str(autobahn.wamp.json_lib.__name__)

   factory = WebSocketServerFactory("ws://localhost:9000")
   factory.protocol = StreamingHashServerProtocol
   listenWS(factory)
   reactor.run()
