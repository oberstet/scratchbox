import choosereactor
from twisted.internet import reactor
print "Master is using Twisted reactor class %s" % str(reactor.__class__)
#from twisted.internet import kqreactor
#kqreactor.install()

import sys
from twisted.internet import protocol
from twisted.internet import reactor
from zope.interface import implements
from twisted.internet import reactor, interfaces

# http://www.rikkus.info/sysv-ipc-vs-unix-pipes-vs-unix-sockets
# http://unix.stackexchange.com/questions/1537/measure-pipe-throughput-in-the-shell/1538#1538

class LineStreamProducer:

   implements(interfaces.IPushProducer)

   def __init__(self, proto):
      self.sentAmount = 0
      self.sentMsgs = 0
      self.proto = proto
      self.paused = False
      self.msg = "*" * 1024 * 32
      #self.msg = "Hello, world!\n"
      self.msgLen = len(self.msg)

   def pauseProducing(self):
      #print "pauseProducing", self.sentAmount, self.sentMsgs
      self.paused = True

   def resumeProducing(self):
      #print "resumeProducing", self.sentAmount, self.sentMsgs
      self.paused = False
      
      while not self.paused:
         self.proto.transport.write(self.msg)
         self.sentAmount += self.msgLen
         self.sentMsgs += 1

   def stopProducing(self):
      print "stopProducing", self.sentAmount, self.sentLines
      self.paused = True
      

class MyPP(protocol.ProcessProtocol):

   def connectionMade(self):
      print "connectionMade!"
      producer = LineStreamProducer(self)
      self.transport.registerProducer(producer, True)
      producer.resumeProducing()
      #for i in xrange(100000):
      #while True:
      #   self.transport.write("Hello, world!\n")

   def outReceived(self, data):
      print "outReceived! with %d bytes!" % len(data)
      print data

   def errReceived(self, data):
      print "errReceived! with %d bytes!" % len(data)
      print data

   def inConnectionLost(self):
      print "inConnectionLost! stdin is closed! (we probably did it)"

   def outConnectionLost(self):
      print "outConnectionLost! The child closed their stdout!"

   def errConnectionLost(self):
      print "errConnectionLost! The child closed their stderr."

   def processExited(self, reason):
      print "processExited, status %s" % (reason.value.exitCode,)

   def processEnded(self, reason):
      print "processEnded, status %s" % (reason.value.exitCode,)
      print "quitting"
      reactor.stop()

pp = MyPP()
exe = sys.executable
print exe
#reactor.spawnProcess(pp, "tail", ["tail", "-f", "test.log"], {})
# usePTY=True
#reactor.spawnProcess(pp, "/Users/oberstet/python1/bin/python", ["/Users/oberstet/python1/bin/python", "streaming_child.py"], {})
reactor.spawnProcess(pp, exe, [exe, "child.py"], {})
reactor.run()
