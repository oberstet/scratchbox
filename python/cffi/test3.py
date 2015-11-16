import os
import sys
import argparse
import binascii

from cffi import FFI

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import succeed
from twisted.internet.task import react, LoopingCall

import cmmap


ffi = FFI()

ffi.cdef("""
typedef struct {
    uint32_t msg_type;
    uint64_t request;
    wchar_t uri[100];
    uint32_t foo;
} wamp_msg_subscribe_t;

typedef struct {
    uint32_t msg_type;
    uint64_t request;
    uint64_t subscription;
} wamp_msg_subscribed_t;

// PUBLISH
typedef struct {
    uint32_t msg_type;
    uint64_t request;
    wchar_t topic[100];
    bool acknowledge;
    bool exclude_me;

    // exclude (vector of uint64_t)
    uint32_t exclude_offset;
    uint32_t exclude_length;

    // eligible (vector of uint64_t)
    uint32_t eligible_offset;
    uint32_t eligible_length;

    // application payload in different serialization formats
    uint32_t args_json_offset;
    uint32_t args_json_length;
    uint32_t kwargs_json_offset;
    uint32_t kwargs_json_length;
    uint32_t args_msgpack_offset;
    uint32_t args_msgpack_length;
    uint32_t kwargs_msgpack_offset;
    uint32_t kwargs_msgpack_length;
} wamp_msg_publish_t;
""")


DATA = b'\x07\0\0\0\0\0\0\0foobarbing'
OFFSET = 300

class ShmArea(object):

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise Exception("path {} does not exist".format(filename))
        size = os.stat(filename).st_size
        with open(filename, 'rb') as fd:
            self._map = cmmap.mmap(prot=cmmap.PROT_READ, length=size, flags=cmmap.MAP_SHARED, fd=fd.fileno(), buffer=False)

    def get(self, offset):
        print self._map, self._map + offset
        msg_type = ffi.cast("uint32_t*", self._map + offset)[0]
        if msg_type == 3:
            return ffi.cast("wamp_msg_subscribed_t*", self._map + offset)
        elif msg_type == 2:
            return ffi.cast("wamp_msg_subscribe_t*", self._map + offset)
        else:
            raise Exception("invalid msg_type {}".format(msg_type))


def run_reader(reactor, shmfile, size=1024):
    print("run_reader", reactor.__class__, shmfile)

    area = ShmArea(shmfile)

    msg = area.get(0)
    print msg.msg_type, msg.request, ffi.string(msg.uri)

    msg = area.get(OFFSET)
    print msg.msg_type, msg.request, msg.subscription

    return succeed(None)

    with open(shmfile, 'rb') as fd:
        shm = cmmap.mmap(prot=cmmap.PROT_READ, length=size, flags=cmmap.MAP_SHARED, fd=fd.fileno(), buffer=False)
        msg = ffi.cast("wamp_msg_subscribed_t*", shm)
        print("msg: {} {}".format(msg.request, msg.subscription))

    return succeed(None)


def run_writer(reactor, shmfile, size=1024):
    print("run_writer", reactor.__class__, shmfile)

    with open(shmfile, 'rw+') as fd:
        shm = cmmap.mmap(prot=cmmap.PROT_READ|cmmap.PROT_WRITE, flags=cmmap.MAP_SHARED, length=size, fd=fd.fileno(), buffer=False)

        msg = ffi.cast("wamp_msg_subscribe_t*", shm)
        msg.msg_type = 2
        msg.request = 23
        msg.uri = u'com.example.add2'
        msg.foo = 255

        msg = ffi.cast("wamp_msg_subscribed_t*", shm + OFFSET)
        msg.msg_type = 3
        msg.request = 23
        msg.subscription = 666
        print("msg: {} {}".format(msg.request, msg.subscription))

    return succeed(None)


def run_writer3(reactor, shmfile, size=1024):
    print("run_writer", reactor.__class__, shmfile)

    if False:
        if os.path.exists(shmfile):
            print("removing existing file")
            os.remove(shmfile)

        with open(shmfile, 'wb+') as fd:
            fd.write(DATA)
            fd.truncate(size)
            fd.flush()

        return succeed(None)

    with open(shmfile, 'rw+') as fd:
#  m = cmmap.mmap(prot=cmmap.PROT_READ, length=len(data), flags=cmmap.MAP_SHARED, fd=f.fileno())
#        shm = cmmap.mmap(prot=cmmap.PROT_WRITE, length=size, flags=cmmap.MAP_SHARED, fd=fd.fileno(), buffer=False)
#        shm = cmmap.mmap(prot=cmmap.PROT_WRITE, length=size, flags=cmmap.MAP_SHARED, fd=fd.fileno(), buffer=True)
        shm = cmmap.mmap(prot=cmmap.PROT_READ|cmmap.PROT_WRITE, flags=cmmap.MAP_SHARED, length=size, fd=fd.fileno(), buffer=True)
        print(shm, type(shm), len(shm))
        #shm[0:len(DATA)] = DATA
        print(binascii.hexlify(shm[0:10]))
        #msg = ffi.cast("wamp_msg_subscribed_t*", shm)
        #print fd, shm, type(shm), msg, type(msg)
        #msg.request = 23
        #msg.subscription = 666
        #print("msg: {} {}".format(msg.request, msg.subscription))

    return succeed(None)


def run_writer2(reactor, shmfile, size=1000):
    print("run_writer", reactor.__class__, shmfile)

    if not os.path.exists(shmfile):
        with open(shmfile, 'wb') as out:
            out.truncate(size)

    with open(shmfile, 'wb') as fd:
        shm = cmmap.mmap(prot=cmmap.PROT_WRITE, length=size, flags=cmmap.MAP_SHARED, fd=fd.fileno(), buffer=False)
        msg = ffi.cast("wamp_msg_subscribed_t*", shm)
        #msg.request = 23
        #msg.subscription = 666
        print("msg: {} {}".format(msg.request, msg.subscription))

    return succeed(None)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-w", "--writer", action="store_true",
                        help="If true, this is the writer.")

    parser.add_argument("--shmfile", type=str, default='shm.map',
                        help='Shared memory map file.')

    args = parser.parse_args()

    log.startLogging(sys.stdout)

    print(cmmap.PROT_READ)
    print(cmmap.PROT_WRITE)
    print(cmmap.MAP_SHARED)

    if args.writer:
        react(run_writer, (args.shmfile,))
    else:
        react(run_reader, (args.shmfile,))
