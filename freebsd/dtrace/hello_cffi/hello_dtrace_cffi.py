import sys
import os
from cffi import FFI


DTRACE_ABI_CDEF = open("dtrace.h").read()
print len(DTRACE_ABI_CDEF)

DTRACE_API_C = """
#include "/usr/src/cddl/contrib/opensolaris/lib/libdtrace/common/dtrace.h"
"""

DTRACE_API_INCLUDE_DIRS = [
   "/usr/src/sys/cddl/compat/opensolaris/",
   "/usr/src/sys/cddl/contrib/opensolaris/uts/common"
]

DTRACE_API_LIB_DIRS = [
   "/lib",
   "/usr/lib"
]

DTRACE_API_LIBRARIES = [
   "elf",
   "thr",
   "util",
   "z",
   "ctf",
   "rtld_db",
   "proc",

   #"dtrace.so"
   #"/lib/libdtrace.so.2"
   #"/usr/lib/libdtrace.a"
   "dtrace"
]


def get_dtrace(ffi, api_mode = False):

   if api_mode:
      dtrace = ffi.verify(DTRACE_API_C,
         include_dirs = DTRACE_API_INCLUDE_DIRS,
         library_dirs = DTRACE_API_LIB_DIRS,
         libraries = DTRACE_API_LIBRARIES)
   else:
      ffi.cdef(DTRACE_ABI_CDEF)

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



class DTraceProgram:

   def __init__(self, dtrace, prog):
      self._dtrace = dtrace
      self._prog = prog


   def execute(self):
      info = self._dtrace._ffi.new("dtrace_proginfo_t[1]")
      res = self._dtrace._dtrace.dtrace_program_exec(self._dtrace._dtp, self._prog, info)
      if res == -1:
         err_no, err_msg = self._dtrace.get_error()
         raise Exception("could not execute instrumentation: {}".format(err_msg))
      else:
         print("probe executing")



class DTrace:

   ## /usr/src/sys/cddl/contrib/opensolaris/uts/common/sys/dtrace.h
   DTRACE_PROBESPEC_NONE = -1
   DTRACE_PROBESPEC_PROVIDER = 0
   DTRACE_PROBESPEC_MOD = 1
   DTRACE_PROBESPEC_FUNC = 2
   DTRACE_PROBESPEC_NAME = 3

   def __init__(self):
      self._DTRACE_VERSION = 3
      self._ffi = FFI()
      self._C = self._ffi.dlopen(None)
      #print "X"*10, self._C.stdout
      self._dtrace = get_dtrace(self._ffi)
      self._dtp = None
      self._fd = None

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


   def compile(self, program):
      prog = self._dtrace.dtrace_program_strcompile(self._dtp, program.encode('utf8'), self._dtrace.DTRACE_PROBESPEC_NAME, 0, 0, self._ffi.NULL)
      if prog == self._ffi.NULL:
         err_no, err_msg = self.get_error()
         raise Exception("could not compile D program - {}".format(err_msg))

      return DTraceProgram(self, prog)

   def go(self, fd = None):
      if self._dtp:

         fd = fd or sys.stdout
         self._fd = self._ffi.cast("FILE*", fd)

         self._chew = self._ffi.callback("int (const dtrace_probedata_t*, const dtrace_recdesc_t*, void*)", self.chew) 

         res = self._dtrace.dtrace_go(self._dtp)
         if res != 0:
            err_no, err_msg = self.get_error()
            raise Exception("could not start instrumentation: {}".format(e))
         else:
            print("instrumentation started")

   def work(self):
      if self._dtp:
         res = self._dtrace.dtrace_work(self._dtp, self._fd, self._ffi.NULL, self._chew, self._ffi.NULL)
         print("work result: {}".format(res))

   def sleep(self):
      if self._dtp:
         res = self._dtrace.dtrace_sleep(self._dtp)
         print("woke up")


   def stop(self):
      if self._dtp:
         res = self._dtrace.dtrace_stop(self._dtp)
         if res == -1:
            err_no, err_msg = self.get_error()
            raise Exception("could not stop instrumentation: {}".format(err_msg))
         else:
            print("instrumentation stopped")


   def close(self):
      if self._dtp:
         self._dtrace.dtrace_close(self._dtp)
         self._dtp = None


   def chew(self, data, rec, arg):
      print("chew!", data, rec, arg)

      # A NULL rec indicates that we've processed the last record.
      if rec == self._ffi.NULL:
         return self._dtrace.DTRACE_CONSUME_NEXT

      return self._dtrace.DTRACE_CONSUME_THIS
      #return self._dtrace.DTRACE_CONSUME_ABORT




D_PROGRAM1 = """
BEGIN { printf("hello from dtrace\\n"); }
"""

D_PROGRAM2 = """
syscall::open*:entry { printf("%s %s\\n", execname, copyinstr(arg0)); }
"""

dt = DTrace()
dt.open()
dt.set_option("bufsize", "4m")
dt.set_option("aggsize", "4m")
prog = dt.compile(D_PROGRAM2)
prog.execute()
dt.go()
while True:
   dt.sleep()
   dt.work()
dt.stop()
dt.close()
