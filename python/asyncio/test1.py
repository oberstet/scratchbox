import asyncio

@asyncio.coroutine
def slow_operation(future):
   yield from asyncio.sleep(1)
   future.set_result('Future in done!')

def got_result(future):
   print(future.result())
   loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.Task(slow_operation(future))
future.add_done_callback(got_result)
loop.run_forever()
