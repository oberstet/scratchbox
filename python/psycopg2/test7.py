import sys
import psycopg2

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""DROP TYPE IF EXISTS t_station CASCADE""")
cur.execute("""DROP TYPE IF EXISTS t_employee CASCADE""")
cur.execute("""DROP TYPE IF EXISTS t_address CASCADE""")

cur.execute("""CREATE TYPE t_station AS (x INT, y INT, label VARCHAR)""")
cur.execute("""CREATE TYPE t_address AS (city VARCHAR, street VARCHAR, no INT, stations t_station[])""")
cur.execute("""CREATE TYPE t_employee AS (name VARCHAR, age INT, coins INT[], notes VARCHAR, address t_address)""")

cur.execute("""
CREATE OR REPLACE FUNCTION test_employee(e t_employee)
  RETURNS t_employee AS
$$
BEGIN
   RETURN e;
END
$$ LANGUAGE plpgsql;
""")

from collections import namedtuple

station = namedtuple('station', 'x y label')

# this adapter invokes the basic tuple adapter and adds a specific cast.
class StationAdapter(object):
   def __init__(self, adapted):
      self.adapted = adapted
   def prepare(self,conn):
      self._conn = conn
   def getquoted(self):
      a = psycopg2.extensions.adapt(tuple(self.adapted))
      a.prepare(self._conn)
      return a.getquoted() + '::t_station'

psycopg2.extensions.register_adapter(station, StationAdapter)



v1 = ('foo', 44, [1, 2, 3], None, ('Duckhausen', None, 18, [station(10, None, 'blub'), station(None, 5, None)]))
#v1 = ('foo', 44, [1, 2, 3], None, ('Duckhausen', None, 18, []))

print cur.mogrify("SELECT test_employee(%s)", [v1])

cur.execute("SELECT test_employee(%s)", [v1])
print cur.fetchone()
