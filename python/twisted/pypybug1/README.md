1.
Install the following under PyPy (a regular "pypy setup.py install" will do it)

http://pypi.python.org/packages/source/z/zope.interface/zope.interface-3.8.0.tar.gz
http://pypi.python.org/packages/source/T/Twisted/Twisted-12.1.0.tar.bz2

2.
Run

~/pypy-1.9/bin/pypy testcase.py pool ssl

3.
Open a browser

https://192.168.1.141:8090/

replacing the IP for your machine.

=> This will lock up the program on Linux, abort on FreeBSD.

=> CPython will work ..

If you remove either "pool" or "ssl" from the command line it will work on PyPy.

Note that I already added the 2 tricks:

 _ssl.py file
 import socket at the very beginning


 These make i.e. testcase4.py work, but NOT testcase1.py.


 ====



Here is the problem:

      [autobahn@office-autobahnws-1 ~/scm/scratchbox/python/twisted/pypybug1]$ python -V
      Python 2.7.3
      [autobahn@office-autobahnws-1 ~/scm/scratchbox/python/twisted/pypybug1]$ pypy -V
      Python 2.7.2 (124c48df1aab, Apr 10 2012, 12:54:44)
      [PyPy 1.9.1-dev0 with GCC 4.2.1]
      [autobahn@office-autobahnws-1 ~/scm/scratchbox/python/twisted/pypybug1]$ python testcase4.py
      foo() begin
      import and create SSL begin
      import and create SSL end
      foo() end
      [autobahn@office-autobahnws-1 ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase4.py
      foo() begin
      import and create SSL begin
      Fatal error: pthread_mutex_lock(&mutex_gil)
      Abort trap: 6
      [autobahn@office-autobahnws-1 ~/scm/scratchbox/python/twisted/pypybug1]$
