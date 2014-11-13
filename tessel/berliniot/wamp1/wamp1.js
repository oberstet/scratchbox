var tessel = require('tessel');
var accel = require('accel-mma84').use(tessel.port['B']);
var autobahn = require('wamp-tessel');

var leds = [tessel.led[0], tessel.led[1]];

accel.on('ready', function () {
   var rates = accel.availableOutputRates();
   console.log("accelerometer initialized (output rates: " + rates + ")");
   accel.setOutputRate(12.5, function rateSet () {
      main();
   });
});

accel.on('error', function (err) {
   console.log('Error:', err);
});

function main () {

   var connection = new autobahn.Connection({
      url: "ws://crossbar-test.cloudapp.net/ws",
      realm: "ms_iot_hack_01"
   //   url: "ws://crossbar-test.cloudapp.net:8080/ws",
   //   realm: "realm1"
   });

   var accel_threshold = .5;

   connection.onopen = function (session, details) {

      function toggle_lights (args) {
         var led = args[0];
         console.log("toggling light " + led);
         leds[led].toggle();
      }

      session.register("io.crossbar.iotberlin.alarmapp.toggle_lights", toggle_lights).then(
         function () {
            console.log("toggle_lights registered");
         },
         function (e) {
            console.log(e);
         }
      );

      accel.on('data', function (xyz) {
         var data = {
            x: xyz[0].toFixed(2),
            y: xyz[1].toFixed(2),
            z: xyz[2].toFixed(2)
         };
         console.log("accelerometer", data);
         session.publish("io.crossbar.iotberlin.alarmapp.on_accelerometer", [data]);
      });
   };

   connection.onclose = function (reason, details) {
      console.log("Connection lost: " + reason, details);
   };

   connection.open();
}
