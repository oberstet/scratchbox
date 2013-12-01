# Stuff

The default username is `pi` and the default password is `raspberry`.

http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card
http://www.ideaheap.com/2013/07/stopping-sd-card-corruption-on-a-raspberry-pi/


## PyPy

	mkdir $HOME/tarballs
	cd $HOME/tarballs
	wget https://bitbucket.org/pypy/pypy/downloads/pypy-2.2.1-linux-armhf-raspbian.tar.bz2
	cd $HOME
	tar xvjf tarballs/pypy-2.2.1-linux-armhf-raspbian.tar.bz2
	wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | $HOME/pypy-2.2.1-linux-armhf-raspbian/bin/pypy



## Update

[How to update](http://raspberrypi.stackexchange.com/questions/4698/how-can-i-keep-my-raspbian-wheezy-up-to-date) and keep updated the Pi.

	sudo apt-get update
	sudo apt-get upgrade
 