#!/bin/sh

python -c "exec(\"import sys\\nprint 'Platform', sys.platform\\nprint sys.version\\nprint\")"

python test2_leveldb.py 1000 1
python test2_zodb.py 1000 1
python test2_sqlite.py 1000 1

python test2_leveldb.py 100000 10000
python test2_zodb.py 100000 10000
python test2_sqlite.py 100000 10000

python test2_leveldb.py 1000000 0
python test2_zodb.py 1000000 0
python test2_sqlite.py 1000000 0
