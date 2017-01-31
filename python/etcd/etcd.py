from __future__ import print_function

import json

from pprint import pprint

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

from twisted.web.client import HTTPConnectionPool

from twisted.internet.defer import Deferred

import binascii

import binascii
from twisted.web.client import HTTPConnectionPool

from twisted.web.iweb import IBodyProducer, UNKNOWN_LENGTH
from twisted.internet import defer
from twisted.web.client import Agent
from twisted.web.http_headers import Headers


def increment_last_byte(byte_string):
    s = bytearray(byte_string)
    s[-1] = s[-1] + 1
    return bytes(s)


class EtcdSender(object):

    length = UNKNOWN_LENGTH

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return defer.succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass


class EtcdReceiver(protocol.Protocol):
    def __init__(self, cb, done=None):
        self._buf = ''
        self._cb = cb
        self._done = done

    def dataReceived(self, data):
        self._buf += data
        while True:
            i = self._buf.find('\n')
            if i > 0:
                data = self._buf[:i]
                try:
                    obj = json.loads(data)
                except:
                    pass
                else:
                    for evt in obj['result'].get('events', []):
                        if 'kv' in evt:
                            d = evt['kv']

                            key = binascii.a2b_base64(d['key'])
                            value = binascii.a2b_base64(d['value'])
                            create_revision = d['create_revision']
                            mod_revision = d['mod_revision']
                            version = d['version']

                            self._cb(key, value)
                            #self._cb(evt['kv'])
                self._buf = self._buf[i + 1:]
            else:
                break

    def connectionLost(self, reason):
        # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
        if self._done:
            self._done.callback(reason)
            self._done = None



#self._session.register(self.set, u'crossbar.fabric.etcd.set')
#self._session.register(self.set, u'crossbar.fabric.etcd.run')

from twisted.internet.defer import CancelledError

class Client(object):

    def __init__(self, reactor, url, pool=None):
        self._url = url
        self._pool = pool or HTTPConnectionPool(reactor, persistent=True)
        self._agent = Agent(reactor, pool=self._pool)

    def start_watching(self, prefixes, on_watch):
        d = self._start_watching(prefixes, on_watch)

        def on_err(err):
            if isinstance(err.value, CancelledError):
                # swallow canceling!
                pass
            else:
                return err
        d.addErrback(on_err)

        return d

    def _start_watching(self, prefixes, on_watch):
        data = []
        headers = dict()
        url = b'{}/v3alpha/watch'.format(self._url)

        # create watches for all key prefixes
        for key in prefixes:
            range_end = increment_last_byte(key)
            obj = {
                'create_request': {
                    'progress_notify': True,
                    'key': binascii.b2a_base64(key),
                    'range_end': binascii.b2a_base64(range_end)
                }
            }
            data.append(json.dumps(obj).encode('utf8'))

        # HTTP/POST request in one go, but response is streaming ..
        d = self._agent.request('POST',
                                url,
                                Headers(headers),
                                EtcdSender(b'\n'.join(data)))

        def handle_response(response):
            if response.code == 204:
                done = defer.succeed('')
            else:
                done = defer.Deferred()
                response.deliverBody(EtcdReceiver(on_watch, done))
            return done

        d.addCallback(handle_response)
        return d

    def run_transaction(self, txn):
        pass

# Using LMDB as a persistent local cache for etcd
#
# The app is using LMDB API exclusively for read ops
# and etcd transactions directly to etcd for write ops.
#

#operator --> etcd --> (full replication) --> LMDB --> Python
