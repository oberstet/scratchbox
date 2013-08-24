from zope.interface import implementer
from twisted.plugin import IPlugin
from apphost.interfaces import IApphostPlugin


@implementer(IPlugin, IApphostPlugin)
class Plugin1(object):

    def __init__(self, name):
    	self._name = name

    #def hello(self):
    #    return "Hello from %s" % self._name


plugin1 = Plugin1("Awesome-Plugin1")
