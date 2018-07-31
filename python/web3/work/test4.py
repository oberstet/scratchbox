import os
import time

from web3.auto.infura import w3

# web3.eth.gasPrice

print("PID={}".format(os.getpid()))

blocks = []

for i in range(240):
    b = w3.eth.getBlock("latest")
    blocks.append(b)
    print('latest block retrieved ..')
    time.sleep(1)
