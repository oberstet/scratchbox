The bug will only pop up when doing SSL _and_ adbapi.ConnectionPool

      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase.py
      no adbapi.ConnectionPool created
      running plain TCP on 8090
      connection made
      received:  300
      ^Cconnection lost
      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase.py ssl
      no adbapi.ConnectionPool created
      running SSL on 8090
      connection made
      received:  1
      received:  299
      ^Cconnection lost
      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase.py pool
      creating adbapi.ConnectionPool
      running plain TCP on 8090
      connection made
      received:  300
      ^Cconnection lost
      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase.py pool ssl
      creating adbapi.ConnectionPool
      running SSL on 8090
      connection made
      Fatal error: pthread_mutex_unlock(&mutex_gil)
      Abort trap: 6
      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$
