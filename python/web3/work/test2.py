from web3.auto.infura import w3
#from web3.auto import w3

print(w3.isConnected())
print(w3.eth.getBlock('latest'))
