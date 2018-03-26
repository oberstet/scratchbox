import txaio
txaio.use_twisted()  # noqa

from autobahn.twisted.choosereactor import install_optimal_reactor

#from crossbar.controller import cli
from crossbar.controller import personality

install_optimal_reactor()
