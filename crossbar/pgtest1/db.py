from txpostgres import txpostgres

from twisted.internet.defer import inlineCallbacks, returnValue

from autobahn import wamp
from autobahn.twisted.wamp import ApplicationSession



class MyDatabaseComponent(ApplicationSession):

   @inlineCallbacks
   def onJoin(self, details):

      ## create a new database connection pool. connections are created lazy (as needed)
      ## see: https://twistedmatrix.com/documents/current/api/twisted.enterprise.adbapi.ConnectionPool.html
      ##
      pool = txpostgres.ConnectionPool(None,
                                       host = '127.0.0.1',
                                       port = 5432,
                                       database = 'test',
                                       user = 'testuser',
                                       password = 'testuser')

      yield pool.start()
      print("DB connection pool started")

      ## we'll be doing all database access via this database connection pool
      ##
      self.db = pool

      ## register all procedures on this class which have been
      ## decorated to register them for remoting.
      ##
      regs = yield self.register(self)
      print("registered {} procedures".format(len(regs)))


   @wamp.register(u'com.example.now.v1')
   def get_dbnow(self):
      ## this variant demonstrates basic usage for running queries

      d = self.db.runQuery("SELECT now()")

      def got(rows):
         res = "{0}".format(rows[0][0])
         return res

      d.addCallback(got)
      return d


   @wamp.register(u'com.example.now.v2')
   @inlineCallbacks
   def get_dbnow_inline(self):
      ## this variant is using inline callbacks which makes code "look synchronous",
      ## nevertheless run asynchronous under the hood

      rows = yield self.db.runQuery("SELECT now()")
      res = "{0}".format(rows[0][0])
      returnValue(res)


   @wamp.register(u'com.example.now.v3')
   def get_dbnow_interaction(self):
      ## this variant runs the query inside a transaction (which might do more,
      ## and still be atomically committed/rolled back)

      def run(txn):
         d = txn.execute("SELECT now()")

         def on_cursor_ready(cur):
            rows = cur.fetchall()
            res = "{0}".format(rows[0][0])
            return res
         d.addCallback(on_cursor_ready)

         return d

      return self.db.runInteraction(run)


   @wamp.register(u'com.example.now.v4')
   def get_dbnow_interaction_coroutine(self):
      ## this variant runs the query inside a transaction (which might do more,
      ## and still be atomically committed/rolled back). Further, we are using
      ## a co-routine based coding style here.

      @inlineCallbacks
      def run(txn):
         cur = yield txn.execute("SELECT now()")
         rows = cur.fetchall()
         res = "{0}".format(rows[0][0])
         returnValue(res)

      return self.db.runInteraction(run)



if __name__ == '__main__':
   from autobahn.twisted.wamp import ApplicationRunner

   runner = ApplicationRunner(url = "ws://127.0.0.1:8080/ws", realm = "realm1")
   runner.run(MyDatabaseComponent)
