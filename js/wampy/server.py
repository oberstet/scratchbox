###############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
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
import six
import datetime

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.internet.endpoints import serverFromString

from autobahn.wamp import router
from autobahn.twisted.util import sleep
from autobahn.twisted import wamp, websocket


class MyBackendComponent(wamp.ApplicationSession):

   @inlineCallbacks
   def onJoin(self, details):

      def square(x):
         print("Someone is calling me;)")
         return x * x

      reg = yield self.register(square, u'com.mathservice.square')
      print("Registered procedure with ID {}".format(reg.id))



if __name__ == '__main__':

   ## 0) start logging to console
   log.startLogging(sys.stdout)

   ## 1) create a WAMP router factory
   router_factory = router.RouterFactory()

   ## 2) create a WAMP router session factory
   session_factory = wamp.RouterSessionFactory(router_factory)

   from autobahn.wamp import types

   config = types.ComponentConfig(realm = "realm1")

   ## 3) Optionally, add embedded WAMP application sessions to the router
   session_factory.add(MyBackendComponent(config))

   from autobahn.wamp.serializer import MsgPackSerializer, JsonSerializer
   serializers = [MsgPackSerializer()]
   #serializers = [MsgPackSerializer(), JsonSerializer()]

   ## 4) create a WAMP-over-WebSocket transport server factory
   transport_factory = websocket.WampWebSocketServerFactory(session_factory, \
                                                            serializers = serializers, \
                                                            debug = False, \
                                                            debug_wamp = True)

   ## 5) start the server from a Twisted endpoint
   server = serverFromString(reactor, "tcp:8080")
   server.listen(transport_factory)

   ## 6) now enter the Twisted reactor loop
   reactor.run()
