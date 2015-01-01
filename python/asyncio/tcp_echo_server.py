try:
   import asyncio
except ImportError:
   import trollius as asyncio

import sys

try:
   import signal
except ImportError:
   signal = None


class EchoServer(asyncio.Protocol):

   def connection_made(self, transport):
      self.transport = transport

   def data_received(self, data):
      self.transport.write(data)


if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   print ('Using backend: {0}'.format(loop.__class__.__name__))

   if signal is not None and sys.platform != 'win32':
      loop.add_signal_handler(signal.SIGINT, loop.stop)

   f = loop.create_server(EchoServer, '127.0.0.1', 9000)
   server = loop.run_until_complete(f)
   try:
      loop.run_forever()
   finally:
      server.close()
      loop.close()
