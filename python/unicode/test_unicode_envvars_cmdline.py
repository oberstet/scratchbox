# coding: utf8

# Allowed characters in linux environment variable names
# http://stackoverflow.com/a/2821183/884770

import os, sys, six

val = os.environ[u'MYTICKET']
if six.PY2:
    val = val.decode('utf8')
print(u'{} {}'.format(type(val), val))

val = sys.argv[1]
if six.PY2:
    val = val.decode('utf8')
print(u'{} {}'.format(type(val), val))
