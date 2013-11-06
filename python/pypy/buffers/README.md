# Findings

## Array fromstring/tostring

  1. The [patch](https://bitbucket.org/pypy/pypy/commits/d592e1e60494eef43c4ebce9b69095e6bbc2eb7b) by Alex Gaynor has *drastically* improved PyPy `array.fromstring` and `array.tostring` performance
  2. The performance is now nearly at CPython's speed
  3. The Linux "perf stat" clearly shows the improvements (branches, stalled cycles)
  4. The improvement applies to both `array('B')` and `array('L')`

## bytearray

  1. The performance of `bytearray` roundtripping from string and to string is roughly 6x lower with PyPy compared to CPython. This is huge.
  2. Linux "perf stat" shows that there is *massive* branching going on (and also multiple times more stalling and in general executed instructions)
  3. The patch by Alex did not change that (and that wasn't expected I guess from looking at the patch)


# Pointers

  * code is in  `pypy/pypy/module/array/interp_array.py`


# Measurements

## Array fromstring/tostring

### array 'B'

#### CPython 2.7.5

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$ make
      perf stat /home/oberstet/local/bin/python    -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
      10 loops, best of 3: 127 msec per loop

       Performance counter stats for '/home/oberstet/local/bin/python -m timeit -c from array import array; array('B', '*'*100000000).tostring()':

             5181,527343 task-clock                #    0,994 CPUs utilized
                      79 context-switches          #    0,015 K/sec
                       7 cpu-migrations            #    0,001 K/sec
               2.955.675 page-faults               #    0,570 M/sec
          17.185.594.397 cycles                    #    3,317 GHz                     [83,38%]
          12.003.414.403 stalled-cycles-frontend   #   69,85% frontend cycles idle    [83,33%]
           8.231.700.731 stalled-cycles-backend    #   47,90% backend  cycles idle    [66,68%]
          10.588.568.544 instructions              #    0,62  insns per cycle
                                                   #    1,13  stalled cycles per insn [83,37%]
           1.508.568.569 branches                  #  291,144 M/sec                   [83,36%]
              16.210.531 branch-misses             #    1,07% of all branches         [83,29%]

             5,211804316 seconds time elapsed


#### PyPy (before patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
      10 loops, best of 3: 340 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c from array import array; array('B', '*'*100000000).tostring()':

            13701,244472 task-clock                #    0,998 CPUs utilized
                      21 context-switches          #    0,002 K/sec
                       1 cpu-migrations            #    0,000 K/sec
               2.959.727 page-faults               #    0,216 M/sec
          45.463.397.380 cycles                    #    3,318 GHz                     [83,31%]
          11.869.735.751 stalled-cycles-frontend   #   26,11% frontend cycles idle    [83,34%]
           7.673.197.740 stalled-cycles-backend    #   16,88% backend  cycles idle    [66,68%]
          75.344.159.854 instructions              #    1,66  insns per cycle
                                                   #    0,16  stalled cycles per insn [83,34%]
           9.854.434.125 branches                  #  719,236 M/sec                   [83,34%]
              22.807.040 branch-misses             #    0,23% of all branches         [83,34%]

            13,733203383 seconds time elapsed


#### PyPy (after patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c "from array import array; array('B', '*'*100000000).tostring()"
      10 loops, best of 3: 145 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c from array import array; array('B', '*'*100000000).tostring()':

             5889,840955 task-clock                #    0,998 CPUs utilized
                      13 context-switches          #    0,002 K/sec
                       1 cpu-migrations            #    0,000 K/sec
               2.959.429 page-faults               #    0,502 M/sec
          19.538.998.819 cycles                    #    3,317 GHz                     [83,33%]
          13.456.378.207 stalled-cycles-frontend   #   68,87% frontend cycles idle    [83,33%]
           9.524.633.886 stalled-cycles-backend    #   48,75% backend  cycles idle    [66,66%]
          12.752.735.297 instructions              #    0,65  insns per cycle
                                                   #    1,06  stalled cycles per insn [83,33%]
           1.913.280.026 branches                  #  324,844 M/sec                   [83,33%]
              22.007.282 branch-misses             #    1,15% of all branches         [83,36%]

             5,903791519 seconds time elapsed

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$


### array 'L'

#### CPython 2.7.5

      perf stat /home/oberstet/local/bin/python    -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
      10 loops, best of 3: 133 msec per loop

       Performance counter stats for '/home/oberstet/local/bin/python -m timeit -c from array import array; array('L', '*'*8*12500000).tostring()':

             5406,647189 task-clock                #    0,998 CPUs utilized
                      12 context-switches          #    0,002 K/sec
                       1 cpu-migrations            #    0,000 K/sec
               2.955.675 page-faults               #    0,547 M/sec
          17.920.523.944 cycles                    #    3,315 GHz                     [83,32%]
          12.521.833.508 stalled-cycles-frontend   #   69,87% frontend cycles idle    [83,32%]
           9.771.487.583 stalled-cycles-backend    #   54,53% backend  cycles idle    [66,64%]
          10.940.572.166 instructions              #    0,61  insns per cycle
                                                   #    1,14  stalled cycles per insn [83,32%]
           1.504.389.222 branches                  #  278,248 M/sec                   [83,37%]
              17.118.757 branch-misses             #    1,14% of all branches         [83,38%]

             5,419481083 seconds time elapsed


#### PyPy (before patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
      10 loops, best of 3: 343 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c from array import array; array('L', '*'*8*12500000).tostring()':

            13834,263048 task-clock                #    0,998 CPUs utilized
                      18 context-switches          #    0,001 K/sec
                      21 cpu-migrations            #    0,002 K/sec
               2.959.728 page-faults               #    0,214 M/sec
          45.900.241.527 cycles                    #    3,318 GHz                     [83,33%]
          12.472.331.025 stalled-cycles-frontend   #   27,17% frontend cycles idle    [83,33%]
           7.494.587.107 stalled-cycles-backend    #   16,33% backend  cycles idle    [66,65%]
          74.840.369.801 instructions              #    1,63  insns per cycle
                                                   #    0,17  stalled cycles per insn [83,33%]
           9.619.837.488 branches                  #  695,363 M/sec                   [83,35%]
              22.670.764 branch-misses             #    0,24% of all branches         [83,35%]

            13,866491736 seconds time elapsed


#### PyPy (after patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c "from array import array; array('L', '*'*8*12500000).tostring()"
      10 loops, best of 3: 148 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c from array import array; array('L', '*'*8*12500000).tostring()':

             6013,161571 task-clock                #    0,998 CPUs utilized
                      10 context-switches          #    0,002 K/sec
                       0 cpu-migrations            #    0,000 K/sec
               2.959.431 page-faults               #    0,492 M/sec
          19.943.822.654 cycles                    #    3,317 GHz                     [83,34%]
          14.064.190.183 stalled-cycles-frontend   #   70,52% frontend cycles idle    [83,34%]
          10.230.363.530 stalled-cycles-backend    #   51,30% backend  cycles idle    [66,68%]
          12.182.947.084 instructions              #    0,61  insns per cycle
                                                   #    1,15  stalled cycles per insn [83,34%]
           1.685.939.165 branches                  #  280,375 M/sec                   [83,34%]
              22.398.701 branch-misses             #    1,33% of all branches         [83,32%]

             6,027330571 seconds time elapsed

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$


## bytearray string roundtripping

### CPython

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$ make test_bytearray
      perf stat /home/oberstet/local/bin/python    -m timeit -c "str(bytearray('*'*100000000))"
      10 loops, best of 3: 127 msec per loop

       Performance counter stats for '/home/oberstet/local/bin/python -m timeit -c str(bytearray('*'*100000000))':

             5144,167012 task-clock                #    0,998 CPUs utilized
                      10 context-switches          #    0,002 K/sec
                       3 cpu-migrations            #    0,001 K/sec
               2.955.666 page-faults               #    0,575 M/sec
          17.065.466.531 cycles                    #    3,317 GHz                     [83,32%]
          11.895.427.942 stalled-cycles-frontend   #   69,70% frontend cycles idle    [83,32%]
           8.539.873.832 stalled-cycles-backend    #   50,04% backend  cycles idle    [66,64%]
          10.598.787.344 instructions              #    0,62  insns per cycle
                                                   #    1,12  stalled cycles per insn [83,32%]
           1.508.296.092 branches                  #  293,205 M/sec                   [83,36%]
              16.559.372 branch-misses             #    1,10% of all branches         [83,39%]

             5,156358959 seconds time elapsed

#### PyPy (before patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c "str(bytearray('*'*100000000))"
      10 loops, best of 3: 730 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67840-934879cb2719-linux64/bin/pypy -m timeit -c str(bytearray('*'*100000000))':

            29424,858774 task-clock                #    0,998 CPUs utilized
                      40 context-switches          #    0,001 K/sec
                       5 cpu-migrations            #    0,000 K/sec
               9.181.888 page-faults               #    0,312 M/sec
          97.635.610.018 cycles                    #    3,318 GHz                     [83,33%]
          59.541.536.987 stalled-cycles-frontend   #   60,98% frontend cycles idle    [83,33%]
          37.396.420.623 stalled-cycles-backend    #   38,30% backend  cycles idle    [66,66%]
          90.774.049.672 instructions              #    0,93  insns per cycle
                                                   #    0,66  stalled cycles per insn [83,33%]
          14.082.731.539 branches                  #  478,600 M/sec                   [83,34%]
              80.866.332 branch-misses             #    0,57% of all branches         [83,33%]

            29,493195748 seconds time elapsed

#### PyPy (after patch by Alex Gaynor)

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c "str(bytearray('*'*100000000))"
      10 loops, best of 3: 723 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit -c str(bytearray('*'*100000000))':

            29086,466902 task-clock                #    0,998 CPUs utilized
                      53 context-switches          #    0,002 K/sec
                       2 cpu-migrations            #    0,000 K/sec
               9.183.035 page-faults               #    0,316 M/sec
          96.514.023.051 cycles                    #    3,318 GHz                     [83,33%]
          58.438.305.852 stalled-cycles-frontend   #   60,55% frontend cycles idle    [83,33%]
          34.414.785.167 stalled-cycles-backend    #   35,66% backend  cycles idle    [66,66%]
          90.912.947.097 instructions              #    0,94  insns per cycle
                                                   #    0,64  stalled cycles per insn [83,33%]
          14.042.364.355 branches                  #  482,780 M/sec                   [83,34%]
              79.749.439 branch-misses             #    0,57% of all branches         [83,34%]

            29,154173576 seconds time elapsed

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$


