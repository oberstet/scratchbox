import sys, copy
import psycopg2
import psycopg2.extras
import psycopg2.extensions
import json

from pprint import pprint

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""
CREATE OR REPLACE FUNCTION mysp7(OUT a integer, OUT b integer)
RETURNS SETOF RECORD AS $$
BEGIN
  a := 10; b := 10;
  RETURN NEXT;
  a := 11; b := 20;
  RETURN NEXT;
  RETURN;
END;
$$ LANGUAGE plpgsql; 
""")

cur.execute("select mysp7()")
res = cur.fetchall()
print res


def cast_record(s, curs):
   if s is None:
      return None
   ## FIXME: how to parse s as Python _list_ and recursively
   ## to casting of elements?
   return None

RECORD = psycopg2.extensions.new_type((2249,), "RECORD", cast_record)
psycopg2.extensions.register_type(RECORD)

psycopg2.extensions.register_type(
   psycopg2.extensions.new_array_type(
      (2287,), 'RECORD[]', RECORD))


cur.execute("select mysp7()")
res = cur.fetchall()
print res
#print json.dumps(res)
