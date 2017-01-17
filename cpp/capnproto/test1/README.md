# Cap’n Proto

* https://capnproto.org/cxx.html

# cppyy

You need a gcc 4.9 toolchain!

* http://doc.pypy.org/en/latest/cppyy.html#installation
* https://bitbucket.org/pypy/pypy/issues/2467/cpppypy-fails-to-build-on-gcc-5-and-clang

## Test

See: http://doc.pypy.org/en/latest/cppyy.html#basic-bindings-example

```console
export CPPYYHOME=${HOME}/pypy-5.6-linux_x86_64-portable/site-packages/cppyy_backend
export LD_LIBRARY_PATH=${CPPYYHOME}/lib:${LD_LIBRARY_PATH}
export PATH=${CPPYYHOME}/bin:${PATH}
```

Now build the library:

```console
which genreflex
genreflex MyClass.h
clang++ -std=c++11 -fPIC -rdynamic -O2 -shared -I$CPPYYHOME/include MyClass_rflx.cpp -o libMyClassDict.so -L$CPPYYHOME/lib -lCling
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

## Another try

```console
cd /tmp
wget https://pypi.python.org/packages/e7/5d/d371630d8268545450f8b0cdd0671d048f7996ad1819a1d2b45404e3fd5a/PyPy-cppyy-backend-6.6.9.0.tar.gz#md5=eacdd3becafc9b77b4b3121936c32c42
tar xvf PyPy-cppyy-backend-6.6.9.0.tar.gz
cd PyPy-cppyy-backend-6.6.9.0
```

Now edit `src/backend/cppyy/src/clingcwrapper.cxx` and change line 525 from

```cpp
cppresult->std::string::~string();
```

to

```cpp
cppresult->std::string::~basic_string();
```

and change line 715

to

```cpp
std::cerr << "Warning: " << msg.str() << '\n';
```

Then

```console
CC=`which clang` \
CXX=`which clang++` \
CXXFLAGS="-std=c++11" \
MAKE_NPROCS=4 \
~/pypy-5.6-linux_x86_64-portable/bin/pip install --no-cache-dir --verbose .
```

If everything runs well (and this takes like 10-15min):

```console
...
    -- Set runtime path of "/home/oberstet/pypy-5.6-linux_x86_64-portable/site-packages/cppyy_backend/lib/libcppyy_backend.so" to ""
    install finished
done
  Removing source in /tmp/pip-YrtrlD-build
Successfully installed PyPy-cppyy-backend-6.6.9.0
Cleaning up...
oberstet@thinkpad-t430s:~/scm/oberstet/scratchbox/cpp/capnproto/test1/PyPy-cppyy-backend-6.6.9.0$
```
