Wifi AP: 192.168.240.1
MAC: 90:a2:da:f0:0c:4e

ssh -l root 192.168.1.126

http://fibasile.github.io/arduino-yun-getting-started.html

root@Arduino:~# uname -a
Linux Arduino 3.8.3 #8 Mon Aug 19 16:22:39 CEST 2013 mips GNU/Linux
root@Arduino:~# python -V
Python 2.7.3
root@Arduino:~# python
Python 2.7.3 (default, Aug  8 2013, 22:36:42)
[GCC 4.6.4 20121210 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>

http://download.linino.org/dogstick/all-in-one/latest/packages/


1. Install some packages

		opkg update
		opkg install bzip2
		opkg install tar
		opkg install unzip

2. Download and install stuff

		cd /tmp
		curl --insecure https://pypi.python.org/packages/source/T/Twisted/Twisted-13.2.0.tar.bz2 -o Twisted-13.2.0.tar.bz2
		curl --insecure https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.0.5.zip -o zope.interface-4.0.5.zip
		curl --insecure https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.1.tar.gz -o setuptools-1.4.1.tar.gz 

3. Install stuff

		unzip zope.interface-4.0.5.zip
		cd zope.interface-4.0.5/
		python setup.py install
		cd ..
		tar xvjf Twisted-13.2.0.tar.bz2
		cd Twisted-13.2.0
		python setup.py install
		cd ..
		tar xvzf setuptools-1.4.1.tar.gz
		cd setuptools-1.4.1
		cd 
