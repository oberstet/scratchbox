CPY=${HOME}/local/bin/python
PYPY_1=${HOME}/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy
PYPY_2=${HOME}/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy

all: test_array

test_array: test_array_B test_array_L

test_array_B:
	perf stat $(CPY)    -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
	perf stat $(PYPY_1) -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
	perf stat $(PYPY_2) -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"

test_array_I:
	perf stat $(CPY)    -m timeit -c "from array import array; array('I', '*'*4*25000000).tostring()"
	perf stat $(PYPY_1) -m timeit -c "from array import array; array('I', '*'*4*25000000).tostring()"
	perf stat $(PYPY_2) -m timeit -c "from array import array; array('I', '*'*4*25000000).tostring()"

test_array_L:
	perf stat $(CPY)    -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
	perf stat $(PYPY_1) -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
	perf stat $(PYPY_2) -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"

test_bytearray:
	perf stat $(CPY)    -m timeit -c "str(bytearray('*'*100000000))"
	perf stat $(PYPY_1) -m timeit -c "str(bytearray('*'*100000000))"
	perf stat $(PYPY_2) -m timeit -c "str(bytearray('*'*100000000))"

test_sb1:
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(100000000, 1)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(10000000, 10)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(1000000, 100)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(100000, 1000)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(10000, 10000)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(1000, 100000)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(100, 1000000)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(10, 10000000)"
	perf stat $(PYPY_2) -m timeit "from test_stringbuilder1 import test" "test(1, 100000000)"

test_sj1_pypy:
	#perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(100000000, 1)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(10000000, 10)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(1000000, 100)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(100000, 1000)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(10000, 10000)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(1000, 100000)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(100, 1000000)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(10, 10000000)"
	perf stat $(PYPY_2) -m timeit "from test_stringjoin1 import test" "test(1, 100000000)"

test_aa1_pypy:
	#perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(100000000, 1)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(10000000, 10)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(1000000, 100)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(100000, 1000)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(10000, 10000)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(1000, 100000)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(100, 1000000)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(10, 10000000)"
	perf stat $(PYPY_2) -m timeit "from test_arrayappend1 import test" "test(1, 100000000)"
