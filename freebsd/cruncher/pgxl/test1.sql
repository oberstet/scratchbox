-- Teil 1
DROP TABLE IF EXISTS test;

-- Teil 2
CREATE TABLE test (id INT NOT NULL, foo TEXT)
DISTRIBUTE BY REPLICATION
;

-- Teil 3
INSERT INTO test (id, foo) VALUES (1, 'bar1');
INSERT INTO test (id, foo) VALUES (2, 'bar2');
INSERT INTO test (id, foo) VALUES (3, 'bar3');

-- Teil 4
SELECT COUNT(*) FROM test;


-- Teile 1-4 als 1 Block
DO $$
DECLARE
   l_cnt INT;
BEGIN
   DROP TABLE IF EXISTS test;
   CREATE TABLE test (id INT NOT NULL, foo TEXT) DISTRIBUTE BY REPLICATION;
   INSERT INTO test (id, foo) VALUES (1, 'bar1');
   INSERT INTO test (id, foo) VALUES (2, 'bar2');
   INSERT INTO test (id, foo) VALUES (3, 'bar3');
   SELECT COUNT(*) INTO l_cnt FROM test;
   RAISE NOTICE '%', l_cnt::text;
END;
$$
