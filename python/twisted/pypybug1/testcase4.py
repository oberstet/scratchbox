import thread
import socket
import time

def foo():
   print "foo() begin"
   time.sleep(2)
   print "foo() end"

thread.start_new_thread(foo, ())

time.sleep(1)

print "import and create SSL begin"

from OpenSSL import SSL
ctx = SSL.Context(SSL.SSLv23_METHOD)

print "import and create SSL end"

time.sleep(2)
