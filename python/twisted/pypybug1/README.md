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
