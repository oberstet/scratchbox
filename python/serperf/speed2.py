import json
from autobahn.wamp.serializer import JsonObjectSerializer, MsgPackObjectSerializer, CBORObjectSerializer
from autobahn.wamp import message
from time import time


def test_serialize(n, rounds, ser, obj):
    print("serializing object {}".format(obj))
    i = 0
    last = time()
    loop = rounds
    res = []
    while True:
        octets = ser.serialize(obj)
        i += 1
        if i % n == 0:
            now = time()
            ops = float(N) / (now - last)
            res.append(ops)
            print("{} objs/sec".format(int(round(ops))))
            last = now
            loop -= 1
            if not loop:
                break
    return res


def test_unserialize(n, rounds, ser, obj):
    octets = ser.serialize(obj)
    print("unserializing object {}".format(obj))
    i = 0
    last = time()
    loop = rounds
    res = []
    while True:
        obj = ser.unserialize(octets)
        i += 1
        if i % n == 0:
            now = time()
            ops = float(N) / (now - last)
            res.append(ops)
            print("{} objs/sec".format(int(round(ops))))
            last = now
            loop -= 1
            if not loop:
                break
    return res


if __name__ == '__main__':

    import sys
    import platform
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--serializer',
        dest='serializer',
        choices=['json', 'msgpack', 'cbor'],
        default='json',
        help='Serializer to use. Choose from: json, msgpack, cbor.')

    parser.add_argument('--mode',
        dest='mode',
        choices=['ser', 'unser'],
        default='ser',
        help='Mode. Choose from: ser, unser.')

    parser.add_argument('--rounds',
        dest='rounds',
        type=int,
        default=20,
        help='Number of rounds to run this test.')

    parser.add_argument('--count',
        dest='count',
        type=int,
        default=1000000,
        help='Number of serializations/unserializations nto perform per round')

    options = parser.parse_args()

    SERMAP = {
        'json': JsonObjectSerializer,
        'msgpack': MsgPackObjectSerializer,
        'cbor': CBORObjectSerializer
    }
    ser = SERMAP[options.serializer]()

    msg = message.Call(1, u'com.example.add2', args=(1, 2), kwargs={u'foo': 23, u'bar': u'baz'}, receive_progress=True)
    obj = msg.marshal()

    if options.mode == 'serialize':
        print("testing serializing using {}".format(ser.__class__))
        ops = test_serialize(ser, obj)
    elif options.mode == 'unserialize':
        print("testing unserializing using {}".format(ser.__class__))
        ops = test_unserialize(ser, obj)
    else:
        raise Exception("logic error")

    # arithmetic mean over second half of results for individual rounds
    ops = ops[len(ops) / 2:]
    avg = int(round(sum(ops) / float(len(ops))))

    print("{} ops/sec".format(avg))
    print(platform.platform())
    print(sys.version)
