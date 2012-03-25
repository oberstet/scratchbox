import random, hashlib, binascii


def _newid1(i = None):
   return ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_") for k in xrange(16)])

def _newid2(i):
   return hashlib.md5("sdfdsf" + str(i) + "foobar").digest()

def _newid3(i):
   return binascii.b2a_base64(_newid2(i))[:16]

R = 1L
def rnd():
   global R
   R = (1664525L * R + 1013904223L) & 0xffffffffffffffff
   return R

def _newid4(i = None):
   return ('00000000000000000000000000000000%x' % rnd())[-16:]

newid = _newid4
