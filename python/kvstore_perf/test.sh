#!/bin/sh

python -c "exec(\"import sys\\nprint 'Platform', sys.platform\\nprint sys.version\\nprint\")"

python test_pymap.py 1000
python test_leveldb.py 1000 1
python test_zodb.py 1000 1
python test_sqlite.py 1000 1

python test_pymap.py 100000
python test_leveldb.py 100000 10000
python test_zodb.py 100000 10000
python test_sqlite.py 100000 10000

python test_pymap.py 1000000
python test_leveldb.py 1000000 0
python test_zodb.py 1000000 0
python test_sqlite.py 1000000 0
