import math
import asyncio
from asyncio import coroutine

# decorator required
@coroutine
def fast_sqrt_coroutine(x):
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


# decorator no stricly necessary, the "yield from asyncio.sleep"
# will make the function a coroutine automatically
@coroutine
def slow_sqrt_coroutine(x):
   yield from asyncio.sleep(1)
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


def fast_sqrt_future(x):
   future = asyncio.Future()
   if x >= 0:
      future.set_result(math.sqrt(x))
   else:
      future.set_exception(Exception("negative number"))
   return future


def slow_sqrt_future(x):
   loop = asyncio.get_event_loop()
   future = asyncio.Future()
   def doit():
      if x >= 0:
         future.set_result(math.sqrt(x))
      else:
         future.set_exception(Exception("negative number"))
   loop.call_later(1, doit)
   return future


@coroutine
def run_test():
   for x in [2, -2]:
      for f in [fast_sqrt_coroutine,
                slow_sqrt_coroutine,
                fast_sqrt_future,
                slow_sqrt_future]:
         try:
            res = yield from f(x)
            print("{} result: {}".format(f, res))
         except Exception as e:
            print("{} exception: {}".format(f, e))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())