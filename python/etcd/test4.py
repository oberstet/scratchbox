from zope.interface import implements

from twisted.web.iweb import IBodyProducer, UNKNOWN_LENGTH
from twisted.internet import defer
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
import urllib

from twisted.internet.task import react

from autobahn.twisted.util import sleep

from twisted.internet.defer import succeed, inlineCallbacks
from twisted.internet.task import react

from autobahn.twisted.util import sleep

from twisted.internet import protocol


class StringProducer(object):
    #implements(IBodyProducer)

    length = UNKNOWN_LENGTH

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        print('start producing')
        consumer.write(self.body)
        #return defer.succeed(None)
        return defer.Deferred()

    def pauseProducing(self):
        print('pause producing')
        pass

    def stopProducing(self):
        print('stop producing')
        pass

def httpRequest(reactor, url, values={}, headers={}, method='POST'):
    # Construct an Agent.
    agent = Agent(reactor)
    #data = urllib.urlencode(values)
    data = b'{"create_request": {"key": "Zm9v"} }'

    d = agent.request(method,
                      url,
                      Headers(headers),
                      StringProducer(data) if data else None)

    def handle_response(response):
        if response.code == 204:
            d = defer.succeed('')
        else:
            class SimpleReceiver(protocol.Protocol):
                def __init__(s, d):
                    s.buf = ''; s.d = d
                def dataReceived(s, data):
                    s.buf += data
                    print(data)
                def connectionLost(s, reason):
                    # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
                    s.d.callback(s.buf)

            d = defer.Deferred()
            response.deliverBody(SimpleReceiver(d))
        return d

    d.addCallback(handle_response)
    return d

@inlineCallbacks
def main(reactor):
    data = b'{"create_request": {"key": "Zm9v"} }'
    url = b'http://localhost:2379/v3alpha/watch'

    yield httpRequest(reactor, url)
#        "http://...",
#        {
#            'query_arg': 'value',
#        },
#        headers={'Content-Type': ['application/x-www-form-urlencoded']}
#    )
    #yield sleep(300)

react(main)


