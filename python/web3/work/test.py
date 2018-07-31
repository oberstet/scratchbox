import asyncio
from web3.auto import w3


async def printlast():
    last = await w3.eth.getBlock('latest')
    print(last)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(printlast())
    #loop.run_forever()
    loop.close()
