CPY=${HOME}/local/bin/python
PYPY_1=${HOME}/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy
PYPY_2=${HOME}/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy

all: test_array

test_array: test_array_b test_array_l

test_array_b:
	perf stat $(CPY)    -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
	perf stat $(PYPY_1) -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
	perf stat $(PYPY_2) -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"

test_array_l:
	perf stat $(CPY)    -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
	perf stat $(PYPY_1) -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
	perf stat $(PYPY_2) -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"

test_bytearray:
	perf stat $(CPY)    -m timeit -c "str(bytearray('*'*100000000))"
	perf stat $(PYPY_1) -m timeit -c "str(bytearray('*'*100000000))"
	perf stat $(PYPY_2) -m timeit -c "str(bytearray('*'*100000000))"
