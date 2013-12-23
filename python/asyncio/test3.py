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
import types, inspect, functools


def maybe_async(value):
   if isinstance(value, types.GeneratorType) or isinstance(value, asyncio.futures.Future):
      return value
   else:
      future = asyncio.Future()
      future.set_result(value)
      return future


# adapted from:
# http://hg.python.org/cpython/file/dfe327390cc2/Lib/asyncio/tasks.py#l70
def maybe_async2(func):
   if inspect.isgeneratorfunction(func):
      coro = func
   else:
      @functools.wraps(func)
      def coro(*args, **kw):
         res = func(*args, **kw)
         if isinstance(res, asyncio.futures.Future) or inspect.isgenerator(res):
            res = yield from res
         return res
   return coro


def maybe_async3(func, *args, **kw):
   res = func(*args, **kw)
   if isinstance(res, asyncio.futures.Future) or inspect.isgenerator(res):
      res = yield from res
   return res


def yields(value):
   return isinstance(value, asyncio.futures.Future) or inspect.isgenerator(value)
#   return isinstance(value, asyncio.futures.Future) or isinstance(value, types.GeneratorType)


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

            # Variant 1b
            res = f(x)
            if yields(res):
               res = yield from res

            # Variant 2
            #res = yield from maybe_async(f(x))

            # Variant 3
            #res = yield from asyncio.coroutine(f)(x)

            # Variant 4
            #res = yield from maybe_async2(f)(x)

            # Variant 5
            #res = yield from maybe_async3(f, x)

            print("{} result: {}".format(f, res))
         except Exception as e:
            print("{} exception: {}".format(f, e))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())