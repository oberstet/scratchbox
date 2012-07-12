from pprint import pformat

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

class BeginningPrinter(Protocol):
   def __init__(self, finished):
      self.finished = finished
      self.remaining = 1024 * 10

   def dataReceived(self, bytes):
      if self.remaining:
         display = bytes[:self.remaining]
         print 'Some data received:'
         print display
         self.remaining -= len(display)

   def connectionLost(self, reason):
      print 'Finished receiving body:', reason.getErrorMessage()
      self.finished.callback(None)

agent = Agent(reactor, connectTimeout = 2)
#agent = Agent(reactor)

d = agent.request(
   'GET',
   'http://192.168.1.141/test1/php/api.php',
   Headers({'User-Agent': ['Twisted Web Client Example']}),
   None)

def cbRequest(response):
   print 'Response version:', response.version
   print 'Response code:', response.code
   print 'Response phrase:', response.phrase
   print 'Response headers:'
   print pformat(list(response.headers.getAllRawHeaders()))
   finished = Deferred()
   response.deliverBody(BeginningPrinter(finished))
   return finished

d.addCallback(cbRequest)

def cbShutdownOk(ignored):
   reactor.stop()

def cbShutdownError(e):
   print str(e)
   reactor.stop()

#connectTimeout

d.addCallbacks(cbShutdownOk, cbShutdownError)

reactor.run()
