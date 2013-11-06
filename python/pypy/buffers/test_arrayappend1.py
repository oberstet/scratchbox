import sys
from array import array


def test(chopcount, chopsize):
   chop = '*' * chopsize
   achop = array('B', chop)

   n = chopcount * chopsize
   a = array('B')

   i = 0
   while i < chopcount:
      a.extend(achop)
      i += 1

   s = a.tostring()
   assert(len(s) == n)


if __name__ == "__main__":
   chopcount = int(sys.argv[1])
   chopsize = int(sys.argv[2])
   test(chopcount, chopsize)
