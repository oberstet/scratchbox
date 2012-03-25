import leveldb

db = leveldb.LevelDB('/tmp/leveldb1')

try:
   v = db.Get('hello')
   print "ok, already have ", v
except:
   db.Put('hello', 'world')
   print "ok, inserted data"
