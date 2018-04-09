# Image Building

Build instructions for building the Docker images in this repo.

**This is only useful to Crossbar.io developers - or if you want to tweak the Dockerfiles to your needs. Otherwise, just use our images published to Dockerhub**.


## Requirements

This assumes you have Docker already installed.

Further, the commands shown assume that you are able to run Docker without `sudo`. The latter can be done by

```console
sudo usermod -aG docker oberstet
```

and rebooting.


## Building the Images

For building a new set of images, edit [versions.sh](versions.sh), and then

```console
source versions.sh
make build
```


## Cross-building images

Here are some notes on using Qemu for building Docker images for CPU architectures different from the host, like for armhf or aarch64 on a x86-64 host.

