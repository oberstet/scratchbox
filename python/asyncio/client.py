import asyncio
import json
import random

class MathClient(asyncio.Protocol):

   def connection_made(self, transport):

      loop = asyncio.get_event_loop()
      
      def ask():
         value = random.random()
         transport.write(json.dumps(value).encode('utf8'))
         loop.call_later(1, ask)

      ask()

   def data_received(self, data):
      print('data received: {}'.format(data.decode()))

   def connection_lost(self, exc):
      asyncio.get_event_loop().stop()


loop = asyncio.get_event_loop()
coro = loop.create_connection(MathClient, '127.0.0.1', 8888)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
