# Arduino Yun - Random Notes

## System description

The Arduino Yun consists of a MCU and a main CPU. The main CPU is MIPS-based and runs Linux (a distro called [Linino](https://github.com/arduino/linino) derived from OpenWRT).

The base system already includes a Python 2.7.3:

	root@Arduino:~# uname -a
	Linux Arduino 3.8.3 #8 Mon Aug 19 16:22:39 CEST 2013 mips GNU/Linux
	root@Arduino:~# python -V
	Python 2.7.3
	root@Arduino:~# python
	Python 2.7.3 (default, Aug  8 2013, 22:36:42)
	[GCC 4.6.4 20121210 (prerelease)] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

## Installing Autobahn on the Yun

1. Install some packages

		opkg update
		opkg install bzip2
		opkg install tar
		opkg install unzip
		opkg install wget

2. Install Python `setuptools` and `virtualenv`

		cd /tmp
		wget https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.1.tar.gz 
		tar xvzf setuptools-1.4.1.tar.gz
		cd setuptools-1.4.1
		python setup.py install

		cd /tmp
		wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz
		tar xvzf virtualenv-1.10.1.tar.gz
		cd virtualenv-1.10.1
		python setup.py install
		 
3. Create a new Python environment on SD Card

		virtualenv -p /usr/bin/python --always-copy /mnt/sda1/python1

4. Install Python `zope.interface`, `twisted` and `autobahn` into the new Python environment

		cd /tmp
		wget https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.0.5.zip
		unzip zope.interface-4.0.5.zip
		cd zope.interface-4.0.5
		/mnt/sda1/python1/bin/python setup.py install

		cd /tmp
		wget https://pypi.python.org/packages/source/T/Twisted/Twisted-13.2.0.tar.bz2
		tar xvjf Twisted-13.2.0.tar.bz2
		cd Twisted-13.2.0
		/mnt/sda1/python1/bin/python setup.py install

		cd /tmp
		wget https://pypi.python.org/packages/source/a/autobahn/autobahn-0.6.5.zip
		unzip autobahn-0.6.5.zip
		cd autobahn-0.6.5/autobahn
		/mnt/sda1/python1/bin/python setup.py install

## Resources
 
 * http://fibasile.github.io/arduino-yun-getting-started.html
 * http://download.linino.org/dogstick/all-in-one/latest/packages/

## My Yun

 * Wifi AP: 192.168.240.1
 * MAC: 90:a2:da:f0:0c:4e
 * ssh -l root 192.168.1.126
