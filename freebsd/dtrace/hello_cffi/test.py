from cffi import FFI
ffi = FFI()

DTRACE_VERSION = 3

ffi.cdef("""
   int printf(const char *format, ...);

   typedef struct dtrace_hdl dtrace_hdl_t;
   extern dtrace_hdl_t *dtrace_open(int, int, int *);
   extern const char *dtrace_errmsg(dtrace_hdl_t *, int);
""")

C = ffi.dlopen(None)
#C.printf("SDFSDF")

# I am running into https://lists.freebsd.org/pipermail/svn-src-head/2014-March/056553.html
#lib_z = ffi.dlopen("/lib/libz.so.6") # <= does not help =(

# this is the lib I need to load ..
#lib_ctf = ffi.dlopen("/lib/libctf.so.2")

dtrace = ffi.dlopen("/usr/home/oberstet/scm/scratchbox/freebsd/dtrace/hello_cffi/libfoo.so")
print dtrace

err = ffi.new("int*")
#dtp = ffi.new("dtrace_hdl_t*")
dtp = dtrace.dtrace_open(DTRACE_VERSION, 0, err)
print dtp
print err[0]
err_msg = dtrace.dtrace_errmsg(dtp, err[0])
print err_msg
#print "{}".format(dtrace.dtrace_errmsg(dtp, err[0]))
C.printf("%s\n", err_msg)

print ffi.string(err_msg).decode('utf8')