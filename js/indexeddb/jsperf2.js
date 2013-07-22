var store1size = 10000;
var readsize = 100000;

window.onload = function () {
   var db;
   var dbname = "testdb";
   var store1name = "store1";

   window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;

   indexedDB.deleteDatabase(dbname);

   var request = indexedDB.open(dbname, 1);

   request.onerror = function (event) {
      console.log("could not open database (" + event.target.webkitErrorMessage + ")");
   };

   request.onupgradeneeded = function (event) {
      db = event.target.result;

      var store1 = db.createObjectStore(store1name);
      console.log("database created.");

      function addrecords (count) {
         var value = Math.random().toString(36).substr(2, 16);
         var req = store1.put(value, count);
         if (count > 0) {
            addrecords(count - 1);
         } else {
            var req = store1.count();
            req.onsuccess = function (event) {
               var ended = (new Date).getTime();
               console.log(req.result + " records added in " + (ended - started) + "ms (" + Math.round(req.result / ((ended - started) / 1000)) + " records/s)");
            };
         }
      };

      var started = (new Date).getTime();
      addrecords(store1size - 1);
   };

   request.onsuccess = function(event) {
      db = event.target.result;
      console.log("database opened.");

      function getrecords (count, got) {
         var transaction = db.transaction([store1name], "readonly");
         var store = transaction.objectStore(store1name);
         var key = Math.floor(Math.random() * store1size);
         var request = store.get(key);
         request.onsuccess = function (event) {
            var res = request.result;
            if (got < count) {
               getrecords(count, got + 1);
            } else {
               var ended = (new Date).getTime();
               console.log(got + " records read in " + (ended - started) + "ms (" + Math.round(got / ((ended - started) / 1000)) + " records/s)");
            }
         };
      };

      var started = (new Date).getTime();
      getrecords(readsize, 0);
   };
}
