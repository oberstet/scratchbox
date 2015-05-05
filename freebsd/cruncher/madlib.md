
# Installation

Getting MADlib up and running:

* build
* install
* activate (for each DB)

## Build

To **build** MADlib, run the following as user `postgres`:

```console
cd /tmp
git clone https://github.com/madlib/madlib.git
git checkout v1.7.1
CFLAGS="-O3 -march=native -mtune=native" CXXFLAGS="-O3 -march=native -mtune=native" ./configure
cd build
make
```

## Install

To **install** MADlib, run the following as user `root`:

```console
cd /tmp/madlib/build
make install
```
This will install MADlib into `/usr/local/madlib/`.

## Activate

For each database where MADlib should be available, run the following as user `postgres`:

```console
madpack -p postgres -c postgres@localhost:5432/adr install
psql -d adr -c "GRANT USAGE ON SCHEMA madlib TO PUBLIC"
```

In this example, we activate MADlib in the **adr** database for use by anyone.

## Test

To test, run the following from a database session:

```sql
SELECT madlib.normal_cdf(0);
```

This should output 0.5.

To verify the installed version:

```sql
select pg_catalog.version(), madlib.version();
```

# Programming

## Summary Statistics

MADlib includes a [summary statistics function](http://doc.madlib.net/latest/group__grp__summary.html).

> Note: Under the hood, this function will generate plain SQL. There is no C/C++ code involved, and there is no auto-parallelization with this function (it does NOT run on multiple cores).

To compute summary statistics for a table `basis.tbl_pk_konto_bda`, while storing results in (a new) table `basis.tbl_pk_konto_bda_summary`:

```sql
DROP TABLE IF EXISTS basis.tbl_pk_konto_bda_summary;

SELECT * FROM madlib.summary('basis.tbl_pk_konto_bda', 'basis.tbl_pk_konto_bda_summary');
-- Total query runtime: 170685 ms.
```

To check the results:

```sql
select * from basis.tbl_pk_konto_bda_summary;
```

To compute more extensive summary statistics:

```sql
DROP TABLE IF EXISTS basis.tbl_pk_konto_bda_summary;

SELECT * FROM madlib.summary(source_table := 'basis.tbl_pk_konto_bda',
                             output_table := 'basis.tbl_pk_konto_bda_summary',
                             target_cols := NULL,
                             grouping_cols := NULL,
                             get_distinct := TRUE,
                             get_quartiles := TRUE,
                             ntile_array := '{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9}'::float8[],
                             how_many_mfv := 5,
                             get_estimates := FALSE)
;
```

