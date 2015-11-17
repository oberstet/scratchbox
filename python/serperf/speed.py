import json
from autobahn.wamp.serializer import JsonObjectSerializer, MsgPackObjectSerializer
from autobahn.wamp import message
from time import time

N = 1000000
ROUNDS = 20


def test_serialize(ser, obj):
    print("serializing object {}".format(obj))
    i = 0
    last = time()
    loop = ROUNDS
    res = []
    while True:
        octets = ser.serialize(obj)
        i += 1
        if i % N == 0:
            now = time()
            ops = float(N) / (now - last)
            res.append(ops)
            print("{} objs/sec".format(int(round(ops))))
            last = now
            loop -= 1
            if not loop:
                break
    return res

def test_unserialize(ser, obj):
    octets = ser.serialize(obj)
    print("unserializing object {}".format(obj))
    i = 0
    last = time()
    loop = ROUNDS
    res = []
    while True:
        obj = ser.unserialize(octets)
        i += 1
        if i % N == 0:
            now = time()
            ops = float(N) / (now - last)
            res.append(ops)
            print("{} objs/sec".format(int(round(ops))))
            last = now
            loop -= 1
            if not loop:
                break
    return res


msg = message.Call(1, u'com.example.add2', args=(1, 2), kwargs={u'foo': 23, u'bar': u'baz'}, receive_progress=True)
obj = msg.marshal()
serializers = [JsonObjectSerializer(), MsgPackObjectSerializer()]

res = {
    'ser': {},
    'unser': {}
}

for ser in serializers:
    print("testing serializing using {}".format(ser.__class__))
    ops = test_serialize(ser, obj)
    ops = ops[len(ops) / 2:]
    avg = int(round(sum(ops) / float(len(ops))))
    res['ser'][ser.__class__.__name__] = avg
    print

for ser in serializers:
    print("testing unserializing using {}".format(ser.__class__))
    ops = test_unserialize(ser, obj)
    ops = ops[len(ops) / 2:]
    avg = int(round(sum(ops) / float(len(ops))))
    res['unser'][ser.__class__.__name__] = avg
    print

from pprint import pprint
import sys
import platform

print(platform.platform())
print(sys.version)
print
pprint(res)
