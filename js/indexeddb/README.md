    Unified communication and storage API
    We problably need a combination of : IndexedDB + WebWorkers + WebSocket
    IndexedDB:
    Everything happens within transactions
    Transactions auto-commit !
    Is there manual commit and/or rollback? Only rollback (“abort()”)
    Is there a way to get notified when transaction was committed and/or rolled back? Yes and yes (“oncomplete, onabort, onerror”).
    stream == database OR stream == object store?
    Fully compatible wrapper/shim (drop in replacement) OR value-added DB layer?
    Tag transaction start/end time? Only start or only end time? Tag transaction with counter?
    Conflict “resolution”: plainly apply all transactions in timestamp order .. but what if offline?
    Return array of values for get() .. from the replicas. Let the app resolve back to single value.
    