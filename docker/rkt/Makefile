RKT_VERSION='1.25.0'

build:
	time docker build \
		--build-arg RKT_VERSION=${RKT_VERSION} \
		-t crossbario/rkt-armhf \
		-f ./Dockerfile.armhf .

qemu_deps:
	mkdir -p ./.qemu
	cp /usr/bin/qemu-aarch64-static ./.qemu
	cp /usr/bin/qemu-arm-static ./.qemu

# https://github.com/rkt/rkt/archive/v1.25.0.tar.gz


pi@raspberrypi:~/rkt-1.25.0 $ export PATH=~/go/bin:${PATH}
pi@raspberrypi:~/rkt-1.25.0 $ which go
/home/pi/go/bin/go
pi@raspberrypi:~/rkt-1.25.0 $ go version
go: cannot find GOROOT directory: /usr/local/go
pi@raspberrypi:~/rkt-1.25.0 $ export GOROOT=~/go
pi@raspberrypi:~/rkt-1.25.0 $ go version
go version go1.8.1 linux/arm
pi@raspberrypi:~/rkt-1.25.0 $


Edge Server runs (from prepared image):
- Ubuntu
- Docker
- bundled Docker images for:
	- private Docker registry
	- Crossbar.io Fabric

Pis run (from prepared image):
- Raspbian
- Docker
- bundled Docker images for:
	- Autobahn Python
	- Autobahn JavaScript
	- Autobahn C++

Presentation Server runs:
- Windows
- Edge / Chromium / Firefox

Crossbar.io Fabric Center
- Cloud Service
- Edge Server can work independently with limited features


When Pi starts, a Crossbar.io Fabric node is started
from a Docker container using systemd

The Crossbar.io Fabric Docker container contains a node controller
with a node (management) router.

The node controller will connect to the upstream Crossbar.io Fabric Center.

The uplink Crossbar.io Fabric Center URL is configurable in the
node configuration. Eg in the image for Conti, this is set to the (fixed) local IP
of the "edge server" in the Hackathon setup, because we are running Crossbar.io Fabric Center
there.

Another service is started under a dedicated user (crossbar-docker-agent)
that is in the Docker group, and connects to and registers procedures
for Docker management with the node router in above container.

The Crossbar.io Fabric Docker Agent is written
in Python 3 (asyncio) / Autobahn.



start worker under
specific OS user

different workers can run
under different OS users

start worker isolated
in OS container

start worker with resource
limits in place

all of above require root

=> node controller runs under root





system agent runs as root
crossbar runs as non-root


ab client runs as root and
connects to node router



stage1: cannot get environment: rkt needs systemd-nspawn >= 220.
/usr/bin/systemd-nspawn version not supported: systemd 215



- A CF Docker agent is starting from systemd (undockerized)
- The agent will start a Crossbar.io node (Dockerized)
- The node controller router listens on an UDS
- The CF Docker agent connects to the node controller router via UDS


- Crossbar.io is started as a Docker container from systemd

