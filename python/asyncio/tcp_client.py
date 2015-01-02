import psutil
p = psutil.Process()
print p.cpu_affinity()
p.cpu_affinity([1])
print p.cpu_affinity()

from twisted.internet import epollreactor
epollreactor.install()
#from twisted.internet import kqreactor
#kqreactor.install()
#from twisted.internet import selectreactor
#selectreactor.install()
#from twisted.internet import pollreactor
#pollreactor.install()


from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol

from autobahn.util import rtime


class WelcomeMessage(Protocol):
   def connectionMade(self):
      print("connected")
      self.transport.loseConnection()

   def connectionLost(self, reason):   
      print("connection lost: {}".format(reason))


def gotProtocol(p):
   print("got protocol: {}".format(p))

# point = TCP4ClientEndpoint(reactor, "127.0.0.1", 9000)
# d = connectProtocol(point, WelcomeMessage())
# d.addCallback(gotProtocol)

def connect_n(n):
   point = TCP4ClientEndpoint(reactor, "127.0.0.1", 9000)
   for i in range(n):
      d = connectProtocol(point, WelcomeMessage())
      d.addCallback(gotProtocol)


class ConnectOnly(Protocol):
   def connectionMade(self):
      pass


class MassConnect:
   def __init__(self):
      self._endpoint = TCP4ClientEndpoint(reactor, "127.0.0.1", 9000)
      self._pending = 0
      self._low_watermark = 100
      self._high_watermark = 800
      self._target = 10000
      self._connected = []
      self._do_print_stats = True

   def run(self):
      print("Starting ..")
      self._started = rtime()
      self._ended = None
      self._print_stats()
      self._connect()
      #while len(self._connected) < self._target:
      #   self._connect_more()

   def _print_stats(self):
      if self._do_print_stats:
         print("{} connected, {} pending".format(len(self._connected), self._pending))
         reactor.callLater(1, self._print_stats)

   def _connect(self):
      if len(self._connected) < self._target:
         if self._pending <= self._low_watermark:
            #print("low watermark reached ({} pending)".format(self._pending))
            self._connect_more()
         #else:
         #print len(self._connected)
         reactor.callLater(0.01, self._connect)
      else:
         self._do_print_stats = False
         self._ended = rtime()
         secs = self._ended - self._started
         conns_per_sec = float(len(self._connected)) / float(secs)
         print("all connected: {} in {} seconds ({} connections/sec)".format(len(self._connected), secs, conns_per_sec))
         reactor.stop()

   def _connect_more(self):
      def got_connection(p):
         self._connected.append(p)
         self._pending -= 1

      def connection_failed(err):
         print("connection failed:", err, len(self._connected))
         self._pending -= 1

      while self._pending < self._high_watermark and self._pending + len(self._connected) < self._target:
         d = connectProtocol(self._endpoint, ConnectOnly())
         self._pending += 1
         d.addCallbacks(got_connection, connection_failed)

      #print("high watermark reached ({} pending)".format(self._pending))

#      print "*"


#connect_n(10)

test = MassConnect()
test.run()

reactor.run()
