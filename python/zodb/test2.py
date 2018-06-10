# https://github.com/zc/zrs

import random

import ZODB
import ZODB.FileStorage
import BTrees
import persistent
import transaction

from zc.zrs import primary

from twisted.internet import reactor


class Account(persistent.Persistent):

    def __init__(self, no):
        self.no = no
        self.balance = random.random()

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount


storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)

with db.transaction() as txn:
    txn.root.accounts = BTrees.OOBTree.BTree()

with db.transaction() as txn:
    for i in range(1000):
        key = 'account-{}'.format(i)
        txn.root.accounts[key] = Account(i)

ps = primary.Primary(storage, ('', 8000), reactor)
reactor.run()
