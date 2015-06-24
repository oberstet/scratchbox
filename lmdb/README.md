
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

The 3 important files we will need are

```console
oberstet@bvr-sql18:~/scm/lmdb/libraries/liblmdb> ls -la lmdb.h liblmdb.so liblmdb.a
-rw-r--r-- 1 oberstet users 596532 Jun 24 17:21 liblmdb.a
-rwxr-xr-x 1 oberstet users 287473 Jun 24 17:21 liblmdb.so
-rw-r--r-- 1 oberstet users  71462 Jun 23 16:25 lmdb.h
```

When stripping the SO, we can get it down to 80kB:

```console
oberstet@bvr-sql18:~/scm/lmdb/libraries/liblmdb> strip liblmdb.so
oberstet@bvr-sql18:~/scm/lmdb/libraries/liblmdb> size liblmdb.so
   text    data     bss     dec     hex filename
  75810    1424       8   77242   12dba liblmdb.so
oberstet@bvr-sql18:~/scm/lmdb/libraries/liblmdb> ls -la liblmdb.so
-rwxr-xr-x 1 oberstet users 80696 Jun 24 17:27 liblmdb.so
```

This is very nice. LMDB is **tiny**.

