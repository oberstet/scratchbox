var topicGamepadStart = 'io.crossbar.demo.gamepad.on_start';
var topicGamepadAdded = 'io.crossbar.demo.gamepad.on_gamepad_added';
var topicGamepadRemoved = 'io.crossbar.demo.gamepad.on_gamepad_removed';
var topicGamepadChanged = 'io.crossbar.demo.gamepad.on_gamepad_changed';


var session = null;

function publishOrLog (topic, evt) {
   if (session) {
      session.publish(topic, [evt]);
   } else {
      console.log(topic, evt);
   }
}

publishOrLog(topicGamepadStart, {time: performance.now()});


var gamepads = {};
var gamepadsLastValues = {};


function onGamepadConnect (e) {
   addGamepad(e.gamepad);
}


function onGamepadDisconnect (e) {
   removeGamepad(e.gamepad);
}


function addGamepad (gamepad) {
   gamepads[gamepad.index] = gamepad;
   gamepadsLastValues[gamepad.index] = {
      buttons: {},
      axes: {}
   };

   publishOrLog(topicGamepadAdded, {
      time: performance.now(),
      id: gamepad.id,
      index: gamepad.index,
      buttons: gamepad.buttons.length,
      axes: gamepad.axes.length,
   });

   document.getElementById("hint").innerHTML = "Ok, " + Object.keys(gamepads).length + " gamepad(s) connected.";

   window.requestAnimationFrame(readGamepads);
}


function removeGamepad (gamepad) {
   delete gamepads[gamepad.index];
   delete gamepadsLastValues[gamepad.index];

   publishOrLog(topicGamepadRemoved, {
      time: performance.now(),
      id: gamepad.id,
      index: gamepad.index
   });

   if (!Object.keys(gamepads).length) {
      document.getElementById("hint").innerHTML = "Press any button on your gamepad to connect ..";
   }
}


function readGamepads() {
   scanGamepads();

   var changeEvent = {
      time: performance.now(),
      gamepads: {}
   };

   for (j in gamepads) {

      var gamepad = gamepads[j];

      changeEvent

      for (var i = 0; i < gamepad.buttons.length; ++i) {
         var val = gamepad.buttons[i];
         if (typeof(val) == "object") {
            val = val.value;
         }

         if (gamepadsLastValues[j].buttons[i] != val) {
            gamepadsLastValues[j].buttons[i] = val;

            if (!changeEvent.gamepads[j]) {
               changeEvent.gamepads[j] = {buttons: {}};
            }

            changeEvent.gamepads[j].buttons[i] = val;
         }
      }

      for (var i = 0; i < gamepad.axes.length; ++i) {
         var val = gamepad.axes[i];

         if (gamepadsLastValues[j].axes[i] != val) {
            gamepadsLastValues[j].axes[i] = val;

            if (!changeEvent.gamepads[j]) {
               changeEvent.gamepads[j] = {axes: {}};
            }
            if (!changeEvent.gamepads[j].axes) {
               changeEvent.gamepads[j].axes = {};
            }

            changeEvent.gamepads[j].axes[i] = val;
         }
      }
   }

   if (Object.keys(changeEvent.gamepads).length) {
      publishOrLog(topicGamepadChanged, changeEvent);
   }

   window.requestAnimationFrame(readGamepads);
}


function scanGamepads() {
   var gamepads = navigator.getGamepads();
   for (var i = 0; i < gamepads.length; ++i) {
      if (gamepads[i]) {
         if (!(gamepads[i].index in gamepads)) {
            addGamepad(gamepads[i]);
         } else {
            gamepads[gamepads[i].index] = gamepads[i];
         }
      }
   }
}


window.addEventListener("gamepadconnected", onGamepadConnect);
window.addEventListener("gamepaddisconnected", onGamepadDisconnect);

scanGamepads();


///////////////

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
connection.onopen = function (newSession, details) {
   console.log("Connected");
   session = newSession;
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

