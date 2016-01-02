import os
from twisted.internet.defer import inlineCallbacks
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.conch.ssh.agent import SSHAgentClient


def main(reactor, *argv):
    if "SSH_AUTH_SOCK" not in os.environ:
        raise Exception("no ssh-agent is running!")

    factory = Factory()
    factory.protocol = SSHAgentClient
    endpoint = UNIXClientEndpoint(reactor, os.environ["SSH_AUTH_SOCK"])
    d = endpoint.connect(factory)

    @inlineCallbacks
    def on_connect(proto):
        print("connected to agent. keys held currently:")
        keys = yield proto.requestIdentities()
        for blob, comment in keys:
            print("Key: {}".format(comment))
        proto.transport.loseConnection()

    return d.addCallback(on_connect)


if __name__ == '__main__':
    from twisted.internet.task import react
    react(main, [])
