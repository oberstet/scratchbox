import sys
from twisted.python import log

log.startLogging(sys.stderr)

import logging
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

log.msg("This is important!")

logging.debug("WANRIN 1")
logger.debug("WANRIN 2")