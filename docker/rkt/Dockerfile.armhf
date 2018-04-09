FROM armhf/debian:jessie

COPY .qemu/qemu-arm-static /usr/bin/qemu-arm-static

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ARG RKT_VERSION
ENV DEBIAN_FRONTEND noninteractive
ENV PATH /opt/go/bin:${PATH}
ENV GOROOT /opt/go

RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
               git \
               curl \
               wget \
               file \
               bc \
               patch \
               gnupg \
               ca-certificates \
               build-essential \
               autoconf \
               automake \
               squashfs-tools \
               libssl-dev \
               libacl1-dev \
               libsystemd-dev

RUN mkdir -p /opt && \
    cd /opt && \
    wget https://storage.googleapis.com/golang/go1.8.1.linux-armv6l.tar.gz && \
    tar xvf go1.8.1.linux-armv6l.tar.gz && \
    rm *.tar.gz && \
    /opt/go/bin/go version

RUN cd /tmp && \
    wget https://github.com/rkt/rkt/archive/v${RKT_VERSION}.tar.gz && \
    tar xvf v${RKT_VERSION}.tar.gz && \
    rm v${RKT_VERSION}.tar.gz && \
    cd rkt-${RKT_VERSION} && \
    ./autogen.sh && \
    ./configure --with-stage1-flavors=host --disable-tpm && \
    make -j4 && \
    mkdir -p /opt && \
    rm -rf /opt/rkt && \
    mv build-rkt-1.25.0/target/ /opt/rkt && \
    /opt/rkt/bin/rkt version

RUN /opt/go/bin/go version && \
    /opt/rkt/bin/rkt version
