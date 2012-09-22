import sys
import psycopg2

from pprint import pprint

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


from psycopg2.extensions import register_type, register_adapter, adapt
from psycopg2.extras import CompositeCaster

def register_flexmap(conn, types):

   casters = {}

   class DictComposite(CompositeCaster):
      def make(self, attrs):
         o = {}
         for i in xrange(len(self.attnames)):
            if attrs[i] is not None:
               o[self.attnames[i]] = attrs[i]
         o['record'] = self.schema + '.' + self.name
         return o

   for t in types:
      caster = DictComposite._from_db(t, conn)
      register_type(caster.typecaster, conn)     
      if caster.array_typecaster is not None:
         register_type(caster.array_typecaster, conn)
      casters[t] = caster

   class DictAdapter(object):
      def __init__(self, adapted):
         self.adapted = adapted
         
      def prepare(self, conn):
         self._conn = conn
         
      def getquoted(self):
         if self.adapted.has_key('record') and casters.has_key(self.adapted['record']):
            c = casters[self.adapted['record']]
            v = []
            for n in c.attnames:
               v.append(self.adapted.get(n, None))
            a = adapt(tuple(v))
            a.prepare(self._conn)
            return a.getquoted() + '::' + self.adapted['record']
         else:
            return adapt(None).getquoted()
   
   register_adapter(dict, DictAdapter)


register_flexmap(conn, ['t_station', 't_address', 't_employee'])


v1 = {'record': 't_employee',
      'name': 'foo',
      'age': 44,
      'coins': [1, 2, 3],
      'ignored': 'unknown attrs get ignored!',
      'address': {'record': 't_address',
                  'city': 'Duckhausen',
                  'no': 18,
                  'stations': [{'record': 't_station', 'x': 10},
                               {'record': 't_station', 'label': 'hello', 'y': 10}]
      }}


#print cur.mogrify("SELECT test_employee(%s)", [v1])
cur.execute("SELECT test_employee(%s)", [v1])
v2 = cur.fetchone()[0]

pprint(v1)
pprint(v2)
