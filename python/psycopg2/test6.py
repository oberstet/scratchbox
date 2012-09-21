import simplejson, json, sys
from decimal import Decimal

import psycopg2
import psycopg2.extras
import psycopg2.extensions

from pprint import pprint

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""DROP TYPE IF EXISTS t_employee CASCADE""")
cur.execute("""DROP TYPE IF EXISTS t_address CASCADE""")
cur.execute("""CREATE TYPE t_address AS (city VARCHAR, street VARCHAR, no INT)""")
cur.execute("""CREATE TYPE t_employee AS (name VARCHAR, age INT, coins INT[], notes VARCHAR, address t_address)""")
cur.execute("""
CREATE OR REPLACE FUNCTION test_employee(e t_employee)
  RETURNS t_employee AS
$BODY$
DECLARE
   l_adr t_address;
BEGIN
   e.notes := NULL;
   l_adr.street := 'sdfsd';
   l_adr.no := 23;
   e.address := l_adr;
   RETURN e;
END
$BODY$
  LANGUAGE plpgsql;
""")

from pgutil import register_composite_as_dict

empCaster = register_composite_as_dict('t_employee', cur)
adrCaster = register_composite_as_dict('t_address', cur)

#e = empCaster.totuple({'name': 'foo', 'age': 44, 'address': {'no': 18, 'city': 'Duckhausen'}, 'ignored': None, 'coins': [1,2,3]})
e = empCaster.totuple({'name': 'foo', 'age': 44, 'ignored': None, 'coins': [1,2,3]})

cur.execute("SELECT test_employee(%s)", [e])
print cur.fetchone()[0]
