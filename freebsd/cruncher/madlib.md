
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
