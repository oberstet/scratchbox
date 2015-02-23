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

> Note: This is a *huge* package: long build time, pulls in lots of dependencies - like GCC!

To build R from the ports collection:

```
cd /usr/ports/math/R
make config
```

Leave all default options and add the following:

* `ATLAS`


# Java JDK

> Note: This is a *huge* package and pulls in lots of dependencies including the kitchen sink and X!. It will happily *ignore* our `/etc/make.conf` which is set up to ignore any X stuff. Don't know how to work around.

To build the OpenJDK from the port collection (probably a bad idea .. see the note):

```
cd /usr/ports/java/openjdk8
make config
make
make install clean
```

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

To automatically start PostgreSQL at server/container start:

```
echo 'postgresql_enable="YES"' >> /etc/rc.conf
```

The PostgreSQL server will run under user/group `pgsql/pgsql`.

To initialize the database, run

```
/usr/local/etc/rc.d/postgresql initdb
```

You can then start PostgreSQL by running:

```
/usr/local/etc/rc.d/postgresql start
```

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
createlang plpythonu
```

# Todo

* PL/R
* PL/V8
* MADlib
* Samba
* Nginx
* Crossbar.io


# Command hints

To list the files installed from a port or package:

```
pkg info -l postgresql94-contrib-9.4.1
```
