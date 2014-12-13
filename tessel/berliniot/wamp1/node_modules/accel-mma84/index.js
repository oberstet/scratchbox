// Copyright 2014 Technical Machine, Inc. See the COPYRIGHT
// file at the top-level directory of this distribution.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

var util = require('util');
var EventEmitter = require('events').EventEmitter;
var queue = require('sync-queue');

// The SparkFun breakout board defaults to 1, set to 0 if SA0 jumper on the bottom of the board is set
var I2C_ADDRESS = 0x1D;  // 0x1D if SA0 is high, 0x1C if low

// See the many application notes for more info on setting all of these registers:
// http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MMA8452Q
// MMA8452 registers
var OUT_X_MSB = 0x01;
var XYZ_DATA_CFG = 0x0E;
var WHO_AM_I = 0x0D;
var CTRL_REG1 = 0x2A;
var CTRL_REG4 = 0x2D;

function Accelerometer (hardware, callback) {
  var self = this;
  // Command Queue
  self.queue = new queue();
  // Port assignment
  self.hardware = hardware;
  // Rate at which data is collected and is ready to be read
  self.outputRate = 12.5;
  // Sets full-scale range to +/-2, 4, or 8g. Used to calc real g values.
  self.scaleRange = 2;
  // Interrupt pin for the data ready event
  self.dataInterrupt = self.hardware.digital[1];
  // Address for i2C
  // TODO: Account for manual address changes?
  self.i2c = hardware.I2C(I2C_ADDRESS);

  // Check that we can read the correct chip id
  self.queue.place(function one() {
    self._getChipID(function IDRead(err, c) {
      if (err) {
        err = new Error("Could not connect to MMA8452Q. No reponse on I2C lines. Error: "+err);
        return self._failProcedure(err);
      }
      // should always return 0x2A
      if (c !== 0x2A) {
        // This is the wrong chip
        err = new Error("Could not connect to MMA8452Q, received " + c.toString() + ". Expected 0x2A.");
        // Fail the init
        return self._failProcedure(err);
      }

      // Set the scale range to standard
      self.setScaleRange(self.scaleRange, function(err) {
        if (err) {
          return self._failProcedure(err, callback);
        }
        else {
          // Set the output rate to standard
          self.setOutputRate(self.outputRate, function(err) {
            if (err) {
              return self._failProcedure(err, callback);
            }
            else {
              // Emit the ready event
              setImmediate(function emitReady() {
                self.emit('ready');
                self.queue.next();
              });
              // Call the callback with object
              if (callback) callback(null, self);

              return;
            }
          });
        }
      });

      // Set up an interrupt handler for data ready
      self.dataInterrupt.once('low', self._dataReady.bind(self));
    });
  });

  self.on('newListener', function(event) {
    // If we have a new sample listener
    if (event == 'data' || event == 'sample') {
      // Enable interrupts at whatever rate was previously set.
      self.enableDataInterrupts(true, queueNext);
    }
  });

  self.on('removeListener', function(event) {
    // If we have a new || event == 'sample' listener
    if (event == 'data' || event == 'sample') {
      // Disable interrupt.
      self.enableDataInterrupts(false, queueNext);
    }
  });

  self.queue.next();
}

util.inherits(Accelerometer, EventEmitter);

Accelerometer.prototype._changeRegister = function(change, callback) {
  var self = this;

  // Put the accelerometer into standby
  self._modeStandby(function inStandby(err) {
    if (err) {
      return self._failProcedure(err, callback);
    }
    else {
      // Make whatever change was requested
      change( function setActive(err) {
        if (err) {
          return self._failProcedure(err, callback);
        }
        else {
          // Put the accelerometer back into active mode
          self._modeActive(callback);
        }
      });
    }
  });
};

Accelerometer.prototype._dataReady = function() {
  var self = this;
  // Data is ready so grab the data
  self.getAcceleration(function(err, xyz) {
    // If we had an error, emit it
    if (err) {
      // Emitting error
      self.emit('error', err);
    }
    // If there was no error
    else {
      // Emit the data
      self.emit('data', xyz); // old-style, deprecated
      self.emit('sample', xyz);
    }

     self.dataInterrupt.once('low', self._dataReady.bind(self));
  });
};

