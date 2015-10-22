import tempfile
import cmmap
from multiprocessing import Process

from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct {
        uint64_t request;
        uint64_t subscription;
    } wamp_msg_subscribed_t;
""")


def test_file():
    fd, filename = tempfile.mkstemp()
    f = open(filename, 'wb')
    data = b'\x07\0\0\0\0\0\0\0foobarbing'
    f.write(data)
    f.close()

    f = open(filename, 'rb+')
    m = cmmap.mmap(prot=cmmap.PROT_READ, length=len(data), flags=cmmap.MAP_SHARED, fd=f.fileno(), buffer=False)
    m = ffi.cast("wamp_msg_subscribed_t*", m)
    print m
    print m.request
#    m = cmmap.mmap(prot=cmmap.PROT_READ, length=len(data), flags=cmmap.MAP_SHARED, fd=f.fileno())
#    assert m[:] == data


test_file()
