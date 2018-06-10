import lmdb
import random
import datetime
from typing import Optional, List, Dict

import dbutil


class User(object):

    oid: int
    name: str
    authid: str
    email: str
    birthday: datetime.date
    is_friendly: bool
    tags: Optional[List[str]]
    ratings: Dict[str, float] = {}
    friends: List[int] = []
    referred_by: int = None


class Transaction(dbutil.BaseTransaction):
    """
    Definition of application database schema
    """

    users_by_authid: dbutil.MapStringOid = dbutil.MapStringOid(slot=1)
    """
    Maps user authid to user OID.
    """

    users: dbutil.MapOidPickle = dbutil.MapOidPickle(slot=2)
    """
    Maps user OID to user object (in pickle format).
    """

    def attach(self):
        self.users.attach(self)
        self.users_by_authid.attach(self)


users = []

user1 = User()
user1.oid = 1
user1.name = 'Homer Simpson'
user1.authid = 'homer'
user1.email = 'homer.simpson@example.com'
user1.birthday = datetime.date(1950, 12, 24)
user1.is_friendly = True
user1.tags = ['relaxed', 'beerfan']
users.append(user1)

user2 = User()
user2.oid = 2
user2.name = 'Crocodile Dundee'
user2.authid = 'crocoboss'
user2.email = 'croco@example.com'
user2.birthday = datetime.date(1960, 2, 4)
user2.is_friendly = False
user2.tags = ['red', 'yellow']
user2.referred_by = user1.oid
users.append(user2)

user3 = User()
user3.oid = 3
user3.name = 'Foobar Space'
user3.authid = 'foobar'
user3.email = 'foobar@example.com'
user3.birthday = datetime.date(1970, 5, 7)
user3.is_friendly = True
user3.tags = ['relaxed', 'beerfan']
user3.referred_by = user1.oid
users.append(user3)


env = lmdb.open('.db4')

with Transaction(env, write=True) as txn:
    for user in users:
        _user = txn.users[user.oid]
        if not _user:
            txn.users[user.oid] = user
            txn.users_by_authid[user.authid] = user.oid
            print('user stored', user)
        else:
            print('user loaded', _user)

with Transaction(env, write=True) as txn:
    for i in range(100):

        user = User()
        user.oid = i + 10
        user.name = 'Test {}'.format(i)
        user.authid = 'test-{}'.format(i)
        for j in range(10):
            user.ratings['test-rating-{}'.format(j)] = random.random()

        _user = txn.users[user.oid]
        if not _user:
            txn.users[user.oid] = user
            txn.users_by_authid[user.authid] = user.oid
            print('user stored', user, user.oid, user.authid)
        else:
            print('user loaded', _user, _user.oid, _user.authid)
