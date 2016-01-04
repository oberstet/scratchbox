import os
from twisted.internet.defer import inlineCallbacks
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.conch.ssh.agent import SSHAgentClient

@inlineCallbacks
def main(reactor, *argv):
    if "SSH_AUTH_SOCK" not in os.environ:
        raise Exception("no ssh-agent is running!")
    endpoint = UNIXClientEndpoint(reactor, os.environ["SSH_AUTH_SOCK"])
    proto = yield endpoint.connect(Factory.forProtocol(SSHAgentClient))
    print("connected to agent. keys held currently:")
    for blob, comment in (yield proto.requestIdentities()):
        print("Key: {}".format(comment))
    proto.transport.loseConnection()

if __name__ == '__main__':
    from twisted.internet.task import react
    react(main, [])
