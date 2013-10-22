import os, sys, time

# http://twistedmatrix.com/documents/current/core/examples/#auto10
# http://twistedmatrix.com/trac/ticket/4387
# http://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor
# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-in-python
# https://pypi.python.org/pypi/affinity


if True:

   from twisted.internet import protocol
   from twisted.internet import reactor
   
   f = open("test.log", 'w')
   fds = [f, sys.stdout]

   def loop():
      try:
         msg = "loop %d %d\n" % (os.getpid(), os.getppid())
         for fd in fds:
            fd.write(msg)
            fd.flush()
      except Exception, e:
         f.write("EXCEPTION" + str(e))
         f.write("closed")
         f.close()
         reactor.stop()
      else:
         reactor.callLater(1, loop)
      
   loop()
   reactor.run()

else:

   f = open("test.log", 'w')
   fds = [f, sys.stdout]
   try:
      while True:
         msg = "loop %d %d\n" % (os.getpid(), os.getppid())
         for fd in fds:
            fd.write(msg)
            fd.flush()
         #print "loop %d %d" % (os.getpid(), os.getppid())
         time.sleep(1)
   except Exception, e:
      f.write("EXCEPTION" + str(e))
   finally:
      f.write("closed")
      f.close()
      
