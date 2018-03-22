from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.util import sleep
from pprint import pformat

class MySession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        config = self.config.extra or {'iterations': 300, 'delay': .2}
        self.log.info('****** MySession joined realm "{realm}" ******', realm=details.realm)
        self.log.info('****** {config}', config=self.config.extra)

        self._tick = 1
        for i in range(config['iterations']):
            self.log.info('****** INFO - TICK {}'.format(self._tick))
            self.log.error('****** ERR  - TICK {}'.format(self._tick))
            self._tick += 1
            yield sleep(config['delay'])
        self.leave()
