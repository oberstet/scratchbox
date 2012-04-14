from OpenSSL import SSL
import sys, thread

if 'imp' in sys.argv:
   print "importing socket"
   import socket
else:
   print "no socket imported"


def foo():
   return

thread.start_new_thread(foo, ())

ctx = SSL.Context(SSL.SSLv23_METHOD)
