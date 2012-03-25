import sys, time, random, os, sqlite3

N = int(sys.argv[1])
COMMITSIZE = int(sys.argv[2])

DBPATH = '/tmp/leveldb2_sqlite'

print "running test on SQLite3, ", "records = %d" % N, "commit size = %d" % COMMITSIZE

from randstr import newid

try:
   os.remove(DBPATH)
except:
   pass
conn = sqlite3.connect(DBPATH)
print "created scratch new DB"

c = conn.cursor()
c.execute("create table tab1 (k text, v text)")

start_time = time.time()

for i in xrange(N):
   c.execute('insert into tab1 values (?,?)', (newid(i), str(i)))
   if COMMITSIZE > 0 and i % COMMITSIZE == 0:
      conn.commit()
conn.commit()

elapsed_time = time.time() - start_time

c.close()

#for r in c.execute('select k, v from tab1'):
#   print r


print "ok, inserted %d records in %.1f seconds, %d recs/sec" % (N, elapsed_time, round(float(N)/elapsed_time))
print
