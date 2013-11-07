# UTF8 Validation

UTF8 validation here is the _incremental_ and _correct_ checking if a incoming octet stream actually is a valid UTF8 one.

Why is this important?

WebSocket has 2 payload types: text (= UTF8) and binary.

A conforming WS implementation MUST check incoming text payload for UTF8 conformance (for security and other reasons).

However, no language implementation I looked at of UTF8 is fully correct.

So I ported a state-machine based incremental validator to Python and other langs.

In WebSocket, the UTF8 validation can often become _the_ bottleneck of overall performance (besides XOR masking).

Hence: this stuff _is_ important for WS performance.


## Results (new)

                                                slower than ref

      Python/wsaccel_cffi           444.4 MB/s   ref
      Python/wsaccel                439.6 MB/s   1.1 %

      PyPy2.1/pure                  369.2 MB/s  16.8 %
      PyPy2.1/wsaccel_cffi          396.9 MB/s  10.7 %
      PyPy2.1/wsaccel               304.9 MB/s  31.4 %

      PyPy-current/pure             373.5 MB/s  16.0 %
      PyPy-current/wsaccel_cffi     399.0 MB/s  10.2 %
      PyPy-current/wsaccel          408.1 MB/s   8.2 %



Logs

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ scons
      scons: Reading SConscript files ...
      scons: done reading SConscript files.
      scons: Building targets ...
      gcc -o utf8validator.os -c -std=c99 -Wall -O3 -march=native -fPIC utf8validator.c
      gcc -o libutf8validator.so -shared utf8validator.os
      scons: done building targets.
      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/local/bin/python test.py

      !!! Skipping pure Python validators when running CPython [way too slow]

      ................................................................................

      using UTF8 validator test_cffi_validator.Utf8ValidatorCFFI

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 7.2013 s [444.4 MB/s]

      ................................................................................

      using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 7.2794 s [439.6 MB/s]

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-2.1/bin/pypy test.py
      ................................................................................

      using UTF8 validator utf8validator_str_dfa_local_state.Utf8Validator

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 8.6671 s [369.2 MB/s]

      ................................................................................

      using UTF8 validator test_cffi_validator.Utf8ValidatorCFFI

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 8.0634 s [396.9 MB/s]

      ................................................................................

      using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 10.4952 s [304.9 MB/s]

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-c-jit-67866-08b6eb67086a-linux64/bin/pypy test.py
      ................................................................................

      using UTF8 validator utf8validator_str_dfa_local_state.Utf8Validator

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 8.5675 s [373.5 MB/s]

      ................................................................................

      using UTF8 validator test_cffi_validator.Utf8ValidatorCFFI

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 8.0197 s [399.0 MB/s]

      ................................................................................

      using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>

      OK, validator works.
      warming up ..

      cooling down ..

      testing ..

      runtime 7.8403 s [408.1 MB/s]

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$




## Testing (old)

We compare the performance of Utf8Validator, either Python pure code running on CPython or PyPy (which is the attached `utf8validator.py`) or a [Cython port of that code](https://github.com/methane/wsaccel/blob/master/wsaccel/utf8validator.pyx) (the code is really a straight forward rewrite .. no algo change or such):

You can install `wsaccel` from PyPI into your CPy and PyPy.


## Update Results

      PyPy current / pure with tuple DFA + copy to local    8.712 s
      PyPy current / pure with string DFA                  10.219 s
      PyPy current / pure with string DFA + copy to local   4.353 s
      PyPy current / wsaccel                                3.968 s

      CPy/wsaccel                                           3.649 s

Logs

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/utf8$ ~/pypy-20131102/bin/pypy test.py
      ................................................................................

      using UTF8 validator utf8validator.Utf8Validator

      warming up ..

      cooling down ..

      testing ..

      runtime 8.71992993355

      ................................................................................

      using UTF8 validator utf8validator_str_dfa.Utf8Validator

      warming up ..

      cooling down ..

      testing ..

      runtime 10.2193830013

      ................................................................................

      using UTF8 validator utf8validator_str_dfa_local_state.Utf8Validator

      warming up ..

      cooling down ..

      testing ..

      runtime 4.35324215889

      ................................................................................

      using UTF8 validator <type 'wsaccel.utf8validator.Utf8Validator'>

      warming up ..

      cooling down ..

      testing ..

      runtime 3.9676759243



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
