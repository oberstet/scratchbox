var WebSocketServer = require('ws').Server;

var wss = new WebSocketServer({port: 9000, verifyClient: function (info) {
   console.log("Client connecting ..");
   console.log("URL", info.url);
   console.log("Origin", info.origin);
   console.log("Protocols", info.protocol);
   return true;
}});

wss.on('connection', function (client) {
   console.log("Client connected.");
   console.log("Protocol", client.protocol);
   client.on('message', function (message) {
      console.log('received: %s', message);
   });
   client.send('something');
});
