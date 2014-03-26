import sys, threading
from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


log.startLogging(sys.stdout)

def foo(tid):
   print("Main thread {} called from thread {}".format(threading.current_thread().ident, tid))

def application(environ, start_response):
   tid = threading.current_thread().ident
   print("Request on thread: {}".format(tid))
   reactor.callFromThread(foo, tid)
   start_response('200 OK', [('Content-type', 'text/plain')])
   return ['Hello, world!']

resource = WSGIResource(reactor, reactor.getThreadPool(), application)
site = Site(resource)
site.log = lambda _: None
reactor.listenTCP(8080, site)
print("Maint thread: {}".format(threading.current_thread().ident))
reactor.run()
