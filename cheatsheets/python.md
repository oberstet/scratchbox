## Building

On Windows, got with Python 2.7 / 32 Bit MSI installer for least hassles.

On Unix, distro maintainers usually fuck around with upstream sources .. generally for no reason / no good.

Hence, go with the source, Luke!

### Ubuntu

Get stuff for building

	sudo apt-get install libbz2-dev
	sudo apt-get install libssl-dev
	sudo apt-get install libsqlite3-dev
	sudo apt-get install libreadline6-dev
	sudo apt-get install ncurses-dev

Then do the usual `configure`, `make`, `make install` dance.
