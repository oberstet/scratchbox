import sys, random, time, pprint

if 'bsd' in sys.platform or sys.platform.startswith('darwin'):
   from twisted.internet import kqreactor
   kqreactor.install()
elif sys.platform in ['win32']:
   from twisted.application.reactors import installReactor
   installReactor("iocp")
elif sys.platform.startswith('linux'):
   from twisted.internet import epollreactor
   epollreactor.install()

from twisted.internet import reactor

from twisted.python import log
from twisted.internet.defer import Deferred, \
                                   DeferredList, \
                                   gatherResults, \
                                   returnValue, \
                                   inlineCallbacks

from twisted.internet.threads import deferToThread

def newid():
   return ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_") for i in xrange(16)])


if sys.platform.startswith('win'):
   rtime = time.clock
   _ = rtime()
else:
   rtime = time.time


class Test:

   def __init__(self, n, release):
      self.n = n
      self.release = release
      self.times = {}

   def work_start(self, id):
      self.times[id]['t2'] = rtime()
      return id

   def work_end(self, id):
      self.times[id]['t3'] = rtime()

   def add(self):
      if self.c < self.n:
         id = newid()
         self.times[id] = {}
         self.times[id]['t1'] = rtime()
         d = deferToThread(self.work_start, id)
         d.addCallback(self.work_end)
         self.dl.append(d)
         self.c += 1
         if self.release:
            reactor.callLater(0, self.add)
         else:
            self.add()
      else:
         self.doneadd()

   def doneadd(self):
      d = DeferredList(self.dl)
      d.addCallback(self.end)

   def run(self):
      self.c = 0
      self.dl = []
      self.started = rtime()
      self.add()

   def end(self, _):
      self.ended = rtime()
      print "release to reactor between deferToThread:", self.release
      print "total run-time: %s ms" % int(round(1000. * (self.ended - self.started)))
      s21 = 0
      s32 = 0
      m21 = 0
      m32 = 0
      a21 = []
      a32 = []
      for t in self.times.values():
         v21 = 1.e6 * (t['t2'] - t['t1'])
         v32 = 1.e6 * (t['t3'] - t['t2'])
         s21 += v21
         s32 += v32
         if v21 > m21:
            m21 = v21
         if v32 > m32:
            m32 = v32
         a21.append(v21)
         a32.append(v32)
         #print v21, v32

      l = float(len(self.times))

      print "avg. thread switch IN  time: %s us" % int(round(s21/l))
      print "max. thread switch IN  time: %s us" % int(round(m21))

      print "avg. thread switch OUT time: %s us" % int(round(s32/l))
      print "max. thread switch OUT time: %s us" % int(round(m32))

      try:
         import numpy
         #print numpy.histogram(a21)
         #print numpy.histogram(a32)
      except:
         pass

      try:
         import matplotlib.pyplot as plt
         #plt.hist(a21)
         #plt.hist(a32)
         #plt.show()
      except:
         pass

      reactor.stop()


if __name__ == '__main__':
   log.startLogging(sys.stdout)
   print "Using Twisted reactor class %s" % str(reactor.__class__)
   n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
   release = len(sys.argv) > 2 and sys.argv[2] == "yes"
   ps = int(sys.argv[3]) if len(sys.argv) > 3 else 10
   t = Test(n, release)
   t.run()
   reactor.suggestThreadPoolSize(ps)
   print "Thread pool size suggested:", ps
   print "Worker count:", n
   reactor.run()
