from cffi import FFI
ffi = FFI()
 
 # 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW'


ffi.dlopen(None, ffi.RTLD_GLOBAL)
# I am running into https://lists.freebsd.org/pipermail/svn-src-head/2014-March/056553.html

ffi.dlopen("libelf.so", ffi.RTLD_GLOBAL)

ffi.dlopen("libz.so", ffi.RTLD_GLOBAL)
 
# this is the lib I need to load ..
ffi.dlopen("libctf.so", ffi.RTLD_GLOBAL)


ffi.dlopen("librtld_db.so", ffi.RTLD_GLOBAL | ffi.RTLD_LAZY)

ffi.dlopen("libproc.so", ffi.RTLD_GLOBAL)


print ffi.dlopen("librtld_db.so") 
