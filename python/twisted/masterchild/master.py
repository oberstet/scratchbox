from twisted.internet import protocol
from twisted.internet import reactor

class MyPP(protocol.ProcessProtocol):

    def connectionMade(self):
        print "connectionMade!"

    def outReceived(self, data):
        print "outReceived! with %d bytes!" % len(data)

    def errReceived(self, data):
        print "errReceived! with %d bytes!" % len(data)

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
#reactor.spawnProcess(pp, "tail", ["tail", "-f", "test.log"], {})
# usePTY=True
reactor.spawnProcess(pp, "/Users/oberstet/python1/bin/python", ["/Users/oberstet/python1/bin/python", "child.py"], {})
reactor.run()
