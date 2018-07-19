import time

from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.internet.utils import getProcessOutput

from autobahn.util import utcnow

from monitor import Monitor


__all__ = ('HWMonitor',)


class HWMonitor(Monitor):
    """
    Hardware monitoring. This monitor is reading hardware sensor data from IPMI.

    WARNING:
      - This component must be run as root, since ipmitool requires superuser privs.
      - This component should NOT be polled more frequently than every 5 secs, since
        retrieving IPMI sensor values is relatively expensive!
    """

    ID = u'hw'

    def __init__(self, config=None):
        Monitor.__init__(self, config)
        self._sensors = set(self._config.get(u'sensors', []))

    @inlineCallbacks
    def poll(self):
        """
        Measure current stats value and return new stats.
        """
        Monitor.poll(self)

        # create new, empty event
        #
        current = {
            # the UTC timestamp when measurement was taken
            u'timestamp': utcnow(),

            # the effective last period in secods
            u'last_period': self._last_period,

            # duration in seconds the retrieval of sensor values took
            u'command_duration': None,

            # actual sensor readings
            u'sensors': []
        }

        # read out IPMI sensor data via ipmitool (which needs root!)
        #
        cmd_started = time.time()
        res = yield getProcessOutput('/usr/bin/ipmitool', ['sdr'])
        current[u'command_duration'] = time.time() - cmd_started

        # extract sensor reading
        #
        for line in res.splitlines():
            sensor, value, status = tuple([x.strip() for x in line.split('|')])
            if sensor in self._sensors:
                value, unit = value.split(' ', 1)
                value = float(value)
                unit = unit.strip()
                current[u'sensors'].append({
                    u'id': sensor,
                    u'value': value,
                    u'unit': unit,
                    u'status': status
                })

        self._last_value = current

        returnValue(self._last_value)


if __name__ == '__main__':

    from pprint import pprint

    from twisted.internet import reactor
    from twisted.internet.task import LoopingCall

    monitor = HWMonitor()

    @inlineCallbacks
    def loop():
        res = yield monitor.poll()
        pprint(res)

    lc = LoopingCall(loop)
    lc.start(10.)

    reactor.run()
