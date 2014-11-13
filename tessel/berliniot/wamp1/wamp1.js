var tessel = require('tessel');
var accel = require('accel-mma84').use(tessel.port['B']);
var autobahn = require('wamp-tessel');

var leds = [tessel.led[0], tessel.led[1]];

leds[0].toggle();


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

   var blinking_freq = 0;
   var blinking_timer = null;

   connection.onopen = function (session, details) {

      console.log("connected!");

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
         //console.log("accelerometer", data);
         session.publish("io.crossbar.iotberlin.alarmapp.on_accelerometer", [data]);
      });

      function set_blinking (args) {
         var freq = args[0];
         if (blinking_freq != freq) {
            blinking_freq = freq;
            if (blinking_timer) {
               clearInterval(blinking_timer);
               blinking_timer = null;
               console.log("blinking disabled");
            }
            if (blinking_freq) {
               console.log("enabled blinking", blinking_freq);
               blinking_timer = setInterval(function () {
                  leds[0].toggle();
                  leds[1].toggle();
               }, blinking_freq);
            }
         }
      }

      session.register("io.crossbar.iotberlin.alarmapp.set_blinking", set_blinking).then(
         function () {
            console.log("set_blinking registered");
         },
         function (e) {
            console.log(e);
         }
      );
   };

   connection.onclose = function (reason, details) {
      console.log("Connection lost: " + reason, details);
   };

   connection.open();
}
