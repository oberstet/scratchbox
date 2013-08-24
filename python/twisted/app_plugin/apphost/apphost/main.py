from twisted.plugin import getPlugins

import apphost
from apphost.interfaces import IApphostPlugin


def run():
   for plugin in getPlugins(IApphostPlugin, apphost.plugins):
      print plugin.hello()


if __name__ == '__main__':
   run()
