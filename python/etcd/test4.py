from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
import etcd


@inlineCallbacks
def main(reactor):
    # etcd client
    client = etcd.Client(reactor, b'http://localhost:2379')

    # get a key
    value = yield client.get(b'/foo/bar')
    print(value)

    # iterate over key range

    # watch keys for change events
    prefixes = [b'/cf/', b'/foo/']

    # our callback that will be invoked for every change event
    def on_watch(key, value):
        print(key, value)

    d = client.start_watching(prefixes, on_watch)

    # sleep for 10 seconds and cancel watching
    yield sleep(10)
    yield d.cancel()

    # submit transaction

react(main)
