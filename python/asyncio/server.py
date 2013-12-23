import asyncio
import math
import json

class MathServer(asyncio.Protocol):

   @asyncio.coroutine
   def slow_sqrt(self, x):
      yield from asyncio.sleep(1)
      return math.sqrt(x)

   def fast_sqrt(self, x):
      return math.sqrt(x)

   def connection_made(self, transport):
      self.transport = transport

   #@asyncio.coroutine
   def data_received(self, data):
      print('data received: {}'.format(data.decode()))
      x = json.loads(data.decode())
      res = self.fast_sqrt(x)
      #res = yield from self.slow_sqrt(x)
      self.transport.write(json.dumps(res).encode('utf8'))
      self.transport.close()


loop = asyncio.get_event_loop()
coro = loop.create_server(MathServer, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
print('serving on {}'.format(server.sockets[0].getsockname()))

try:
   loop.run_forever()
except KeyboardInterrupt:
   print("exit")
finally:
   server.close()
   loop.close()
