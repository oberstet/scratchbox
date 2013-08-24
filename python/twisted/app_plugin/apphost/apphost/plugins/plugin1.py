from zope.interface import implements
from twisted.plugin import IPlugin
from apphost.interfaces import IApphostPlugin


class Plugin1(object):
    implements(IPlugin, IApphostPlugin)

    def __init__(self, name):
    	self._name = name

    def hello(self):
        return "Hello from %s" % self._name


plugin1 = Plugin1("Awesome-Plugin1")
