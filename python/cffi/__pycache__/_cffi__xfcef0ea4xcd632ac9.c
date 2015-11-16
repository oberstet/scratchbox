
#include <Python.h>
#include <stddef.h>

/* this block of #ifs should be kept exactly identical between
   c/_cffi_backend.c, cffi/vengine_cpy.py, cffi/vengine_gen.py */
#if defined(_MSC_VER)
# include <malloc.h>   /* for alloca() */
# if _MSC_VER < 1600   /* MSVC < 2010 */
   typedef __int8 int8_t;
   typedef __int16 int16_t;
   typedef __int32 int32_t;
   typedef __int64 int64_t;
   typedef unsigned __int8 uint8_t;
   typedef unsigned __int16 uint16_t;
   typedef unsigned __int32 uint32_t;
   typedef unsigned __int64 uint64_t;
   typedef __int8 int_least8_t;
   typedef __int16 int_least16_t;
   typedef __int32 int_least32_t;
   typedef __int64 int_least64_t;
   typedef unsigned __int8 uint_least8_t;
   typedef unsigned __int16 uint_least16_t;
   typedef unsigned __int32 uint_least32_t;
   typedef unsigned __int64 uint_least64_t;
   typedef __int8 int_fast8_t;
   typedef __int16 int_fast16_t;
   typedef __int32 int_fast32_t;
   typedef __int64 int_fast64_t;
   typedef unsigned __int8 uint_fast8_t;
   typedef unsigned __int16 uint_fast16_t;
   typedef unsigned __int32 uint_fast32_t;
   typedef unsigned __int64 uint_fast64_t;
   typedef __int64 intmax_t;
   typedef unsigned __int64 uintmax_t;
# else
#  include <stdint.h>
# endif
# if _MSC_VER < 1800   /* MSVC < 2013 */
   typedef unsigned char _Bool;
# endif
#else
# include <stdint.h>
# if (defined (__SVR4) && defined (__sun)) || defined(_AIX)
#  include <alloca.h>
# endif
#endif

#if PY_MAJOR_VERSION < 3
# undef PyCapsule_CheckExact
# undef PyCapsule_GetPointer
# define PyCapsule_CheckExact(capsule) (PyCObject_Check(capsule))
# define PyCapsule_GetPointer(capsule, name) \
    (PyCObject_AsVoidPtr(capsule))
#endif

#if PY_MAJOR_VERSION >= 3
# define PyInt_FromLong PyLong_FromLong
#endif

#define _cffi_from_c_double PyFloat_FromDouble
#define _cffi_from_c_float PyFloat_FromDouble
#define _cffi_from_c_long PyInt_FromLong
#define _cffi_from_c_ulong PyLong_FromUnsignedLong
#define _cffi_from_c_longlong PyLong_FromLongLong
#define _cffi_from_c_ulonglong PyLong_FromUnsignedLongLong

#define _cffi_to_c_double PyFloat_AsDouble
#define _cffi_to_c_float PyFloat_AsDouble

#define _cffi_from_c_int_const(x)                                        \
    (((x) > 0) ?                                                         \
        ((unsigned long long)(x) <= (unsigned long long)LONG_MAX) ?      \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromUnsignedLongLong((unsigned long long)(x)) :       \
        ((long long)(x) >= (long long)LONG_MIN) ?                        \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromLongLong((long long)(x)))

#define _cffi_from_c_int(x, type)                                        \
    (((type)-1) > 0 ? /* unsigned */                                     \
        (sizeof(type) < sizeof(long) ?                                   \
            PyInt_FromLong((long)x) :                                    \
         sizeof(type) == sizeof(long) ?                                  \
            PyLong_FromUnsignedLong((unsigned long)x) :                  \
            PyLong_FromUnsignedLongLong((unsigned long long)x)) :        \
        (sizeof(type) <= sizeof(long) ?                                  \
            PyInt_FromLong((long)x) :                                    \
            PyLong_FromLongLong((long long)x)))

