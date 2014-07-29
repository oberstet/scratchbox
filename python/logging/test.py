import sys
import logging
from twisted.python import log

logging.basicConfig(level = logging.DEBUG)

observer = log.PythonLoggingObserver()
observer.start()

log.msg("This is important!", logLevel = logging.CRITICAL)
log.msg("Don't mind", logLevel = logging.DEBUG, system = "sys23")
