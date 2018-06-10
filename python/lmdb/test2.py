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

    def __delitem__(self, key):
        _key = struct.pack('<H', self._table) + self._serialize_key(key)
        self._txn._txn.delete(_key)

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

    def __enter__(self):
        self._txn = lmdb.Transaction(env, write=self._write)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # https://docs.python.org/3/reference/datamodel.html#object.__exit__
        # If the context was exited without an exception, all three arguments will be None.
        if exc_type is None:
            self._txn.commit()
            print('LMDB transaction committed')
        else:
            self._txn.abort()
            print('LMDB transaction aborted', exc_type, exc_value, traceback)


##
## app code: variant 1, using CBOR
##


class AppTx(Transaction):
    """
    Definition of application database schema
    """

    def __init__(self, write=False):
        Transaction.__init__(self, write=write)
        self.users_by_authid = MapStringOid(1, self)
        self.users = MapOidCbor(2, self)


env = lmdb.open('.db3')

user_oid = 1
user_authid = 'joe50xyz'
user = {
    'name': 'joe',
    'authid': user_authid,
    'email': 'joe.doe@digital.com',
    'birthday': {
        'year': 1950,
        'month': 12,
        'day': 24
    },
    'ratings': {
        'dawn-of-the-dead': 6.9,
        'day-of-the-dead': 7.5,
        'land-of-the-dead': 8.9
    },
    'tags': ['geek', 'vip']
}

with AppTx(write=True) as txn:

    _user_oid = txn.users_by_authid[user_authid]

    if _user_oid:
        user = txn.users[_user_oid]
        print('user loaded', user)
    else:
        txn.users_by_authid[user_authid] = user_oid
        txn.users[user_oid] = user
        print('user stored', user)



##
## app code: variant 2, using native Python object
##

env = lmdb.open('.db4')

user_oid = 1
user_authid = 'joe50xyz'

class User(object):

    def __init__(self):
        self.name = 'joe'
        self.authid = user_authid
        self.email = 'joe.doe@digital.com'
        self.birthday = datetime.date(1950, 12, 24)
        self.ratings = {
            'dawn-of-the-dead': 6.9,
            'day-of-the-dead': 7.5,
            'land-of-the-dead': 8.9
        }
        self.tags = ('geek', 'vip')

user = User()

class AppTx2(Transaction):
    """
    Definition of application database schema
    """

    def __init__(self, write=False):
        Transaction.__init__(self, write=write)

        # index: string -> oid
        self.users_by_authid = MapStringOid(1, self)

        # table: oid -> user
        self.users = MapOidPickle(2, self)


with AppTx2(write=True) as txn:

    _user_oid = txn.users_by_authid[user_authid]

    if _user_oid:
        user = txn.users[_user_oid]
        print('user loaded', user)
    else:
        txn.users_by_authid[user_authid] = user_oid
        txn.users[user_oid] = user
        print('user stored', user)
