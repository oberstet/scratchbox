var isServer = true;

window.onload = function () {
   console.log("start");

   server(function () {
      var s = 0;
      for (var i = 0; i < 10; ++i) {
         s += i;
      }
      console.log(s);
   });

   client(function () {
      var x = 23 * 666;
      console.log(x);
   });
}

function server (block) {
   if (isServer) {
      console.log("executing code on server");
      console.log(block.toString());
      block();
   } else {
      console.log("skipping server code");
   }
}

function client (block) {
   if (!isServer) {
      console.log("executing code on client");
      console.log(block.toString());
      block();
   } else {
      console.log("skipping client code");
   }
}
