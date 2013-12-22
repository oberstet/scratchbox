import math
import asyncio
from asyncio import coroutine

## With coroutine style, decorators are needed on application
## functions, even though the functions may be plain old.
## There seems to be no analogue of Twisted maybeDeferred()

@coroutine
def fast_sqrt(x):
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


@coroutine
def slow_sqrt(x):
   yield from asyncio.sleep(1)
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


@coroutine
def run_test():
   for x in [2, -2]:
      for f in [fast_sqrt, slow_sqrt]:
         try:
            res = yield from f(x)
            print("{} result: {}".format(f, res))
         except Exception as e:
            print("{} exception: {}".format(f, e))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())