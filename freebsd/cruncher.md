# Base host setup

**Update system**

```
freebsd-update fetch
freebsd-update install
```

**Fetch/update ports collection**

```
portsnap fetch
portsnap extract
portsnap update
```

**Configure ports building**

```
cat >> /etc/make.conf << EOT
MAKE_JOBS_NUMBER=4
CPUTYPE?=native
CFLAGS= -O2 -pipe -funroll-loops
COPTFLAGS= -O2 -pipe -funroll-loops
BUILD_OPTIMIZED=YES
BUILD_STATIC=YES
WITHOUT_DEBUG=YES
WITHOUT_X11=YES
WITHOUT_FONTCONFIG=YES
OPTIONS_UNSET=X11
EOT
```

**Install some tools**

```
pkg install -y vim-lite
pkg install -y sudo
pkg install -y bash-static
pkg install -y ncurses
pkg install -y wget
pkg install -y curl
pkg install -y bzip2
pkg install -y zip
pkg install -y gtar
pkg install -y openssl
pkg install -y expat
pkg install -y sqlite3
pkg install -y libffi
pkg install -y pkg-config
pkg install -y readline
pkg install -y libxml
pkg install -y libxslt
pkg install -y gmake
pkg install -y git
```

**Install `htop`**

```
pkg install -y htop
echo "linproc /compat/linux/proc linprocfs rw,late 0 0" >> /etc/fstab
mkdir -p /usr/compat/linux/proc; ln -s /usr/compat /compat; mount linproc
```

This OpenJDK implementation requires fdescfs(5) mounted on /dev/fd and
procfs(5) mounted on /proc.

If you have not done it yet, please do the following:

mount -t fdescfs fdesc /dev/fd
mount -t procfs proc /proc

To make it permanent, you need the following lines in /etc/fstab:

```
cat >> /etc/fstab << EOT
fdesc   /dev/fd     fdescfs     rw  0   0
proc    /proc       procfs      rw  0   0
EOT
```




**Enable DTrace**

```
kldload dtraceall
echo "dtraceall_load=YES" >> /boot/loader.conf
```

**Install DTrace toolkit**

```
cd /usr/ports/sysutils/DTraceToolkit
make install clean
```

# Python

To build CPython 2.7 from ports collection:

```
cd /usr/ports/lang/python27/
make install clean
```

The Python interpreter will be created under `/usr/local/bin/python2.7`.


# V8

To build Google V8 JavaScript engine from ports collection:

```
cd /usr/ports/lang/v8
make
make install clean
```

This will create the V8 dynamic library under `/usr/local/lib/libv8.so.1`.


# Node

> Note: Make sure you have V8 build before.

To build Node from ports collection:

```
cd /usr/ports/www/node
make
make install clean
```

This will create the Node executable under `/usr/local/bin/node`.

You will want the Node package manager (`npm`) as well:

```
cd /usr/ports/www/npm
make
make install clean
```

The Node package manager exectuable will be created under `/usr/local/bin/npm`.


# OpenLDAP

To build the OpenLDAP server from the ports collection:

```
cd /usr/ports/net/openldap24-server/
make config
```

Add the following options to the already selected ones:

* `SHA2`
* `SMBPWD`

Then

```
make install clean
```

Edit the server configuration

* `/usr/local/etc/openldap/slapd.conf`

and add the following to `/etc/rc.conf`

```
cat >> /etc/rc.conf << EOT
slapd_enable="YES"
slapd_flags='-h "ldapi://%2fvar%2frun%2fopenldap%2fldapi/ ldap://0.0.0.0/"'
slapd_sockets="/var/run/openldap/ldapi"
EOT
```

To start the server:

```
/usr/local/etc/rc.d/slapd start
```

The server (by default) runs under the non-privileged user `ldap`.


# R

http://www.r-project.org/
http://www.freshports.org/math/R
https://svnweb.freebsd.org/ports/head/math/R/
http://www.freshports.org/math/libR/

> Note: This is a *huge* package: long build time, pulls in lots of dependencies - like GCC!

To build R from the ports collection:

```
cd /usr/ports/math/R
make config
```

Then

```
make
make install clean
```


Leave all default options and add the following:

