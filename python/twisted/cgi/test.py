import sys, os

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.web.twcgi import CGIScript, CGIProcessProtocol
from twisted.python import log, filepath
from twisted.web import resource, server, static


class CgiScript(CGIScript):

   def __init__(self, filename, filter):
      CGIScript.__init__(self, filename)
      self.filter = filter

   def runProcess(self, env, request, qargs = []):
      p = CGIProcessProtocol(request)
      reactor.spawnProcess(p, self.filter, [self.filter, self.filename], env, os.path.dirname(self.filename))


class CgiDirectory(resource.Resource, filepath.FilePath):

   cgiscript = CgiScript

   def __init__(self, pathname, filter):
      resource.Resource.__init__(self)
      filepath.FilePath.__init__(self, pathname)
      self.filter = filter

   def getChild(self, path, request):
      fnp = self.child(path)
      print fnp.path
      if not fnp.exists():
         return static.File.childNotFound
      elif fnp.isdir():
         return CgiDirectory(fnp.path, self.filter)
      else:
         return self.cgiscript(fnp.path, self.filter)
      return resource.NoResource()

   def render(self, request):
      notFound = resource.NoResource("CGI directories do not support directory listing.")
      return notFound.render(request)


if __name__ == '__main__':
   
   log.startLogging(sys.stdout)

   php = "/Users/oberstet/local/bin/php-cgi"
   #php = "C:\\php554\\php-cgi.exe"

   cgi = CgiDirectory("php", php)

   root = File(".")
   root.putChild("cgi", cgi)
   #root = cgi

   factory = Site(root)
   reactor.listenTCP(8880, factory)
   reactor.run()
