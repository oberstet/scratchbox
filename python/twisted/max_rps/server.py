
from autobahn.twisted.choosereactor import install_reactor

install_reactor(verbose=True)

import sys

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log
from twisted.internet.task import LoopingCall

log.startLogging(sys.stdout)

import psutil
p = psutil.Process()
p.cpu_affinity([0])
print("CPU affinity set: {}".format(p.cpu_affinity()))

size_histo = {}
def print_histo():
    print size_histo

lc = LoopingCall(print_histo)
lc.start(1)


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        l = len(data)
        if l not in size_histo:
            size_histo[l] = 0
        size_histo[l] += 1
        for d in data:
            self.transport.write(d)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()