#define _cffi_to_c_int(o, type)                                          \
    ((type)(                                                             \
     sizeof(type) == 1 ? (((type)-1) > 0 ? (type)_cffi_to_c_u8(o)        \
                                         : (type)_cffi_to_c_i8(o)) :     \
     sizeof(type) == 2 ? (((type)-1) > 0 ? (type)_cffi_to_c_u16(o)       \
                                         : (type)_cffi_to_c_i16(o)) :    \
     sizeof(type) == 4 ? (((type)-1) > 0 ? (type)_cffi_to_c_u32(o)       \
                                         : (type)_cffi_to_c_i32(o)) :    \
     sizeof(type) == 8 ? (((type)-1) > 0 ? (type)_cffi_to_c_u64(o)       \
                                         : (type)_cffi_to_c_i64(o)) :    \
     (Py_FatalError("unsupported size for type " #type), (type)0)))

#define _cffi_to_c_i8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[1])
#define _cffi_to_c_u8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[2])
#define _cffi_to_c_i16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[3])
#define _cffi_to_c_u16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[4])
#define _cffi_to_c_i32                                                   \
                 ((int(*)(PyObject *))_cffi_exports[5])
#define _cffi_to_c_u32                                                   \
                 ((unsigned int(*)(PyObject *))_cffi_exports[6])
#define _cffi_to_c_i64                                                   \
                 ((long long(*)(PyObject *))_cffi_exports[7])
#define _cffi_to_c_u64                                                   \
                 ((unsigned long long(*)(PyObject *))_cffi_exports[8])
#define _cffi_to_c_char                                                  \
                 ((int(*)(PyObject *))_cffi_exports[9])
#define _cffi_from_c_pointer                                             \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[10])
#define _cffi_to_c_pointer                                               \
    ((char *(*)(PyObject *, CTypeDescrObject *))_cffi_exports[11])
#define _cffi_get_struct_layout                                          \
    ((PyObject *(*)(Py_ssize_t[]))_cffi_exports[12])
#define _cffi_restore_errno                                              \
    ((void(*)(void))_cffi_exports[13])
#define _cffi_save_errno                                                 \
    ((void(*)(void))_cffi_exports[14])
#define _cffi_from_c_char                                                \
    ((PyObject *(*)(char))_cffi_exports[15])
#define _cffi_from_c_deref                                               \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[16])
#define _cffi_to_c                                                       \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[17])
#define _cffi_from_c_struct                                              \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[18])
#define _cffi_to_c_wchar_t                                               \
    ((wchar_t(*)(PyObject *))_cffi_exports[19])
#define _cffi_from_c_wchar_t                                             \
    ((PyObject *(*)(wchar_t))_cffi_exports[20])
#define _cffi_to_c_long_double                                           \
    ((long double(*)(PyObject *))_cffi_exports[21])
#define _cffi_to_c__Bool                                                 \
    ((_Bool(*)(PyObject *))_cffi_exports[22])
#define _cffi_prepare_pointer_call_argument                              \
    ((Py_ssize_t(*)(CTypeDescrObject *, PyObject *, char **))_cffi_exports[23])
#define _cffi_convert_array_from_object                                  \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[24])
#define _CFFI_NUM_EXPORTS 25

typedef struct _ctypedescr CTypeDescrObject;

static void *_cffi_exports[_CFFI_NUM_EXPORTS];
static PyObject *_cffi_types, *_cffi_VerificationError;

static int _cffi_setup_custom(PyObject *lib);   /* forward */

static PyObject *_cffi_setup(PyObject *self, PyObject *args)
{
    PyObject *library;
    int was_alive = (_cffi_types != NULL);
    (void)self; /* unused */
    if (!PyArg_ParseTuple(args, "OOO", &_cffi_types, &_cffi_VerificationError,
                                       &library))
        return NULL;
    Py_INCREF(_cffi_types);
    Py_INCREF(_cffi_VerificationError);
    if (_cffi_setup_custom(library) < 0)
        return NULL;
    return PyBool_FromLong(was_alive);
}

static int _cffi_init(void)
{
    PyObject *module, *c_api_object = NULL;

    module = PyImport_ImportModule("_cffi_backend");
    if (module == NULL)
        goto failure;

    c_api_object = PyObject_GetAttrString(module, "_C_API");
    if (c_api_object == NULL)
        goto failure;
    if (!PyCapsule_CheckExact(c_api_object)) {
        PyErr_SetNone(PyExc_ImportError);
        goto failure;
    }
    memcpy(_cffi_exports, PyCapsule_GetPointer(c_api_object, "cffi"),
           _CFFI_NUM_EXPORTS * sizeof(void *));

    Py_DECREF(module);
    Py_DECREF(c_api_object);
    return 0;

  failure:
    Py_XDECREF(module);
    Py_XDECREF(c_api_object);
    return -1;
}

#define _cffi_type(num) ((CTypeDescrObject *)PyList_GET_ITEM(_cffi_types, num))

/**********/



#include <sys/mman.h>

void *offset(void *mapped, size_t offset) {
    return (void*)((char*)mapped + offset);
}


static PyObject *
_cffi_f_mmap(PyObject *self, PyObject *args)
{
  void * x0;
  size_t x1;
  int x2;
  int x3;
  int x4;
  size_t x5;
  Py_ssize_t datasize;
  void * result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;
  PyObject *arg4;
  PyObject *arg5;

  if (!PyArg_ParseTuple(args, "OOOOOO:mmap", &arg0, &arg1, &arg2, &arg3, &arg4, &arg5))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, size_t);
  if (x1 == (size_t)-1 && PyErr_Occurred())
    return NULL;

  x2 = _cffi_to_c_int(arg2, int);
  if (x2 == (int)-1 && PyErr_Occurred())
    return NULL;

  x3 = _cffi_to_c_int(arg3, int);
  if (x3 == (int)-1 && PyErr_Occurred())
    return NULL;

  x4 = _cffi_to_c_int(arg4, int);
  if (x4 == (int)-1 && PyErr_Occurred())
    return NULL;

  x5 = _cffi_to_c_int(arg5, size_t);
  if (x5 == (size_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = mmap(x0, x1, x2, x3, x4, x5); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(0));
}

static PyObject *
_cffi_f_offset(PyObject *self, PyObject *args)
{
  void * x0;
  size_t x1;
  Py_ssize_t datasize;
  void * result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:offset", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(0), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, size_t);
  if (x1 == (size_t)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = offset(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(0));
}

static int _cffi_const_MAP_ANONYMOUS(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_ANONYMOUS);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_ANONYMOUS", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return ((void)lib,0);
}

static int _cffi_const_MAP_FIXED(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_FIXED);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_FIXED", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_ANONYMOUS(lib);
}

static int _cffi_const_MAP_GROWSDOWN(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_GROWSDOWN);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_GROWSDOWN", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_FIXED(lib);
}

static int _cffi_const_MAP_HUGETLB(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_HUGETLB);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_HUGETLB", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_GROWSDOWN(lib);
}

static int _cffi_const_MAP_LOCKED(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_LOCKED);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_LOCKED", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_HUGETLB(lib);
}

