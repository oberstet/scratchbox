var topicGamepadStart = 'io.crossbar.demo.gamepad.on_start';
var topicGamepadAdded = 'io.crossbar.demo.gamepad.on_gamepad_added';
var topicGamepadRemoved = 'io.crossbar.demo.gamepad.on_gamepad_removed';
var topicGamepadChanged = 'io.crossbar.demo.gamepad.on_gamepad_changed';

// the URL of the WAMP Router (Crossbar.io)
//
var wsuri;
if (document.location.origin == "file://") {
   wsuri = "ws://127.0.0.1:8080/ws";

} else {
   wsuri = (document.location.protocol === "http:" ? "ws:" : "wss:") + "//" +
               document.location.host + "/ws";
}


// the WAMP connection to the Router
//
var connection = new autobahn.Connection({
   url: wsuri,
   realm: "realm1"
});


// fired when connection is established and session attached
//
connection.onopen = function (session, details) {
   console.log("Connected");

   session.subscribe(topicGamepadAdded, function (args) {
      var gamepad = args[0];

      console.log("Gamepad connected:", gamepad);

   }).then(
      function () {
         console.log("ok, subscribed to topic " + topicGamepadAdded);
      },
      function (e) {
         console.log("failed to subscribe to topic " + topicGamepadAdded);
      }
   );

   session.subscribe(topicGamepadChanged, function (args) {
      var changed = args[0];

      console.log("Gamepad changed:", changed);

   }).then(
      function () {
         console.log("ok, subscribed to topic " + topicGamepadChanged);
      },
      function (e) {
         console.log("failed to subscribe to topic " + topicGamepadChanged);
      }
   );
};


// fired when connection was lost (or could not be established)
//
connection.onclose = function (reason, details) {
   console.log("Connection lost: " + reason);
}


// now actually open the connection
//
connection.open();
