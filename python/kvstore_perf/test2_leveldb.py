import sys, time, random, shutil, leveldb

N = int(sys.argv[1])
COMMITSIZE = int(sys.argv[2])
DBPATH = '/tmp/leveldb2'

print "running test on LevelDB, ", "records = %d" % N, "commit size = %d" % COMMITSIZE

from randstr import newid

shutil.rmtree(DBPATH, ignore_errors = True)
db = leveldb.LevelDB(DBPATH)
print "create scratch new DB"

start_time = time.time()

for i in xrange(N):
   if COMMITSIZE > 0 and i % COMMITSIZE == 0:
      db.Put(newid(i), str(i), sync = True)
   else:
      db.Put(newid(i), str(i))

elapsed_time = time.time() - start_time

print "ok, inserted %d records in %.1f seconds, %d recs/sec" % (N, elapsed_time, round(float(N)/elapsed_time))
print
