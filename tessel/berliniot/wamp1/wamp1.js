var tessel = require('tessel');
var autobahn = require('wamp-tessel');

var leds = [tessel.led[0], tessel.led[1]];

// the WAMP connection to the Router
//
var connection = new autobahn.Connection({
   url: "ws://crossbar-test.cloudapp.net/ws",
   realm: "ms_iot_hack_01"
//   url: "ws://crossbar-test.cloudapp.net:8080/ws",
//   realm: "realm1"
});

// fired when connection is established and session attached
//
connection.onopen = function (session, details) {

   function toggleLed(args) {
      var ledNo = args[0];
      console.log("toggling LED " + ledNo);
      leds[ledNo].toggle();
   }

   session.register("io.crossbar.iot.hack.test.toggleLed", toggleLed).then(
      function () {
         console.log("toggleLed registered");
      },
      function (e) {
         console.log("could not register toggleLed", e);
      }
   );

   session.subscribe("io.crossbar.iot.hack.test",
      function(args) {
         console.log(args[0]);
      });

   setInterval(function() {
      session.publish("io.crossbar.iot.hack.test", ["IoT hacked"])
   }, 2000)

};

// fired when connection was lost (or could not be established)
//
connection.onclose = function (reason, details) {
   console.log("Connection lost: " + reason, details);
}

// now actually open the connection
//
connection.open();