import sys
import os
from cffi import FFI


DTRACE_ABI_CDEF = """
//
// fixes
//
typedef unsigned int uint_t;

//
// Directly taken from:
// usr/src/sys/cddl/contrib/opensolaris/uts/common/sys/dtrace.h
//

typedef uint32_t dtrace_id_t;    /* probe identifier */
typedef uint32_t dtrace_epid_t;     /* enabled probe identifier */
typedef uint32_t dtrace_aggid_t; /* aggregation identifier */
typedef int64_t dtrace_aggvarid_t;  /* aggregation variable identifier */
typedef uint16_t dtrace_actkind_t;  /* action kind */
typedef int64_t dtrace_optval_t; /* option value */
typedef uint32_t dtrace_cacheid_t;  /* predicate cache identifier */

typedef enum dtrace_probespec {
   DTRACE_PROBESPEC_NONE = -1,
   DTRACE_PROBESPEC_PROVIDER = 0,
   DTRACE_PROBESPEC_MOD,
   DTRACE_PROBESPEC_FUNC,
   DTRACE_PROBESPEC_NAME
} dtrace_probespec_t;

typedef uint8_t dtrace_stability_t; /* stability code (see attributes(5)) */
typedef uint8_t dtrace_class_t;     /* architectural dependency class */

typedef struct dtrace_attribute {
   dtrace_stability_t dtat_name;    /* entity name stability */
   dtrace_stability_t dtat_data;    /* entity data stability */
   dtrace_class_t dtat_class;    /* entity data dependency */
} dtrace_attribute_t;


typedef struct dtrace_recdesc {
   dtrace_actkind_t dtrd_action;    /* kind of action */
   uint32_t dtrd_size;        /* size of record */
   uint32_t dtrd_offset;         /* offset in ECB's data */
   uint16_t dtrd_alignment;      /* required alignment */
   uint16_t dtrd_format;         /* format, if any */
   uint64_t dtrd_arg;         /* action argument */
   uint64_t dtrd_uarg;        /* user argument */
} dtrace_recdesc_t;


typedef struct dtrace_eprobedesc {
   dtrace_epid_t dtepd_epid;     /* enabled probe ID */
   dtrace_id_t dtepd_probeid;    /* probe ID */
   uint64_t dtepd_uarg;       /* library argument */
   uint32_t dtepd_size;       /* total size */
   int dtepd_nrecs;        /* number of records */
   dtrace_recdesc_t dtepd_rec[1];      /* records themselves */
} dtrace_eprobedesc_t;




//
// Directly taken from:
// /usr/src/cddl/contrib/opensolaris/lib/libdtrace/common/dtrace.h
//
typedef struct dtrace_hdl dtrace_hdl_t;
typedef struct dtrace_prog dtrace_prog_t;
typedef struct dtrace_vector dtrace_vector_t;
typedef struct dtrace_aggdata dtrace_aggdata_t;

typedef struct dtrace_proginfo {
   dtrace_attribute_t dpi_descattr; /* minimum probedesc attributes */
   dtrace_attribute_t dpi_stmtattr; /* minimum statement attributes */
   uint_t dpi_aggregates;  /* number of aggregates specified in program */
   uint_t dpi_recgens;  /* number of record generating probes in prog */
   uint_t dpi_matches;  /* number of probes matched by program */
   uint_t dpi_speculations; /* number of speculations specified in prog */
} dtrace_proginfo_t;


extern dtrace_hdl_t *dtrace_open(int, int, int *);
extern int dtrace_go(dtrace_hdl_t *);
extern int dtrace_stop(dtrace_hdl_t *);
extern void dtrace_sleep(dtrace_hdl_t *);
extern void dtrace_close(dtrace_hdl_t *);

extern int dtrace_errno(dtrace_hdl_t *);
extern const char *dtrace_errmsg(dtrace_hdl_t *, int);

extern int dtrace_setopt(dtrace_hdl_t *, const char *, const char *);

extern dtrace_prog_t *dtrace_program_strcompile(dtrace_hdl_t *,
    const char *, dtrace_probespec_t, uint_t, int, char *const []);

extern int dtrace_program_exec(dtrace_hdl_t *, dtrace_prog_t *,
    dtrace_proginfo_t *);

extern void dtrace_program_info(dtrace_hdl_t *, dtrace_prog_t *,
    dtrace_proginfo_t *);



"""

