

# PyPy

Python, the *language*, has different *implementations*, including:

 * [CPython](http://www.python.org/)
 * [PyPy](http://pypy.org/)
 * [Jython](http://jython.org/)
 * [IronPython](http://ironpython.net/)

PyPy is an implementation of the Python language which includes a [JIT compiler](http://en.wikipedia.org/wiki/Just-in-time_compilation) that produces high-performance machine code *at run-time*.

We will use PyPy for all load testing and performance benchmarking, and we will run under **Linux/x64** (or **FreeBSD/amd64**).

*Notes.*

> 1. **Comparing Python implementations**: In general, you neither can nor should expect the results obtained with PyPy to be reproducable with those obtained using a different Python implementation.
>
> 2. **JIT Warmup**: Since PyPy is using a JIT compilation model, it is very important to do a couple of "dry" test runs with *representative load* against a testee running under PyPy *before* actually recording test results - and *without* restarting the testee in between. This allows the JIT compiler generate machine code on hot code paths.
>The same applies to Java HotSpot. It does not apply to C++ (using a ahead-of-time compiler).
>
> 3. **Comparing PyPy versions**: PyPy is a very active and fast moving project. Comparing the results obtained from using a current PyPy to those from a 6 months old PyPy is of limited significance and interest. You will be living on the bleeding edge.
> 4. **Comparing PyPy on different platforms**: We are benchmarking heavy networking artillery here. We need an OS with a capable TCP/IP stack and first-class support in PyPy and Twisted (see below). This boils down to Linux (and FreeBSD, probably NetBSD/OpenBSD) right now. OSX falls out of that list since it's networking stack is mediocre. Windows is out since PyPy and Twisted support is suboptimal (it lacks certain bits). Comparing PyPy/Linux and PyPy/FreeBSD however **is** of interest.

## Installing PyPy

In general, the PyPy version that comes with your distro is likely out of date. Don't waste time on it. You should get a current binary from the PyPy website or build from source.

### Installing from binary

Get the bleeding edge (I am using this .. yes, I like the thrill):

	cd ~/tarballs
	wget http://buildbot.pypy.org/nightly/trunk/pypy-c-jit-latest-linux64.tar.bz2

Or (alternatively) - get the latest release:

	cd ~/tarballs
	wget https://bitbucket.org/pypy/pypy/downloads/pypy-2.1-linux64.tar.bz2

Unpack the thing:

	cd ~
	tar xvjf tarballs/pypy-c-jit-latest-linux64.tar.bz2

Now modify your `PATH` (replacing the hash value with what you got):

	vi ~/.bashrc

      export PATH=${HOME}/pypy-c-jit-67840-934879cb2719-linux64/bin:${PATH}
      export LD_LIBRARY_PATH=${HOME}/pypy-c-jit-67840-934879cb2719-linux64/lib:${LD_LIBRARY_PATH}

   source ~/.bashrc

and verify that the correct PyPy binary is found:

	which pypy
	pypy -V

### Installing from source

This is for advanced users - you can read more [here](http://pypy.org/download.html) and [here](http://pypy.readthedocs.org/en/latest/getting-started-python.html#translating-the-pypy-python-interpreter). Building from source will require >4GB RAM and ~30 mins on a fast (!) machine.

The short version follows.

Get the deps (Ubuntu/Debian):

	sudo apt-get install \
		hg gcc make python-dev libffi-dev libsqlite3-dev pkg-config \
		libz-dev libbz2-dev libncurses-dev libexpat1-dev \
		libssl-dev libgc-dev python-sphinx python-greenlet

Get the deps (FreeBSD):

	write me

Tweak your env (FreeBSD):

	export PATH=${HOME}/local/bin:/usr/local/bin:${PATH}
	export LD_LIBRARY_PATH=${HOME}/local/lib:/usr/local/lib:${LD_LIBRARY_PATH}
	export CC=/usr/bin/clang
	export CXX=/usr/bin/clang++
	export CPP=/usr/bin/clang-cpp
	export MAKEFLAGS=-j8
	export CFLAGS="-O3 -march=native"
	export LDFLAGS="-L${HOME}/local/lib -L/usr/local/lib"

Get the repo and build:

	cd ~/build
	hg clone https://bitbucket.org/pypy/pypy
	cd pypy/pypy/goal
	pypy ../../rpython/bin/rpython -Ojit targetpypystandalone

> Note that we use PyPy - say an old version from your distro - to build a new PyPy. You can use a CPython to build PyPy also, but it will take much, much longer.
>

Package up:

	cd ~/build
	cd pypy/pypy/tool/release/
	python package.py ../../.. pypy-my-own-package-name

Now your package will reside somewhere

	/tmp/..

For installation follow the instructions as in the binary install (just unpack the `.tar.bz2` somewhere like in your `$HOME`).

## Installing Python packages under PyPy

### Installing packages from PyPI

To install Python packages from the [Python package repository (PyPI)](https://pypi.python.org/pypi), we first do:

	wget --no-check-certificate https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | pypy

You should now verify that a `easy_install` script is found *that resides under your PyPy* installation (in the `bin` directory next to the `pypy` executable):

	which easy_install

Now we can install other packages needed, e.g. the latest [Twisted](http://twistedmatrix.com/) release, simply like this:

	easy_install twisted

Or for installing [AutobahnPython](http://autobahn.ws/python/) and [AutobahnTestSuite](http://autobahn.ws/testsuite/) latest release (*however see below!*):

	easy_install autobahn
	easy_install autobahntestsuite

The `easy_install` tool will fetch any dependencies automatically over the net and install those first.

### Installing packages from source

Lots of stuff that we will do is bleeding edge, so you will want to know how to get sources from an upstream source repository and install Python packages from that.

Here is how you get AutobahnPython source and install into PyPy:

	cd ~/scm
	git clone git@github.com:tavendo/AutobahnPython.git
	cd AutobahnPython/autobahn
	pypy setup.py install

Similar for AutobahnTestSuite:

	cd ~/scm
	git clone git@github.com:tavendo/AutobahnTestSuite.git
	cd AutobahnTestSuite/autobahntestsuite
	pypy setup.py install

In general, a Python module(s) that is properly packaged will have a `setup.py` file, and running this through the Python executable of your choice will install the package into that Python environment.

> **Pro tip:** if you do deal with Python on a daily basis, I recommend you have a look a [Virtualenv](http://www.virtualenv.org).
