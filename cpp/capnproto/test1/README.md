# Cap’n Proto

* https://capnproto.org/cxx.html

# cppyy

You need a gcc 4.9 toolchain!

* http://doc.pypy.org/en/latest/cppyy.html#installation
* https://bitbucket.org/pypy/pypy/issues/2467/cpppypy-fails-to-build-on-gcc-5-and-clang

## Test

```console
export CPPYYHOME=${HOME}/pypy-5.6-linux_x86_64-portable/site-packages/cppyy_backend
export LD_LIBRARY_PATH=${CPPYYHOME}/lib:${LD_LIBRARY_PATH}
export PATH=${CPPYYHOME}/bin:${PATH}
```

Now build the library:

```console
genreflex MyClass.h
g++-4.9 -std=c++11 -fPIC -rdynamic -O2 -shared -I$CPPYYHOME/include MyClass_rflx.cpp -o libMyClassDict.so -L$CPPYYHOME/lib -lCling
```

Check that the library has no unresolved deps/symbols:

```console
ldd libMyClassDict.so
nm libMyClassDict.so | grep " U "
```

Then

```console
export LD_LIBRARY_PATH=${PWD}:${LD_LIBRARY_PATH}
export PATH=${HOME}/pypy-5.6-linux_x86_64-portable/bin:${PATH}
```

and test:

```console
pypy MyClass.py
```
