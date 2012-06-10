from OpenSSL import SSL
import socket
import thread
thread.start_new_thread(lambda *x: None, ())
SSL.Context(SSL.SSLv23_METHOD)

