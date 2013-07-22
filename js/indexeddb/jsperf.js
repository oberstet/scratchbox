/*
Benchmark.prototype.setup = function() {
   // Math.floor(Math.random() * 10)
   // Math.random().toString(36).substr(2, 16)
};
 */

var db;

var dbname = "testdb";
var store1name = "store1";
var store1size = 100;


function setup (recreate) {
   window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;

   var dbname = "testdb";

   if (recreate) {
      indexedDB.deleteDatabase(dbname);
   }

   var request = indexedDB.open(dbname, 1);

   request.onerror = function (event) {
      console.log("could not open database (" + event.target.webkitErrorMessage + ")");
   };

   request.onupgradeneeded = function (event) {
      db = event.target.result;

      var store1 = db.createObjectStore(store1name);

      for (var i = 0; i < store1size; ++i) {
         var value = Math.random().toString(36).substr(2, 16);
         store1.add(value, i);
      }

      console.log("database created.");
   };

   request.onsuccess = function(event) {
      db = event.target.result;

      console.log("database opened.");
   };
}

function test1 () {
   var transaction = db.transaction([store1name]);
   var store = transaction.objectStore(store1name);

   var request = store.count();
   request.onerror = function (event) {
   };
   request.onsuccess = function (event) {
      var result = request.result;
      console.log(result);
   };
}

function dbget (key) {
   var transaction = db.transaction([store1name]);
   var store = transaction.objectStore(store1name);

   var d = new ab._Deferred();
   var request = store.get(key);

   request.onerror = function (event) {
      d.reject();
   };

   request.onsuccess = function (event) {
      d.resolve(request.result);
   };
   return d;
}


function dbget2 (count) {
   var transaction = db.transaction([store1name]);
   var store = transaction.objectStore(store1name);
   var key = Math.floor(Math.random() * store1size);
   var request = store.get(key);
   request.onsuccess = function (event) {
      var res = request.result;
      if (count > 0) {
         dbget2(count - 1);
      } else {
         console.log("done");
      }
   };
}


function test2 () {
   var deferreds = [];
   for (var i = 0; i < 100000; ++i) {
      var key = Math.floor(Math.random() * store1size);
      deferreds.push(dbget(key));
   }
   when.all(deferreds).then(function (res) {
      console.log(res.length);
   });
}

function test2a () {
   for (var i = 0; i < 100; ++i) {
      test2();
   }
}

function test3 () {
   var transaction = db.transaction([store1name]);
   var store = transaction.objectStore(store1name);

   var deferreds = [];
   for (var i = 0; i < 1000; ++i) {

      var d = new ab._Deferred();
      var key = Math.floor(Math.random() * store1size);
      var request = store.get(key);

      request.onerror = function (event) {
         d.reject();
      };

      request.onsuccess = function (event) {
         d.resolve(request.result);
      };

      deferreds.push(d);
   }

   when.all(deferreds).then(function (res) {
      console.log(res.length);
   });
}

window.onload = function () {
   setup(true);
   test1();
}
