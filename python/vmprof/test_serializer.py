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
            # construct a WAMP message
            msg = message.Call(123456, u'com.myapp.procedure1',            
                args=[1, 2, 3], kwargs={u'foo': 23, u'bar': u'hello'},
                timeout=10000, receive_progress=True)

            # serialize the WAMP message
            payload, is_binary = ser.serialize(msg)
            total_bytes += len(payload)
            total_cnt += 1
        ended = time()
    return ended - started, total_bytes, total_cnt

#        # unserialize message again
#        msg2 = ser.unserialize(payload, binary)


if __name__ == '__main__':

    PROFILE_FILE = 'vmprof_{}.dat'
    RUNTIME = 10

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

    for ser in serializers:

        print("Testing serializer '{}' for {} seconds ..".format(ser.SERIALIZER_ID, RUNTIME))

        profile = PROFILE_FILE.format(ser.SERIALIZER_ID)

        outfd = os.open(profile, os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        vmprof.enable(outfd, period=0.01)
        runtime, total_bytes, total_cnt = test_serialize(ser, RUNTIME)
        vmprof.disable()

        avg_msg_len = round(float(total_bytes) / float(total_cnt))

        print("Serialized {} messages in {} secs ({} total bytes serialized): {} msgs/sec ({} bytes avg.)".format(total_cnt, round(runtime, 1), total_bytes, round(float(total_cnt) / runtime), avg_msg_len))
        print("Profile written to {}.".format(profile))
        print("To view the profile, run: vmprofshow {} --indent=2 --prune_percent=5".format(profile))
        print
