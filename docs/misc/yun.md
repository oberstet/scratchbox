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

When the Yun is started for first time (or after factory reset), it runs Wifi in AP mode. The Yun will create a local network and can be reached via HTTP Web at

	192.168.240.1

The default password is `arduino`.

You can then configure the Yun to connect to another Wifi in client mode. When you do that, it'll reboot, and the Wifi AP mode of Yun will be deactivated.

The Yun can be reset to factory state by pressing the little RST button on the board for at least 30s.

The Yun seems to have 64MB of internal Flash. Half of memory seems to be reserved for factory recovery. That leaves 32MB. Further, the `/` mountpoint only is allocated 8MB, and most of the other memory is mounted at `/tmp`.

Taking into account that `/` is used for everything in the Linux base system, the rest seems not enough for installing all Python packages required to run Autobahn.

Maybe we cram Autobahn and dependencies into `/`, but we first try a different approach: setting up a Python [virtualenv](http://www.virtualenv.org) into `/mnt/sda1`.   


http://docs.python-guide.org/en/latest/dev/virtualenvs/


http://wiki.openwrt.org/doc/techref/flash.layout
http://wiki.openwrt.org/doc/techref/filesystems

## Installing Autobahn on the Yun

1. Install some packages

		opkg update
		opkg install bzip2
		opkg install tar
		opkg install unzip
		opkg install wget
		opkg install fdisk
		opkg install e2fsprogs
		opkg install pyopenssl
		opkg install python-openssl
		opkg install python-bzip2
		opkg install python-sqlite3
		opkg install python-ncurses
		opkg install python-crypto
		opkg install python-cjson


		mkfs.ext3 /dev/sda1
		mkdir /opt
		mount -t ext3 /dev/sda1 /opt
		echo "hello" > /opt/hello.txt
		cat /opt/hello.txt

		mkdir /opt/download
		mkdir /opt/build


root@Arduino:~# cat /etc/config/fstab
config mount
        option target       /opt
        option device       /dev/sda1
        option fstype       ext3
        option options      rw,sync
        option enabled      1
        option enabled_fsck 1


/etc/init.d/fstab restart


> Note: It seems you need to redo the `opkg update` after each reboot of Yun.
> 

2. Install Python `setuptools` and `virtualenv`

> Note: Yun does not come with certificates installed. You can [do that](http://wiki.openwrt.org/doc/howto/wget-ssl-certs), but we skip it for now.
> 
		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz
		cd /opt/build
		tar xvzf ../download/virtualenv-1.10.1.tar.gz
		cd virtualenv-1.10.1
		python setup.py install
		 
3. Create a new Python environment on SD Card


		virtualenv --system-site-packages /opt/python

4. Install Python `zope.interface`, `twisted` and `autobahn` into the new Python environment

		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.1.tar.gz
		cd /opt/build
		tar xvzf ../download/setuptools-1.4.1.tar.gz
		cd setuptools-1.4.1
		/opt/python/bin/python setup.py install

		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.0.5.zip
		cd /opt/build
		unzip ../download/zope.interface-4.0.5.zip
		cd zope.interface-4.0.5
		/opt/python/bin/python setup.py install

		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/T/Twisted/Twisted-13.2.0.tar.bz2
		cd /opt/build
		tar xvjf ../download/Twisted-13.2.0.tar.bz2
		cd Twisted-13.2.0

http://stackoverflow.com/a/5128593/884770
https://gist.github.com/oberstet/7696402

		/opt/python/bin/python setup.py install

		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/a/autobahn/autobahn-0.6.5.zip
		cd /opt/build
		unzip ../download/autobahn-0.6.5.zip
		cd autobahn-0.6.5
		/opt/python/bin/python setup.py install

		cd /opt/download
		wget --no-check-certificate https://pypi.python.org/packages/source/p/pyserial/pyserial-2.7.tar.gz
		cd /opt/build
		tar xvzf ../download/pyserial-2.7.tar.gz
		cd pyserial-2.7
		 



root@Arduino:/opt/build/pyserial-2.7# cat /etc/inittab
::sysinit:/etc/init.d/rcS S boot
::shutdown:/etc/init.d/rcS K shutdown
#ttyATH0::askfirst:/bin/ash --login


http://wiki.openwrt.org/doc/uci


## Resources
 
 * http://fibasile.github.io/arduino-yun-getting-started.html
 * http://download.linino.org/dogstick/all-in-one/latest/packages/

## My Yun

 * Wifi AP: 192.168.240.1
 * MAC: 90:a2:da:f0:0c:4e
 * ssh -l root 192.168.1.126
