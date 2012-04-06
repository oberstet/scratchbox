#!/bin/bash -ex

yum -y update
cd /home/ec2-user
wget http://autobahn.ws/static/appliance/eggs/python272.tar.bz2
tar xvjf python272.tar.bz2
chown -R ec2-user:ec2-user /home/ec2-user/python272*
setcap 'cap_net_bind_service=+ep' /home/ec2-user/python272/bin/python
echo "su -l ec2-user -c '/home/ec2-user/python272/bin/twistd -r epoll autobahnws'" >> /etc/rc.d/rc.local
