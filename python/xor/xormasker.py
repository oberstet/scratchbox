###############################################################################
##
##  Copyright 2012-2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################


from array import array

class XorMaskerNull:

   def __init__(self, mask = None):
      self.ptr = 0

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      self.ptr += len(data)
      return data


class XorMaskerSimple:

   def __init__(self, mask):
      assert len(mask) == 4
      self.ptr = 0
      self.msk = array('B', mask)

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      payload = array('B', data)
      for k in xrange(dlen):
         payload[k] ^= self.msk[self.ptr & 3]
         self.ptr += 1
      return payload.tostring()


class XorMaskerShifted1:

   def __init__(self, mask):
      assert len(mask) == 4
      self.ptr = 0
      self.mskarray = [array('B'), array('B'), array('B'), array('B')]
      for j in xrange(4):
         self.mskarray[0].append(ord(mask[ j & 3]))
         self.mskarray[1].append(ord(mask[(j + 1) & 3]))
         self.mskarray[2].append(ord(mask[(j + 2) & 3]))
         self.mskarray[3].append(ord(mask[(j + 3) & 3]))

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      payload = array('B', data)
      msk = self.mskarray[self.ptr & 3]
      for k in xrange(dlen):
         payload[k] ^= msk[k & 3]
      self.ptr += dlen
      return payload.tostring()


class XorMaskerShifted2:

   def __init__(self, mask):
      assert len(mask) == 4
      self.ptr = 0
      self.mskarray = [array('B'), array('B'), array('B'), array('B')]
      for j in xrange(4):
         self.mskarray[0].append(ord(mask[ j & 3]))
         self.mskarray[1].append(ord(mask[(j + 1) & 3]))
         self.mskarray[2].append(ord(mask[(j + 2) & 3]))
         self.mskarray[3].append(ord(mask[(j + 3) & 3]))

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      payload = array('B', data)
      msk = self.mskarray[self.ptr & 3]
      k = 0
      r = dlen % 4
      l = dlen - r
      while k < l:
         payload[k    ] ^= msk[0]
         payload[k + 1] ^= msk[1]
         payload[k + 2] ^= msk[2]
         payload[k + 3] ^= msk[3]
         k += 4
      self.ptr += dlen
      return payload.tostring()


class XorMaskerTest:

   def __init__(self, mask):
      self.ptr = 0

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      payload = array('B', data)
      self.ptr += dlen
      return payload.tostring()


try:
   from __pypy__.builders import StringBuilder
except:
   pass

class XorMaskerTest2:

   def __init__(self, mask):
      self.ptr = 0

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      r = StringBuilder(dlen)
      r.append(data)
      self.ptr += dlen
      return r.build()


class XorMaskerStringBuilder:

   def __init__(self, mask):
      self.ptr = 0

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      r = StringBuilder(dlen)
      r.append(data)
      self.ptr += dlen
      return r.build()


class XorMaskerSimpleStringBuilder:

   def __init__(self, mask):
      assert len(mask) == 4
      self.ptr = 0
      #self.msk = tuple([ord(c) for c in mask])
      self.msk = mask

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      r = StringBuilder(dlen)

      i = 0
      k = self.ptr
      m = self.msk
      while i < dlen:
#         r.append(chr(ord(data[i]) ^ self.msk[k & 3]))
         r.append(chr(ord(data[i]) ^ ord(m[k & 3])))
         k += 1
         i += 1

      self.ptr += dlen
      return r.build()



class XorMaskerShiftedStringBuilder:

   def __init__(self, mask):
      assert len(mask) == 4
      self.ptr = 0
      #self.msk = tuple([ord(c) for c in mask])
      self.msk = mask

   def pointer(self):
      return self.ptr

   def reset(self):
      self.ptr = 0

   def process(self, data):
      dlen = len(data)
      r = StringBuilder(dlen)

      i = 0
      k = self.ptr
      m = self.msk
      while i < dlen:
         r.append(chr(ord(data[i + 0])))
         r.append(chr(ord(data[i + 1])))
         r.append(chr(ord(data[i + 2])))
         r.append(chr(ord(data[i + 3])))
         r.append(chr(ord(data[i + 4])))
         r.append(chr(ord(data[i + 5])))
         r.append(chr(ord(data[i + 6])))
         r.append(chr(ord(data[i + 7])))
         i += 8

      self.ptr += dlen
      return r.build()

def createXorMasker(mask, len = None):
   if len is None or len < 128:
      return XorMaskerSimple(mask)
   else:
      return XorMaskerShifted1(mask)
