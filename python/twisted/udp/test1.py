import sys, argparse

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class UdpServer(DatagramProtocol):

   def __init__(self, debug = False):
      self._debug = debug
      self._count = 0

   def startProtocol(self):
      print "started"

   def datagramReceived(self, data, (host, port)):
      if self._debug:
         print "received %r from %s:%d" % (data, host, port)
      self.transport.write(data, (host, port))
      self._count += 1
      if self._count % 1000 == 0:
         print self._count


class UdpClient(DatagramProtocol):

   def __init__(self, ip, port, num = 10000, debug = False):
      self._ip = ip
      self._port = port
      self._debug = debug
      self._count = 0
      self._num = num

   def startProtocol(self):
      print "started"
      self.sendHello()

   def sendHello(self):
      self.transport.write("Hello!!!", (self._ip, self._port))

   def datagramReceived(self, data, (host, port)):
      if self._debug:
         print "received %r from %s:%d" % (data, host, port)
      if self._count < self._num:
         self.transport.write(data, (host, port))
         self._count += 1
         if self._count % 1000 == 0:
            print self._count
      else:
         reactor.stop()


def run():
   parser = argparse.ArgumentParser()
   parser.add_argument("-d",
                       "--debug",
                       help = "Enable debug output.",
                       action = "store_true")

   group1dummy = parser.add_argument_group(title = 'Run mode (one of the following)')
   group1 = group1dummy.add_mutually_exclusive_group(required = True)

   group1.add_argument("--client",
                       help = "Run UDP client.",
                       nargs = 3,
                       metavar = ('<server IP>', '<server port>', '<count>'),
                       action = "append")

   group1.add_argument("--server",
                       help = "Run UDP server.",
                       type = int,
                       metavar = "<listen port>",
                       action = "store")

   args = parser.parse_args()
   print args

   if args.debug:
      log.startLogging(sys.stdout)

   if args.server:
      port = args.server
      proto = UdpServer(debug = args.debug)
      reactor.listenUDP(port, proto)

   elif args.client:
      ip = args.client[0][0]
      port = int(args.client[0][1])
      count = int(args.client[0][2])
      proto = UdpClient(ip, port, count, debug = args.debug)
      reactor.listenUDP(0, proto)

   else:
      raise Exception("logic error")

   reactor.run()


if __name__ == '__main__':
   run()
