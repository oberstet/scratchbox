from zope.interface import implements
from twisted.plugin import IPlugin
from apphost.interfaces import IApphostPlugin


class Plugin2(object):
    implements(IPlugin, IApphostPlugin)

    def __init__(self, name):
    	self._name = name

    def hello(self):
        return "Hello from %s" % self._name


plugin2 = Plugin2("Awesome-Plugin2")
