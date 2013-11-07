import binascii
from cffi import FFI


def variant1(ffi, align, size, init = False, initstr = None):

   pp = ffi.new("char*[1]")
   ffi.libc.posix_memalign(pp, align, size)

   p = pp[0]

   if initstr:
      ## If len(inits) > size, this throws
      p[0:size] = initstr
      ffi.xor.xor(p, size)

   elif init:
      ## for writing like this, I had to change the signature of C
      ## function (well, C is fine with that of course)
      for i in xrange(size):
         #p[i] = '\x00'
         p[i] = chr(i & 0xff)

   s = ffi.buffer(p, size)[:]

   print len(s)
   print binascii.hexlify(s)

   ## _manually_ free underlying mem. How would I do that automatically?
   ## How to hook up libc.free to the destructor (GC) of "pp"
   ##
   ffi.libc.free(p)

   ## the pp thingy is GCed automatically


def variant2(ffi, align, size):

   ## this might return 0 if "out of memory", but in that case
   ## we are unlikely to be able to do anything useful anyway
   ##
   p = ffi.gc(ffi.libc.aligned_alloc(align, size), libc.free)

   s = ffi.buffer(p, size)[:]

   print len(s)
   print binascii.hexlify(s)

   ## When p is GCed, the memory allocated with "aligned_malloc"
   ## should be free'ed automagically (by invocation of libc.free),
   ## right?



if __name__ == '__main__':

   ffi = FFI()

   ffi.cdef("""
      // The function posix_memalign() is available since glibc 2.1.91.
      // http://linux.die.net/man/3/posix_memalign

      // signature modified, so we'll be able to direct write from Py
      //
      int posix_memalign(char **memptr, size_t alignment, size_t size);
      //int posix_memalign(void **memptr, size_t alignment, size_t size);


      // The function aligned_alloc() was added to glibc in version 2.16.
      // http://linux.die.net/man/3/aligned_alloc
      //
      void *aligned_alloc(size_t alignment, size_t size);


      void free(void *ptr);

      void xor(char* data, size_t len);
   """)

   ffi.libc = ffi.dlopen(None)
   ffi.xor = ffi.dlopen('libxor.so')

   variant1(ffi, 16, 1024)
   variant1(ffi, 16, 1024, init = True)

   s = ''.join([chr(i) for i in xrange(16)])
   #variant1(ffi, 16, 1024, initstr = '*' * 1024)
   variant1(ffi, 16, 1024, initstr = s * (1024 / 16))

   ## The next variant will only work on _newest_ libc.
   ##
   ## How do I check programatically?
   ## E.g., you can do this in shell: "apt-cache show libc6"
   ##
   ## The Linux man page says there is a macro: _ISOC11_SOURCE
   ##
   ## And then it talks about: http://linux.die.net/man/7/feature_test_macros
   _ISOC11_SOURCE = False
   if _ISOC11_SOURCE:
      variant2(ffi, 16, 1024)

# http://www.freebsd.org/cgi/man.cgi?query=posix_memalign&sektion=3&manpath=FreeBSD+9.2-RELEASE
