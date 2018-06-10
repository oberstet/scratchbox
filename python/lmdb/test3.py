##
## generic part ("library")
##

import os
import shutil
import random
import lmdb
from collections.abc import MutableMapping
import struct
import cbor2
import pickle
import datetime


class PersistentMap(MutableMapping):

    def __init__(self, table, txn):
        MutableMapping.__init__(self)
        self._table = table
        self._txn = txn

    def _serialize_key(self, key):
        raise Exception('not implemented')

    def _serialize_value(self, value):
        raise Exception('not implemented')

    def _deserialize_value(self, data):
        raise Exception('not implemented')

    def __getitem__(self, key):
        _key = struct.pack('<H', self._table) + self._serialize_key(key)
        _data = self._txn._txn.get(_key)
        if _data:
            return self._deserialize_value(_data)
        else:
            return None

    def __setitem__(self, key, value):
        _key = struct.pack('<H', self._table) + self._serialize_key(key)
        _data = self._serialize_value(value)
        self._txn._txn.put(_key, _data)
        self._txn._puts += 1

    def __delitem__(self, key):
        _key = struct.pack('<H', self._table) + self._serialize_key(key)
        self._txn._txn.delete(_key)
        self._txn._dels += 1

    def __iter__(self):
        raise Exception('not implemented')

    def __len__(self):
        raise Exception('not implemented')


class MapStringOid(PersistentMap):

    def _serialize_key(self, key):
        return key.encode('utf8')

    def _serialize_value(self, value):
        return struct.pack('<Q', value)

    def _deserialize_value(self, data):
        return struct.unpack('<Q', data)[0]


class MapOidCbor(PersistentMap):

    def _serialize_key(self, key):
        return struct.pack('<Q', key)

    def _serialize_value(self, value):
        return cbor2.dumps(value)

    def _deserialize_value(self, data):
        return cbor2.loads(data)


class MapOidPickle(PersistentMap):

    def _serialize_key(self, key):
        return struct.pack('<Q', key)

    def _serialize_value(self, value):
        return pickle.dumps(value, protocol=4)

    def _deserialize_value(self, data):
        return pickle.loads(data)



class Transaction(object):

    def __init__(self, write=False):
        self._write = write
        self._txn = None
        self._puts = 0
        self._dels = 0

    def __enter__(self):
        self._txn = lmdb.Transaction(env, write=self._write)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # https://docs.python.org/3/reference/datamodel.html#object.__exit__
        # If the context was exited without an exception, all three arguments will be None.
        if exc_type is None:
            self._txn.commit()
            print('LMDB transaction committed', self._puts, self._dels)
        else:
            self._txn.abort()
            print('LMDB transaction aborted', exc_type, exc_value, traceback)



from typing import Optional

class User(object):

    def __init__(self, oid, name, authid, email=None, birthday=None, is_friendly=True, tags=None, ratings=None, friends=None, referred_by=None):
        self.oid = oid
        self.name = name
        self.authid = authid
        self.email = email
        self.birthday = birthday
        self.is_friendly = is_friendly
        self.tags = tags or []
        self.ratings = ratings or {}
        self.friends = friends or []
        self.referred_by: Optional[User] = referred_by


class AppTransaction(Transaction):
    """
    Definition of application database schema
    """

    def __init__(self, write=False):
        Transaction.__init__(self, write=write)

        # index: string -> oid
        self.users_by_authid = MapStringOid(1, self)

        # table: oid -> user
        self.users = MapOidPickle(2, self)



users = []

user1 = User(oid=1,
             name='Homer Simpson',
             authid='homer',
             email='homer.simpson@example.com',
             birthday=datetime.date(1950, 12, 24),
             is_friendly=True,
             tags=['relaxed', 'beerfan'])
users.append(user1)

user2 = User(oid=2,
             name='Crocodile Dundee',
             authid='crocoboss',
             email='croco@example.com',
             birthday=datetime.date(1960, 2, 4),
             is_friendly=False,
             tags=['red', 'yellow'],
             referred_by=user1)
users.append(user2)

user = User(oid=3,
            name='Foobar Space',
            authid='foobar',
            email='foobar@example.com',
            birthday=datetime.date(1970, 5, 7),
            is_friendly=True,
            tags=['relaxed', 'beerfan'],
            referred_by=user1)
users.append(user)


env = lmdb.open('.db4')

with AppTransaction(write=True) as txn:
    for user in users:
        _user = txn.users[user.oid]
        if not _user:
            txn.users[user.oid] = user
            txn.users_by_authid[user.authid] = user.oid
            print('user stored', user)
        else:
            print('user loaded', _user)


# https://github.com/google/flatbuffers/blob/master/docs/source/CppUsage.md#access-of-untrusted-buffers


with AppTransaction(write=True) as txn:
    for i in range(100):

        user = User(oid=i+10, name='Test {}'.format(i), authid='test-{}'.format(i))
        for j in range(10):
            user.ratings['test-rating-{}'.format(j)] = random.random()

        _user = txn.users[user.oid]
        if not _user:
            txn.users[user.oid] = user
            txn.users_by_authid[user.authid] = user.oid
            print('user stored', user)
        else:
            print('user loaded', _user)
