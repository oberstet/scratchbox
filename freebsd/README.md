# Building a Kernel

```
cd /usr/src/sys/amd64/conf
cp GENERIC BRUMMER_KERNEL_10_1
cd /usr/src
make buildkernel KERNCONF=BRUMMER_KERNEL_10_1
make installkernel KERNCONF=BRUMMER_KERNEL_10_1
```

# Open FDs

Get the system-wide maximum number of open file descriptors:

	$ sysctl kern.maxfiles
	kern.maxfiles: 200000

Get the per-process maximum number of open file descriptors:

	$ sysctl kern.maxfilesperproc
	kern.maxfilesperproc: 200000

Get the system-wide current number of open file descriptors:

	$ sysctl kern.openfiles
	kern.openfiles: 453

Get the system-wide maximum number of open sockets:

	$ sysctl kern.ipc.maxsockets
	kern.ipc.maxsockets: 200000

Get the system-wide current number of open sockets

	$ sysctl kern.ipc.numopensockets
	kern.ipc.numopensockets: 36

Get the TCP accept queue depth maximum:

	$ sysctl kern.ipc.somaxconn
	kern.ipc.somaxconn: 32768

Show connected sockets:

	$ sockstat -c -4 -p 443
	USER     COMMAND    PID   FD PROTO  LOCAL ADDRESS         FOREIGN ADDRESS
	ec2-user pypy-2.4   813   14 tcp4   172.31.1.97:443       37.209.25.107:50458
	ec2-user pypy-2.4   813   15 tcp4   172.31.1.97:443       176.221.120.81:55458
	ec2-user pypy-2.4   813   17 tcp4   172.31.1.97:443       188.96.38.230:59864
	ec2-user pypy-2.4   813   18 tcp4   172.31.1.97:443       37.209.25.107:50360
	ec2-user pypy-2.4   813   19 tcp4   172.31.1.97:443       88.217.57.105:58223
	ec2-user pypy-2.4   813   23 tcp4   172.31.1.97:443       88.217.57.105:58224
	ec2-user pypy-2.4   813   194 tcp4  172.31.1.97:443       88.217.57.105:49835
	ec2-user pypy-2.4   813   376 tcp4  172.31.1.97:443       88.217.57.105:58230
	ec2-user pypy-2.4   813   797 tcp4  172.31.1.97:443       37.209.25.107:50397

# User Management

Delete a user including home directory:

	pw userdel foobar -r

