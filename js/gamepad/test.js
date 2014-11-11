var session = null;
var baseUri = 'io.crossbar.demo.gamepad.oberstet';

var controllers = {};
var controllersLastValues = {};


function onGamepadConnect (e) {
   addGamepad(e.gamepad);
}


function onGamepadDisconnect (e) {
   removeGamepad(e.gamepad);
}


function addGamepad (gamepad) {
   controllers[gamepad.index] = gamepad;
   controllersLastValues[gamepad.index] = {
      buttons: {},
      axes: {}
   };
   window.requestAnimationFrame(readGamepads);
}


function removeGamepad (gamepad) {
   delete controllers[gamepad.index];
   delete controllersLastValues[gamepad.index];
}


function readGamepads() {
   scanGamepads();

   var changeEvent = {
      time: performance.now(),
      controllers: {}
   };

   for (j in controllers) {

      var controller = controllers[j];

      changeEvent

      for (var i = 0; i < controller.buttons.length; ++i) {
         var val = controller.buttons[i];
         if (typeof(val) == "object") {
            val = val.value;
         }

         if (controllersLastValues[j].buttons[i] != val) {
            controllersLastValues[j].buttons[i] = val;

            if (!changeEvent.controllers[j]) {
               changeEvent.controllers[j] = {buttons: {}};
            }

            changeEvent.controllers[j].buttons[i] = val;
         }
      }

      for (var i = 0; i < controller.axes.length; ++i) {
         var val = controller.axes[i];

         if (controllersLastValues[j].axes[i] != val) {
            controllersLastValues[j].axes[i] = val;

            if (!changeEvent.controllers[j]) {
               changeEvent.controllers[j] = {axes: {}};
            }
            if (!changeEvent.controllers[j].axes) {
               changeEvent.controllers[j].axes = {};
            }

            changeEvent.controllers[j].axes[i] = val;
         }
      }
   }

   if (Object.keys(changeEvent.controllers).length) {
      if (session) {

      } else {
         console.log(baseUri, changeEvent);
      }
   }

   window.requestAnimationFrame(readGamepads);
}


function scanGamepads() {
   var gamepads = navigator.getGamepads();
   for (var i = 0; i < gamepads.length; ++i) {
      if (gamepads[i]) {
         if (!(gamepads[i].index in controllers)) {
            addGamepad(gamepads[i]);
         } else {
            controllers[gamepads[i].index] = gamepads[i];
         }
      }
   }
}


window.addEventListener("gamepadconnected", onGamepadConnect);
window.addEventListener("gamepaddisconnected", onGamepadDisconnect);

scanGamepads();
