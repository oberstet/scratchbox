import sys, time

N = int(sys.argv[1])

print "running test on Python map, ", "records = %d" % N

from randstr import newid


start_time = time.time()

db = {}

for i in xrange(N):
   db[newid(i)] = i

elapsed_time = time.time() - start_time

print "ok, inserted %d records in %.1f seconds, %d recs/sec" % (N, elapsed_time, round(float(N)/elapsed_time))
print
