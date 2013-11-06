import sys

def test(chopcount, chopsize):
   chop = '*' * chopsize

   n = chopcount * chopsize

   sl = []

   i = 0
   while i < chopcount:
      sl.append(chop)
      i += 1

   s = ''.join(sl)
   assert(len(s) == n)


if __name__ == "__main__":
   chopcount = int(sys.argv[1])
   chopsize = int(sys.argv[2])
   test(chopcount, chopsize)
