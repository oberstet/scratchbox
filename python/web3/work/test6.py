import time
import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

contract_address = '0x31bd34ef7dbd96a20098b7a5aaf67a45bbef2726'
contract_address = Web3.toChecksumAddress(contract_address)

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

abi = json.loads(abi)

# INFURA_API_KEY

#from web3.auto import w3
#from web3.auto.infura import w3

from web3 import Web3
web3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io'))

#print(w3.isConnected())
#print(w3.eth.getBlock('latest'))

# Contract instance in concise mode
#abi = contract_interface['abi']
contract_instance = web3.eth.contract(address=contract_address, abi=abi, ContractFactoryClass=ConciseContract)

i = 0
while True:
    started = time.time()
    value = contract_instance.greet()
    ended = time.time()
    i += 1
    ms = int(1000. * (ended - started))
    print('request {} returned {} in {} ms'.format(i, value, ms))

# Getters + Setters for web3.eth.contract object
#contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
#print('Setting value to: Nihao')
#print('Contract value: {}'.format(contract_instance.greet()))
