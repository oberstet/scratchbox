import sys
from __pypy__.builders import StringBuilder

def test(chopcount, chopsize):
   chop = '*' * chopsize

   n = chopcount * chopsize
   sb = StringBuilder(n)

   i = 0
   while i < chopcount:
      sb.append(chop)
      i += 1

   s = sb.build()
   assert(len(s) == n)


if __name__ == "__main__":
   chopcount = int(sys.argv[1])
   chopsize = int(sys.argv[2])
   test(chopcount, chopsize)
