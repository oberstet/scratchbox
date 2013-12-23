import asyncio
import inspect
import math
import json
from collections import deque

class MathServer(asyncio.Protocol):

   @asyncio.coroutine
   def slow_sqrt(self, x):
      yield from asyncio.sleep(2)
      return math.sqrt(x)

   def fast_sqrt(self, x):
      return math.sqrt(x)

   def consume(self):
      while True:
         self.waiter = asyncio.Future()
         yield from self.waiter
         while len(self.receive_queue):
            data = self.receive_queue.popleft()
            if self.transport:
               try:
                  res = self.process(data)
                  if isinstance(res, asyncio.Future) or inspect.isgenerator(res):
                     res = yield from res
               except Exception as e:
                  print(e)

   def connection_made(self, transport):
      self.transport = transport
      self.receive_queue = deque()
      asyncio.Task(self.consume())

   def data_received(self, data):
      self.receive_queue.append(data)
      if not self.waiter.done():
         self.waiter.set_result(None)
      print("data_received {} {}".format(len(data), len(self.receive_queue)))

   def process(self, data):
      x = json.loads(data.decode())
      #res = self.fast_sqrt(x)
      res = yield from self.slow_sqrt(x)
      self.transport.write(json.dumps(res).encode('utf8'))
      #self.transport.close()

   def connection_lost(self, exc):
      self.transport = None


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
