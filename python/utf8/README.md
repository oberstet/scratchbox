# UTF8 Validation

UTF8 validation here is the _incremental_ and _correct_ checking if a incoming octet stream actually is a valid UTF8 one.

Why is this important?

WebSocket has 2 payload types: text (= UTF8) and binary.

A conforming WS implementation MUST check incoming text payload for UTF8 conformance (for security and other reasons).

However, no language implementation I looked at of UTF8 is fully correct.

So I ported a state-machine based incremental validator to Python and other langs.

In WebSocket, the UTF8 validation can often become _the_ bottleneck of overall performance (besides XOR masking).

Hence: this stuff _is_ important for WS performance.


## Testing

We compare the performance of Utf8Validator, either Python pure code running on CPython or PyPy (which is the attached `utf8validator.py`) or a [Cython port of that code](https://github.com/methane/wsaccel/blob/master/wsaccel/utf8validator.pyx) (the code is really a straight forward rewrite .. no algo change or such):
 
You can install `wsaccel` from PyPI into your CPy and PyPy.


## Results

	   CPython / pure          145.115 s
	   CPython / wsaccel         0.728 s
	   PyPy 2.1 / pure           2.383 s
	   PyPy 2.1 / wsaccel        1.066 s
	   PyPy current / pure       2.567 s
	   PyPy current / wsaccel    0.808 s


This shows that currently for this workload CPython/wsaccel is fastest. And this results matches the one from full-scale WebSocket testing - look at test 9.1.6 the first 3 columns [here](http://autobahn.ws/testsuite/reports/servers/index.html).


### CPython 2.7.5

	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/local/bin/python -V
	   Python 2.7.5
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/local/bin/python test.py 
	   ................................................................................
	
	   using UTF8 validator utf8validator.Utf8Validator
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 145.115168095
	
	   ................................................................................
	
	   using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 0.728343009949
	
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ 


### PyPy 2.1 release

	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-2.1/bin/pypy -V
	   Python 2.7.3 (480845e6b1dd, Jul 31 2013, 09:57:07)
	   [PyPy 2.1.0 with GCC 4.6.3]
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-2.1/bin/pypy test.py 
	   ................................................................................
	
	   using UTF8 validator utf8validator.Utf8Validator
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 2.38252902031
	
	   ................................................................................
	
	   using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 1.06610894203
	
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ 


### PyPy 31.10.2013

	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-20131102/bin/pypy -V
	   Python 2.7.3 (b96a176fed01+, Nov 02 2013, 14:21:28)
	   [PyPy 2.2.0-alpha0 with GCC 4.6.3]
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-20131102/bin/pypy test.py 
	   ................................................................................
	
	   using UTF8 validator utf8validator.Utf8Validator
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 2.5673251152
	
	   ................................................................................
	
	   using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>
	
	   warming up ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   cooling down ..
	
	   testing ..
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	   validating payload of length 16777210 in one go
	
	   runtime 0.80845284462
	
	   oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ 
