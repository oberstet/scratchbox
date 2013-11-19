# Twisted

## Base Config

### Buildbot

	buildbot.twistedmatrix.com:9987

### Buildslave

	tavendo-freebsd-9.2-amd64

### Builders

	freebsd-9.2-amd64-python2.7
	freebsd-9.2-amd64-pypy2.2
	freebsd-9.2-amd64-pypy-nightly

#### Python 2.7

This builder is **supported** by the Twisted project.

The CPython used is the latest 2.7.x from the FreeBSD ports collection (which currently is CPython 2.7.5 from [here](http://ftp.freebsd.org/pub/FreeBSD/ports/amd64/packages-9.2-release/python/python27-2.7.5_1.tbz)) rather than the system supplied CPython.

The Python used is built with Clang (not GCC).

#### PyPy 2.2

This builder is **supported** by the Twisted project.

The PyPy used is PyPy 2.2 from the FreeBSD ports collection (which currently does not yet exist, but will soon .. thanks to David Naylor, the PyPy port maintainer).

The PyPy used is built with Clang (not GCC).

#### PyPy Nightly

This builder is **unsupported** by the Twisted project.

The PyPy used is the one directly built from the PyPy source repository - the same binary built for the PyPy project.

The PyPy used is built with Clang (not GCC).

### Unix User

	bbslave_twisted

## Setup

	su -l bbslave_twisted
	buildslave create-slave --log-count 10 work buildbot.twistedmatrix.com:9987 tavendo-freebsd-9.2-amd64 <PASSWORD>
	cd work
	vi info/admin
	vi info/host
	buildslave start
	tail -f twistd.log


## Resources

 * http://twistedmatrix.com/trac/wiki/ContinuousIntegration/TestSlaveConfiguration


# PyPy

## Base Config

### Buildbot

	buildbot.pypy.org:10407

### Buildslave

	tavendo-freebsd-9.2-amd64

### Builders

	pypy-c-jit-freebsd-9-x86-64

### Unix User

	bbslave_pypy

## Setup

	su -l bbslave_pypy
	buildslave create-slave --log-count 10 work buildbot.pypy.org:10407 tavendo-freebsd-9.2-amd64 <PASSWORD>
	cd work
	vi info/admin
	vi info/host
	buildslave start

## Resources

 * http://buildbot.pypy.org/nightly/trunk/
 * https://bitbucket.org/pypy/buildbot/src/14c6a7e422d3b13695265fbc2f47917edc8ce969/README_BUILDSLAVE?at=default
 * https://bitbucket.org/pypy/buildbot/src/14c6a7e422d3b13695265fbc2f47917edc8ce969/requirements.txt?at=default



su -l bbslave_twisted
tail -f work/twistd.log

su -l bbslave_pypy
tail -f work/twistd.log

/usr/local/bin/svstat /var/service/bbslave_twisted
/usr/local/bin/svstat /var/service/bbslave_pypy

/usr/local/bin/svc -d /var/service/bbslave_twisted
/usr/local/bin/svc -d /var/service/bbslave_pypy

08:00:27:D9:BB:E9
tvd_build_txpypy
192.168.1.112

tavendo.dyndns-wiki.com:5003
