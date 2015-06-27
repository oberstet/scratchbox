# Running the test

The test was run on a Xeon E3 v3 running FreeBSD 10.1 using PyPy 2.6.

Start `server.py`.

To measure the syscall rate during the test, note the PID of the running server and start the following DTrace command (inserting the PID you noted):

```
dtrace -n syscall:::entry'/pid == 26112/{ @syscalls[probefunc] = count(); } tick-1sec {printa(@syscalls); trunc(@syscalls);}'
```

Then start `client.py` modifying the flags `QUEUED_WRITES` and `FORCE_REACTOR_ENTER` in `client.py` for each subtest.


## Test 1

Directly calling into `transport.write`, and no entering of the reactor while in the writing loop:

```
QUEUED_WRITES = False
FORCE_REACTOR_ENTER = False
```

The request rate during this test was:

```
1620521.45316 calls/s (95784789 succeeded)
```

The syscall statistics in a typical 1s period during the test:

```
  write                                                             1
  _umtx_op                                                          2
  sendto                                                           80
  recvfrom                                                         81
  madvise                                                         202
  kevent                                                          321
```

## Test 2

Directly calling into `transport.write`, entering the reactor while in the writing loop:

```
QUEUED_WRITES = False
FORCE_REACTOR_ENTER = True
```

The request rate during this test was:

```
62782.1704721 calls/s (3766965 succeeded)
```

The syscall statistics in a typical 1s period during the test:

```
  madvise                                                           1
  write                                                             1
  _umtx_op                                                          2
  recvfrom                                                      44300
  sendto                                                        44300
  kevent                                                       177200
```

## Test 3

Buffering writes, entering the reactor while in the writing loop:

```
QUEUED_WRITES = True
FORCE_REACTOR_ENTER = True
```

The request rate during this test was:

```
449640.974788 calls/s (26978673 succeeded)
```

The syscall statistics in a typical 1s period during the test:

```
  write                                                             1
  _umtx_op                                                          2
  madvise                                                          38
  recvfrom                                                         98
  sendto                                                           98
  kevent                                                          393
```
