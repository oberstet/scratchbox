###############################################################################
##
##  Copyright 2013 (C) Tavendo GmbH
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

## make sure we run a capable OS/reactor
##
startupMsgs = []
if 'bsd' in sys.platform:
   from twisted.internet import kqreactor
   kqreactor.install()
   startupMsgs.append("Alrighty: you run a capable kqueue platform - good job!")
elif sys.platform.startswith('linux'):
   from twisted.internet import epollreactor
   epollreactor.install()
   startupMsgs.append("Alrighty: you run a capable epoll platform - good job!")
elif sys.platform.startswith('darwin'):
   from twisted.internet import kqreactor
   kqreactor.install()
   startupMsgs.append("Huh, you run OSX and have kqueue, but don't be disappointed when performance sucks;)")
elif sys.platform == 'win32':
   raise Exception("Sorry dude, Twisted/Windows select/iocp reactors lack the necessary bits.")
else:
   raise Exception("Hey man, what OS are you using?")

import pkg_resources
from twisted.internet import reactor
startupMsgs.append("Using Twisted reactor class %s on Twisted %s" % (str(reactor.__class__), pkg_resources.require("Twisted")[0].version))


import sys, os
from os import environ
from sys import argv, executable
from socket import AF_INET

from twisted.python import log
from twisted.internet.protocol import Factory
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web import static


def master(options):
   """
   Start of the master process.
   """
   if not options.silence:
      print "Master started on PID %s" % os.getpid()

   ## we just need some factory like thing .. it won't be used on master anyway
   ## for actual socket accept
   ##
   factory = Factory()

   ## create socket, bind and listen ..
   port = reactor.listenTCP(options.port, factory, backlog = options.backlog)

   ## .. but immediately stop reading: we only want to accept on workers, not master
   port.stopReading()

   ## fire off background workers
   ##
   for i in range(options.workers):

      args = [executable, __file__, "--fd", str(port.fileno())]

      ## pass on cmd line args to worker ..
      args.extend(sys.argv[1:])

      reactor.spawnProcess(
         None, executable, args,
         childFDs = {0: 0, 1: 1, 2: 2, port.fileno(): port.fileno()},
         env = environ)

   reactor.run()


class CountingSite(Site):
   def __init__(self, root):
      Site.__init__(self, root)
      self.cnt = 0

   def getResourceFor(self, request):
      self.cnt += 1
      return Site.getResourceFor(self, request)


class FixedResource(Resource):
   isLeaf = True

   def __init__(self, payload):
      Resource.__init__(self)
      self.payload = payload

   def render_GET(self, request):
      return self.payload


def worker(options):
   """
   Start background worker process.
   """
   workerPid = os.getpid()

   payload = "*" * options.payload

   if options.resource == 'file':
      f = open('index.html', 'wb')
      f.write(payload)
      f.close()
      root = static.File('.')

   elif options.resource == 'data':
      root = static.Data(payload, 'text/html')

   elif options.resource == 'fixed':
      root = FixedResource(payload)

   else:
      raise Exception("logic error")

   if not options.silence:
      print "Worker started on PID %s using resource %s" % (workerPid, root)

   if not options.silence:
      site = CountingSite(root)
   else:
      site = Site(root)
   site.log = lambda _: None # disable any logging
 
   ## The master already created the socket, just start listening and accepting
   ##
   port = reactor.adoptStreamPort(options.fd, AF_INET, site)

   if not options.silence:
      def stat():
         print "Worker %s processed %d requests"  % (workerPid, site.cnt)
         reactor.callLater(options.interval, stat)

      stat()

   reactor.run()



if __name__ == '__main__':

   import argparse

   parser = argparse.ArgumentParser(description = 'Twisted Web Multicore Server')
   parser.add_argument('--port', dest = 'port', type = int, default = 8080, help = 'TCP port to run on.')
   parser.add_argument('--workers', dest = 'workers', type = int, default = 4, help = 'Number of workers to spawn - should fit the number of (phyisical) CPU cores.')
   parser.add_argument('--backlog', dest = 'backlog', type = int, default = 8192, help = 'TCP accept queue depth. You must tune your OS also as this is just advisory!')
   parser.add_argument('--silence', dest = 'silence', action = "store_true", default = False, help = 'Silence log output.')
   parser.add_argument('--resource', dest = 'resource', choices = ['file', 'data', 'fixed'], default = 'file', help = 'Resource type.')
   parser.add_argument('--interval', dest = 'interval', type = int, default = 5, help = 'Worker stats update interval.')
   parser.add_argument('--payload', dest = 'payload', type = int, default = 40, help = 'Payload length of response.')

   parser.add_argument('--fd', dest = 'fd', type = int, default = None, help = 'If given, this is a worker which will use provided FD and all other options are ignored.')

   options = parser.parse_args()

   if not options.silence:
      log.startLogging(sys.stdout)

   if options.fd is not None:
      # run worker
      worker(options)
   else:
      if not options.silence:
         for m in startupMsgs:
            print m
      # run master
      master(options)
