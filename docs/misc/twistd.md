# Running a Server

Twistd will daemonize a server, but it will not start it on system startup, watch it and automatically restart it.

[Daemontools](http://cr.yp.to/daemontools.html) was built for exact that purpose.

It is possible tun tun a Twistd plugin under Daemontools, but only if the daemonization done by Twistd is turned off.

# Command Line Parsing

Twistd uses `twisted.python.usage`, which compared to the modern Python module `argparse` is a little arcane and less featureful.

# Reactor Installation

Twistd will automatically choose or let the user choose a reactor. This can be replicated with only a few lines of code.

# Log File Handling

[Daemontools](http://cr.yp.to/daemontools.html) provides [Multilog](http://cr.yp.to/daemontools/multilog.html).

