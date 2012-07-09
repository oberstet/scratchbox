Calling ExtDirect from Curl
===========================

Shows how to call into ExtDirect using **curl**.

Download and unpack ExtJS.

Start PHP with embedded Web server in ExtJS root directory:

    cd extjs-4.1.0/
    php -S 127.0.0.1:8000

Run **curl** against ExtDirect endpoint

    curl -v -H "Content-Type: application/json" -d @body.txt "http://127.0.0.1:8000/examples/direct/php/router.php"

This will output something like

    * About to connect() to 127.0.0.1 port 8000 (#0)
    *   Trying 127.0.0.1... connected
    * Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
    > POST /examples/direct/php/router.php HTTP/1.1
    > User-Agent: curl/7.21.1 (i686-pc-mingw32) libcurl/7.21.1 OpenSSL/0.9.8k zlib/1.2.3
    > Host: 127.0.0.1:8000
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 79
    >
    < HTTP/1.1 200 OK
    < Host: 127.0.0.1:8000
    < Connection: close
    < X-Powered-By: PHP/5.4.4
    < Content-Type: text/javascript
    <
    {"type":"rpc","tid":1,"action":"TestAction","method":"multiply","result":984}* Closing connection #0
    

The request body was:

    {"action":"TestAction","method":"multiply","data":["123"],"type":"rpc","tid":1}
         
