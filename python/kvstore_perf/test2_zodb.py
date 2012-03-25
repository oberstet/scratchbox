import sys, time, random, os, shutil

N = int(sys.argv[1])
COMMITSIZE = int(sys.argv[2])
if len(sys.argv) > 3:
   USEFILE = int(sys.argv[3])
else:
   USEFILE = 1

DBPATH = '/tmp/leveldb2_zodb'

print "running test on ZODB (" + ("FileStorage" if USEFILE else "MappingStorage") + "), ", "records = %d" % N, "commit size = %d" % COMMITSIZE

import logging
logging.basicConfig()

import ZODB
from ZODB.DB import DB
from ZODB.FileStorage import FileStorage
from ZODB.MappingStorage import MappingStorage
from BTrees.OOBTree import OOBTree
import transaction

shutil.rmtree(DBPATH, ignore_errors = True)
os.mkdir(DBPATH)

if USEFILE:
   storage = FileStorage(os.path.join(DBPATH, 'Data.fs'))
else:
   storage = MappingStorage()

print "created scratch new DB"


db = DB(storage)
conn = db.open()
dbroot = conn.root()
dbroot['tab1'] = OOBTree()
tab1 = dbroot['tab1']

from randstr import newid

start_time = time.time()

for i in xrange(N):
   tab1[newid(i)] = str(i)
   if COMMITSIZE > 0 and i % COMMITSIZE == 0:
      transaction.commit()
transaction.commit()

elapsed_time = time.time() - start_time

db.close()

print "ok, inserted %d records in %.1f seconds, %d recs/sec" % (N, elapsed_time, round(float(N)/elapsed_time))
print
