import os
from time import time
import vmprof

from autobahn.wamp import message
from autobahn.wamp import serializer

# https://github.com/msgpack/msgpack-python

def test_serialize(ser, runtime):
    total_cnt = 0
    total_bytes = 0

    started = time()
    ended = started

    while (ended - started) < runtime:
        for i in range(100000):
            # construct a WAMP message (do NOT refactor this from here ..)
            msg = message.Call(123456, u'com.myapp.procedure1',            
                args=[1, 2, 3], kwargs={u'foo': 23, u'bar': u'hello'},
                timeout=10000, receive_progress=True)

            # serialize the WAMP message
            payload, is_binary = ser.serialize(msg)
            total_bytes += len(payload)
            total_cnt += 1
        ended = time()

    return ended - started, total_bytes, total_cnt


def test_unserialize(ser, runtime):
    msg = message.Call(123456, u'com.myapp.procedure1',            
        args=[1, 2, 3], kwargs={u'foo': 23, u'bar': u'hello'},
        timeout=10000, receive_progress=True)

    # serialize the WAMP message
    payload, is_binary = ser.serialize(msg)

    total_cnt = 0
    total_bytes = 0

    started = time()
    ended = started

    while (ended - started) < runtime:
        for i in range(100000):
            # unserialize message
            msg = ser.unserialize(payload, is_binary)

            total_bytes += len(payload)
            total_cnt += 1
        ended = time()

    return ended - started, total_bytes, total_cnt


if __name__ == '__main__':

    PROFILE_FILE = 'vmprof_{}_{}.dat'
    RUNTIME = 5

    tests = [test_serialize, test_unserialize]
    serializers = []

    # JSON serializer is always available
    serializers.append(serializer.JsonSerializer())
    #serializers.append(serializer.JsonSerializer(batched=True))

    # MsgPack serializers are optional
    if hasattr(serializer, 'MsgPackSerializer'):
        serializers.append(serializer.MsgPackSerializer())
        #serializers.append(serializer.MsgPackSerializer(batched=True))
    else:
        print("MsgPack not installed (pip install msgpack-python)")

    for test in tests:
        for ser in serializers:

            print("Running {} on serializer {} for {} seconds ..".format(test.__name__, ser.__class__, RUNTIME))

            profile = PROFILE_FILE.format(test.__name__, ser.SERIALIZER_ID)

            outfd = os.open(profile, os.O_RDWR | os.O_CREAT | os.O_TRUNC)
            vmprof.enable(outfd, period=0.01)
            runtime, total_bytes, total_cnt = test(ser, RUNTIME)
            vmprof.disable()

            avg_msg_len = round(float(total_bytes) / float(total_cnt))

            print("Processed {} messages in {} secs ({} total bytes serialized) at {} msgs/sec ({} bytes avg.)".format(total_cnt, round(runtime, 1), total_bytes, round(float(total_cnt) / runtime), avg_msg_len))
            print("Profile written to {}.".format(profile))
            print("To view the profile, run: vmprofshow {} --indent=2 --prune_percent=5".format(profile))
            print
