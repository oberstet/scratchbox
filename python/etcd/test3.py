from pprint import pprint

from twisted.internet.defer import succeed, inlineCallbacks
from twisted.internet.task import react

from autobahn.twisted.util import sleep

import treq

@inlineCallbacks
def main(reactor):
    data = b'{"create_request": {"key": "Zm9v"} }'
    response = yield treq.post('http://localhost:2379/v3alpha/watch', data=data)

    if response.code != 200:
        raise Exception('watch call returned with {}'.format(response.code))

    if True:
        result = yield response.json()
        pprint(result)
    else:
        def process(data):
            print(data)

        treq.collect(response, process)

        yield sleep(300)

react(main)

# curl http://localhost:2379/v3alpha/watch -X POST -d '{"create_request": {"key":"Zm9v"}}'
