# Python 2.7.9+

Python 2.7.9+ activates strict hostname verification for SSL. This breaks stuff. Here is how to fix.

*Warning: all of the following is a **royal pain in the ass**. But here are the nitty gritty details.*

First off, FreeBSD does not include a certificate database in a base installation. Neither does Python include a certificate database.

The way to add this to FreeBSD is from the port `security/ca_root_nss` or by adding the package:

```console
$ pkg install -y ca_root_nss
```

Then, Python uses the default paths configured in OpenSSL for certificates. You can check those paths by doing:

```python
import ssl
ssl.get_default_verify_paths()
```

Unfortunately, the package `ca_root_nss` installs certificates in a different location than the OpenSSL default paths configured.

All this means that certificate verification currently [fails](http://unix.stackexchange.com/questions/176294/what-should-i-do-about-python-2-7-9-not-looking-for-ssl-certificates-in-the-righ) with Python 2.7.9:

```console
[oberstet@brummer1 ~]$ /usr/local/bin/python2.7
Python 2.7.9 (default, Dec 31 2014, 03:40:40)
[GCC 4.2.1 Compatible FreeBSD Clang 3.3 (tags/RELEASE_33/final 183502)] on freebsd10
Type "help", "copyright", "credits" or "license" for more information.
>>> import ssl
>>> ssl.get_default_verify_paths()
DefaultVerifyPaths(cafile=None, capath=None, openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/etc/ssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/etc/ssl/certs')
>>> import urllib
>>> urllib.urlopen("https://www.google.com")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/urllib.py", line 87, in urlopen
    return opener.open(url)
  File "/usr/local/lib/python2.7/urllib.py", line 213, in open
    return getattr(self, name)(url)
  File "/usr/local/lib/python2.7/urllib.py", line 443, in open_https
    h.endheaders(data)
  File "/usr/local/lib/python2.7/httplib.py", line 997, in endheaders
    self._send_output(message_body)
  File "/usr/local/lib/python2.7/httplib.py", line 850, in _send_output
    self.send(msg)
  File "/usr/local/lib/python2.7/httplib.py", line 812, in send
    self.connect()
  File "/usr/local/lib/python2.7/httplib.py", line 1212, in connect
    server_hostname=server_hostname)
  File "/usr/local/lib/python2.7/ssl.py", line 350, in wrap_socket
    _context=self)
  File "/usr/local/lib/python2.7/ssl.py", line 566, in __init__
    self.do_handshake()
  File "/usr/local/lib/python2.7/ssl.py", line 788, in do_handshake
    self._sslobj.do_handshake()
IOError: [Errno socket error] [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)
>>>
```

Note that there is a FreeBSD [bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=196431) for package `ca_root_nss` addressing this.

Here is how to fix manually:

```console
ln -sf /usr/local/etc/ssl/cert.pem /etc/ssl/cert.pem
```

Also note that CPython (or PyPy) compiled from vanilla sources is looking in yet a different location. Again, here is a manual fix:

```console
ln -s /usr/local/etc/ssl/cert.pem /usr/local/openssl/cert.pem
```

Now verification should work:

```console
[oberstet@brummer1 ~]$ ~/pypy1/bin/pypy
Python 2.7.8 (a980ebb26592ed26706cd33a4e05eb45b5d3ea09, Dec 13 2014, 07:55:06)
[PyPy 2.4.0 with GCC 4.2.1 Compatible FreeBSD Clang 3.4.1 (tags/RELEASE_34/dot1-final 208032)] on freebsd10
Type "help", "copyright", "credits" or "license" for more information.
>>>> import urllib
>>>> urllib.urlopen("https://www.google.com")
<addinfourl at 34444694016L whose fp = <socket._fileobject object at 0x0000000804ba2c98>>
>>>>
```
