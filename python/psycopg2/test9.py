import sys, copy
import psycopg2
import psycopg2.extras
import psycopg2.extensions
import json

from pprint import pprint

import re as regex

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""
CREATE OR REPLACE FUNCTION mysp7(OUT a integer, OUT b integer, OUT c timestamp, OUT d VARCHAR)
RETURNS SETOF RECORD AS $$
BEGIN
  a := 10; b := 10; c := now(); d:= 'sdf';
  RETURN NEXT;
  a := 11; b := 20; c := now(); d:= 'ssss';
  RETURN NEXT;
  RETURN;
END;
$$ LANGUAGE plpgsql; 
""")

from psycopg2.extensions import new_type, new_array_type, register_type

class RecordCaster(object):
    """
    Casts records (= anonymous composite type) into Python lists of strings.
    """

    def __init__(self, oid = 2249, array_oid = 2287):
        self.oid = oid
        self.array_oid = array_oid

        self.typecaster = new_type((oid,), "RECORD", self.parse)
        self.array_typecaster = new_array_type((array_oid,), "RECORD[]", self.typecaster)

    def parse(self, s, curs):
        if s is None:
            return None

        tokens = self.tokenize(s)
        return tokens

    _re_tokenize = regex.compile(r"""
  \(? ([,)])                        # an empty token, representing NULL
| \(? " ((?: [^"] | "")*) " [,)]    # or a quoted string
| \(? ([^",)]+) [,)]                # or an unquoted string
    """, regex.VERBOSE)

    _re_undouble = regex.compile(r'(["\\])\1')

    @classmethod
    def tokenize(self, s):
        rv = []
        for m in self._re_tokenize.finditer(s):
            if m is None:
                raise psycopg2.InterfaceError("can't parse type: %r" % s)
            if m.group(1):
                rv.append(None)
            elif m.group(2):
                rv.append(self._re_undouble.sub(r"\1", m.group(2)))
            else:
                rv.append(m.group(3))

        return rv

caster = RecordCaster()
register_type(caster.typecaster, conn)
register_type(caster.array_typecaster, conn)

cur.execute("select mysp7()")
res = cur.fetchall()
print res
#print json.dumps(res)
