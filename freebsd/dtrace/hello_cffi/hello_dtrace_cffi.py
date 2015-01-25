import sys
from cffi import FFI


def get_dtrace(ffi):

   ffi.cdef("""
typedef struct dtrace_hdl dtrace_hdl_t;

extern dtrace_hdl_t *dtrace_open(int, int, int *);
extern void dtrace_close(dtrace_hdl_t *);

extern int dtrace_errno(dtrace_hdl_t *);
extern const char *dtrace_errmsg(dtrace_hdl_t *, int);

extern int dtrace_setopt(dtrace_hdl_t *, const char *, const char *);
   """)

   # https://lists.freebsd.org/pipermail/svn-src-head/2014-March/056553.html
   LIBS = [
      "libelf.so",
      "libthr.so",
      "libutil.so",
      "libz.so",
      "libctf.so",
      "librtld_db.so",
      "libproc.so",
   ]
   for lib in LIBS:
      try:
         # http://linux.die.net/man/3/dlopen
         ffi.dlopen(lib, ffi.RTLD_GLOBAL | ffi.RTLD_LAZY)
      except Exception as e:
         print("failed to load library {}\n\n: {}".format(lib, e))
         return None

   dtrace = ffi.dlopen("libdtrace.so")

   return dtrace


class DTrace:

   def __init__(self):
      self._DTRACE_VERSION = 3
      self._ffi = FFI()
      self._dtrace = get_dtrace(self._ffi)
      self._dtp = None

   def get_error(self):
      if self._dtp:
         err_no = self._dtrace.dtrace_errno(self._dtp)
         err_msg_c = self._dtrace.dtrace_errmsg(self._dtp, err_no)
         err_msg = self._ffi.string(err_msg_c).decode('utf8')
         return err_no, err_msg
      else:
         return 0, None

   def open(self):
      error = self._ffi.new("int*")
      self._dtp = self._dtrace.dtrace_open(self._DTRACE_VERSION, 0, error)
      if self._dtp == self._ffi.NULL:
         err_msg_c = self._dtrace.dtrace_errmsg(self._dtp, error)
         err_msg = self._ffi.string(err_msg_c).decode('utf8')
         raise Exception(err_msg)

   def set_option(self, key, value):
      if self._dtp:
         res = self._dtrace.dtrace_setopt(self._dtp, key.encode('utf8'), value.encode('utf8'))
         if res == -1:
            err_no, err_msg = self.get_error()
            raise Exception("could not set DTrace option '{}' to '{}' - {}".format(key, value, err_msg))

   def close(self):
      if self._dtp:
         self._dtrace.dtrace_close(self._dtp)
         self._dtp = None



dt = DTrace()
dt.open()
dt.set_option("bufsize", "4m")
dt.set_option("aggsize", "4m")
dt.set_option("foobar", "xxx")
dt.close()

# print dtrace

# DTRACE_VERSION = 3

# err = ffi.new("int*")
# #dtp = ffi.new("dtrace_hdl_t*")
# dtp = dtrace.dtrace_open(DTRACE_VERSION, 0, err)
# print dtp
# print dtp is None, dtp == None, dtp == 0, dtp == ffi.NULL
# print err[0]
# err_msg = dtrace.dtrace_errmsg(dtp, err[0])
# print err_msg

# print ffi.string(err_msg).decode('utf8')
