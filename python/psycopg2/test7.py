import sys
import psycopg2

password = sys.argv[1]

conn = psycopg2.connect(host = "127.0.0.1", port = 5432, database = "test", user = "test", password = password)
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

v1 = ('foo', 44, [1, 2, 3], None, ('Duckhausen', None, 18, [(10, None, 'blub'), (None, 5, None)]))

cur.execute("SELECT test_employee(%s)", [v1])
print cur.fetchone()
