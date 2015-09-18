import os
import shutil
import random
import lmdb

DBFILE = 'test.dat'

if os.path.exists(DBFILE):
    if os.path.isdir(DBFILE):
        shutil.rmtree(DBFILE)
    else:
        os.remove(DBFILE)

env = lmdb.open(DBFILE, max_dbs=10)
table1 = env.open_db('table1', create=True)

print("inserting data ..")
with env.begin(write=True) as txn:
    indices = range(10)
    random.shuffle(indices)
    for i in indices:
        key = 'key{}'.format(i)
        data = 'data{}'.format(i)
        print("inserting data '{}' for key '{}'".format(data, key))
        txn.put(key, data, db=table1)
print

print("iterating over all data ..")
with env.begin() as txn:
    cursor = txn.cursor(db=table1)
    cursor.first()
    for key, value in cursor:
        print((key, value))
print

print("iterating over subset of data ..")
with env.begin() as txn:
    cursor = txn.cursor(db=table1)
    if not cursor.set_range('key5'): # Position at first key >= 'key5'.
        print('Not found!')
    for key, value in cursor:
        print((key, value))
print