* `ATLAS`


http://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software
http://math-atlas.sourceforge.net/


https://software.intel.com/en-us/intel-mkl

https://software.intel.com/en-us/intel-mkl/try-buy


# Java JDK

> Note: This is a *huge* package and pulls in lots of dependencies including the kitchen sink and X!. It will happily *ignore* our `/etc/make.conf` which is set up to ignore any X stuff. Don't know how to work around.

To build the OpenJDK from the port collection (probably a bad idea .. see the note):

```
cd /usr/ports/java/openjdk8
make config
make
make install clean
```

/usr/local/openjdk8/jre/lib/amd64/libnet.so
/usr/local/openjdk8/jre/lib/amd64/server/libjvm.so
/usr/local/openjdk8/jre/lib/amd64/libdt_socket.so
/usr/local/openjdk8/jre/lib/amd64/libnio.so

root@crunchertest:/usr/ports/java/openjdk8 # java -version
openjdk version "1.7.0_76"
OpenJDK Runtime Environment (build 1.7.0_76-b13)
OpenJDK 64-Bit Server VM (build 24.76-b04, mixed mode)


root@crunchertest:/usr/ports/java/openjdk8 # pkg info openjdk
openjdk-7.76.13_1,1
Name           : openjdk
Version        : 7.76.13_1,1
Installed on   : Tue Feb 24 09:54:53 CET 2015
Origin         : java/openjdk7
Architecture   : freebsd:10:x86:64
...



cd /usr/ports/devel/maven31
make install clean




# PostgreSQL

## Base Server

To build PostgreSQL server from the ports collection:

```
cd /usr/ports/databases/postgresql94-server/
make config
```

and add the following options to the already selected ones:

* `DTRACE`
* `INTDATE`
* `LDAP`
* `NLS`
* `OPTIMIZED_CFLAGS`
* `PAM`
* `SSL`
* `TZDATA`
* `XML`

and

```
make install clean
```

To automatically start PostgreSQL at server/container start, add the following to `/etc/rc.conf`:

```
postgresql_enable="YES"
postgresql_data="/usr/local/pgsql/data"
```

zfs create -p -o recordsize=8k -o atime=off -o exec=off -o mountpoint=/pgdata1 zroot/pgdata1
chown -R pgsql:pgsql /pgdata1




#  postgresql_enable="YES"
#  # optional
#  postgresql_data="/usr/local/pgsql/data"
#  postgresql_flags="-w -s -m fast"
#  postgresql_initdb_flags="--encoding=utf-8 --lc-collate=C"
#  postgresql_class="default"
#  postgresql_profiles=""



The PostgreSQL server will run under user/group `pgsql/pgsql`.

To initialize the database, run

```
/usr/local/etc/rc.d/postgresql initdb
```

You can then start PostgreSQL by running:

```
/usr/local/etc/rc.d/postgresql start
```


createuser -P oberstet
createdb oberstet -O oberstet


## Contrib Packages

To build the PostgreSQL contrib packages from the ports collection:

```
cd /usr/ports/databases/postgresql94-contrib
make
make install clean
```

See the README here `/usr/local/share/doc/postgresql/README-contrib`.


## PL/Python

> Note: Make sure you have CPython 2.7 build before!

To build PL/Python (which is a requirement for MADlib) from the ports collection:

```
cd /usr/ports/databases/postgresql94-plpython
make
make install clean
```

This will build the PostgreSQL language extension under `/usr/local/lib/postgresql/plpython2.so`.

To create PL/Python language extension within a PostgreSQL database:

```
su -l pgsql
createlang plpythonu
```

To activate PL/Python on a database:

```
su -l pgsql
psql -d database1
```

PL/Python is an *untrusted* language, and by default, only database superusers can *create* functions in untrusted languages.

To verify the trust status of installed languages:

```shell
$ psql -d oberstet
psql (9.4.1)
Type "help" for help.

oberstet=# select * from pg_language;
  lanname  | lanowner | lanispl | lanpltrusted | lanplcallfoid | laninline | lanvalidator | lanacl 
-----------+----------+---------+--------------+---------------+-----------+--------------+--------
 internal  |       10 | f       | f            |             0 |         0 |         2246 | 
 c         |       10 | f       | f            |             0 |         0 |         2247 | 
 sql       |       10 | f       | t            |             0 |         0 |         2248 | 
 plpgsql   |       10 | t       | t            |         12172 |     12173 |        12174 | 
 plpythonu |       10 | t       | f            |         16393 |     16394 |        16395 | 
(5 rows)
```

