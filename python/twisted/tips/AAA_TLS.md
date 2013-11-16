# Twisted with high-grade TLS

We want TLS with DH / ECDH and PFS so that [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) test will [show](https://www.ssllabs.com/ssltest/analyze.html?d=crossbardemo.tavendo.de) us a AAA rating and the world will be better.

For this, we need to build from source - until required patches land in both Twisted and pyOpenSSL. And we need to run monkey-patched:

 * [TlsContextFactory](https://github.com/crossbario/crossbar/blob/master/crossbar/crossbar/tlsctx.py)
 * [DH Param Generation](https://github.com/crossbario/crossbar/blob/master/crossbar/crossbar/main.py#L139)
 * [Starting](https://github.com/crossbario/crossbar/blob/master/crossbar/crossbar/netservice/hubwebsocket.py#L499)

## Checking servers

	https://www.ssllabs.com/ssltest/analyze.html?d=crossbardemo.tavendo.de
	openssl s_client -host crossbardemo.tavendo.de -port 443

http://wiki.openssl.org/index.php/Command_Line_Utilities#s_client


	"C:\OpenSSL-Win32\bin\openssl.exe" ciphers -v "ALL"


http://pastebin.com/xcUu7uEc
ECDHE-RSA-AES256-GCM-SHA384
what curve is in use?


http://safecurves.cr.yp.to/

http://pastebin.com/7nUaZRMn


http://safecurves.cr.yp.to/refs.html#1999/ansi-x962


Why is there no AES-CTR-HMAC-SHA256 in TLS?



http://www.openssl.org/news/secadv_20110208.txt


https://news.ycombinator.com/item?id=1184126

http://en.wikipedia.org/wiki/OCSP_stapling
http://blog.cloudflare.com/ocsp-stapling-how-cloudflare-just-made-ssl-30
http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_stapling
http://unmitigatedrisk.com/?p=100
http://unmitigatedrisk.com/?p=241

https://www.rapid7.com/db/vulnerabilities/http-openssl-cve-2011-0014
http://www.openssl.org/news/secadv_20110208.txt

https://www.imperialviolet.org/2009/12/20/setting-up-ocsp.html

http://wiki.nikhef.nl/grid/How_to_handle_OpenSSL_and_not_get_hurt_and_what_does_that_library_call_really_do%3F#OCSP

http://trac.nginx.org/nginx/browser/nginx/src/event/ngx_event_openssl_stapling.c


http://tools.ietf.org/html/rfc6066#section-8


https://github.com/openssl/openssl/blob/master/apps/s_server.c#L2261
https://github.com/openssl/openssl/blob/master/apps/s_server.c#L832




"The server will always generate a new DH key during the negotiation, when the DH parameters are supplied via callback and/or when the SSL_OP_SINGLE_DH_USE option of SSL_CTX_set_options(3) is set."

http://www.openssl.org/docs/ssl/SSL_CTX_set_tmp_dh_callback.html
https://www.openssl.org/docs/ssl/SSL_CTX_set_options.html

https://github.com/openssl/openssl/blob/master/ssl/s3_lib.c#L3713



https://github.com/openssl/openssl/blob/master/ssl/s3_srvr.c#L1694
https://github.com/openssl/openssl/blob/master/ssl/s3_srvr.c#L1769


https://github.com/openssl/openssl/blob/master/ssl/s3_lib.c#L3713


## Prep

	mkdir -p $HOME/tarballs
	mkdir -p $HOME/build
	mkdir -p $HOME/local/bin
	mkdir -p $HOME/local/lib
	export PATH=${HOME}/local/bin:${PATH}
	export LD_LIBRARY_PATH=${HOME}/local/lib:${LD_LIBRARY_PATH}

Build stuff (this is for Amazon Linux .. should be fine for Fedora/CentOS too):

	sudo yum -y update
	sudo yum -y install unzip
	sudo yum -y install gcc
	sudo yum -y install gcc-c++
	sudo yum -y install glibc
	sudo yum -y install make
	sudo yum -y install binutils
	sudo yum -y install patch
	sudo yum -y install libaio
	sudo yum -y install bc
	sudo yum -y install zlib-devel
	sudo yum -y install bzip2-devel
	sudo yum -y install openssl-devel
	sudo yum -y install ncurses-devel
	sudo yum -y install sqlite-devel
	sudo yum -y install readline-devel


## OpenSSL

	cd $HOME/tarballs
	wget http://www.openssl.org/source/openssl-1.0.1e.tar.gz
	cd $HOME/build
	tar xvzf ../openssl-1.0.1e.tar.gz
	cd openssl-1.0.1e
	./config --prefix=$HOME/local --openssldir=$HOME/local/openssl shared zlib
	make
	make install


## Python

	cd $HOME/tarballs
	wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2
	cd $HOME/build
	tar xvjf ../Python-2.7.5.tar.bz2
	cd Python-2.7.5
	./configure --prefix=$HOME/local
	make
	make install


## Setuptools, Virtualenv

	cd $HOME/tarballs
	wget https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz
	wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz
	cd $HOME/build
	tar xvzf ../tarballs/setuptools-1.1.6.tar.gz
	cd setuptools-1.1.6
	$HOME/local/bin/python setup.py install
	cd $HOME/build
	tar xvzf ../tarballs/virtualenv-1.10.1.tar.gz
	cd virtualenv-1.10.1
	$HOME/local/bin/python setup.py install


## pyOpenSSL

We build from HEAD with the patch from [here](https://bugs.launchpad.net/pyopenssl/+bug/1233810) applied:

	sudo yum install bzr
	cd $HOME/build
	bzr branch lp:pyopenssl
	cd pyopenssl
	
	wget https://bugs.launchpad.net/pyopenssl/+bug/1233810/+attachment/3853911/+files/ecdh.patch
	patch -p0 < ecdh.patch
	
	vi setup.py
	vi OpenSSL/version.py
	
	$HOME/local/bin/python setup.py build_ext -I$HOME/local/include/ -L$HOME/local/lib/
	$HOME/local/bin/python setup.py build
	$HOME/local/bin/python setup.py install
	

## Twisted

We build regular release:

	cd $HOME/tarballs
	wget https://pypi.python.org/packages/source/T/Twisted/Twisted-13.1.0.tar.bz2
	cd $HOME/build
	tar xvjf ../tarballs/Twisted-13.1.0.tar.bz2
	$HOME/local/bin/python setup.py install


## Run on "privileged" ports (FreeBSD)

Add the following to `sysctl.conf`:

	net.inet.ip.portrange.reservedhigh=0


## Run on "privileged" ports (Linux)

	sudo setcap 'cap_net_bind_service=+ep' $HOME/local/bin/python2.7
	sudo sh -c 'echo "$HOME/local/lib" > /etc/ld.so.conf.d/crossbar.conf'
	sudo ldconfig


> Note: `LD_LIBRARY_PATH` won't cut it! It will get (silently) ignored for executables with escalated priviliges which not only includes `sudo`/`setuid` started programs, but also programs for which `setcap` has been adjusted. The awesome shit known as "GNU glibc" calls this a "security feature". Right;)

