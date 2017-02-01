from __future__ import print_function

import json
import binascii

from twisted.internet.defer import Deferred, succeed, inlineCallbacks, returnValue
from twisted.internet import protocol
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.iweb import IBodyProducer, UNKNOWN_LENGTH
from twisted.web.http_headers import Headers


__all__ = ('Value', 'Client')


def _increment_last_byte(byte_string):
    s = bytearray(byte_string)
    s[-1] = s[-1] + 1
    return bytes(s)


class _BufferedSender(object):

    length = UNKNOWN_LENGTH

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass


class _BufferedReceiver(protocol.Protocol):
    def __init__(self, done):
        self._buf = []
        self._done = done

    def dataReceived(self, data):
        self._buf.append(data)

    def connectionLost(self, reason):
        # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
        if self._done:
            self._done.callback(b''.join(self._buf))
            self._done = None


class _StreamingReceiver(protocol.Protocol):

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

                            try:
                                self._cb(key, value)
                            except Exception as e:
                                print('warning: swallowed exception in watch callback: {}'.format(e))
                self._buf = self._buf[i + 1:]
            else:
                break

    def connectionLost(self, reason):
        # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
        if self._done:
            self._done.callback(reason)
            self._done = None


class Value(object):
    """
    etcd rich value object.
    """

    def __init__(self, value, version=None, create_revision=None, mod_revision=None):
        """

        :param value: The actual value.
        :type value: bytes
        :param version:
        :type version:
        :param create_revision:
        :type create_revision:
        :param mod_revision:
        :type mod_revision
        """
        self.value = value
        self.version = version
        self.create_revision = create_revision
        self.mod_revision = mod_revision

    def __str__(self):
        return 'Value({}, version={}, create_revision={}, mod_revision{})'.format(self.value, self.version, self.create_revision, self.mod_revision)


class Client(object):
    """
    etcd client that talks to the gRPC endpoint of etcd v3.

    See: https://coreos.com/etcd/docs/latest/dev-guide/apispec/swagger/rpc.swagger.json
    """

    def __init__(self, reactor, url, pool=None):
        """

        :param rector:
        :type reactor:
        :param url:
        :type url:
        :param pool:
        :type pool:
        """
        self._url = url
        self._pool = pool or HTTPConnectionPool(reactor, persistent=True)
        self._agent = Agent(reactor, pool=self._pool)

    def get(self, key, range_end=None, prefix=None):
        """
        Retrieve value for key from etcd.

        :param key:
        :type key:
        :param range_end:
        :type range_end:
        :param prefix:
        :type prefix:
        """
        headers = dict()
        url = b'{}/v3alpha/kv/range'.format(self._url)

        obj = {
            'key': binascii.b2a_base64(key)
        }

        if not range_end and prefix is True:
            range_end = _increment_last_byte(key)

        if range_end:
            obj['range_end'] = binascii.b2a_base64(range_end)

        data = json.dumps(obj).encode('utf8')

        d = self._agent.request('POST',
                                url,
                                Headers(headers),
                                _BufferedSender(data))

        @inlineCallbacks
        def handle_response(response):
            if response.code == 200:
                body_received = Deferred()
                response.deliverBody(_BufferedReceiver(body_received))
                body = yield body_received
                obj = json.loads(body)
                count = int(obj.get('count', 0))
                if count == 0:
                    raise Exception('no such key')
                else:
                    if count > 1:
                        values = {}
                        for kv in obj['kvs']:
                            key = binascii.a2b_base64(kv['key'])
                            value = binascii.a2b_base64(kv['value'])
                            mod_revision = int(kv['mod_revision'])
                            create_revision = int(kv['create_revision'])
                            version = int(kv['version'])
                            values[key] = Value(value, version=version, create_revision=create_revision, mod_revision=mod_revision)
                        returnValue(values)
                    else:
                        kv = obj['kvs'][0]
                        value = binascii.a2b_base64(kv['value'])
                        mod_revision = int(kv['mod_revision'])
                        create_revision = int(kv['create_revision'])
                        version = int(kv['version'])
                        value = Value(value, version=version, create_revision=create_revision, mod_revision=mod_revision)
                        returnValue(value)
            else:
                print('unexpected response code {}'.format(response.code))

        d.addCallback(handle_response)
        return d

    def watch(self, prefixes, on_watch, start_revision=None):
        """
        Watch one or more key prefixes and invoke a callback.

        :param prefixes: The prefixes to watch.
        :type prefixes: list of bytes
        :param on_watch: The callback to invoke upon receiving a watch event.
        :type on_watch: callable
        :param start_revision: Watch beginning from this revision.
        :type start_revision: int
        """
        d = self._start_watching(prefixes, on_watch, start_revision)

        def on_err(err):
            if isinstance(err.value, CancelledError):
                # swallow canceling!
                pass
            else:
                return err
        d.addErrback(on_err)

        return d

    def _start_watching(self, prefixes, on_watch, start_revision):
        data = []
        headers = dict()
        url = b'{}/v3alpha/watch'.format(self._url)

        # create watches for all key prefixes
        for key in prefixes:
            range_end = _increment_last_byte(key)
            obj = {
                'create_request': {
                    'progress_notify': True,
                    'start_revision': start_revision,
                    'key': binascii.b2a_base64(key),
                    'range_end': binascii.b2a_base64(range_end)
                }
            }
            data.append(json.dumps(obj).encode('utf8'))

        # HTTP/POST request in one go, but response is streaming ..
        d = self._agent.request('POST',
                                url,
                                Headers(headers),
                                _BufferedSender(b'\n'.join(data)))

        def handle_response(response):
            if response.code == 204:
                done = succeed('')
            else:
                done = Deferred()
                response.deliverBody(_StreamingReceiver(on_watch, done))
            return done

        d.addCallback(handle_response)
        return d

    def submit(self, txn):
        """
        Submit a etcd transaction.
        """
        pass
