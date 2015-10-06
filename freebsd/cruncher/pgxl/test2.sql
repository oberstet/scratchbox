-------------------------------------------------------------------------------
-- Create replicated / sharded tables
-------------------------------------------------------------------------------

-- Im folgenden wird ein triviales, übliches PRODUCT-CUSTOMER-PURCHASE Schema aufgebaut
--
-- PRODUCT: wird auf alle Knoten repliziert. 20 Products
-- CUSTOMER: wird nach customer_id gesharded. 10 Mio. Customers
-- PURCHASE: wird nach customer_id gesharded. 500 Mio. Purchases

select * from information_schema.tables where table_name like '%pgxc%';

select * from pgxc_node;

select * from pgxc_class;

--
-- Products
--

DROP TABLE IF EXISTS product;

CREATE TABLE product (product_id INT NOT NULL, product_group_id INT NOT NULL, name TEXT NOT NULL, price NUMERIC NOT NULL, descr TEXT)
DISTRIBUTE BY REPLICATION
;


INSERT INTO product (product_id, product_group_id, name, price, descr)
SELECT
   id,
   floor(random() * 5),
   'product' || CAST(id AS TEXT),
   round((random() * 100)::numeric, 2),
   'Awesome product ' || CAST(id AS TEXT)
FROM
   generate_series(0, 20-1) AS id
;

ANALYZE product;

SELECT COUNT(*) FROM product;

SELECT * FROM product;

--
-- Customers
--

DROP TABLE IF EXISTS customer
;

CREATE TABLE customer (customer_id INT NOT NULL, co_customer_id INT, p FLOAT NOT NULL, fancy_code VARCHAR(10) NOT NULL, gender CHAR(1) NOT NULL, birth_year INT NOT NULL)
DISTRIBUTE BY HASH(customer_id)
;

INSERT INTO customer (customer_id, co_customer_id, p, fancy_code, gender, birth_year)
SELECT
   id,
   (CASE WHEN random() > 0.3 THEN floor(random() * 10000000)::int ELSE NULL END) AS co_customer_id,
   random(),
   substr(md5(random()::text), 1, 3 + floor(random() * 8)::int),
   (CASE WHEN floor(random()*2)::int = 0 THEN 'M' ELSE 'F' END),
   1900 + floor(random() * 100)::int
FROM generate_series(0, 10000000-1) AS id
;
--  4 nodes:   67587 ms => 150k/s
--  8 nodes: 
-- 16 nodes:   85760 ms => 117k/s
-- 32 nodes:  109421 ms =>  92k/s
-- 32 nodes:  102429 ms

ANALYZE customer;

INSERT INTO customer (customer_id, co_customer_id, p, fancy_code, gender, birth_year)
SELECT
   id,
   null,
   0,
   'foobar',
   'M',
   1950
FROM generate_series(1, 10000000) AS id
;
-- 33608 ms => 300k/s

INSERT INTO customer (customer_id, co_customer_id, p, fancy_code, gender, birth_year)
SELECT customer_id, co_customer_id, p, fancy_code, gender, birth_year FROM customer;
-- 2995 ms => 3.3 mio/s


SELECT birth_year, COUNT(*) FROM customer GROUP BY birth_year ORDER BY birth_year;


--
-- Purchase
--
DROP TABLE IF EXISTS purchase;

CREATE TABLE purchase (purchase_id BIGINT NOT NULL, customer_id INT NOT NULL, product_id INT NOT NULL, cnt INT NOT NULL)
DISTRIBUTE BY HASH(customer_id);

INSERT INTO purchase (purchase_id, customer_id, product_id, cnt)
SELECT
   id AS purchase_id,
   floor(random() * 10000000)::int AS customer_id,
   floor(random() * 20)::int AS product_id,
   floor(random() * 10)::int AS cnt
