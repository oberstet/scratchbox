from time import time

from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet import reactor

N = 100
ROUNDS = 10

pitch = 1./float(N)
started = None

def foo(i, round):
   if round < ROUNDS:
      reactor.callLater(pitch, foo, i, round + 1)
   else:
      #print("{} - {}".format(i, round))
      if i == N - 1:
         ended = time()
         print("{}".format(ended - started))
         reactor.stop()

t = 0
for i in range(N):
   t += pitch
   reactor.callLater(t, foo, i, 0)

started = time()
reactor.run()
