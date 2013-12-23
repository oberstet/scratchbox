import math
import asyncio
from asyncio import coroutine


# a plain function
def fast_sqrt_plain(x):
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


# a coroutine:
# decorator required - otherwise this would be a plain function
@coroutine
def fast_sqrt_coroutine(x):
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


# a coroutine:
# decorator no stricly necessary, the "yield from asyncio.sleep"
# will make the function a coroutine automatically
@coroutine
def slow_sqrt_coroutine(x):
   yield from asyncio.sleep(1)
   if x >= 0:
      return math.sqrt(x)
   else:
      raise Exception("negative number")


# function returning a future
def fast_sqrt_future(x):
   future = asyncio.Future()
   if x >= 0:
      future.set_result(math.sqrt(x))
   else:
      future.set_exception(Exception("negative number"))
   return future


# function returning a future
def slow_sqrt_future(x):
   # do not use "yield from" inside here, since that will
   # make the function a coroutine that yields a future, which
   # is something different than a function returning a future
   #
   loop = asyncio.get_event_loop()
   future = asyncio.Future()
   def doit():
      if x >= 0:
         future.set_result(math.sqrt(x))
      else:
         future.set_exception(Exception("negative number"))
   loop.call_later(1, doit)
   return future



##
## trying to implement something like Twisted defer.maybeDeferred
## http://twistedmatrix.com/documents/current/api/twisted.internet.defer.maybeDeferred.html
##
import types
types.GeneratorType

def maybe_async(value):
   if isinstance(value, types.GeneratorType) or isinstance(value, asyncio.futures.Future):
      return value
   else:
      future = asyncio.Future()
      future.set_result(value)
      return future


@coroutine
def run_test():
   for x in [2, -2]:
      for f in [fast_sqrt_plain,
                fast_sqrt_coroutine,
                slow_sqrt_coroutine,
                fast_sqrt_future,
                slow_sqrt_future]:
         try:
            # Variant 1
            #res = f(x)
            #if isinstance(res, types.GeneratorType) or isinstance(res, asyncio.futures.Future):
            #   res = yield from res

            # Variant 2
            #res = yield from maybe_async(f(x))

            # Variant 3
            res = yield from asyncio.coroutine(f)(x)

            print("{} result: {}".format(f, res))
         except Exception as e:
            print("{} exception: {}".format(f, e))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())