FROM generate_series(0, 500000000-1) AS id
;
-- 4 nodes auf 1 NVMe:             / 300k/s
-- 8 nodes auf 8 NVMes: 1971468 ms / 253k/s
-- 16 nodes:            2243209 ms / 223k/s
-- 32 nodes:            2416041 ms / 207k/s
-- 32 nodes:            2584005 ms / 209k/s
-- 32 nodes:            2549295 ms / 196k/s
-- 32 nodes:            2391655 ms / 196k/s

ANALYZE purchase;

-------------------------------------------------------------------------------
-- Query Performance auf Einzeltabellen
-------------------------------------------------------------------------------

SELECT COUNT(*) FROM purchase;
-- 10204 ms / 48 mio/s

SELECT cnt, COUNT(*) FROM purchase GROUP BY cnt;
--  4 nodes: 23127 ms / 22 mio/s
--  8 nodes: Gesamtlaufzeit der Abfrage: 12031 ms. / 42 mio/s
-- 16 nodes: Gesamtlaufzeit der Abfrage: 6402 ms. / 78 mio/s
-- 32 nodes: Gesamtlaufzeit der Abfrage: 3277 ms. / 153 mio/s
-- 32 nodes: Gesamtlaufzeit der Abfrage: 3182 ms. / 157 mio/s


-------------------------------------------------------------------------------
-- Query Performance auf Node-local Joins
-------------------------------------------------------------------------------

SELECT
   product_group_id,
   COUNT(*) purchase_cnt,
   SUM(cnt) items_sold,
   SUM(cnt * price) revenue
FROM
   purchase pu LEFT JOIN product pr
      ON pu.product_id = pr.product_id
GROUP BY
   product_group_id
ORDER BY
   product_group_id   
;
--  4 nodes: 104340 ms / 4.8 mio/s
--  8 nodes: 42431 ms / 11.8 mio/s
-- 16 nodes: 22948 ms / 21.8 mio/s
-- 32 nodes: 12306 ms / 40.6 mio/s


SELECT
   product_group_id,
   gender,
   COUNT(*) purchase_cnt,
   SUM(cnt) items_sold,
   SUM(cnt * price) revenue
FROM
   purchase pu
      LEFT JOIN product pr ON pu.product_id = pr.product_id
      LEFT JOIN customer co ON pu.customer_id = co.customer_id
GROUP BY
   product_group_id, gender
ORDER BY
   product_group_id, gender
;
--  4 nodes: 157044 ms /  3.2 mio/s
--  8 nodes:  68889 ms /  7.3 mio/s
-- 16 nodes:  36452 ms / 13.7 mio/s
-- 32 nodes:  19792 ms / 25.3 mio/s


-------------------------------------------------------------------------------
-- Query Performance auf Cross-node Joins
-------------------------------------------------------------------------------

-- node-local join
SELECT gender, COUNT(*)
FROM
   purchase pu
      LEFT JOIN customer co ON pu.customer_id = co.customer_id
GROUP BY gender
;
--  4 nodes: 65290 ms /  7.7 mio/s
--  8 nodes: 32466 ms / 15.4 mio/s
-- 16 nodes: 17052 ms / 29.3 mio/s
-- 32 nodes: 9617 ms / 52.0 mio/s

-- cross-node join!
SELECT gender, COUNT(*)
FROM
   purchase pu
      LEFT JOIN customer co ON pu.customer_id = co.co_customer_id
GROUP BY gender
;
--  4 nodes: 203837 ms /  2.5 mio/s
--  8 nodes:  92614 ms /  5.4 mio/s
-- 16 nodes:  44917 ms / 11.1 mio/s
-- 32 nodes: abgebrochen

-------------------------------------------------------------------------------
-- ETL Performance
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS purchase_revenue;

CREATE TABLE purchase_revenue (purchase_id BIGINT NOT NULL, customer_id INT NOT NULL, product_id INT NOT NULL, cnt INT NOT NULL, revenue NUMERIC NOT NULL)
DISTRIBUTE BY HASH(customer_id);

