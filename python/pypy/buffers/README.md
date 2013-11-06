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
