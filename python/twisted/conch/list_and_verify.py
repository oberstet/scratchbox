import os
from twisted.internet.defer import inlineCallbacks
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import UNIXClientEndpoint
from twisted.conch.ssh.agent import SSHAgentClient

# References:
#
# https://twistedmatrix.com/documents/current/api/twisted.conch.ssh.agent.SSHAgentClient.html
# https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.agent
# https://tools.ietf.org/html/rfc4253

# The "blob" returned from agent.requestIdentities() and containing
# the public key is encoded as follow (from the RFC4253):
#
#   The "ssh-rsa" key format has the following specific encoding:
#
#      string    "ssh-rsa"
#      mpint     e
#      mpint     n
#
#   Here the 'e' and 'n' parameters form the signature key blob.
#

# The "blob" returned from agent.signData() and containing
# the signature is encoded as follow (from the RFC4253):
#
#   Signing and verifying using this key format is performed according to
#   the RSASSA-PKCS1-v1_5 scheme in [RFC3447] using the SHA-1 hash.
#
#   The resulting signature is encoded as follows:
#
#      string    "ssh-rsa"
#      string    rsa_signature_blob
#
#   The value for 'rsa_signature_blob' is encoded as a string containing
#   s (which is an integer, without lengths or padding, unsigned, and in
#   network byte order).

from cryptography.exceptions import InvalidSignature

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_ssh_public_key

import struct
from binascii import b2a_hex, b2a_base64


# http://blog.oddbit.com/2011/05/08/converting-openssh-public-keys/
def unpack(keydata):
    parts = []
    while keydata:
        # read the length of the data
        dlen = struct.unpack('>I', keydata[:4])[0]

        # read in <length> bytes
        data, keydata = keydata[4:dlen+4], keydata[4+dlen:]
        parts.append(data)

    return parts


def main(reactor, *argv):
    if "SSH_AUTH_SOCK" not in os.environ:
        raise Exception("no ssh-agent is running!")

    factory = Factory()
    factory.protocol = SSHAgentClient
    endpoint = UNIXClientEndpoint(reactor, os.environ["SSH_AUTH_SOCK"])
    d = endpoint.connect(factory)

    @inlineCallbacks
    def on_connect(agent):
        # we are now connected to the locally running ssh-agent
        # that agent might be the openssh-agent, or eg on Ubuntu 14.04 by
        # default the gnome-keyring / ssh-askpass-gnome application
        print("connected to ssh-agent!")

        print("keys currently held in ssh-agent:\n")
        keys = yield agent.requestIdentities()
        for blob, comment in keys:
            print(comment)
            raw = unpack(blob)
            algo = raw[0]
            if algo == u'ssh-rsa':
                algo, exponent, modulus = raw
                print("RSA key: {} {} 0x{} {}: 0x{} ..".format(comment, algo, b2a_hex(exponent), len(modulus), b2a_hex(modulus)[:16]))
                print(b2a_base64(blob))
            elif algo == u'ssh-ed25519':
                algo, pubkey = raw
                print("Ed25519 key: {} {} {}".format(comment, algo, b2a_hex(pubkey)))

        # we will now ask the ssh-agent to sign some data using the private
        # key that corresponds to the public key that we selected

        print("sign some data:\n")

        # message to sign
        message = 'Hello, world!'

        # the public key that corrsponds to the private key we ask the agent to sign with
        key_blob, key_comment = keys[-1]

        # now ask the agent
        signature_blob = yield agent.signData(key_blob, message)
        algo, signature = unpack(signature_blob)
        print(algo)
        print(b2a_base64(signature))

        # we now verify the signature using cryptography.

        # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#cryptography.hazmat.primitives.serialization.load_ssh_public_key
        public_key = load_ssh_public_key("ssh-rsa {} {}".format(b2a_base64(key_blob), key_comment), backend=default_backend())
        isinstance(public_key, rsa.RSAPublicKey)

        verifier = public_key.verifier(signature, padding.PKCS1v15(), hashes.SHA1())
        verifier.update(message)

        # here we can provoke a failing signature to check that it actually works
        provoke_signature_failure = False
        if provoke_signature_failure:
            verifier.update('make the sig fail')

        try:
            verifier.verify()
        except InvalidSignature:
            print("** Signature is invalid!! **")
        else:
            print("Signature looks good.")

        # that's it. say goodbye.
        print("disconnecting ..")
        agent.transport.loseConnection()

    return d.addCallback(on_connect)


if __name__ == '__main__':
    from twisted.internet.task import react
    react(main, [])
    print("finished.")
