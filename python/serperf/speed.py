import json
from autobahn.wamp.serializer import JsonObjectSerializer, MsgPackObjectSerializer
from autobahn.wamp import message
from time import time

N = 1000000
ROUNDS = 10


def test_serialize(ser, obj):
    print("serializing object {}".format(obj))
    i = 0
    last = time()
    loop = ROUNDS
    while True:
        octets = ser.serialize(obj)
        i += 1
        if i % N == 0:
            now = time()
            print("{} objs/sec".format(int(round(float(N) / (now - last)))))
            last = now
            loop -= 1
            if not loop:
                break

def test_unserialize(ser, obj):
    octets = ser.serialize(obj)
    print("unserializing object {}".format(obj))
    i = 0
    last = time()
    loop = ROUNDS
    while True:
        obj = ser.unserialize(octets)
        i += 1
        if i % N == 0:
            now = time()
            print("{} objs/sec".format(int(round(float(N) / (now - last)))))
            last = now
            loop -= 1
            if not loop:
                break


msg = message.Call(1, u'com.example.add2', args=(1, 2), kwargs={u'foo': 23, u'bar': u'baz'}, receive_progress=True)
obj = msg.marshal()
serializers = [JsonObjectSerializer(), MsgPackObjectSerializer()]

for ser in serializers:
    print("testing serializing using {}".format(ser.__class__))
    test_serialize(ser, obj)
    print

for ser in serializers:
    print("testing unserializing using {}".format(ser.__class__))
    test_unserialize(ser, obj)
    print
