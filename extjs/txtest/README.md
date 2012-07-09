Calling ExtDirect from Twisted
==============================

Shows how to call into ExtDirect using **Twisted**.

Download and unpack ExtJS.

Start PHP with embedded Web server in ExtJS root directory:

    cd extjs-4.1.0/
    php -S 127.0.0.1:8000

Run **curl** against ExtDirect endpoint

    python testcall.py

This will output something like

    2012-07-09 21:39:06+0200 [-] Log opened.
    2012-07-09 21:39:06+0200 [-] Starting factory <HTTPClientFactory: http://127.0.0.1:8000/examples/direct/php/router.php>
    2012-07-09 21:39:06+0200 [HTTPPageGetter,client] result =  984
    2012-07-09 21:39:06+0200 [HTTPPageGetter,client] Stopping factory <HTTPClientFactory: http://127.0.0.1:8000/examples/direct/php/router.php>
    2012-07-09 21:39:06+0200 [-] Main loop terminated.
