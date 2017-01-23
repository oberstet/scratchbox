
aufsetzen als "postfix satellite"

FQDN: bvr-sql18.local.parcit
Relay: svr-cm.local.parcit


/etc/postfix/main.cf

/etc/init.d/postfix reload

sudo dpkg-reconfigure postfix


http://www.simplehelp.net/2008/12/01/how-to-send-email-from-the-linux-command-line/

mail -s "Hello world" tobias.oberstein@parcit.de


```
oberstet@bvr-sql18:~$ telnet svr-cm.local.parcit 25
Trying 10.200.1.23...
Connected to svr-cm.local.parcit.
Escape character is '^]'.
220 SVR-CM.local.parcit Microsoft ESMTP MAIL Service, Version: 7.5.7601.17514 ready at  Fri, 9 Oct 2015 10:50:42 +0200
helo gmail.com
250 SVR-CM.local.parcit Hello [10.200.1.67]
mail from: tobias.oberstein@parcit.de
250 2.1.0 tobias.oberstein@parcit.de....Sender OK
rcpt to: tobias.oberstein@gmail.com
250 2.1.5 tobias.oberstein@gmail.com
data
354 Start mail input; end with <CRLF>.<CRLF>
dgdhg
dfgjh


.
250 2.6.0 <SVR-CMryWtIIZS2TRqf000002a3@SVR-CM.local.parcit> Queued mail for delivery
```
