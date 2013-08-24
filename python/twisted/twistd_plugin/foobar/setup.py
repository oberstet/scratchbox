from setuptools import setup

PROJECT = 'foobar'

setup(
   name = 'foobar',
   install_requires = ['Twisted>=Twisted-13.0'],
   packages = ['foobar', 'twisted.plugins'],
   version = '0.1',
   include_package_data = True,
   #zip_safe = True
)

# Make Twisted regenerate the dropin.cache, if possible.  This is necessary
# because in a site-wide install, dropin.cache cannot be rewritten by
# normal users.
try:
   from twisted.plugin import IPlugin, getPlugins
except ImportError:
    pass
else:
    list(getPlugins(IPlugin))
