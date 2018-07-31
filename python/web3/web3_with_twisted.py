import sys
import time
import argparse

import web3
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

from twisted.internet import defer, task
from twisted.internet.threads import deferToThread
from twisted.internet.task import LoopingCall

# this is sleeping without blocking, other than the stdlib time.sleep()
from autobahn.twisted.util import sleep


# contract source (just for completeness .. already deployed)
contract_source = """
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
"""

# above is deployed here:
contract_address = '0x31bd34ef7dbd96a20098b7a5aaf67a45bbef2726'
contract_address = Web3.toChecksumAddress(contract_address)

# here is the ABI of the contract:
abi = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "greeting",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
"""

#abi = json.loads(abi)


def tick(c):
    sys.stdout.write(c)
    sys.stdout.flush()


def greet(w3):
    contract_instance = w3.eth.contract(address=contract_address, abi=abi, ContractFactoryClass=ConciseContract)
    value = contract_instance.greet()
    return value


@defer.inlineCallbacks
def main(reactor, w3, enable_threadpool=True):
    print('main starting ..')

    # start a looping call: our code will run every 50ms
    c1 = LoopingCall(tick, '.')
    c1.start(.05)

    # start a looping call: our code will run every 75ms
    c2 = LoopingCall(tick, '*')
    c2.start(.075)

    yield sleep(2)

    # do a bunch of contract calls (read-only)
    print('starting contract calls loop ..')
    i = 0
    while i < 6:
        started = time.time()

        if enable_threadpool:
            value = yield deferToThread(greet, w3)
        else:
            value = greet(w3)

        ended = time.time()
        ms = int(1000. * (ended - started))
        i += 1
        print('request {} returned {} in {} ms'.format(i, value, ms))

    print('contract calls loop ended')

    # we let the looping call run for another 2s. note that this sleep()
    # is NOT the stdlib time.sleep(), which is criticial (as we must not block
    # the reactor). this also shows, that even if we ran this test
    # with enable_threadpool=False, as soon as the blocking is resolved (the HTTP request
    # coming back), our stuff will run again asynchronously and concurrently as expected.
    yield sleep(2)
    yield c1.stop()
    yield sleep(1)
    yield c2.stop()

    print('main ended')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--blocked', dest='blocked', action='store_true')
    args = parser.parse_args()

    # provider that will issue HTTPS requests to
    # Infura's Ropsten testnet JSON-RPC HTTP gateway
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io'))

    # run our main function under the default Twisted event reactor
    task.react(main, (w3, not args.blocked))
