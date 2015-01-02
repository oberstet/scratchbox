import psutil
p = psutil.Process()
print p.cpu_affinity()
p.cpu_affinity([0])
print p.cpu_affinity()

from twisted.internet import kqreactor
kqreactor.install()
#from twisted.internet import selectreactor
#selectreactor.install()
#from twisted.internet import pollreactor
#pollreactor.install()

from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
   def connectionMade(self):
      self.transport.registerProducer(self.transport, True)

   def dataReceived(self, data):
      self.transport.write(data)

class EchoFactory(protocol.Factory):
   def buildProtocol(self, addr):
      p = Echo()
      return p

endpoints.serverFromString(reactor, "tcp:9000:backlog=1024").listen(EchoFactory())

print "running on ", reactor.__class__

import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

reactor.run()

pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
