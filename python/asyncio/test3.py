import math
import asyncio
from asyncio import coroutine

@coroutine
def fast_sqrt(x):
   future = asyncio.Future()
   if x >= 0:
      future.set_result(math.sqrt(x))
   else:
      future.set_exception(Exception("negative number"))
   return future


def slow_sqrt(x):
   yield from asyncio.sleep(1)
   future = asyncio.Future()
   if x >= 0:
      future.set_result(math.sqrt(x))
   else:
      future.set_exception(Exception("negative number"))
   return future


@coroutine
def run_test():
   for x in [2, -2]:
      for f in [fast_sqrt, slow_sqrt]:
         try:
            future = yield from f(x)
            print("\n{} {}".format(future, type(future)))
            res = future.result()
            print("{} result: {}".format(f, res))
         except Exception as e:
            print("{} exception: {}".format(f, e))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())