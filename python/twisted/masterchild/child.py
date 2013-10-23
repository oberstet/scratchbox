import os, sys, time

# http://twistedmatrix.com/documents/current/core/examples/#auto10
# http://twistedmatrix.com/trac/ticket/4387
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-in-python
# https://pypi.python.org/pypi/affinity

import choosereactor
from twisted.internet import reactor

#from twisted.internet import kqreactor
#kqreactor.install()

def variant1():

   from twisted.internet import protocol
   from twisted.internet import reactor
   
   f = open("test.log", 'w')
   fds = [f, sys.stdout]

   def loop():
      try:
         msg = "loop %d %d\n" % (os.getpid(), os.getppid())
         for fd in fds:
            fd.write(msg)
            fd.flush()
      except Exception, e:
         f.write("EXCEPTION" + str(e))
         f.write("closed")
         f.close()
         reactor.stop()
      else:
         reactor.callLater(1, loop)
      
   loop()
   reactor.run()


def variant2():

   f = open("test.log", 'w')
   fds = [f, sys.stdout]
   try:
      while True:

         try:
            pid = os.getpid()
         except:
            pid = None

         try:
            ppid = os.getppid()
         except:
            ppid = None

         msg = "loop %s %s\n" % (pid, ppid)
         for fd in fds:
            fd.write(msg)
            fd.flush()
         #print "loop %d %d" % (os.getpid(), os.getppid())
         time.sleep(1)
   except Exception, e:
      f.write("EXCEPTION" + str(e))
   finally:
      f.write("closed")
      f.close()


# http://twistedmatrix.com/documents/current/core/examples/stdin.py
# http://twistedmatrix.com/documents/current/api/twisted.internet.stdio.StandardIO.html
def variant3():
   from twisted.internet import reactor
   from twisted.internet import stdio
   from twisted.protocols import basic
   from twisted.internet import reactor, protocol
   import time

   class Echo(basic.LineReceiver):
      from os import linesep as delimiter
      
      def loop(self):
         self.msg = "%d\n" % self.linesReceived
         self.transport.write(self.msg)
         reactor.callLater(1, self.loop)

      def connectionMade(self):
         #self.transport.write(str(self.res))
         try:
            pid = os.getpid()
         except:
            pid = None

         try:
            ppid = os.getppid()
         except:
            ppid = None

         self.msg = "child: %s parent: %s\n" % (pid, ppid)
         self.transport.write(self.msg)
         self.transport.write("Child is using Twisted reactor class %s" % str(reactor.__class__))

         self.linesReceived = 0
         self.loop()

      def lineReceived(self, line):
         #self.sendLine('Echo: ' + line)
         #self.transport.write('>>> ')
         self.linesReceived += 1
         #time.sleep(0.1)
         x = 0
         N = 10000
         N = 0
         for i in xrange(N):
            x += .1


   class EchoBinary(protocol.Protocol):

      def loop(self):
         self.msg = "%d %d\n" % (self.octetsReceived, self.octetsReceived - self.octetsReceivedLast)
         self.octetsReceivedLast = self.octetsReceived
         self.transport.write(self.msg)
         reactor.callLater(1, self.loop)

      def connectionMade(self):
         #self.transport.write(str(self.res))
         try:
            pid = os.getpid()
         except:
            pid = None

         try:
            ppid = os.getppid()
         except:
            ppid = None

         self.msg = "child: %s parent: %s\n" % (pid, ppid)
         self.transport.write(self.msg)
         self.transport.write("Child is using Twisted reactor class %s" % str(reactor.__class__))

         self.octetsReceived = 0
         self.octetsReceivedLast = 0
         self.loop()

      def dataReceived(self, data):
         self.octetsReceived += len(data)
         #x = 0
         #N = 10000
         #N = 0
         #for i in xrange(N):
         #   x += .1

   #proto = Echo()
   proto = EchoBinary()
   res = stdio.StandardIO(proto)
   print res
   
   reactor.run()


if __name__ == '__main__':
   variant3()
