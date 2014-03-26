def add2(a, b):
   if b < 0:
      raise Exception("2nd number is negative")
   else:
      return a + b


class Foo:

   def __init__(self, title):
      self.title = title

   def hello1(self, msg):
      return "%s: %s" % (self.title, msg)

   def hello2(self, msg):
      return "{}: {}".format(self.title, msg)


def main():
   console.log("Sum: ", add2(2,3))
   console.log(range(5))
   console.log([3*x for x in range(10)])

   foo = Foo("Meister Eder")

   try:
      m = foo.hello1("Pumuckel")
      console.log(m)
   except Exception as e:
      console.log(str(e))


   try:
      m = foo.hello2("Pumuckel")
      console.log(m)
   except Exception as e:
      console.log(str(e))


   try:
      res = add2(2, -1)
      console.log(res)
   except Exception as e:
      console.log(str(e))

