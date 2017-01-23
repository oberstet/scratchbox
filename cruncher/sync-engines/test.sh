#!/bin/sh

sudo /opt/fio/bin/fio --ioengine=sync --numjobs=512  --output=individual-nvmes-sync-512.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=1024 --output=individual-nvmes-sync-1024.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=2048 --output=individual-nvmes-sync-2048.log individual-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=psync --numjobs=512  --output=individual-nvmes-psync-512.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=1024 --output=individual-nvmes-psync-1024.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=2048 --output=individual-nvmes-psync-2048.log individual-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=512  --output=individual-nvmes-pvsync-512.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=1024 --output=individual-nvmes-pvsync-1024.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=2048 --output=individual-nvmes-pvsync-2048.log individual-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=512  --output=individual-nvmes-pvsync2-512.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=1024 --output=individual-nvmes-pvsync2-1024.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=2048 --output=individual-nvmes-pvsync2-2048.log individual-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=512  --output=individual-nvmes-pvsync2-hipri-512.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=1024 --output=individual-nvmes-pvsync2-hipri-1024.log individual-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=2048 --output=individual-nvmes-pvsync2-hipri-2048.log individual-nvmes.fio


sudo /opt/fio/bin/fio --ioengine=sync --numjobs=512  --output=md-nvmes-sync-512.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=1024 --output=md-nvmes-sync-1024.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=2048 --output=md-nvmes-sync-2048.log md-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=psync --numjobs=512  --output=md-nvmes-psync-512.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=1024 --output=md-nvmes-psync-1024.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=2048 --output=md-nvmes-psync-2048.log md-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=512  --output=md-nvmes-pvsync-512.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=1024 --output=md-nvmes-pvsync-1024.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=2048 --output=md-nvmes-pvsync-2048.log md-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=512  --output=md-nvmes-pvsync2-512.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=1024 --output=md-nvmes-pvsync2-1024.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=2048 --output=md-nvmes-pvsync2-2048.log md-nvmes.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=512  --output=md-nvmes-pvsync2-hipri-512.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=1024 --output=md-nvmes-pvsync2-hipri-1024.log md-nvmes.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=2048 --output=md-nvmes-pvsync2-hipri-2048.log md-nvmes.fio