Accelerometer.prototype._failProcedure = function(err, callback) {
  var self = this;

  // Emit the error
  setImmediate(function emitErr() {
    self.emit('error', err);
  });
  // Call the callback
  if (callback) callback(err);

  return;
};

// Get the id of the chip
Accelerometer.prototype._getChipID = function(callback) {
  this._readRegister(WHO_AM_I, function (err, c) {
    if (callback) callback(err, c);
  });
};

Accelerometer.prototype._getClosestOutputRate = function(requestedRate, callback) {

  // If a negative number is requested, stop output (0 hz)
  if (requestedRate < 0) requestedRate = 0;

  // If 0 hz is requested, return just that so that output will be stopped
  if (requestedRate === 0) {

    if (callback) callback(null, 0);

    return;
  }

  // Get the available rates
  var available = this.availableOutputRates();
  // Iterate through each
  for (var i = 0; i < available.length; i++) {
    // The first available rate less than or equal to requested is a match
    if (available[i] <= requestedRate) {
      // Send the match back
      if (callback) callback(null, available[i]);
      return;
    }
  }

  // If there were no match, this number must be between 0 and 1.56. Use 1.56
  if (callback) callback(null, available[available.length-1]);
};

// Sets the MMA8452 to active mode. Needs to be in this mode to output data
Accelerometer.prototype._modeActive = function (callback) {
  var self = this;
  // Set the active bit to begin detection
  self._readRegister(CTRL_REG1, function (err, c) {
    if (err) {
      return _failProcedure(err);
    }
    else {
      return self._writeRegister(CTRL_REG1, c | (0x01), callback);
    }
  });
};

// Sets the MMA8452 to standby mode. It must be in standby to change most register settings
Accelerometer.prototype._modeStandby = function (callback) {
  var self = this;
  // Clear the active bit to go into standby
  self._readRegister(CTRL_REG1, function (err, c) {
    if (err) {
      return self._failProcedure(err, callback);
    }
    else {
      return self._writeRegister(CTRL_REG1, c & ~(0x01), callback);
    }
  });
};

Accelerometer.prototype._readRegister = function (addressToRead, callback) {
  this._readRegisters(addressToRead, 1, function (err, regs) {
    callback(err, regs && regs[0]);
  });
};

Accelerometer.prototype._readRegisters = function (addressToRead, bytesToRead, callback) {
  this.i2c.transfer(new Buffer([addressToRead]), bytesToRead, callback);
};

// Write a single byte to the register.
Accelerometer.prototype._writeRegister = function (addressToWrite, dataToWrite, callback) {
  this.i2c.send(new Buffer([addressToWrite, dataToWrite]), callback);
};

// Sets the accelerometer to read up to 2, 4, or 8 Gs of acceleration (smaller range = better precision)
Accelerometer.prototype._unsafeSetScaleRange = function(scaleRange, callback) {
  var self = this;

  var fsr = scaleRange;
  if (fsr > 8) fsr = 8; //Easy error check
  fsr >>= 2; // Neat trick, see page 22. 00 = 2G, 01 = 4G, 10 = 8G

  // Go into standby to edit registers
  self._changeRegister(function change(complete) {
    if (err) {
      return complete(err);
    }
    else {
      // Write the new scale into the register
      self._writeRegister(XYZ_DATA_CFG, fsr, function wroteReg(err) {
        self.scaleRange = scaleRange;
        return complete(err);
      });
    }
  }, function scaleSet(err) {
    if (callback) {
      callback(err);
    }
    setImmediate(self.queue.next);
  });
}

