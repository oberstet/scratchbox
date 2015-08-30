Demonstrates an issue with msgpack-python. Run `make isntall` and then `make test`:

```console
(python279_1)oberstet@thinkpad-t430s:~/scm/scratchbox/python/msgpack$ make test
python test.py
python test2.py
Traceback (most recent call last):
  File "test2.py", line 7, in <module>
    deserialized = msgpack.unpackb(bytes)
  File "/home/oberstet/python279_1/lib/python2.7/site-packages/msgpack/fallback.py", line 100, in unpackb
    raise ExtraData(ret, unpacker._fb_get_extradata())
msgpack.exceptions.ExtraData: unpack(b) received extra data.
make: *** [test] Fehler 1
```
