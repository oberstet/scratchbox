# Setting up SSH jump host tunneling

## Remoted host configuration

Put the following into `$HOME/.ssh/config`:

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

## Remote client configuration

