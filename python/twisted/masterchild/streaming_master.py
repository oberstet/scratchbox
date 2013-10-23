import sys, os
import cProfile

import choosereactor
from twisted.internet import reactor, protocol, interfaces
from zope.interface import implements

# http://www.rikkus.info/sysv-ipc-vs-unix-pipes-vs-unix-sockets
# http://unix.stackexchange.com/questions/1537/measure-pipe-throughput-in-the-shell/1538#1538
# broken link: http://twistedmatrix.com/documents/13.1.0/api/twisted.internet.interfaces.IFinishableConsumer.html

# adjust pipe buffer: http://stackoverflow.com/a/13906354/884770

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

   def loop(self):
      msg = "%d %d\n" % (self.octetsReceived, self.octetsReceived - self.octetsReceivedLast)
      self.octetsReceivedLast = self.octetsReceived
      print msg
      reactor.callLater(1, self.loop)

   def connectionMade(self):
      self.enableFullDuplex = False
      self.octetsReceived = 0
      self.octetsReceivedLast = 0

      print "connectionMade!"
      consumer = self.transport
      producer = StreamingProducer(consumer, 1024 * 32, 100000)
      consumer.registerProducer(producer, True)

      def finish():
         producer.stopProducing()
         consumer.loseConnection()
         #self.transport.closeStdin()
         #self.transport.closeStdout()
         #self.transport.closeStderr()
      consumer.finish = finish

      producer.resumeProducing()

      if self.enableFullDuplex:
         self.loop()

   def outReceived(self, data):
      if self.enableFullDuplex:
         self.octetsReceived += len(data)
      else:
         print "Received from child on stdout:", data

   def errReceived(self, data):
      if self.enableFullDuplex:
         print "Received from child on stderr:", len(data)
      else:
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


def run():
   proto = StreamingMasterProtocol()
   pyexe = sys.executable
   try:
      pid = os.getpid()
   except:
      pid = None
   print "Master (PID %s) is using Python from %s and Twisted reactor class %s" % (pid, pyexe, str(reactor.__class__))
   reactor.spawnProcess(proto, pyexe, [pyexe, "streaming_child.py"], {})
   reactor.run()   

if __name__ == '__main__':
   #cProfile.run("run()")
   #prof = cProfile.Profile()
   #prof.runcall(run)
   #prof.dump_stats("profile")
   import statprof

   statprof.start()

   try:
      run()
   finally:
      statprof.stop()
      statprof.display()

# http://www.serpentine.com/blog/2012/04/09/reannouncing-statprof-a-statistical-profiler-for-python/
# https://bitbucket.org/robertkern/line_profiler
# http://stackoverflow.com/questions/5616446/is-there-a-statistical-profiler-for-python-if-not-how-could-i-go-about-writing/5616679#5616679

# OSX:
# http://pastebin.com/0ZjJzgjP
# http://pastebin.com/GtnQmyyc
#
#  %   cumulative      self          
# time    seconds   seconds  name    
# 24.54      8.98      8.98  kqreactor.py:239:doKEvent
# 21.86      8.00      8.00  kqreactor.py:89:_updateRegistration
# 17.66      6.46      6.46  fdesc.py:111:writeToFD
# 17.64     12.27      6.46  abstract.py:242:doWrite
# 15.87      5.81      5.81  abstract.py:31:_concatenate
#  0.78      0.28      0.28  abstract.py:262:doWrite

