var WebSocket = require('ws');

var ws = new WebSocket('ws://127.0.0.1:9000/echows', {protocol: ["foo", "bar"]});

ws.onopen = function () {
   console.log("WebSocket connection opened");
   console.log("Protocol", ws.protocol);
   ws.send('Hello, world!');
}

ws.onmessage = function (e) {
   if (typeof e.data === "string") {
      console.log(e.data);
   } else {
      if (e.data instanceof ArrayBuffer) {
         console.log("binary message received (ArrayBuffer)");
      //} else if (e.data instanceof Blob) {
      //   console.log("binary message received (Blob)");
      } else if (e.data instanceof Buffer) {
         console.log("binary message received (NodeJS/Buffer)");
      } else {
         console.log("binary message of illegal type");
      }
   }
   ws.close(1000, "I am done");
}

ws.onclose = function (e) {
   console.log("WebSocket connection closed");
   console.log(e.code);
   console.log(e.reason);
   console.log(e.wasClean);
}
