var session = null;

var bar_x = document.getElementById('x');
var bar_y = document.getElementById('y');
var bar_z = document.getElementById('z');

function toggleLed1() {
   if (session) {
      session.call("io.crossbar.iotberlin.alarmapp.toggle_lights", [0]).then(
         function () {
            console.log("LED 1 toggled");
         },
         function (e) {
            console.log("could not toggle LED 1", e);
         }
      );
   }
}

function toggleLed2() {
   if (session) {
      session.call("io.crossbar.iotberlin.alarmapp.toggle_lights", [1]).then(
         function () {
            console.log("LED 2 toggled");
         },
         function (e) {
            console.log("could not toggle LED 2", e);
         }
      );
   }
}

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
connection.onopen = function (newSession, details) {
   session = newSession;
   console.log("connected!");

   function on_accelerometer (args) {
      var data = args[0];
      //console.log(data);
      bar_x.style.width = '' + (data.x * 200 + 200).toFixed(0) + 'px';
      bar_y.style.width = '' + (data.y * 200 + 200).toFixed(0) + 'px';
      bar_z.style.width = '' + (data.z * 200 + 200).toFixed(0) + 'px';
   }

   session.subscribe("io.crossbar.iotberlin.alarmapp.on_accelerometer", on_accelerometer).then(
      function () {
         console.log("subcribed to accelerometer data");
      },
      function (e) {
         console.log("could not subscribe to accelerometer");
      }
   );
};

// fired when connection was lost (or could not be established)
//
connection.onclose = function (reason, details) {
   console.log("Connection lost: " + reason);
   session = null;
}

// now actually open the connection
//
connection.open();
