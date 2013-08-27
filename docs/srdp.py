###############################################################################
##
##  Copyright 2013 Tavendo GmbH
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

__all__ = ("SrdpFrameHeader",)

import struct, binascii

## https://pypi.python.org/pypi/crcmod
import crcmod


class SrdpFrameHeader:

   def __init__(self,
                opcode = 0,
                device = 0,
                register = 0,
                position = 0,
                length = 0,
                crc16 = 0):
      self.opcode = opcode
      self.device = device
      self.register = register
      self.position = position
      self.length = length
      self.crc16 = crc16


   def computeCrc(self, data = None):
      crc = crcmod.predefined.PredefinedCrc("crc-16")
      header = struct.pack("<HHHH",
                           self.opcode << 12 | self.device,
                           self.register,
                           self.position,
                           self.length)
      crc.update(header)
      if data and len(data) > 0:
         crc.update(data)
      self.crc16 = crc.crcValue


   def serialize(self):
      return struct.pack("<HHHHH",
                         self.opcode << 12 | self.device,
                         self.register,
                         self.position,
                         self.length,
                         self.crc16)
   

   def parse(self, data):
      t = struct.unpack("<HHHHH", data[0:10])
      self.opcode = t[0] >> 12
      self.device = t[0] & 0xfff
      self.register = t[1]
      self.position = t[2]
      self.length = t[3]
      self.crc16 = t[4]


   def checkCrc(self, data = None):
      crc = crcmod.predefined.PredefinedCrc("crc-16")
      header = struct.pack("<HHHH",
                           self.opcode << 12 | self.device,
                           self.register,
                           self.position,
                           self.length)
      crc.update(header)
      if data and len(data) > 0:
         crc.update(data)
      return self.crc16 == crc.crcValue




if __name__ == '__main__':

   ## Assume we (the adapter) have received a READ_REGISTER frame for
   ## device = 1, register = 2 ("/device/1/location/position").
   ## We want to assmble a SRDP READ_ACK frame with the requested data.

   ## sensor data
   ##
   timestamp = 8762345
   longitude = -34.98124
   latitude = 9.12354
   mode = 'C'

   ## According to our example EDS, the register has format "<Iffc"
   data = struct.pack("<Iffc", timestamp, longitude, latitude, mode)


   ## construct READ_ACK frame to send
   ##
   f1 = SrdpFrameHeader(0x02, 1, 2, 0, len(data))
   f1.computeCrc(data)

   wireData = f1.serialize() + data

   ## send frame header and data
   print binascii.hexlify(wireData)


   f2 = SrdpFrameHeader()
   f2.parse(wireData)

   payload = wireData[10:10+f2.length]

   ## check CRC
   print f2.checkCrc(payload)

   print f2.opcode, f2.device, f2.register, f2.position, f2.length

   t = struct.unpack("<Iffc", payload)
   print t
