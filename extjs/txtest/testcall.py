import sys, json

from twisted.python import log
from twisted.internet import reactor
from twisted.web.client import getPage


def printandstop(msg):
   print msg
   reactor.stop()

if __name__ == '__main__':

   log.startLogging(sys.stdout)

   router = "http://127.0.0.1:8000/examples/direct/php/router.php"

   n = 123

   d = {'action': 'TestAction', 'method': 'multiply', 'data': [n], 'type': 'rpc', 'tid': 1}

   body = json.dumps(d)

   d = getPage(url = router,
               method = 'POST',
               postdata = body,
               headers = {'Content-Type': 'application/json'},
               timeout = 2,
               followRedirect = False)

   def onResult(r):
      res = json.loads(r)
      print "result = ", res['result']
      reactor.stop()

   d.addCallback(onResult)
   d.addErrback(printandstop)

   reactor.run()
