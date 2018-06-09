import os
import shutil
import random
import lmdb
from collections.abc import MutableMapping
import struct
import cbor2


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



class Transaction(object):

    def __init__(self, write=False):
        self._txn = None
        self._write = write
        self.users_by_authid = MapStringOid(1, self)
        self.users = MapOidCbor(2, self)

    def __enter__(self):
        self._txn = lmdb.Transaction(env, write=self._write)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)
        # https://docs.python.org/3/reference/datamodel.html#object.__exit__
        # If the context was exited without an exception, all three arguments will be None.
        if exc_type is None:
            self._txn.commit()
            print('LMDB transaction committed')
        else:
            self._txn.abort()
            print('LMDB transaction aborted')



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

with Transaction(write=True) as txn:
    user_oid = txn.users_by_authid[user_authid]
    if user_oid:
        user = txn.users[user_oid]
        print('user loaded', user)
    else:
        txn.users_by_authid[user_authid] = user_oid
        txn.users[user_oid] = user
        print('user stored', user)
