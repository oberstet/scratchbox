// Any copyright is dedicated to the Public Domain.
// http://creativecommons.org/publicdomain/zero/1.0/

/*********************************************
This more advanced accelerometer example logs
a stream of x, y, and z data, then stops the
stream, changes the polling rate, and resumes
streaming from the accelerometer
*********************************************/

var tessel = require('tessel');
var accel = require('../').use(tessel.port['A']); // Replace '../' with 'accel-mma84' in your own code

// Initialize the accelerometer.
accel.on('ready', function () {
  // Stream accelerometer data
  accel.on('data', function(xyz) {
    console.log('x:', xyz[0].toFixed(2),
      'y:', xyz[1].toFixed(2),
      'z:', xyz[2].toFixed(2));
  });
  //After two seconds, change stream rate, then stream again
  setTimeout(function () {
    console.log('Changing the output rate...');
    accel.removeAllListeners('data');
    // Setting the output data rate in Hz
    accel.setOutputRate(1.56, function rateSet() {
      accel.on('data', function (xyz) {
        console.log('slower x:', xyz[0].toFixed(2),
        'slower y:', xyz[1].toFixed(2),
        'slower z:', xyz[2].toFixed(2));
      });
    });
  }, 2000);
});

accel.on('error', function(err){
  console.log('Error:', err);
});
