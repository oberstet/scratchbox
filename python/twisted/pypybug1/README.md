1.
Install the following under PyPy (a regular "pypy setup.py install" will do it)

   * http://pypi.python.org/packages/source/z/zope.interface/zope.interface-3.8.0.tar.gz

   * http://pypi.python.org/packages/source/T/Twisted/Twisted-12.1.0.tar.bz2

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

The file

  _ssl.py

and (additionally) this line at the very beginning

  import socket

 These make i.e. testcase4.py work, but NOT testcase1.py.
