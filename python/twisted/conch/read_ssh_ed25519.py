import binascii
import struct


def unpack(keydata):
    parts = []
    while keydata:
        # read the length of the data
        dlen = struct.unpack('>I', keydata[:4])[0]

        # read in <length> bytes
        data, keydata = keydata[4:dlen+4], keydata[4+dlen:]
        parts.append(data)

    return parts


with open('/home/oberstet/.ssh/id_ed25519.pub', 'r') as f:
    filedata = f.read().strip()
    print(filedata)
    d = filedata.split()
    algo, keydata, comment = d
    blob = binascii.a2b_base64(keydata)
    key = unpack(blob)[1]
    print("algo={}, keylen={}, keydata={}.., comment={}".format(algo, len(key), keydata[:12], comment))