// Sets the output rate of the data (1.56-800 Hz)
Accelerometer.prototype._unsafeSetOutputRate = function (hz, callback) {
  var self = this;

  // Put accel into standby
  self._changeRegister( function setRegisters(finishChange) {
    // Find the closest available rate (rounded down)
    self._getClosestOutputRate(hz, function gotRequested(err, closest) {
      if (err) {
        return finishChange(new Error("Rate must be >= 1.56Hz"));
      }
      else {
        // Set our property
        self.outputRate = closest;

        // Get the binary representation of the rate (for the register)
        var bin = self.availableOutputRates().indexOf(closest);
        // If the binary rep could be found
        if (bin !== -1) {
          // Read the current register value
          self._readRegister(CTRL_REG1, function readComplete(err, regVal) {
            if (err) {
              return finishChange(err);
            }
            else {
               // Clear the three bits of output rate control (0b11000111 = 199)
              regVal &= 199;
              // Move the binary rep into place (bits 3:5)
              if (bin !== 0) regVal |= (bin << 3);
              // Write that value into the control register
              self._writeRegister(CTRL_REG1, regVal, finishChange);
            }
          });
        }
        else {
          return finishChange(new Error("Invalid output rate."));
        }
      }
    })
  },
  function rateSet(err) {
    if (callback) {
      callback(err);
    }
    setImmediate(self.queue.next);
  });
};


// Logs the available interrupt rates in Hz
Accelerometer.prototype.availableOutputRates = function() {
  return [800, 400, 200, 100, 50, 12.5, 6.25, 1.56];
};

// Logs the available accelerometer ranges (in units of Gs)
Accelerometer.prototype.availableScaleRanges = function() {
  // The higher the range, the less accurate the readings are
  return [2, 4, 8];
};

// Enables or disables data interrupts. Set the first param truthy to enable, false to disable.
Accelerometer.prototype.enableDataInterrupts = function(enable, callback) {
  var self = this;

  // Don't call unnecessarily.
  if (this._dataInterrupts == !!enable) {
    return callback && callback();
  }
  this._dataInterrupts = !!enable;

  self.queue.place(function queueEnable() {
    // We're going to change register 4
    self._changeRegister(function change(complete) {
      // Read the register first
      self._readRegister(CTRL_REG4, function(err, reg4) {
        if (err) {
          return complete(err);
        }
        else {
          // If we are enabling, set first bit to 1, else 0
          var regVal = (enable ? (reg4 |= 1) : (reg4 &= ~1));
          // Write to the register
          self._writeRegister(CTRL_REG4, regVal, function(err) {
            return complete(err);
          });
        }
      });
    }, function intSet(err) {
      if (callback) {
        callback(err);
      }
      setImmediate(self.queue.next);
    });
  });
};

// Gets the acceleration from the device, outputs as array [x, y, z]
Accelerometer.prototype.getAcceleration = function (callback) {
  var self = this;

  self.queue.place( function readAccel() {
    self._readRegisters(OUT_X_MSB, 6, function (err, rawData) {
      if (err) throw err;
      // Loop to calculate 12-bit ADC and g value for each axis
      var out = [];
      for (var i = 0; i < 3 ; i++) {
        var gCount = (rawData[i*2] << 8) | rawData[(i*2)+1];  // Combine the two 8 bit registers into one 12-bit number

        gCount = (gCount >> 4); // The registers are left align, here we right align the 12-bit integer

        // If the number is negative, we have to make it so manually (no 12-bit data type)
        if (rawData[i*2] > 0x7F) {
          gCount = -(1 + 0xFFF - gCount); // Transform into negative 2's complement
        }

        out[i] = gCount / ((1<<12)/(2*self.scaleRange));
      }

      callback(null, out);

      setImmediate(self.queue.next);
    });
  });
};

// Queueing version of Accelerometer#_unsafeSetOutputRate
Accelerometer.prototype.setOutputRate = function (hz, callback) {
  this.queue.place(this._unsafeSetOutputRate.bind(this, hz, callback));
};

// Queueing version of Accelerometer#_unsafeSetScaleRange
Accelerometer.prototype.setScaleRange = function(scaleRange, callback) {
  this.queue.place(this._unsafeSetScaleRange.bind(this, scaleRange, callback));
};

function use (hardware, callback) {
  return new Accelerometer(hardware, callback);
}

exports.Accelerometer = Accelerometer;
exports.use = use;
