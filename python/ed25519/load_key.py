from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

# To generate a new key: dd if=/dev/urandom of=node.key count=1 bs=32


# Signing keys are produced from a 32-byte (256-bit) random seed value.
# This value is read in here.
with open('node_ed25519.hex', 'r') as f:
    key_bytes = f.read().strip()
    signing_key = SigningKey(key_bytes, encoder=HexEncoder)

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=HexEncoder)

print(verify_key_hex)
