from twisted.python import usage
from twisted.application.service import MultiService

__all__ = ['makeService', 'Options']


class Options(usage.Options):
   pass


class FoobarService(MultiService):
   def startService(self):
      MultiService.startService(self)


def makeService(options):
   return FoobarService()
