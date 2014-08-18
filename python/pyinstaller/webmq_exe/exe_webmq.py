######################################################################
##
##   Copyright (c) 2012-2013 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

import threading

from webmq.main import runDirect

RUNFOREVER = False

if __name__ == '__main__':
   if RUNFOREVER:
      while True:
         t = threading.Thread(target = runDirect)
         t.start()
         t.join()
   else:
      runDirect(True)
