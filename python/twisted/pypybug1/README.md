The bug pops up when threads are used, and PyOpenSSL is used:


      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ pypy testcase3.py 8090 threads
      starting threads
      Fatal error: pthread_mutex_lock(&mutex_gil)
      Abort trap: 6




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


Here is the output of a patch PyPy


      [autobahn@autobahnws ~/scm/scratchbox/python/twisted/pypybug1]$ ~/pypy2/bin/pypy testcase.py ssl pool
      creating adbapi.ConnectionPool
      running SSL on 8090
      connection made
      Fatal error in RPyGilRelease: 1
      Abort trap: 6


The PyPy was patched to output the error code


      void RPyGilRelease(void)
      {
         int ret;
          _debug_print("RPyGilRelease\n");
      #ifdef RPY_ASSERT
          assert(pending_acquires >= 0);
      #endif
          assert_has_the_gil();
          ret = pthread_mutex_unlock(&mutex_gil);
          if (ret != 0) {
            fprintf(stderr, "Fatal error in RPyGilRelease: %d\n", ret);
            abort();
          }
          ASSERT_STATUS(pthread_cond_signal(&cond_gil));
      }
