
## Building LMDB

Get the stuff:

```console
cd ~
git clone https://github.com/LMDB/lmdb.git
cd lmdb
git checkout LMDB_0.9.15
cd libraries/liblmdb/
```

Now edit `Makefile` for:

```
OPT = -O3 -march=native -mtune=native
```

and do

```console
make
```

> Note: the Makefile is a mess: it doesn't allow overriding compile flags from env var CFLAGS e.g., and the install step doesn't work properly.
