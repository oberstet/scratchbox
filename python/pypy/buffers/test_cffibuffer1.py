from cffi import FFI

ffi = FFI()

## I got a Py string, want to process in C, and get back
## a Py string. Roundtrip over C. This will incur 2 copies.

N = 1000
s_in = "\x00" * N
buf = ffi.new("char[]", s_in)
print len(buf)

## => Do something in C with buf

#s_out = ffi.buffer(buf)[:-1] # ffi will append a \0 octet, eat it!
s_out = ffi.buffer(buf, len(buf) - 1)[:] # ffi will append a \0 octet, eat it!
buf = None # GC of underlying mem

assert(len(s_in), len(s_out))
