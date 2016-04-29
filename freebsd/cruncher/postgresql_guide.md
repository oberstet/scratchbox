# PostgreSQL Programming

## Control Flow

```sql
DO LANGUAGE plpgsql
$$
DECLARE
    l_foo INT := 0;
BEGIN
    IF l_foo = 0 THEN
        NULL;
    ELSIF l_foo = 1 THEN
        NULL;
    ELSE
        NULL;
    END IF;
END;
$$
```

## Idioms

### JSONB manipulation

```sql
-- http://stackoverflow.com/a/23500670
DO LANGUAGE plpgsql
$$
DECLARE
    l_res JSONB := '{}';
BEGIN
    l_res := l_res || jsonb '{"running_before": 23}';
    l_res := l_res || jsonb '{"running_after": 0}';
    RAISE NOTICE '%', l_res::text;
END
$$
```

### Iterating over arrays

```sql
DO LANGUAGE plpgsql
$$
DECLARE
    i INT;
    arr INT[] := array[1, 2, 3];
BEGIN
   FOREACH i IN ARRAY arr
   LOOP
      RAISE NOTICE '%, %', i, arr[i];
   END LOOP;
END
$$
```

### Catching exceptions

```sql
DO LANGUAGE plpgsql
$$
DECLARE
    l_stats JSONB;
BEGIN
    BEGIN
        SELECT svc_sqlbalancer.f_process_stats() INTO l_stats;
    EXCEPTION
        -- ERROR:  function svc_sqlbalancer.f_process_stats() does not exist
        WHEN SQLSTATE '42883' THEN
            NULL;
        WHEN OTHERS THEN
            RAISE;
    END;
END;
$$
```

### Loop a statement from a shell script

```shell
#!/bin/sh

while true; do psql -U oberstet -d adr -c "SELECT now()::text"; sleep 2; done
```

### Size of all Schemata

```sql
select schemaname, pg_size_pretty(SUM(pg_table_size(schemaname || '.' || tablename))) from pg_tables
where schemaname not like 'pg_temp%'
group by schemaname
order by 1
```

### Export Schemata to Flat-files

```sql
DO LANGUAGE plpgsql
$$
DECLARE
    l_rec RECORD;
    l_sql TEXT;
BEGIN
    FOR l_rec IN (
        select schemaname || '.' || tablename as tabname from pg_tables
        where schemaname in ('test_pk', 'test_pk_partitions')
        order by 1
    )
    LOOP
        l_sql := 'COPY ' || l_rec.tabname || ' TO PROGRAM ''/bin/bzip2 > /result/backup/adr_test_pk_export/' || l_rec.tabname || '.csv.bz2''';
        EXECUTE(l_sql);
        RAISE NOTICE '% exported', l_rec.tabname;
    END LOOP;
END;
$$
```

### Anonymous Block

```sql
DO LANGUAGE plpgsql
$$
BEGIN
    RAISE NOTICE 'Hello, world!';
END;
$$
```

### Kicking Users

```sql
select usename, count(*) from pg_stat_activity group by usename;

SELECT pg_terminate_backend(pid) FROM pg_stat_activity where usename not in ('postgres', 'sqlbalancer_master', 'sqlbalancer_worker', 'petzoldm', 'oberstet', 'petrovb', 'wolfp', 'doroszs')
```

### Logging