static int _cffi_const_MAP_NONBLOCK(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_NONBLOCK);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_NONBLOCK", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_LOCKED(lib);
}

static int _cffi_const_MAP_NORESERVE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_NORESERVE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_NORESERVE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_NONBLOCK(lib);
}

static int _cffi_const_MAP_POPULATE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_POPULATE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_POPULATE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_NORESERVE(lib);
}

static int _cffi_const_MAP_PRIVATE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_PRIVATE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_PRIVATE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_POPULATE(lib);
}

static int _cffi_const_MAP_SHARED(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_SHARED);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_SHARED", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_PRIVATE(lib);
}

static int _cffi_const_MAP_STACK(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(MAP_STACK);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "MAP_STACK", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_SHARED(lib);
}

static int _cffi_const_PROT_EXEC(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(PROT_EXEC);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "PROT_EXEC", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_MAP_STACK(lib);
}

static int _cffi_const_PROT_NONE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(PROT_NONE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "PROT_NONE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_PROT_EXEC(lib);
}

static int _cffi_const_PROT_READ(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(PROT_READ);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "PROT_READ", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_PROT_NONE(lib);
}

static int _cffi_const_PROT_WRITE(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(PROT_WRITE);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "PROT_WRITE", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_PROT_READ(lib);
}

static int _cffi_setup_custom(PyObject *lib)
{
  return _cffi_const_PROT_WRITE(lib);
}

static PyMethodDef _cffi_methods[] = {
  {"mmap", _cffi_f_mmap, METH_VARARGS, NULL},
  {"offset", _cffi_f_offset, METH_VARARGS, NULL},
  {"_cffi_setup", _cffi_setup, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}    /* Sentinel */
};

#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef _cffi_module_def = {
  PyModuleDef_HEAD_INIT,
  "_cffi__xfcef0ea4xcd632ac9",
  NULL,
  -1,
  _cffi_methods,
  NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit__cffi__xfcef0ea4xcd632ac9(void)
{
  PyObject *lib;
  lib = PyModule_Create(&_cffi_module_def);
  if (lib == NULL)
    return NULL;
  if (((void)lib,0) < 0 || _cffi_init() < 0) {
    Py_DECREF(lib);
    return NULL;
  }
  return lib;
}

#else

PyMODINIT_FUNC
init_cffi__xfcef0ea4xcd632ac9(void)
{
  PyObject *lib;
  lib = Py_InitModule("_cffi__xfcef0ea4xcd632ac9", _cffi_methods);
  if (lib == NULL)
    return;
  if (((void)lib,0) < 0 || _cffi_init() < 0)
    return;
  return;
}

#endif
