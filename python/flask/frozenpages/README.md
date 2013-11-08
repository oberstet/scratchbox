# Frozen Flask and Flask-FlatPages

This follows the very good example [here](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/). Read the latter and try as follows.

> The is only one minor thing that needed to be changed vs above blog post (the import needs to be `from flask_flatpages import FlatPages`, not `from flaskext.flatpages`) import FlatPages
> 


Install:

	easy_install -U Flask Frozen-Flask Flask-FlatPages

Try:

	make test

Freeze and test:

	make freeze_and_test

Cleanup:

	make clean

# Sphinx and Flask

Todo: readup stuff [here](http://sphinx-doc.org/web/quickstart.html). That describes hooks we can use to integrate Sphinx stuff Flask, and then freeze out using FrozenFlask.

