from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol

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
      self._low_watermark = 10
      self._high_watermark = 50
      self._target = 300
      self._connected = []

   def run(self):
      print("Starting ..")
      self._print_stats()
      self._connect()
      #while len(self._connected) < self._target:
      #   self._connect_more()

   def _print_stats(self):
      print("{} connected, {} pending".format(len(self._connected), self._pending))
      reactor.callLater(1, self._print_stats)

   def _connect(self):
      if self._pending <= self._low_watermark:
         self._connect_more()
      #else:
      #print len(self._connected)
      reactor.callLater(0.01, self._connect)

   def _connect_more(self):
      def got_connection(p):
         self._connected.append(p)
         self._pending -= 1

      while self._pending <= self._high_watermark:
         d = connectProtocol(self._endpoint, ConnectOnly())
         self._pending += 1
         d.addCallback(got_connection)

#      print "*"


#connect_n(10)

test = MassConnect()
test.run()

reactor.run()
