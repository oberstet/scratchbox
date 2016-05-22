# Setting up SSH jump host tunneling

## Usage

### Setup

Install [autossh](http://www.harding.motd.ca/autossh/).

On Ubuntu/Debian:

```console
sudo apt-get install autossh
```

On MacOSX (untested):

```console
cd ~
wget http://www.harding.motd.ca/autossh/autossh-1.4e.tgz
tar xvzf autossh-1.4e.tgz
cd autossh-1.4e
./configure
make
sudo make install
```

On Windows: please install a sane OS.

Then, in your `$HOME/.ssh/config`, add the following:

```console
# the following configures the forward SSH tunnels
# to the jump host for remote maintenance access
Host jumper
    # login to jumphost to create the tunnels
    User ec2-user
    Hostname jumper.tavendo.de
    ForwardAgent yes

    # SSH level keep alive
    ServerAliveInterval 5
    ServerAliveCountMax 3

    # SSH shell access to bvr-sql18
    LocalForward 2222 localhost:2222

    # Git access (via svr-git01)
    LocalForward 2223 localhost:2223

    # SSH shell access to bvr-file1
    LocalForward 2224 localhost:2224

    # ADR (PostgreSQL 9.5 main cluster)
    LocalForward 5532 localhost:5432

    # ADRANA (PostgreSQL 9.5 test cluster)
    LocalForward 5522 localhost:5422

    # Livemon (bvr-sql18)
    LocalForward 8090 localhost:8090

    # Glances (bvr-sql18)
    LocalForward 8091 localhost:8091

    # Netdata (bvr-sql18)
    LocalForward 8092 localhost:8092

    # Glances (bvr-file1)
    LocalForward 8093 localhost:8093
```

In your `$HOME/.bashrc`, add the following:

```shell
# login to jump host (this is only needed for testing / administration of the jump host)
alias jumper='ssh ec2-user@jumper.tavendo.de'

# this will setup all forwarding tunnels
alias parcit_tunnel='autossh -M 0 -f -T -N jumper'

# remote SSH login to bvr-sql18
alias parcit_sql18='ssh -p 2222 oberstet@localhost'

# remote SSH login to bvr-file1
alias parcit_file1='ssh -p 2224 oberstet@localhost'
```

To keep alive the tunnels, save the following into `$HOME/parcit_keepalive.sh` (and `chmod +x $HOME/parcit_keepalive.sh`):

```shell
#!/bin/sh

while [ 1 ]
do
    echo "TUNNEL KEEP ALIVE **********************************"
    date
    echo

    # check connection to jump host and list the reverse tunnels
    # listening on the jump host
    ssh -t ec2-user@jumper.tavendo.de "netstat -lnt | grep 127"

    # check ADR database connection
    psql -p 5532 -h localhost -d postgres -U postgres -c "select now()"

    # check ADR test cluster database connection
    psql -p 5522 -h localhost -d postgres -U postgres -c "select now()"

    # check Git
    ssh -T -p 2223 gituser@localhost

    # check Web services
    curl localhost:8090 > /dev/null
    curl localhost:8091 > /dev/null
    curl localhost:8092 > /dev/null
    curl localhost:8093 > /dev/null

    echo "**********************************"
    echo

    sleep 30 
done
```

### Using

Start the forward tunnels (this should only be needed to be done once per system boot):

```console
parcit_tunnel
```

Then, in a terminal window, run

```console
~/parcit_keepalive.sh
```

To clone a Git repo:

```console
git clone ssh://gituser@localhost:2223/RA
``` 

To log into `bvr-sql18`:

```console
parcit_sql18
```

To log into `bvr-file1`:

```console
parcit_file1
```

To log into the ADR DB:

```console
psql -p 5532 -h localhost -d adr -U oberstet
```

## Administration

See also [here](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/).

On the remoting host (`bvr-sql18`), put the following into `$HOME/.ssh/config` **under tunnel adminstrator user**:

```
# the following configures the reverse SSH tunnels
# to the jump host for remote maintenance access
Host jumper
    # login to jumphost to create the tunnels
    User ec2-user
    Hostname jumper.tavendo.de
    ForwardAgent yes

    # SSH level keep alive
    ServerAliveInterval 5
    ServerAliveCountMax 3

    # SSH shell access to bvr-sql18
    RemoteForward 2222 localhost:22

    # Git access (via svr-git01)
    RemoteForward 2223 svr-git01:22

    # SSH shell access to bvr-file1
    RemoteForward 2224 bvr-file1:22

    # ADR (PostgreSQL 9.5 main cluster)
    RemoteForward 5432 localhost:5432

    # ADRANA (PostgreSQL 9.5 test cluster)
    RemoteForward 5422 localhost:5422

    # Livemon (bvr-sql18)
    RemoteForward 8090 localhost:80

    # Glances (bvr-sql18)
    RemoteForward 8091 localhost:61208

    # Netdata (bvr-sql18)
    RemoteForward 8092 localhost:19999

    # Glances (bvr-file1)
    RemoteForward 8093 bvr-file1:61208
```

Put the following into `$HOME/.bashrc`:

```shell
# setup tunnels via autossh. for configuration, see $HOME/.ssh/config
# see: https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/
alias create_tunnels='autossh -M 0 -f -T -N jumper'
```
