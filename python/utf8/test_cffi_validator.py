import binascii, sys
from cffi import FFI

def test_utf8_incremental(v):
   """
   These tests verify that the UTF-8 decoder/validator can operate incrementally.
   """

   #v = Validator()

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



class Utf8ValidatorCFFI:
   def __init__(self, ffi):
      self._ffi = ffi
      self._vld = ffi.new("utf8_validator_t[]", 1)[0]
      self._vld_addr = ffi.addressof(self._vld)
      self.reset()

   def reset(self):
      self._ffi.validator.utf8vld_reset(self._vld_addr)

   def validate(self, ba):
      self._ffi.validator.utf8vld_validate(self._vld_addr, ba, 0, len(ba))
      return self._vld.is_valid != 0, \
             self._vld.ends_on_codepoint != 0, \
             self._vld.current_index, \
             self._vld.total_index


if __name__ == '__main__':

   ffi = FFI()

   ffi.cdef("""
      typedef struct {
         int state;
         int current_index;
         int total_index;
         int is_valid;
         int ends_on_codepoint;
      } utf8_validator_t;

      void utf8vld_reset (utf8_validator_t* validator);

      void utf8vld_validate (utf8_validator_t* validator, const char* data, size_t offset, size_t length);
   """)

   ffi.validator = ffi.dlopen('libutf8validator.so')

   vld = Utf8ValidatorCFFI(ffi)

   test_utf8_incremental(vld)