"""
typedef struct dtrace_probedesc {
   dtrace_id_t dtpd_id;       /* probe identifier */
   char dtpd_provider[DTRACE_PROVNAMELEN]; /* probe provider name */
   char dtpd_mod[DTRACE_MODNAMELEN];   /* probe module name */
   char dtpd_func[DTRACE_FUNCNAMELEN]; /* probe function name */
   char dtpd_name[DTRACE_NAMELEN];     /* probe name */
} dtrace_probedesc_t;
/*
 * DTrace Data Consumption Interface
 */
typedef enum {
   DTRACEFLOW_ENTRY,
   DTRACEFLOW_RETURN,
   DTRACEFLOW_NONE
} dtrace_flowkind_t;

#define  DTRACE_CONSUME_ERROR    -1 /* error while processing */
#define  DTRACE_CONSUME_THIS     0  /* consume this probe/record */
#define  DTRACE_CONSUME_NEXT     1  /* advance to next probe/rec */
#define  DTRACE_CONSUME_ABORT    2  /* abort consumption */

/*
typedef struct dtrace_probedata {
   dtrace_hdl_t *dtpda_handle;      /* handle to DTrace library */
   dtrace_eprobedesc_t *dtpda_edesc;   /* enabled probe description */
   dtrace_probedesc_t *dtpda_pdesc; /* probe description */
   processorid_t dtpda_cpu;      /* CPU for data */
   caddr_t dtpda_data;        /* pointer to raw data */
   dtrace_flowkind_t dtpda_flow;    /* flow kind */
   const char *dtpda_prefix;     /* recommended flow prefix */
   int dtpda_indent;       /* recommended flow indent */
} dtrace_probedata_t;

typedef int dtrace_consume_probe_f(const dtrace_probedata_t *, void *);
typedef int dtrace_consume_rec_f(const dtrace_probedata_t *,
    const dtrace_recdesc_t *, void *);

extern int dtrace_consume(dtrace_hdl_t *, FILE *,
    dtrace_consume_probe_f *, dtrace_consume_rec_f *, void *);

#define  DTRACE_STATUS_NONE   0  /* no status; not yet time */
#define  DTRACE_STATUS_OKAY   1  /* status okay */
#define  DTRACE_STATUS_EXITED 2  /* exit() was called; tracing stopped */
#define  DTRACE_STATUS_FILLED 3  /* fill buffer filled; tracing stoped */
#define  DTRACE_STATUS_STOPPED   4  /* tracing already stopped */

extern int dtrace_status(dtrace_hdl_t *);
*/

/*
 * DTrace Work Interface
 */
typedef enum {
   DTRACE_WORKSTATUS_ERROR = -1,
   DTRACE_WORKSTATUS_OKAY,
   DTRACE_WORKSTATUS_DONE
} dtrace_workstatus_t;

extern dtrace_workstatus_t dtrace_work(dtrace_hdl_t *, FILE *,
    dtrace_consume_probe_f *, dtrace_consume_rec_f *, void *);

"""

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
         print res

   def sleep(self):
      if self._dtp:
         res = self._dtrace.dtrace_sleep(self._dtp)
         print("woke up")


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



D_PROGRAM = """
BEGIN { printf("hello from dtrace\\n"); }
"""

dt = DTrace()
dt.open()
dt.set_option("bufsize", "4m")
dt.set_option("aggsize", "4m")
prog = dt.compile(D_PROGRAM)
print prog
prog.execute()
dt.go()
while True:
   dt.sleep()
   dt.work()
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
