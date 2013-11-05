import sys, time


def validate(Validator, payload):
   """
   Simulates UTF8 validation in one go. In the actual WebSocket
   implementation within AutobahnPython, the validator is
   driven incrementally, as data arrives from the wire.
   """
   validator = Validator()

   validator.reset()
   lastResult = (True, True, 0, 0)

   lastResult = validator.validate(payload)

   if not lastResult[0]:
      raise Exception("encountered invalid UTF-8 while processing text message at payload octet index %d" % lastResult[3])

   if not lastResult[1]:
      raise Exception("UTF-8 text message payload ended within Unicode code point at payload octet index %d" % lastResult[3])



def fake_test_9_1_6(Validator, runs = 1):
   """
   Fake the AutobahnTestsuite test 9.1.6

   http://autobahn.ws/testsuite/reports/servers/index.html
   https://github.com/tavendo/AutobahnTestSuite
   https://github.com/tavendo/AutobahnTestSuite/blob/master/autobahntestsuite/autobahntestsuite/case/case9_1_1.py
   https://github.com/tavendo/AutobahnTestSuite/blob/master/autobahntestsuite/autobahntestsuite/case/case9_1_6.py
   """
   PAYLOAD = "BAsd7&jh23"
   DATALEN = 16 * 2**20

   payload = PAYLOAD * (DATALEN /  len(PAYLOAD)) # not exactly, but good enough

   for i in range(runs):
      #print "validating payload of length %d in one go" % len(payload)
      validate(Validator, payload)



def test_utf8_incremental(Validator):
   """
   These tests verify that the UTF-8 decoder/validator can operate incrementally.
   """

   v = Validator()

   v.reset()
   assert (True, True, 15, 15) == v.validate("\xc2\xb5@\xc3\x9f\xc3\xb6\xc3\xa4\xc3\xbc\xc3\xa0\xc3\xa1")

   v.reset()
   assert (False, False, 0, 0) == v.validate("\xF5")

   ## the following 3 all fail on eating byte 7 (0xA0)
   v.reset()
   assert (True, True, 6, 6) == v.validate("\x65\x64\x69\x74\x65\x64")
   assert (False, False, 1, 7) == v.validate("\xED\xA0\x80")

   v.reset()
   assert (True, True, 4, 4) == v.validate("\x65\x64\x69\x74")
   assert (False, False, 3, 7) == v.validate("\x65\x64\xED\xA0\x80")

   v.reset()
   assert (True, False, 7, 7) == v.validate("\x65\x64\x69\x74\x65\x64\xED")
   assert (False, False, 0, 7) == v.validate("\xA0\x80")



if __name__ == '__main__':
   VALIDATORS = []

   from utf8validator import Utf8Validator as ValidatorPython
   VALIDATORS.append(ValidatorPython)

   from utf8validator_str_dfa import Utf8Validator as ValidatorPythonStrDfa
   VALIDATORS.append(ValidatorPythonStrDfa)

   from utf8validator_str_dfa_local_state import Utf8Validator as ValidatorPythonStrDfaLocalState
   VALIDATORS.append(ValidatorPythonStrDfaLocalState)

   try:
      from wsaccel.utf8validator import Utf8Validator as ValidatorCython
      VALIDATORS.append(ValidatorCython)
   except:
      print "wsaccel not installed"

   for V in VALIDATORS:
      print "."*80
      print
      print "using UTF8 validator", str(V)
      print

      ## quick test the validator works (non-exhaustive)
      test_utf8_incremental(V)

      runs = 100

      print "warming up .."
      fake_test_9_1_6(V, runs)
      print

      print "cooling down .."
      time.sleep(3)
      print

      print "testing .."
      t0 = time.time()
      fake_test_9_1_6(V, runs)
      t1 = time.time()
      print
      print "runtime", t1 - t0
      print
