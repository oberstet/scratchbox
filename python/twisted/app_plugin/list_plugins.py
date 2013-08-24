from twisted.plugin import getPlugins

import apphost
from apphost.interfaces import IApphostPlugin

for plugin in getPlugins(IApphostPlugin, apphost.plugins):
	print plugin, plugin.hello()
