import time

__all__ = ('Monitor',)


class Monitor(object):
    """
    Livemon monitor base class.
    """

    ID = u'base'

    def __init__(self, config=None):
        """

        :param config: Submonitor specific configuration.
        :type config: dict or None
        """
        # submonitor specific configuration
        self._config = config

        # time of last poll
        self._last_poll = None

        # effective period corresponding to last poll
        self._last_period = None

        # last measurement
        self._last_value = None

    def poll(self):
        """
        Measure current stats value and return new stats.
        """

        # effective period since last poll
        #
        now = time.time()
        if self._last_poll:
            self._last_period = now - self._last_poll
        self._last_poll = now

    def get(self):
        """
        Get current stats/mesasurement values.
        """
        return self._last_value
