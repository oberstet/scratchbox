var autobahn = require('autobahn');

var connection = new autobahn.Connection({
   url: "ws://crossbar-test.cloudapp.net/ws",
   realm: "ms_iot_hack_01"
//   url: "ws://crossbar-test.cloudapp.net:8080/ws",
//   realm: "realm1"
});

connection.onopen = function (session, details) {

   console.log("connected!");

   // alarm active state and procedures
   //
   var alarm_active = false;

   function get_alarm_active () {
      return alarm_active;
   }

   session.register("io.crossbar.iotberlin.alarmapp.get_alarm_active", get_alarm_active).then(
      function () {
         console.log("registered get_alarm_active");
      },
      function (e) {
         console.log(e);
      }
   );

   function set_alarm_active (args) {
      var active = args[0];

      console.log("set_alarm_active", alarm_active, active);

      if (alarm_active != active) {
         alarm_active = active;
         session.publish("io.crossbar.iotberlin.alarmapp.on_alarm_active", [alarm_active])

         if (alarm_active) {
            session.call("io.crossbar.iotberlin.alarmapp.set_blinking", [500]);

            session.call("io.crossbar.hack.take_picture").then(
               function (res) {
                  console.log("got picture");
                  session.publish("io.crossbar.iotberlin.on_picture_taken", [res]);
               },
               function (e) {
                  console.log(e);
               }
            );

            console.log("ALARM triggered!!!");
         } else {
            session.call("io.crossbar.iotberlin.alarmapp.set_blinking", [0]);
            console.log("ALARM cleared");
         }
      }
      return alarm_active;
   }

   session.register("io.crossbar.iotberlin.alarmapp.set_alarm_active", set_alarm_active).then(
      function () {
         console.log("registered set_alarm_active");
      },
      function (e) {
         console.log(e);
      }
   );


   // alarm armed state and procedures
   //
   var alarm_armed = false;

   function get_alarm_armed () {
      return alarm_armed;
   }

   session.register("io.crossbar.iotberlin.alarmapp.get_alarm_armed", get_alarm_armed).then(
      function () {
         console.log("registered get_alarm_armed");
      },
      function (e) {
         console.log(e);
      }
   );

   var th = 0.1;

   function on_accelerometer (args) {
      var data = args[0];
      console.log(data);

      var trigger =
         (Math.abs(0 - data.x) > th) ||
         (Math.abs(0 - data.y) > th) ||
         (Math.abs(1 - data.z) > th);

      if (trigger) {
         if (alarm_armed) {
            set_alarm_active([true]);
         }
      }
   }

   var accel_subscription = null;

   function set_alarm_armed (args) {

      var active = args[0];

      console.log("set_alarm_armed", alarm_armed, active);

      if (alarm_armed != active) {

         alarm_armed = active;

         if (alarm_armed) {

            session.subscribe("io.crossbar.iotberlin.alarmapp.on_accelerometer", on_accelerometer).then(
               function (sub) {
                  console.log("subcribed to on_accelerometer")
                  accel_subscription = sub;
               },
               function (e) {
                  console.log(e);
               }
            );

         } else {

            if (accel_subscription) {
               accel_subscription.unsubscribe().then(
                  function () {
                     console.log("unsubscribed from on_accelerometer")
                  },
                  function (e) {
                     console.log(e);
                  }
               );
            }
         }
         session.publish("io.crossbar.iotberlin.alarmapp.on_alarm_armed", [alarm_armed])
      }

      return alarm_armed;
   }

   session.register("io.crossbar.iotberlin.alarmapp.set_alarm_armed", set_alarm_armed).then(
      function () {
         console.log("registered set_alarm_armed");
      },
      function (e) {
         console.log(e);
      }
   );

   //console.log(set_alarm_armed(false));
};

connection.onclose = function (reason, details) {
   console.log("Connection lost: " + reason);
}

connection.open();
