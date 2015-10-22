from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct {
        unsigned char r, g, b, alpha;
        bool exclude_me;
        int* a;
    } pixel_t;
""")

print 800*600*(4+4+8)

image = ffi.new("pixel_t[]", 800*600)
image[100].a = ffi.new("int[]", 5)

#f = open('data', 'rb')     # binary mode -- important
#f.readinto(ffi.buffer(image))
#f.close()

image[100].r = 255
image[100].g = 192
image[100].b = 128
image[100].exclude_me = True
image[100].a[3] = 23

f = open('data', 'wb')
f.write(ffi.buffer(image))
f.close()
