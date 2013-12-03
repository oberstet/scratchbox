# Twisted `transport.write`

We follow the codepath within Twisted for a TCP server doing a `transport.write`.

We look at the [kqueue reactor](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L38) that derives of the [posixbase reactor](https://github.com/twisted/twisted/blob/trunk/twisted/internet/posixbase.py#L268).

1. Sending data (for TCP on Unix) with `transport.write()` begins in class `t.i.abstract.FileDescriptor` which implements `ITransport` [here](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L339). Data written is append to the list `_tempDataBuffer`.

1. `FileDescriptor` will [startWriting](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L436) on the FD. This [calls](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L436) into the abstract reactor, which in turn [calls](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L137) the underlying concrete reactor.

1. When the FD (socket) with data to be written is not in the list of writers, it is [added](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L144). If so, this will [result](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L87) in a **1st syscall to `kqueue()`**.

1. The user application code now continues, until the next reactor [main loop](https://github.com/twisted/twisted/blob/trunk/twisted/internet/base.py#L1190) run the [next iteration](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L229) which will [block in](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L237) in the **2nd syscall to `kqueue()`** until there is activity on any of the registered readers/writers FDs.

1. When there is FD activity, the syscall returns from the kernel, and reader/writer [processing is done](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L257).

1. In the case of the FD we wanted to write to becomes writable, `doWrite()` is [called](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L280) which is forwarded to the abstract `doWrite()` method [here](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L234).

1. The actual writing of previously buffered data is then done [here](https://github.com/twisted/twisted/blob/trunk/twisted/internet/tcp.py#L247), which is the **3rd syscall to `send()`**.

1. When there is no more buffered data to be written, the writer is [removed](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L270), which is [forwarded](https://github.com/twisted/twisted/blob/trunk/twisted/internet/abstract.py#L429) to the concrete reactor, which then actually [removes](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L179) the writer [doing](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L201) by [doing](https://github.com/twisted/twisted/blob/trunk/twisted/internet/kqreactor.py#L87) a **4th syscall to `kqueue()`**.
