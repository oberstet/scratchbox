import os
from twisted.internet.defer import inlineCallbacks
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.conch.ssh.agent import SSHAgentClient

import struct
from binascii import b2a_hex, b2a_base64


def unpack(keydata):
    parts = []
    while keydata:
        # read the length of the data
        dlen = struct.unpack('>I', keydata[:4])[0]

        # read in <length> bytes
        data, keydata = keydata[4:dlen+4], keydata[4+dlen:]
        parts.append(data)

    return parts

@inlineCallbacks
def main(reactor, *argv):
    if "SSH_AUTH_SOCK" not in os.environ:
        raise Exception("no ssh-agent is running!")
    endpoint = UNIXClientEndpoint(reactor, os.environ["SSH_AUTH_SOCK"])
    proto = yield endpoint.connect(Factory.forProtocol(SSHAgentClient))
    print("connected to agent. keys held currently:")
    for blob, comment in (yield proto.requestIdentities()):
        raw = unpack(blob)
        algo = raw[0]
        if algo == u'ssh-rsa':
            algo, exponent, modulus = raw
            print("RSA key: {} {} 0x{} {}: 0x{} ..".format(comment, algo, b2a_hex(exponent), len(modulus), b2a_hex(modulus)[:16]))
            print(b2a_base64(blob))
        elif algo == u'ssh-ed25519':
            algo, pubkey = raw
            print("Ed25519 key: {} {} {}".format(comment, algo, b2a_hex(pubkey)))
        else:
            print("Key of unknown type {}".format(algo))

    proto.transport.loseConnection()

if __name__ == '__main__':
    from twisted.internet.task import react
    react(main, [])
