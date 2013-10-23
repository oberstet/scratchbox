import sys

import choosereactor
from twisted.internet import reactor, protocol, interfaces
from zope.interface import implements

# http://www.rikkus.info/sysv-ipc-vs-unix-pipes-vs-unix-sockets
# http://unix.stackexchange.com/questions/1537/measure-pipe-throughput-in-the-shell/1538#1538
# broken link: http://twistedmatrix.com/documents/13.1.0/api/twisted.internet.interfaces.IFinishableConsumer.html

class StreamingProducer:

   implements(interfaces.IPushProducer)

   def __init__(self, consumer, writeSize, msgCount):
      self.consumer = consumer
      self.writeSize = writeSize
      self.msgCount = msgCount

      self.paused = False
      self.sentAmount = 0
      self.sentMsgs = 0
      self.msg = "*" * self.writeSize

   def pauseProducing(self):
      #print "pauseProducing", self.sentAmount, self.sentMsgs
      self.paused = True

   def resumeProducing(self):
      #print "resumeProducing", self.sentAmount, self.sentMsgs
      self.paused = False
      
      while not self.paused and self.sentMsgs < self.msgCount:
         self.consumer.write(self.msg)
         self.sentAmount += self.writeSize
         self.sentMsgs += 1

      if self.sentMsgs >= self.msgCount:
         print "FINSIH"
         self.consumer.finish()

   def stopProducing(self):
      print "stopProducing", self.sentAmount, self.msgCount
      self.paused = True
      


class StreamingMasterProtocol(protocol.ProcessProtocol):

   def connectionMade(self):
      print "connectionMade!"
      consumer = self.transport
      producer = StreamingProducer(consumer, 1024 * 32, 1000000)
      consumer.registerProducer(producer, True)

      def finish():
         producer.stopProducing()
         consumer.loseConnection()
         #self.transport.closeStdin()
         #self.transport.closeStdout()
         #self.transport.closeStderr()
      consumer.finish = finish

      producer.resumeProducing()

   def outReceived(self, data):
      print "Received from child on stdout:", data

   def errReceived(self, data):
      print "Received from child on stderr:", data

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
      print "stopping reactor .."
      reactor.stop()



if __name__ == '__main__':
   proto = StreamingMasterProtocol()
   pyexe = sys.executable
   print "Master is using Python from %s and Twisted reactor class %s" % (pyexe, str(reactor.__class__))
   reactor.spawnProcess(proto, pyexe, [pyexe, "child.py"], {})
   reactor.run()
