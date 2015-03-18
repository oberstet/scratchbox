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

postgres=# ALTER USER pgsql WITH ENCRYPTED PASSWORD '123456';
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

http://www.postgresql.org/docs/current/static/ddl-partitioning.html



# Using PostgreSQL from R Studio (Desktop)

```
install.packages("RPostgreSQL")

library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname="oberstet", host="bvr-sql18", port=5432, user="oberstet", password="23664775")

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