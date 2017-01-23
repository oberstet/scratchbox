#!/bin/sh

sudo /opt/fio/bin/fio --ioengine=sync --numjobs=512  --output=sync-512.log test.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=1024 --output=sync-1024.log test.fio
sudo /opt/fio/bin/fio --ioengine=sync --numjobs=2048 --output=sync-2048.log test.fio

sudo /opt/fio/bin/fio --ioengine=psync --numjobs=512  --output=psync-512.log test.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=1024 --output=psync-1024.log test.fio
sudo /opt/fio/bin/fio --ioengine=psync --numjobs=2048 --output=psync-2048.log test.fio

sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=512  --output=pvsync-512.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=1024 --output=pvsync-1024.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync --numjobs=2048 --output=pvsync-2048.log test.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=512  --output=pvsync2-512.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=1024 --output=pvsync2-1024.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --numjobs=2048 --output=pvsync2-2048.log test.fio

sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=512  --output=pvsync2-hipri-512.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=1024 --output=pvsync2-hipri-1024.log test.fio
sudo /opt/fio/bin/fio --ioengine=pvsync2 --hipri=1 --numjobs=2048 --output=pvsync2-hipri-2048.log test.fio

