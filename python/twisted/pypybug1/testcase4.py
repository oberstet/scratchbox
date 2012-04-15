from OpenSSL import SSL
import thread
import socket

def foo():
   return

thread.start_new_thread(foo, ())

ctx = SSL.Context(SSL.SSLv23_METHOD)
