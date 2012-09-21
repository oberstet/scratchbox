import simplejson, json, sys
from decimal import Decimal

import psycopg2
import psycopg2.extras
import psycopg2.extensions
from psycopg2.extensions import adapt

from pprint import pprint

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
conn.autocommit = True
cur = conn.cursor()

#psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)

cur.execute("""DROP TYPE IF EXISTS t_station CASCADE""")
cur.execute("""DROP TYPE IF EXISTS t_employee CASCADE""")
cur.execute("""DROP TYPE IF EXISTS t_address CASCADE""")

cur.execute("""CREATE TYPE t_station AS (x INT, y INT, label VARCHAR)""")
cur.execute("""CREATE TYPE t_address AS (city VARCHAR, street VARCHAR, no INT, stations t_station[])""")
cur.execute("""CREATE TYPE t_employee AS (name VARCHAR, age INT, coins INT[], notes VARCHAR, address t_address)""")

cur.execute("""
CREATE OR REPLACE FUNCTION test_employee(e t_employee, roundtrip BOOLEAN DEFAULT TRUE)
  RETURNS t_employee AS
$$
DECLARE
   l_adr t_address;
   l_stations t_station[];
   l_station  t_station;
BEGIN
   IF roundtrip THEN
      RETURN e;
   END IF;
   e.notes := 'something';
   l_adr := e.address;
   l_adr.street := 'sdfsd';
   l_adr.no := 23;
   l_adr.stations := l_stations;
   e.address := l_adr;
   RETURN e;
END
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION test_json(e json)
  RETURNS json AS
$$
BEGIN
   RETURN e;
END
$$ LANGUAGE plpgsql;
""")

v1 = ('foo', 44, [1, 2, 3], None, ('Duckhausen', None, 18, [(10, None, 'blub'), (None, 5, None)]))

cur.execute("SELECT test_employee(%s, %s)", [v1, False])
print cur.fetchone()

sys.exit(0)


from pgutil import register_composite_as_dict

casters = {}
acasters = {}

stationCaster = register_composite_as_dict('t_station', conn)

stationCaster.casters = casters
stationCaster.acasters = acasters
casters[stationCaster.oid] = stationCaster
acasters[stationCaster.array_oid] = stationCaster


empCaster = register_composite_as_dict('t_employee', conn)

empCaster.casters = casters
empCaster.acasters = acasters
casters[empCaster.oid] = empCaster
acasters[empCaster.array_oid] = empCaster


adrCaster = register_composite_as_dict('t_address', conn)

adrCaster.casters = casters
adrCaster.acasters = acasters
casters[adrCaster.oid] = adrCaster
acasters[adrCaster.array_oid] = adrCaster


e0 = {'name': 'foo', 'age': 44, 'ignored': None, 'coins': [1,2,3]}

e1 = {'name': 'foo',
              'age': 44,
              'address': {'no': 18,
                          'city': 'Duckhausen'},
               'ignored': None,
               'coins': [1,2,3]}

e2 = {'name': 'foo',
              'age': 44,
              'address': {'no': 18,
                          'city': 'Duckhausen',
                          'stations': [{'x': 10, 'label': 'blub'},
                                       {'y': 5, 'ignored': False}]},
               'ignored': None,
               'coins': [1,2,3]}

for e in [e0, e1, e2]:
   print "-"*40
   try:
      mangled = empCaster.totuple(e)
      print mangled
      #cur.execute("SELECT test_employee(%s, %s)", [empCaster.totuple(e), False])
      #print cur.fetchone()
   except Exception, e:
      print e

   #print "*"*40
   #try:
   #   cur.execute("SELECT test_json(%s)", [e])
   #   print cur.fetchone()
   #except Exception, e:
   #   print e
