var db;

window.onload = function () {
   console.log("start ..");

   window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;
   window.IDBTransaction = window.IDBTransaction || window.webkitIDBTransaction || window.msIDBTransaction;
   window.IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange || window.msIDBKeyRange;

   if (!window.indexedDB) {
      window.alert("IndexedDB not supported on your browser.");
   } else {
      init();
   }
}

function init() {
   // This is what our customer data looks like.
   const customerData = [
     { ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" },
     { ssn: "555-55-5555", name: "Donna", age: 32, email: "donna@home.org" }
   ];

   const dbName = "mydb2";

   var request = indexedDB.open(dbName, 2);

   request.onerror = function(event) {
      console.log("could not open database");
   };

   request.onupgradeneeded = function(event) {
     db = event.target.result;

     db.createObjectStore("foobar");

     // Create an objectStore to hold information about our customers. We're
     // going to use "ssn" as our key path because it's guaranteed to be
     // unique.
     var objectStore = db.createObjectStore("customers", { keyPath: "ssn" });

     // Create an index to search customers by name. We may have duplicates
     // so we can't use a unique index.
     objectStore.createIndex("name", "name", { unique: false });

     // Create an index to search customers by email. We want to ensure that
     // no two customers have the same email, so use a unique index.
     objectStore.createIndex("email", "email", { unique: true });

     // Store values in the newly created objectStore.
     for (var i in customerData) {
       objectStore.add(customerData[i]);
     }

      console.log("database created.");
   };

   request.onsuccess = function(event) {
      db = event.target.result;
      console.log("database opened.");

      var transaction = db.transaction(["customers"]);
      var objectStore = transaction.objectStore("customers");
      var request = objectStore.get("444-44-4444");
      request.onerror = function(event) {
        // Handle errors!
      };
      request.onsuccess = function(event) {
        // Do something with the request.result!
        alert("Name for SSN 444-44-4444 is " + request.result.name);
      };
   };
}

function test () {
   var transaction = db.transaction(["customers"]);
   var store = transaction.objectStore("customers");
   dbget(store, '444-44-4444').then(ab.log, ab.log);
}

function dbget (store, key) {
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
