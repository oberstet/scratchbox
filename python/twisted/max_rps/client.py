
from autobahn.twisted.choosereactor import install_reactor

install_reactor(verbose=True)

import sys

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log

from twisted.internet.defer import inlineCallbacks, DeferredList
from twisted.internet.task import LoopingCall

from autobahn.util import rtime

from autobahn.twisted.util import sleep

from collections import deque


log.startLogging(sys.stdout)

import psutil
p = psutil.Process()
p.cpu_affinity([1])
print("CPU affinity set: {}".format(p.cpu_affinity()))


size_histo = {}
def print_histo():
    print size_histo

lc = LoopingCall(print_histo)
lc.start(1)


QUEUED_WRITES = True


class ByteSender(protocol.Protocol):

    LOWER_WATERMARK = 10000
    UPPER_WATERMARK = 20000
    BATCH_SIZE = 2
    RECHECK_MS = 10
    RUNTIME = 60

    def print_stats(self):
        if self._started:
            self._total += self._cnt
            stopped = rtime()
            cps = float(self._cnt) / float(stopped - self._started)
            print("{} calls/s ({} succeeded)".format(cps, self._total))

        self._started = rtime()
        self._cnt = 0

    def dataReceived(self, data):
        #print("Data received", data)
        l = len(data)
        if l not in size_histo:
            size_histo[l] = 0
        size_histo[l] += 1

        self._cnt_outstanding -= l
        self._cnt += l

    def send_queued_stuff(self):
        while len(self._send_queue):
            data = self._send_queue.popleft()
            self.transport.write(data)
        reactor.callLater(10. / 1000., self.send_queued_stuff)

    def write(self, data):
        if QUEUED_WRITES:
            self._send_queue.append(data)
        else:
            self.transport.write(data)

    def connectionMade(self):
        print("session ready")
        self._send_queue = deque()
        self.send_queued_stuff()


        self._stop_calling = False
        self._done = False
        self._cnt_outstanding = 0
        self._started = None
        self._total = 0
        self._debug = False

        lc = LoopingCall(self.print_stats)
        lc.start(1)

        def stop():
            lc.stop()
            self._stop_calling = True
            self._done = True
            self._test_ended = rtime()
            self.stop()

        reactor.callLater(self.RUNTIME, stop)

        self._test_started = rtime()
        self.issue_calls()

    @inlineCallbacks
    def issue_calls(self):
        while not self._stop_calling:
            #self.transport.write(b"\0")
            self.write(b"\0")
            self._cnt_outstanding += 1
            yield sleep(0)
            if self._cnt_outstanding > self.UPPER_WATERMARK:
                if self._debug:
                    print("high-watermark reached: stopping")
                self._stop_calling = True
                self.check_outstanding()

    def check_outstanding(self):
        if not self._done:
            if self._cnt_outstanding < self.LOWER_WATERMARK:
                if self._debug:
                    print("low-watermark reached: starting")
                self._stop_calling = False
                self.issue_calls()
            else:
                reactor.callLater(float(self.RECHECK_MS) / 1000., self.check_outstanding)

    def stop(self):
        print("=" * 65)
        cps = float(self._total) / float(self._test_ended - self._test_started)
        print("{} calls/s ({} succeeded)".format(cps, self._total))

        from twisted.internet import reactor
        reactor.stop()


endpoint = endpoints.clientFromString(reactor, b"tcp:127.0.0.1:1234")
d = endpoints.connectProtocol(endpoint, ByteSender())

def on_connect_success(proto):
    print proto

def on_connect_fail(err):
    print err

d.addCallbacks(on_connect_success, on_connect_fail)

reactor.run()