To change the trust status, so all users on a database can create functions in an untrusted language:

```
UPDATE pg_language SET lanpltrusted = true WHERE lanname = 'plpythonu';
```


## PL/V8

> Note: You will need V8 build before.

[PL/V8](https://code.google.com/p/plv8js/) is a JavaScript procedural language extension for PostgreSQL using the V8 engine under the hood. For build instructions, see [here](https://code.google.com/p/plv8js/wiki/PLV8).


## PL/R

[PL/R](http://www.joeconway.com/plr/) is a R procedural language extension for PostgreSQL. For build instructions see [here](https://github.com/jconway/plr) and [here](http://www.joeconway.com/plr/doc/plr-install.html).

cd /tmp
wget http://www.joeconway.com/plr/plr-8.3.0.16.tar.gz
tar xvzf plr-8.3.0.16.tar.gz

## MADlib

[MADlib](http://madlib.net/) is an in-database machine learning library for PostgreSQL. See the build instructions [here](https://github.com/madlib/madlib/wiki/Installation-Guide) and [building from source](https://github.com/madlib/madlib/wiki/Building-MADlib-from-Source).


MADlib currently has no support for 9.4 (http://jira.madlib.net/browse/MADLIB-894)

http://comments.gmane.org/gmane.comp.statistics.madlib.devel/298

ls -la /usr/local/madlib/Versions/1.7/ports/postgres/

> There should be a directory for each major version of postgres supported by
your build, if there is not a 9.4 directory then you did not successfully
build a 9.4 compatible version of MADlib.


cd /tmp
wget --no-check-certificate https://github.com/madlib/madlib/archive/v1.7.0.tar.gz
tar xvzf v1.7.0.tar.gz
cd v1.7.0
setenv CC `which clang`
setenv CXX `which clang`
ln -s /usr/local/bin/python2.7 /usr/local/bin/python
ln -s /usr/local/bin/bash /bin/bash
./configure
gmake
sudo gmake install


setenv CC `which gcc48`
setenv CXX `which g++48`

cd /usr/ports/lang/gcc48
make install clean

pkg add gmake gcc48

export CC=`which gcc48`
export CXX=`which g++48`



cd /usr/ports/devel/boost-all/
make install clean


cd /usr/ports/math/eigen3/


$ find /usr/local/madlib/Current/ports/postgres/9.4/
/usr/local/madlib/Current/ports/postgres/9.4/
/usr/local/madlib/Current/ports/postgres/9.4/lib
/usr/local/madlib/Current/ports/postgres/9.4/lib/libmadlib.so
/usr/local/madlib/Current/ports/postgres/9.4/modules
/usr/local/madlib/Current/ports/postgres/9.4/modules/lda
/usr/local/madlib/Current/ports/postgres/9.4/modules/lda/lda.py
/usr/local/madlib/Current/ports/postgres/9.4/modules/lda/__init__.py
...

$ ldd /usr/local/madlib/Current/ports/postgres/9.4/lib/libmadlib.so
/usr/local/madlib/Current/ports/postgres/9.4/lib/libmadlib.so:
    libstdc++.so.6 => /usr/local/lib/gcc48/libstdc++.so.6 (0x801ae4000)
    libm.so.5 => /lib/libm.so.5 (0x801e00000)
    libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x802028000)
    libc.so.7 => /lib/libc.so.7 (0x80081f000)


$ /usr/local/madlib/Versions/1.7.1/bin/madpack -p postgres -c pgsql@localhost:5432/oberstet install
Password for user pgsql: 
madpack.py : INFO : Detected PostgreSQL version 9.4.
madpack.py : INFO : *** Installing MADlib ***
madpack.py : INFO : MADlib tools version    = 1.7.1 (/usr/local/madlib/Versions/1.7.1/bin/../madpack/madpack.py)
madpack.py : INFO : MADlib database version = None (host=localhost:5432, db=oberstet, schema=madlib)
madpack.py : INFO : Testing PL/Python environment...
madpack.py : INFO : > PL/Python environment OK (version: 2.7.9)
madpack.py : INFO : Installing MADlib into MADLIB schema...
madpack.py : INFO : > Creating MADLIB schema
madpack.py : INFO : > Creating MADLIB.MigrationHistory table
madpack.py : INFO : > Writing version info in MigrationHistory table
madpack.py : INFO : > Creating objects for modules:
madpack.py : INFO : > - array_ops
madpack.py : INFO : > - bayes
madpack.py : INFO : > - crf
madpack.py : INFO : > - elastic_net
madpack.py : INFO : > - linalg
madpack.py : INFO : > - pmml
madpack.py : INFO : > - prob
madpack.py : INFO : > - quantile
madpack.py : INFO : > - sketch
madpack.py : INFO : > - stats
madpack.py : INFO : > - svd_mf
madpack.py : INFO : > - svec
madpack.py : INFO : > - tsa
madpack.py : INFO : > - conjugate_gradient
madpack.py : INFO : > - data_profile
madpack.py : INFO : > - lda
madpack.py : INFO : > - svec_util
madpack.py : INFO : > - utilities
madpack.py : INFO : > - assoc_rules
madpack.py : INFO : > - cart
madpack.py : INFO : > - convex
madpack.py : INFO : > - glm
madpack.py : INFO : > - kernel_machines
madpack.py : INFO : > - linear_systems
madpack.py : INFO : > - recursive_partitioning
madpack.py : INFO : > - regress
madpack.py : INFO : > - sample
madpack.py : INFO : > - summary
madpack.py : INFO : > - kmeans
madpack.py : INFO : > - pca
madpack.py : INFO : > - validation
madpack.py : INFO : MADlib 1.7.1 installed successfully in MADLIB schema.




$ psql oberstet
psql (9.4.1)
Type "help" for help.

oberstet=# GRANT USAGE ON SCHEMA madlib TO PUBLIC;
GRANT
oberstet=# 




## PostgreSQL XL

[PostgreSQL XL](http://www.postgres-xl.org/). See the [documentation](http://files.postgres-xl.org/documentation/index.html).


## Samba

Write me.

## Web Server

Write me.


## GitLab

Write me.


## Apache Solr

Write me.


# Command hints

To list the files installed from a port or package:

```
pkg info -l postgresql94-contrib-9.4.1
```

# Cmake

Building R requires Cmake as a dependency, which triggers the following issue:

```
root@crunchertest:/usr/ports/devel/cmake # make
===>  Staging for cmake-3.1.3
===>   cmake-3.1.3 depends on file: /usr/local/share/cmake/Modules/CMake.cmake - found
===>   cmake-3.1.3 depends on shared library: libcurl.so - found (/usr/local/lib/libcurl.so.4.3.0)
===>   cmake-3.1.3 depends on shared library: libexpat.so - found (/usr/local/lib/libexpat.so.1.6.0)
===>   Generating temporary packing list
make[2]: don't know how to make install/strip. Stop

make[2]: stopped in /usr/ports/devel/cmake/work/cmake-3.1.3
*** Error code 2

Stop.
make[1]: stopped in /usr/ports/devel/cmake
*** Error code 1

Stop.
make: stopped in /usr/ports/devel/cmake
```

To work around, comment the following line in `/usr/ports/devel/cmake/Makefile`:

```
.if defined(STRIP) && ${STRIP} != "" && !defined(WITH_DEBUG)
#INSTALL_TARGET=        install/strip
.endif
```


# Apache Solr

http://mirror.synyx.de/apache/lucene/solr/ref-guide/apache-solr-ref-guide-5.0.pdf

http://lucene.apache.org/solr/
http://www.freshports.org/textproc/apache-solr/

cd /usr/ports/textproc/apache-solr
make install clean


http://netty.io/
https://svnweb.freebsd.org/ports/head/java/netty/
http://www.freshports.org/java/netty/



root@crunchertest:/usr/ports/textproc/apache-solr # /usr/local/openjdk8/bin/java -version
openjdk version "1.8.0_31"
OpenJDK Runtime Environment (build 1.8.0_31-b13)
OpenJDK 64-Bit Server VM (build 25.31-b07, mixed mode)
root@crunchertest:/usr/ports/textproc/apache-solr # /usr/local/openjdk7/bin/java -version
openjdk version "1.7.0_76"
OpenJDK Runtime Environment (build 1.7.0_76-b13)
OpenJDK 64-Bit Server VM (build 24.76-b04, mixed mode)



root@crunchertest:/usr/ports/textproc/apache-solr # pkg info -l apache-solr
apache-solr-4.10.1:
    /usr/local/etc/rc.d/solr
    /usr/local/share/examples/apache-solr/README.txt
...





# Testing MADlib

select madlib.array_mean(array[1,2,3]);

select madlib.normal_cdf(0);




http://cran.r-project.org/doc/manuals/r-release/R-admin.html#Installing-R-under-Unix_002dalikes


export CC=`which gcc48`
export CXX=`which g++48`
export CFLAGS="-march=native -O2 -pipe -funroll-loops"
export CXXFLAGS="-march=native -O2 -pipe -funroll-loops"

./configure --enable-R-shlib


R:
cd /usr/ports/math/R
make config

OPTIONS:
ATLAS
LIBR
PCRE_PORT
THREADS

make install clean


root@crunchertest:/usr/ports/math/R # ldd /usr/local/lib/R/lib/libR.so
/usr/local/lib/R/lib/libR.so:
    libquadmath.so.0 => /usr/local/lib/gcc48/libquadmath.so.0 (0x801969000)
    libm.so.5 => /lib/libm.so.5 (0x801bb6000)
    libf77blas.so.2 => /usr/local/lib/libf77blas.so.2 (0x801dde000)
    libgfortran.so.3 => /usr/local/lib/gcc48/libgfortran.so.3 (0x801ffc000)
    libintl.so.8 => /usr/local/lib/libintl.so.8 (0x80246c000)
    libreadline.so.6 => /usr/local/lib/libreadline.so.6 (0x802676000)
    libpcre.so.1 => /usr/local/lib/libpcre.so.1 (0x8028c0000)
    liblzma.so.5 => /usr/lib/liblzma.so.5 (0x802b33000)
    libbz2.so.1 => /usr/local/lib/libbz2.so.1 (0x802d58000)
    libz.so.6 => /lib/libz.so.6 (0x802f69000)
    libgomp.so.1 => /usr/local/lib/gcc48/libgomp.so.1 (0x80317f000)
    libthr.so.3 => /lib/libthr.so.3 (0x80338e000)
    libc.so.7 => /lib/libc.so.7 (0x80081f000)
    libatlas.so.2 => /usr/local/lib/libatlas.so.2 (0x8035b3000)
    libgcc_s.so.1 => /usr/local/lib/gcc48/libgcc_s.so.1 (0x804082000)
    libncurses.so.8 => /lib/libncurses.so.8 (0x804299000)



root@crunchertest:/usr/ports/math/R # which R
/usr/local/bin/R

root@crunchertest:/usr/ports/math/R # R --version
R version 3.0.2 Patched (2013-11-12 r64207) -- "Frisbee Sailing"
Copyright (C) 2013 The R Foundation for Statistical Computing
Platform: amd64-portbld-freebsd10.1 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
http://www.gnu.org/licenses/.





http://www.postgresql.org/docs/9.4/static/extend-pgxs.html
/usr/local/bin/pg_config


tar xvzf ../tarballs/plr-8.3.0.16.tar.gz
cd plr
export USE_PGXS=1
gmake
su
gmake install


$ ldconfig -r | grep libR
    281:-lR.1 => /usr/local/lib/R/lib/libR.so.1


/etc/rc.d/ldconfig restart


root@crunchertest:/usr/home/oberstet/build/plr # gmake install
/bin/mkdir -p '/usr/local/lib/postgresql'
/bin/mkdir -p '/usr/local/share/postgresql/extension'
/bin/mkdir -p '/usr/local/share/postgresql/extension'
/bin/mkdir -p '/usr/local/share/doc/postgresql/extension'
/usr/bin/install -c -o root -g wheel -m 755  plr.so '/usr/local/lib/postgresql/plr.so'
/usr/bin/install -c -o root -g wheel -m 644 plr.control '/usr/local/share/postgresql/extension/'
/usr/bin/install -c -o root -g wheel -m 644 plr--8.3.0.16.sql plr--unpackaged--8.3.0.16.sql plr.sql '/usr/local/share/postgresql/extension/'
/usr/bin/install -c -o root -g wheel -m 644 README.plr '/usr/local/share/doc/postgresql/extension/'


cat /usr/local/share/postgresql/extension/plr.sql


/usr/local/lib/R/lib/


psql --dbname=oberstet < /usr/local/share/postgresql/extension/plr.sql



$ psql --dbname=oberstet 
psql (9.4.1)
Type "help" for help.

oberstet=#  CREATE EXTENSION plr;
ERROR:  function "plr_call_handler" already exists with same argument types
oberstet=# select * from pg_language;
  lanname  | lanowner | lanispl | lanpltrusted | lanplcallfoid | laninline | lanvalidator | lanacl 
-----------+----------+---------+--------------+---------------+-----------+--------------+--------
 internal  |       10 | f       | f            |             0 |         0 |         2246 | 
 c         |       10 | f       | f            |             0 |         0 |         2247 | 
 sql       |       10 | f       | t            |             0 |         0 |         2248 | 
 plpgsql   |       10 | t       | t            |         12172 |     12173 |        12174 | 
 plpythonu |       10 | t       | t            |         16393 |     16394 |        16395 | 
 plr       |       10 | t       | f            |         18063 |         0 |            0 | 
(6 rows)

oberstet=# 
oberstet=# UPDATE pg_language SET lanpltrusted = true WHERE lanname = 'plr';
UPDATE 1
oberstet=# 


SELECT r_version();

CREATE OR REPLACE FUNCTION r_max (integer, integer) RETURNS integer
AS
'
    if (arg1 > arg2)
       return(arg1)
    else
       return(arg2)
'
LANGUAGE 'plr' STRICT;

SELECT r_max(2,3);


CREATE OR REPLACE FUNCTION r_sd (float[]) RETURNS float
AS
'
   return(sd(arg1))
'
LANGUAGE 'plr' STRICT;

SELECT r_sd(array[1.2, 3.4, 5.0, 9.9]);

SELECT generate_series(5, 23);

SELECT r_sd(array_agg(generate_series)) FROM generate_series(5, 23);




PL/V8
PL/Java
R Studio Server


# iPython

OS container: iPython notebook server

http://ipython.org/
http://www.numpy.org/
http://www.scipy.org/
http://scikit-learn.org/
http://ipython-books.github.io/


http://nbviewer.ipython.org/gist/z-m-k/4484816/ipyD3sample.ipynb
http://nbviewer.ipython.org/github/dboyliao/cookbook-code/blob/master/notebooks/chapter06_viz/04_d3.ipynb
http://jakevdp.github.io/blog/2014/01/10/d3-plugins-truly-interactive/


oberstet@thinkpad-t430s:~$ ipython notebook
2015-02-26 14:21:23.540 [NotebookApp] Using existing profile dir: u'/home/oberstet/.config/ipython/profile_default'
2015-02-26 14:21:23.542 [NotebookApp] Using system MathJax
2015-02-26 14:21:23.552 [NotebookApp] Serving notebooks from local directory: /home/oberstet
2015-02-26 14:21:23.552 [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
2015-02-26 14:21:23.552 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).



# R Studio Server

OS container: R Studio server


https://support.rstudio.com/hc/en-us/articles/200552306-Getting-Started


wget --no-check-certificate https://github.com/rstudio/rstudio/tarball/v0.98.507



# SQL Workbench

cd $HOME
mkdir sqlworkbench
cd sqlworkbench
wget http://www.sql-workbench.net/Workbench-Build117.zip
unzip Workbench-Build117.zip
wget https://jdbc.postgresql.org/download/postgresql-9.4-1201.jdbc41.jar
chmod +x sqlwbconsole.sh
chmod +x sqlworkbench.sh
./sqlworkbench.sh

