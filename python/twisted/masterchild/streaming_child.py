# http://twistedmatrix.com/documents/current/core/examples/stdin.py
# http://twistedmatrix.com/documents/current/api/twisted.internet.stdio.StandardIO.html
# http://twistedmatrix.com/documents/current/core/examples/#auto10
# http://twistedmatrix.com/trac/ticket/4387
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-in-python
# https://pypi.python.org/pypi/affinity

import os

import choosereactor
from twisted.internet import reactor, protocol, stdio


class StreamingClientProtocol(protocol.Protocol):

   def loop(self):
      msg = "%d %d\n" % (self.octetsReceived, self.octetsReceived - self.octetsReceivedLast)
      self.octetsReceivedLast = self.octetsReceived
      self.transport.write(msg)
      reactor.callLater(1, self.loop)

   def connectionMade(self):
      try:
         pid = os.getpid()
      except:
         pid = None

      try:
         ppid = os.getppid()
      except:
         ppid = None

      self.enableFullDuplex = False

      self.octetsReceived = 0
      self.octetsReceivedLast = 0

      if not self.enableFullDuplex:
         msg = "Child PID %s, Parent PID %s\n" % (pid, ppid)
         self.transport.write(msg)
         self.transport.write("Child is using Twisted reactor class %s" % str(reactor.__class__))
         self.loop()

   def dataReceived(self, data):
      self.octetsReceived += len(data)
      if self.enableFullDuplex:
         self.transport.write(data)

   def connectionLost(self, reason):
      reactor.stop()



if __name__ == '__main__':
   proto = StreamingClientProtocol()
   stdio.StandardIO(proto)
   reactor.run()
