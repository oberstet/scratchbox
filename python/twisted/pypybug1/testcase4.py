from OpenSSL import SSL
import sys, os, thread, time

if 'imp' in sys.argv:
   print "importing socket"
   import socket
else:
   print "no socket imported"


def print_time():
   count = 0
   while count < 5:
      time.sleep(1)
      count += 1
      print count

thread.start_new_thread(print_time, ())

ctx = SSL.Context(SSL.SSLv23_METHOD)
