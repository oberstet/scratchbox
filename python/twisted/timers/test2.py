import timeit
import time

def f1():
   pass

def f2(x = 3):
   return x*x

def f3():
   return map(lambda x: x^2, range(10))

for f in [f1, f2, f3]:
   for i in range(5):
      print f, timeit.timeit(f, number = 1000000)
      time.sleep(2)
