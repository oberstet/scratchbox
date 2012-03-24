import logging
logging.basicConfig()

import ZODB
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import transaction, persistent


class Account(persistent.Persistent):
   def __init__(self):
      self.balance = 0.0

   def deposit(self, amount):
      self.balance += amount

   def cash(self, amount):
      assert amount < self.balance
      self.balance -= amount


storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

print root.keys()

root['account-1'] = Account()
root['account-2'] = Account()

transaction.commit()

print root.keys()
