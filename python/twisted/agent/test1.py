from pprint import pformat

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, HTTPConnectionPool, _HTTP11ClientFactory, HTTP11ClientProtocol
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


class HTTP11ClientProtocolPatched(HTTP11ClientProtocol):

    def request(self, request):
        if self._state != 'QUIESCENT':
            return fail(RequestNotSent())

        self._state = 'TRANSMITTING'
        _requestDeferred = maybeDeferred(request.writeTo, self.transport)

        def cancelRequest(ign):
            if self.timedOut:
                # Request timeout was hit
                self._giveUp(Failure(TimeoutError("Request took longer than %s seconds" % request.timeout)))
            else:
                # Explicitly cancel the request's deferred if it's still trying to
                # write when this request is cancelled.
                if self._state in ('TRANSMITTING', 'TRANSMITTING_AFTER_RECEIVING_RESPONSE'):
                    _requestDeferred.cancel()
                else:
                    self._giveUp(Failure(CancelledError()))
        self._finishedRequest = Deferred(cancelRequest)

        if self.timeout > 0:
            self.timedOut = False
            def timeout():
                self.timedOut = True
                self._finishedRequest.cancel()
            td = reactor.callLater(self.timeout, timeout)
            #td.cancel()
            #self._finishedRequest.addBoth(td.cancel) # where/how to cancel?

        # Keep track of the Request object in case we need to call stopWriting
        # on it.
        self._currentRequest = request

        self._transportProxy = TransportProxyProducer(self.transport)
        self._parser = HTTPClientParser(request, self._finishResponse)
        self._parser.makeConnection(self._transportProxy)
        self._responseDeferred = self._parser._responseDeferred

        def cbRequestWrotten(ignored):
            if self._state == 'TRANSMITTING':
                self._state = 'WAITING'
                self._responseDeferred.chainDeferred(self._finishedRequest)

        def ebRequestWriting(err):
            if self._state == 'TRANSMITTING':
                self._state = 'GENERATION_FAILED'
                self.transport.loseConnection()
                self._finishedRequest.errback(
                    Failure(RequestGenerationFailed([err])))
            else:
                log.err(err, 'Error writing request, but not in valid state '
                             'to finalize request: %s' % self._state)

        _requestDeferred.addCallbacks(cbRequestWrotten, ebRequestWriting)

        return self._finishedRequest


class _HTTP11ClientFactoryPatched(_HTTP11ClientFactory):
   def buildProtocol(self, addr):
      proto =  HTTP11ClientProtocolPatched(self._quiescentCallback)
      proto.timeout = 2 #self.timeout
      return proto


pool = HTTPConnectionPool(reactor, True)
pool._factory = _HTTP11ClientFactoryPatched
pool.timeout = 2


agent = Agent(reactor, connectTimeout = 2, pool = pool)
#agent = Agent(reactor)

d = agent.request(
   'GET',
   'http://192.168.1.141/test1/php/api.php',
   Headers({'User-Agent': ['Twisted Web Client Example']}),
   None)

#reactor.callLater(2, d.cancel)


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