For logging configuration, see [here](http://www.postgresql.org/docs/current/static/runtime-config-logging.html).

To get the current logging facility (see [here](http://blog.endpoint.com/2014/11/dear-postgresql-where-are-my-logs.html)):

```sql
show log_destination;
```

For `syslog` logging:

```sql
show syslog_facility;
show syslog_ident;
```

### Database and Table Size

Get size of a database:

```sql
select pg_size_pretty(pg_database_size('adr'))
```

Get size of a table (excluding indices):

```sql
select pg_size_pretty(pg_table_size('basis_partitions.tbl_pk_kunde_201401'))
```

Get total size of all indices on a table:

```sql
select pg_size_pretty(pg_indexes_size('basis_partitions.tbl_pk_kunde_201401'))
```

### Looping

```sql
DO LANGUAGE plpgsql
$$
DECLARE
   i INT := 0;
BEGIN
   WHILE i < 10
   LOOP
      i := i + 1;
   END LOOP;
END;
$$
```

or

```sql
DO LANGUAGE plpgsql
$$
DECLARE
    l_rec RECORD;
    l_sql TEXT;
BEGIN
    FOR l_rec IN (select schemaname || '.' || tablename AS tabname from pg_tables where schemaname = 'cleans' and tablename like 'tbl_%')
    LOOP
        l_sql := 'DROP TABLE ' || l_rec.tabname;
        RAISE NOTICE '%', l_sql;
    END LOOP;
END;
$$
```

### Conditionals

```sql
IF EXISTS (SELECT 1 FROM people WHERE person_id = my_person_id) THEN
  -- do something
END IF;
```

# Shutdown

http://rhaas.blogspot.de/2015/03/postgresql-shutdown.html

```console
psql -c CHECKPOINT && pg_ctl stop -m fast
```

```console
systemctl stop postgresql
```

Hard (!) killing all processes by user `postgres`:

```console
sudo pkill -9 -e -u postgres
```


# Tuning

* http://thebuild.com/presentations/not-my-job.pdf
* 

# Listing PostgreSQL Processes

Here are the PostgreSQL background processes and 2 client processes running:

```console
bvr-sql18:/home/oberstet # pgrep -au postgres
9461 /usr/lib/postgresql94/bin/postgres -D /var/lib/pgsql/data
9462 postgres: logger process                                 
9467 postgres: checkpointer process                           
9468 postgres: writer process                                 
9469 postgres: wal writer process                             
9470 postgres: autovacuum launcher process                    
9471 postgres: stats collector process                        
9511 postgres: oberstet postgres ::1(39237) idle              
9512 postgres: oberstet adr ::1(39238) idle                   
```

To watch PostgreSQL processes in `htop`, call

```console
htop -u postgres
```


# Log in as superuser

To log into PostgreSQL as database superuser (aka "DBA"), SSH into the server using
your personal account, su to root, then su to pgsql:

```console
$ su
Password:
root@crunchertest:/usr/home/oberstet # su -l pgsql
$ psql -d postgres
psql (9.4.1)
Type "help" for help.

postgres=#
```

# Change superuser password

```console
$ psql -d postgres
psql (9.4.1)
Type "help" for help.

postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD '123456';
```

# Listing database users

```console
$ psql -d postgres
psql (9.4.1)
Type "help" for help.

postgres=# SELECT * FROM pg_user;
 usename  | usesysid | usecreatedb | usesuper | usecatupd | userepl |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+-----------+---------+----------+----------+-----------
 oberstet |    16384 | f           | f        | f         | f       | ******** |          |
 eppk     |    18082 | f           | f        | f         | f       | ******** |          |
 pgsql    |       10 | t           | t        | t         | t       | ******** |          |
(3 rows)

postgres=#
```

# Activate File FDW in a database

```console
$ psql -d eppk
psql (9.4.1)
Type "help" for help.

eppk=# CREATE EXTENSION file_fdw;
CREATE EXTENSION
eppk=#
```

# Create a FDW table for flat-files

You need to create a "server" _once_:

```console
CREATE SERVER raw_data FOREIGN DATA WRAPPER file_fdw;
```

Create a flat-file on the server:

```
$ cat /tmp/file1.csv
1,2,"a,sdasd",5
3,4,"kdh""jfgd",9
```

Then, to create a table on a flat-file:

```console
CREATE FOREIGN TABLE file1
(
   f1 INT,
   f2 INT,
   f3 TEXT,
   f4 INT
)
SERVER raw_data
OPTIONS (filename '/tmp/file1.csv', format 'csv', quote '"');

SELECT * FROM file1;
```

To drop a FDW table:

```console
DROP FOREIGN TABLE file1;
```

## References

* http://www.postgresql.org/docs/current/static/sql-createforeigntable.html
* http://www.postgresql.org/docs/current/static/file-fdw.html

# Partitioning

* http://www.postgresql.org/docs/current/static/ddl-partitioning.html

# Using PostgreSQL from R Studio (Desktop)

```
install.packages("RPostgreSQL")

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname="oberstet", host="bvr-sql18", port=5432, user="oberstet", password="123456")

dbExistsTable(con, c("public","test1"))
myTable <- dbReadTable(con, c("public","test1"))
```

# Using psql from Command Line

```
$ "C:\Prg\pgAdmin III\1.20\psql.exe" -h bvr-sql18 -d oberstet -U oberstet
psql (9.4.0, server 9.4.1)
WARNING: Console code page (850) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

oberstet=> select * from test1;
 f1  | f2
-----+----
 foo | 23
 foo | 23
 foo | 23
 foo | 23
(4 rows)


oberstet=>
```

# Autovacuum


>  Hi,
> after a server crash the following messages appear in the log file every
> minute:
>


> 2013-06-25 15:02:15 CEST [::18264:1:] LOG:  autovacuum: found orphan temp
> table "pg_temp_47"."est_backup_ids_temp" in database "estudis1314"
> 2013-06-25 15:02:15 CEST [::18264:2:] LOG:  autovacuum: found orphan temp
> table "pg_temp_47"."est_backup_files_temp" in database "estudis1314"


select relname,nspname from pg_class join pg_namespace on (relnamespace=
pg_namespace.oid) where pg_is_other_temp_schema(relnamespace);

On finding you can drop those schemas,if you want to get rid of the
messages, just do DROP SCHEMA pg_temp_NNN CASCADE;


select distinct nspname from pg_class join pg_namespace on (relnamespace=
pg_namespace.oid) where pg_is_other_temp_schema(relnamespace) order by 1;

DROP SCHEMA pg_temp_2 CASCADE;

