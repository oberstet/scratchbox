from pprint import pprint

from twisted.internet.defer import succeed, inlineCallbacks
from twisted.internet.task import react

import treq

@inlineCallbacks
def main(reactor, key):
    response = yield treq.get('http://localhost:2379/v2/keys/{}'.format(key))
    result = yield response.json()
    pprint(result)

react(main, ('test',))
