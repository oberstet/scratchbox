from cffi import FFI

ffi = FFI()

## I got a Py string, want to process in C, and get back
## a Py string. Roundtrip over C. This will incur 2 copies.

s_in = "\x00" * 1000
buf = ffi.new("char[]", s_in)

## => Do something in C with buf

s_out = ffi.buffer(buf)[:-1] # ffi will append a \0 octet, eat it!
buf = None # GC of underlying mem

assert(len(s_in), len(s_out))
