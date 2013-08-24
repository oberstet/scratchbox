# Twisted Plugin Template

A minimal Twisted `twistd` service plugin template.

## Directory structure

Plugin Package:

	./foobar/foobar/main.py
	./foobar/foobar/__init__.py

Plugin Hook:

	./foobar/twisted/plugins/foobar_plugin.py

Packaging:

	./foobar/MANIFEST.in
	./foobar/setup.py

## Background

 * [The Twisted Plugin System](https://twistedmatrix.com/documents/current/core/howto/plugin.html)
 * [Writing a twistd Plugin](http://twistedmatrix.com/documents/current/core/howto/tap.html)
 * [Here](https://bitbucket.org/jerub/twisted-plugin-example/src)
 * [Here](http://krondo.com/?p=2345)
 * [Here](http://stackoverflow.com/questions/7275295/how-do-i-write-a-setup-py-for-a-twistd-twisted-plugin-that-works-with-setuptools)