INSERT INTO purchase_revenue (purchase_id, customer_id, product_id, cnt, revenue)
SELECT
   pu.purchase_id,
   pu.customer_id,
   pu.product_id,
   pu.cnt,
   pu.cnt * pr.price AS revenue
FROM
   purchase pu LEFT JOIN product pr
      ON pu.product_id = pr.product_id
;
--  4 nodes: 245227 ms /  2.0 mio/sec
--  8 nodes: 100135 ms /  5.0 mio/sec
-- 16 nodes:  51678 ms /  9.7 mio/sec
-- 32 nodes:  27983 ms / 17.9 mio/sec

ANALYZE purchase_revenue;

SELECT * FROM purchase_revenue LIMIT 100;

SELECT COUNT(*) FROM purchase_revenue;

---

DROP TABLE IF EXISTS purchase_customer_details;

CREATE TABLE purchase_customer_details (purchase_id BIGINT NOT NULL, customer_id INT NOT NULL, customer_gender CHAR(1) NOT NULL, co_customer_id INT, co_customer_gender CHAR(1))
DISTRIBUTE BY HASH(customer_id);

INSERT INTO purchase_customer_details (purchase_id, customer_id, customer_gender, co_customer_id, co_customer_gender)
SELECT pu.purchase_id, pu.customer_id, co1.gender, co1.co_customer_id, co2.gender
FROM
   purchase pu
      LEFT JOIN customer co1 ON pu.customer_id = co1.customer_id
      LEFT JOIN customer co2 ON co1.co_customer_id = co2.customer_id
;
--  4 nodes: 237553 ms / 2.1 mio/s
--  8 nodes: 106664 ms / 4.7 mio/s
-- 16 nodes:  56343 ms / 8.9 mio/s
-- 32 nodes: abgebrochen

ANALYZE purchase_customer_details;


SELECT customer_gender, co_customer_gender, COUNT(*) FROM purchase_customer_details GROUP BY 1, 2;
--  4 nodes: 42829 ms / 11.8 mio/s
--  8 nodes: 18883 ms / 26.5 mio/s
-- 16 nodes:  9648 ms / 51.8 mio/s
--


CREATE OR REPLACE FUNCTION null_concat (text, text)
RETURNS text AS
'SELECT
CASE WHEN $1 IS NULL THEN $2
WHEN $2 IS NULL THEN $1
ELSE $1 || $2 END;'
LANGUAGE SQL IMMUTABLE;

CREATE OPERATOR + (LEFTARG = TEXT,  RIGHTARG = TEXT, PROCEDURE = null_concat);



DROP TABLE IF EXISTS concat_test;

CREATE TABLE concat_test (customer_id INT NOT NULL, f1 TEXT, f2 TEXT, f3 TEXT)
DISTRIBUTE BY HASH(customer_id);

INSERT INTO concat_test (customer_id, f1, f2, f3)
SELECT
   id AS customer_id,
   md5(random()::text) AS f1,
   (case when random() > .9 then md5(random()::text) else null end) as f2,
   (case when random() > .3 then md5(random()::text) else null end) as f3
FROM generate_series(0, 100000000-1) AS id
;
-- 650953 ms / 154k/s
-- abgebrochen


INSERT INTO concat_test (customer_id, f1, f2, f3)
SELECT customer_id, f1 + f2 + f3, f2 + f3, f1 + f2 FROM concat_test;
-- 11797 ms / 8.5 mio/s


INSERT INTO concat_test SELECT * FROM concat_test;
-- Abfrage war erfolgreich durchgeführt: 200000000 Zeilen, 17027 ms Ausführungszeit.
-- Abfrage war erfolgreich durchgeführt: 400000000 Zeilen, 33648 ms Ausführungszeit.
-- Abfrage war erfolgreich durchgeführt: 800000000 Zeilen, 66110 ms Ausführungszeit.
-- Abfrage war erfolgreich durchgeführt: 1600000000 Zeilen, 139302 ms Ausführungszeit.

select min(f1), max(f1), count(*) from concat_test

select 3200000000/77.374  
77651 