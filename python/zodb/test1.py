import logging
logging.basicConfig()

import ZODB
from ZODB.FileStorage import FileStorage
from ZODB.MappingStorage import MappingStorage
from ZODB.DB import DB
from BTrees.OOBTree import OOBTree
import transaction
from persistent import Persistent


class Account(Persistent):
   def __init__(self):
      self.balance = 0.0

   def deposit(self, amount):
      self.balance += amount

   def cash(self, amount):
      assert amount < self.balance
      self.balance -= amount

if False:
   storage = FileStorage('Data.fs')
else:
   storage = MappingStorage()
   
db = DB(storage)
conn = db.open()
dbroot = conn.root()

print dbroot.keys()

if not dbroot.has_key('subscriptions'):
   print 'initializing subscriptions'
   dbroot['subscriptions'] = OOBTree()
   t = dbroot['subscriptions']
   for b in ['foo', 'bar', 'foobar']:
      BASEURI = "http://example.com/%s" % b
      for i in xrange(5):
         t[BASEURI + '#event%d' % i] = [i, 1,2,3]
   transaction.commit()
else:
   print 'subscriptions already initialized'

subs = dbroot['subscriptions']
print subs

print subs.minKey()
print subs.minKey("http://example.com/")
print subs.minKey("http://example.com/fo")

#dbroot['account-1'] = Account()
#dbroot['account-2'] = Account()
#transaction.commit()
#print dbroot.keys()


if not dbroot.has_key('prefixmap'):
   print 'initializing prefixmap'
   dbroot['prefixmap'] = OOBTree()
   t = dbroot['prefixmap']
   t['http://example.com/foobar#'] = 'foobar'
   t['http://example.com/goose#'] = 'goose'
   t['http://example.com/goosedog#'] = 'goosedog'
   t['http://example.com/goosee#'] = 'goosee'
   transaction.commit()
else:
   print 'prefixmap already initialized'

prefixmap = dbroot['prefixmap']
for k in prefixmap.items():
   print k

def shrink(f):
   k = prefixmap.maxKey(f)
   v = prefixmap[k]
   print f, k, v, v + ':' + f[len(k):], f[:len(k)] == k

shrink('http://example.com/goosedog#100')
shrink('http://example.com/goose#100')
shrink('http://example.com/goo#100')

db.close()
