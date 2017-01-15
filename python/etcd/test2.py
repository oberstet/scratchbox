import os
import random
import json
import binascii
from pprint import pprint

from twisted.internet.defer import succeed, inlineCallbacks, returnValue
from twisted.internet.task import react

import txaio
txaio.use_twisted()

from autobahn.twisted.util import sleep

import treq


class Etcd(object):

    ACTION_CREATE = 'create'
    ACTION_MODIFY = 'modify'
    ACTION_DELETE = 'delete'

    log = txaio.make_logger()

    def __init__(self, prefix, hosts=['http://localhost:2379']):
        self._prefix = prefix
        self._hosts = hosts

    def _select_host(self):
        return random.choice(self._hosts)

    @inlineCallbacks
    def set(self, key, value):
        value_serialized = json.dumps(value).encode()
        response = yield treq.put('{}/v2/keys/{}/{}'.format(self._select_host(), self._prefix, key),
                                  data={'value': value_serialized},
                                  headers={'Content-Type': ['application/x-www-form-urlencoded']})
        if response.code != 200:
            pass
        print(response.code)

    @inlineCallbacks
    def get(self, key):
        response = yield treq.get('{}/v2/keys/{}/{}'.format(self._select_host(), self._prefix, key))
        result = yield response.json()
        if 'errorCode' in result:
            if result['errorCode'] == 100:
                # key not found
                returnValue(None)
            else:
                self.log.warn('etcd get(): unprocessed error code {error_code}', error_code=errorCode)
        else:
            returnValue(result['node']['value'])

    @inlineCallbacks
    def watch(self, key, callback):
        while True:
            try:
                response = yield treq.get('{}/v2/keys/{}/{}'.format(self._select_host(), self._prefix, key), params={'wait': 'true', 'recursive': 'true'})
                if response.code == 200:
                    result = yield response.json()
                    if result['action'] == 'set':
                        if 'prevNode' in result:
                            if result['node']['value'] != result['prevNode']['value']:
                                callback(result['node']['key'], self.ACTION_MODIFY, result['node']['value'])
                            else:
                                # value unchanged!
                                pass
                        else:
                            callback(result['node']['key'], self.ACTION_CREATE, result['node']['value'])
                    elif result['action'] == 'delete':
                        callback(result['node']['key'], self.ACTION_DELETE, None)
                    else:
                        self.log.warn('etcd watch returned with unknown action "{action}"', action=result['action'])
                else:
                    self.log.warn('etcd watch returned with status code != 200 ({status_code})', status_code=response.code)
            except Exception:
                self.log.failure('{log_failure.value}')


@inlineCallbacks
def main(reactor, etcd):
#    key = u'test'
#
#    value_got = yield etcd.get(key)
#    print(type(value_got))
#    pprint(value_got)
#
#    value_set = binascii.b2a_hex(os.urandom(10)).decode()
#    yield etcd.set(key, value_set)
#
#    value_got = yield etcd.get(key)
#    print(type(value_got))
#    pprint(value_got)

    def on_change(key, action, value):
        print(key, action, value)

    key = ''
    etcd.watch(key, on_change)

    yield sleep(300)

etcd = Etcd('fabric')
react(main, (etcd,))
