import argparse

from twisted.internet import task
from twisted.internet.defer import inlineCallbacks

import autobahn
from autobahn.wamp.types import PublishOptions
from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner

# submonitors
from cpumonitor import CPUMonitor
from procmonitor import ProcessMonitor
from iomonitor import IOMonitor
from rammonitor import RAMMonitor
from hwmonitor import HWMonitor

# map: submonitor name -> submonitor class
MONITORS = {
    'cpumon': CPUMonitor,
    'procmon': ProcessMonitor,
    'iomon': IOMonitor,
    'rammon': RAMMonitor,
    'hwmon': HWMonitor,
}


class Livemon(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("Livemon connected: {}".format(details))

        tick_period = self.config.extra['options']['tick_period']

        if tick_period:

            self._ticks = 0

            def tick():
                self._ticks += 1
                print("Livemon: tick {}".format(self._ticks))

            self._ticks_lc = task.LoopingCall(tick)
            self._ticks_lc.start(tick_period)
        else:
            self._ticks_lc = None

        # submonitor instances
        self._monitors = {}

        # looping calls which poll the submonitors
        self._monitors_lc = {}

        # URI prefix for topics/procs (eg "de.parcit.adr.livemon")
        prefix = self.config.extra['options']['prefix']

        # setup submonitors
        for monitor_key, monitor_config in self.config.extra['monitors'].items():

            if monitor_key not in MONITORS:
                raise Exception("unknown monitor type '{}'".format(monitor_key))

            # monitor class
            klass = MONITORS[monitor_key]

            # instantiate monitor
            mon = klass(monitor_config.get('config', None))

            # register monitor procs
            yield self.register(mon.get, u"{}.get_{}_stats".format(prefix, klass.ID))

            # topic under which stats are published
            topic = u"{}.on_{}_stats".format(prefix, klass.ID)

            # setup looping call which polls the submonitor and publishes events
            # note: we have to create the poll() function with a creator function because
            # of the way Python closures work
            def create_poller(mon, period, topic):

                @inlineCallbacks
                def poll():
                    try:
                        options = PublishOptions(acknowledge=True)

                        stats = yield mon.poll()

                        if stats:
                            # add target period, as the submonitor will only add the effective
                            # period ("last_period")
                            stats['period'] = period

                            yield self.publish(topic, stats, options=options)

                    except Exception as e:
                        print("failed to publish monitor stats for monitor '{}': {}".format(klass.ID, e))

                return poll

            self._monitors[monitor_key] = mon
            self._monitors_lc[monitor_key] = task.LoopingCall(create_poller(mon, monitor_config['period'], topic))
            self._monitors_lc[monitor_key].start(monitor_config['period'])

        print("Livemon running.")

    def onLeave(self, details):
        print("Livemon session lost: {} - {}".format(details.reason, details.message))

        if self._ticks_lc:
            self._ticks_lc.stop()

        for lc in self._monitors_lc.values():
            lc.stop()

        print("Livemon: monitors stopped.")

        self.disconnect()

    def onDisconnect(self):
        print("Livemon transport disconnected.")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--quiet', action='store_true', help='Be quiet and do not bother asking silly questions.')

    # target database
    #
    parser.add_argument("--router", type=unicode, default=u"ws://bvr-sql18.local.parcit/ws", help='WAMP router URL.')
    parser.add_argument("--realm", type=unicode, default=u"adr", help='WAMP router realm.')

    args = parser.parse_args()

    extra = {
        u'options': {
            # URI prefix for topics/procedures
            u'prefix': u'de.parcit.adr.livemon',

            # period under which livemon will log a "tick" to the syslog
            u'tick_period': 10.
        },

        # configured submonitors
        u'monitors': {
            u'cpumon': {
                u'period': 1.
            },
            u'iomon': {
                u'period': 1.,
                u'config': {
                    # storage block devices to be monitored
                    # FIXME: the Livemon frontend is currently hardcoded
                    # for the following storage definition
                    u'storage': [
                        {
                            u'id': u'WORK',
                            u'devices': [
#                                (u'md2', u'RAID-0'),
                                (u'nvme0n1', u'Intel P3700'),
                                (u'nvme1n1', u'Intel P3700'),
                                (u'nvme2n1', u'Intel P3700'),
                                (u'nvme3n1', u'Intel P3700'),
                                (u'nvme4n1', u'Intel P3700'),
                                (u'nvme5n1', u'Intel P3700'),
                                (u'nvme6n1', u'Intel P3700'),
                                (u'nvme7n1', u'Intel P3700')
                            ]
                        },
#                        {
#                            u'id': u'RESULT',
#                            u'devices': [
#                                (u'md3', u'RAID-10'),
#                                (u'sdb', u'Intel DC S3700'),
#                                (u'sdd', u'Intel DC S3700'),
#                                (u'sde', u'Intel DC S3700'),
#                                (u'sdf', u'Intel DC S3700'),
#                                (u'sdg', u'Intel DC S3700'),
#                                (u'sdh', u'Intel DC S3700'),
#                                (u'sdi', u'Intel DC S3700'),
#                                (u'sdai', u'Intel DC S3700'),
#                                (u'sdaj', u'Intel DC S3700'),
#                                (u'sdah', u'Intel DC S3700'),
#                            ]
#                        },
                    ]
                }
            },
            u'rammon': {
                u'period': 1.
            },
            u'procmon': {
                u'period': 2.,
                u'config': {
                    # map: executable path -> process type
                    u'process_types': {
                        # Benchmark tools
                        u'/usr/bin/fio': u'benchmark',
                        u'/usr/local/bin/stress': u'benchmark',
                        u'/usr/bin/stress': u'benchmark',

                        # PostgreSQL
                        u'/opt/pg954/bin/postgres': u'postgres',

                        # Postgres-XL
                        u'/opt/pgxl/bin/postgres': u'pgxl',

                        # R
                        u'/usr/bin/R': u'r',
                        u'/usr/lib/R/bin/exec/R': u'r',

                        # Crossbar.io
                        u'/opt/crossbar/bin/crossbar': u'crossbar',
                        u'/opt/crossbar/bin/pypy': u'crossbar',
                        u'/opt/cpy2712/bin/crossbar': u'crossbar',
                        u'/opt/crossbar1610/bin/crossbar': u'crossbar',

                        # Python
                        u'/opt/cpy2712/bin/python': u'python',
                        u'/opt/cpy2712/bin/python2': u'python',
                        u'/opt/cpy2712/bin/python2.7': u'python',

                        # Backup tools
                        u'/bin/tar': u'backup',
                        u'/bin/bzip2': u'backup',
                        u'/bin/gzip': u'backup',
                        u'/usr/bin/pbzip2': u'backup',
                        u'/opt/pg953/bin/pg_dump': u'backup',
                        u'/opt/pg953/bin/pg_dumpall': u'backup',

                        # FS tools
                        u'/sbin/fstrim': u'trim',
                    },

                    # when an executable can't be mapped via "process_types", assign it
                    # to this process type
                    u'process_type_unassigned': u'unassigned',

                    # either a list of process types to filter for, or None to monitor all processes
                    u'filter_process_types': [
                        u'benchmark',
                        u'postgres',
                        u'pgxl',
                        u'r',
                        u'crossbar',
                        u'python',
                        u'backup',
                        u'trim'
                    ],
                }
            },
            u'hwmon': {
                u'period': 10.,
                u'config': {
                    # list of IPMI sensors to be monitored
                    u'sensors': [
                        u'Temp_CPU0',
                        u'Temp_CPU1',
                        u'Temp_CPU2',
                        u'Temp_CPU3',
                        u'Temp_Inlet',
                        u'Temp_Outlet2',
                        u'Temp_Outlet1',
                        u'Temp_Ambient_FP',
                        u'Temp_Ambient_BP0',
                        u'Temp_Ambient_BP1',
                        u'Temp_PCH',
                        u'Temp_MemRiser1',
                        u'Temp_MemRiser2',
                        u'Temp_MemRiser3',
                        u'Temp_MemRiser4',
                        u'Temp_MemRiser5',
                        u'Temp_MemRiser6',
                        u'Temp_MemRiser7',
                        u'Temp_MemRiser8',
                        u'Fan_SYS1',
                        u'Fan_SYS2',
                        u'Fan_SYS3',
                        u'Fan_SYS4',
                        u'Fan_SYS5',
                        u'Fan_SYS6',
                        u'Fan_SYS7',
                        u'Fan_SYS8',
                        u'PSU_Power',
                        u'Fan_PSU1',
                        u'Fan_PSU2',
                        u'Fan_PSU3',
                        u'Fan_PSU4',
                        u'Temp_PSU1_Inlet',
                        u'Temp_PSU2_Inlet',
                        u'Temp_PSU3_Inlet',
                        u'Temp_PSU4_Inlet',
                    ]
                }
            }
        }
    }

    print('Running on Autobahn {}'.format(autobahn.__version__))
    runner = ApplicationRunner(url=args.router, realm=args.realm, extra=extra)
    runner.run(Livemon, auto_reconnect=True)
