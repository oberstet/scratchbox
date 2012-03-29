Embedded Key-Value Stores Random Insert Performance
===================================================

Objective
---------

Compare the random insert performance of embedded Python databases
that provide (at least) an ordered mapping from string keys to
string values.


Caveat
------

This is not polished code. This is just a "data point" - ie. there
are many pitfalls when doing performance measurements with databases.
There are likely flaws.


Contestants
-----------

 * SQLite3
 * LevelDB
 * ZODB


Test Setup
----------

 * Physical Host:
   * (R)INTEL (R)Core i7 Quad, 3.4 GHz, 12GB RAM
   * Win7 64 Bit Prof.
   * (R)Oracle (R)VirtualBox 4.1.10

 * VM1:
   * Ubuntu 10.04 LTS 32 Bit
   * Python 2.7.2 stock (built from source)
   * PyPy 1.8 release (rebuilt from PyPy site)
   * 2GB RAM, 2 Cores

 * VM2:
   * FreeBSD 9 i386
   * Python 2.7.2 stock (built from source)
   * PyPy 1.8.1-dev (built from repo)
   * 2GB RAM, 2 Cores


Testing
-------

Was driven by the shell script

    test.sh

Code should be easy to find / follow from there.


Results
-------

See the results subfolder.

Discussion: tbd.


py-LevelDB
----------

I was using http://code.google.com/p/py-leveldb which is a CPython-API based
wrapper for LevelDB that uses the native C++ API of LevelDB.

Building.

    svn checkout http://py-leveldb.googlecode.com/svn/trunk/ py-leveldb-read-only
    cd py-leveldb-read-only
    ./compile_leveldb.sh
    python setup.py build
    python setup.py install
