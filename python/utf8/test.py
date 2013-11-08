import sys, time


def validate(validator, payload):
   """
   Simulates UTF8 validation in one go. In the actual WebSocket
   implementation within AutobahnPython, the validator is
   driven incrementally, as data arrives from the wire.
   """
   validator.reset()
   lastResult = validator.validate(payload)

   return

   if not lastResult[0]:
      raise Exception("encountered invalid UTF-8 while processing text message at payload octet index %d" % lastResult[3])

   if not lastResult[1]:
      raise Exception("UTF-8 text message payload ended within Unicode code point at payload octet index %d" % lastResult[3])



def fake_test_9_1_6(validator, payload, runs = 1):
   """
   Fake the AutobahnTestsuite test 9.1.6

   http://autobahn.ws/testsuite/reports/servers/index.html
   https://github.com/tavendo/AutobahnTestSuite
   https://github.com/tavendo/AutobahnTestSuite/blob/master/autobahntestsuite/autobahntestsuite/case/case9_1_1.py
   https://github.com/tavendo/AutobahnTestSuite/blob/master/autobahntestsuite/autobahntestsuite/case/case9_1_6.py
   """
   for i in range(runs):
      #print "validating payload of length %d in one go" % len(payload)
      validate(validator, payload)



def test_utf8_incremental(validator):
   """
   These tests verify that the UTF-8 decoder/validator can operate incrementally.
   """

   validator.reset()
   assert (True, True, 15, 15) == validator.validate("\xc2\xb5@\xc3\x9f\xc3\xb6\xc3\xa4\xc3\xbc\xc3\xa0\xc3\xa1")

   validator.reset()
   assert (False, False, 0, 0) == validator.validate("\xF5")

   ## the following 3 all fail on eating byte 7 (0xA0)
   validator.reset()
   assert (True, True, 6, 6) == validator.validate("\x65\x64\x69\x74\x65\x64")
   assert (False, False, 1, 7) == validator.validate("\xED\xA0\x80")

   validator.reset()
   assert (True, True, 4, 4) == validator.validate("\x65\x64\x69\x74")
   assert (False, False, 3, 7) == validator.validate("\x65\x64\xED\xA0\x80")

   validator.reset()
   assert (True, False, 7, 7) == validator.validate("\x65\x64\x69\x74\x65\x64\xED")
   assert (False, False, 0, 7) == validator.validate("\xA0\x80")



if __name__ == '__main__':
   VALIDATORS = []

   if 'PyPy' in sys.version:

      from utf8validator import Utf8Validator as ValidatorPython
      #VALIDATORS.append(ValidatorPython())

      from utf8validator_str_dfa import Utf8Validator as ValidatorPythonStrDfa
      #VALIDATORS.append(ValidatorPythonStrDfa())

      from utf8validator_str_dfa_local_state import Utf8Validator as ValidatorPythonStrDfaLocalState
      #VALIDATORS.append(ValidatorPythonStrDfaLocalState())

      from utf8validator_bytearray_dfa_local_state import Utf8Validator as ValidatorPythonBytearrayDfaLocalState
      #VALIDATORS.append(ValidatorPythonBytearrayDfaLocalState())

   else:
      print
      print "!!! Skipping pure Python validators when running CPython [way too slow]"
      print


   try:
      from cffi import FFI

      ffi = FFI()

      ffi.cdef("""
         typedef struct {
            size_t current_index;
            size_t total_index;
            int state;
            int is_valid;
            int ends_on_codepoint;
         } utf8_validator_t;

         void utf8vld_reset (utf8_validator_t* validator);

         void utf8vld_validate (utf8_validator_t* validator, const uint8_t* data, size_t offset, size_t length);
      """)

      ffi.validator = ffi.dlopen('libutf8validator.so')


      from test_cffi_validator import Utf8ValidatorCFFI
      VALIDATORS.append(Utf8ValidatorCFFI(ffi))
   except:
      print "cffi not installed"


   try:
      if True or not 'PyPy' in sys.version:
         from wsaccel.utf8validator import Utf8Validator as ValidatorCython
         #VALIDATORS.append(ValidatorCython())
      else:
         print "skipping installed wsaccel on PyPy"
   except:
      print "wsaccel not installed"


   #PAYLOAD = "BAsd7&jh23"

   import random
   PAYLOAD = ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_") for i in xrange(16)])

   DATALEN = 16 * 2**20
   payload = PAYLOAD * (DATALEN /  len(PAYLOAD)) # not exactly, but good enough


   for validator in VALIDATORS:
      print "."*80
      print
      print "using UTF8 validator", str(validator.__class__)
      print

      ## quick test the validator works (non-exhaustive)
      #test_utf8_incremental(validator)
      #print "OK, validator works."

      runs = 200

      print "warming up .."
      fake_test_9_1_6(validator, payload, runs)
      print

      print "cooling down .."
      time.sleep(3)
      print

      print "testing .."
      t0 = time.time()
      fake_test_9_1_6(validator, payload, runs)
      t1 = time.time()
      totalBytes = float(runs * DATALEN)
      duration = t1 - t0
      print
      print "runtime %.4f s [%.1f MB/s]" % (duration, totalBytes / duration / 1024. / 1024.)
      print
