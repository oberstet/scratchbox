import sys
from twisted.python import log
from twisted.internet import reactor

from twisted.internet.endpoints import serverFromString

from twisted.cred import checkers, portal

from twisted.conch.manhole import ColoredManhole
from twisted.conch.manhole_ssh import ConchFactory, TerminalRealm


if __name__ == '__main__':

   log.startLogging(sys.stdout)

   checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
   checker.addUser('oberstet', 'secret')

   namespace = {'foo': 23}

   rlm = TerminalRealm()
   rlm.chainedProtocolFactory.protocolFactory = lambda _: ColoredManhole(namespace)

   ptl = portal.Portal(rlm, [checker])

   factory = ConchFactory(ptl)

   server = serverFromString(reactor, "tcp:6022")
   server.listen(factory)

   reactor.run()
