import sys, copy
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
CREATE OR REPLACE FUNCTION test_employee(val t_employee)
  RETURNS t_employee AS
$$
BEGIN
   RETURN val;
END
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION test_json(val json)
  RETURNS json AS
$$
BEGIN
   RETURN val;
END
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION test_hstore(val hstore)
  RETURNS hstore AS
$$
BEGIN
   RETURN val;
END
$$ LANGUAGE plpgsql;
""")


from psycopg2.extensions import register_type, register_adapter, adapt
from psycopg2.extras import CompositeCaster, \
                            Json, \
                            register_json, \
                            register_default_json, \
                            HstoreAdapter, \
                            register_hstore

def register_flexmap(conn, types):
   
   register_hstore(conn)
   register_json(conn)

   casters = {}

   class DictComposite(CompositeCaster):
      def make(self, attrs):
         o = {}
         for i in xrange(len(self.attnames)):
            if attrs[i] is not None:
               o[self.attnames[i]] = attrs[i]
         o['type'] = self.schema + '.' + self.name
         return o

   for t in types:
      caster = DictComposite._from_db(t, conn)
      register_type(caster.typecaster, conn)     
      if caster.array_typecaster is not None:
         register_type(caster.array_typecaster, conn)
      casters[t] = caster

   class DictAdapter(object):
      def __init__(self, adapted):
         ## remember value to be adaptated - a Python dict
         self.adapted = adapted
         
         ## remember type field of dict-value to be adapted
         if adapted.has_key('type'):
            self._type = adapted['type']
            #del(adapted['type'])
         else:
            self._type = None
         
         ## create adapter to hstore if requested
         if self._type == 'hstore':
            self._hstoreAdapter = HstoreAdapter(adapted)
         
      def prepare(self, conn):
         self._conn = conn
         if self._type == 'hstore':
            self._hstoreAdapter.prepare(conn)
         
      def getquoted(self):
         if self._type is not None:
            if self._type == 'json':
               return adapt(Json(self.adapted)).getquoted() + '::json'
            elif self._type == 'hstore':
               return self._hstoreAdapter.getquoted()
            elif casters.has_key(self._type):
               c = casters[self._type]
               v = []
               for n in c.attnames:
                  v.append(self.adapted.get(n, None))
               a = adapt(tuple(v))
               a.prepare(self._conn)
               return a.getquoted() + '::' + self._type
            else:
               raise psycopg2.ProgrammingError("unknown type %s in dictionary type hint" % self._type)
         else:
            raise psycopg2.ProgrammingError("dictionary is missing type hint")
   
   register_adapter(dict, DictAdapter)


register_flexmap(conn, ['t_station', 't_address', 't_employee'])


p1 = {'type': 't_employee',
      'name': 'foo',
      'age': 44,
      'coins': [1, 2, 3],
      'ignored': 'unknown attrs get ignored!',
      'address': {'type': 't_address',
                  'city': 'Duckhausen',
                  'no': 18,
                  'stations': [{'type': 't_station', 'x': 10},
                               {'type': 't_station', 'label': 'hello', 'y': 10}]
      }}

pprint(p1)
cur.execute("SELECT test_employee(%s)", [p1])
pprint(cur.fetchone()[0])

p2 = copy.deepcopy(p1)
p2['type'] = 'json'

pprint(p2)
cur.execute("SELECT test_json(%s)", [p2])
pprint(cur.fetchone()[0])

p3 = {'type': 'hstore',
      'key1': 'val1',
      'key2': 'val2',
      'key3': None,
      #'key4': 123,
      #'key5': [1,2,3]
      }

pprint(p3)
print cur.mogrify("SELECT test_hstore(%s)", [p3])
cur.execute("SELECT test_hstore(%s)", [p3])
pprint(cur.fetchone()[0])

try:
   print adapt({}).getquoted()
except Exception, e:
   print e

try:
   print adapt({'type': 'nonexistent'}).getquoted()
except Exception, e:
   print e
