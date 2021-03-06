from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep

import etcd
import txaio


@inlineCallbacks
def main(reactor):

    # a Twisted etcd client
    client = etcd.Client(reactor, u'http://localhost:2379')

    # get etcd status
    status = yield client.status()
    print(status)

    # get value for a key
    try:
        value = yield client.get(b'/cf/foo')
        print('value={}'.format(value))
    except IndexError:
        print('no such key =(')

    # set a value for some keys
    for i in range(3):
        rev = yield client.set('/cf/foo0{}'.format(i).encode(), b'woa;)')
        print('value set, revision={}'.format(rev))

    # delete key
    key = u'/cf/foo02'.encode()
    rev = yield client.delete(key)
    print(rev)

    # iterate over key range (maybe an async iter in the future?)
    pairs = yield client.get(b'/cf/foo01', b'/cf/foo05')
    for key, value in pairs.items():
        print('key={}: {}'.format(key, value))

    # iterate over keys with given prefix
    pairs = yield client.get(b'/cf/foo0', prefix=True)
    for key, value in pairs.items():
        print('key={}: {}'.format(key, value))

    # watch keys for change events
    prefixes = [b'/cf/', b'/foo/']

    # our callback that will be invoked for every change event
    def on_watch(key, value):
        print('watch callback fired for key {}: {}'.format(key, value))

    # start watching on given key prefixes
    d = client.watch(prefixes, on_watch)

    # sleep for n seconds ..
    delay = 10
    print('watching {} for {} seconds ..'.format(prefixes, delay))
    yield sleep(delay)

    # .. and stop watching
    yield d.cancel()

    # submit transaction

    # create lease

if __name__ == '__main__':
    txaio.start_logging(level='info')
    react(main)
