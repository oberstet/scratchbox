## Measurements

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/pypy/buffers$ make test_sb1
      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(100000000, 1)"
      10 loops, best of 3: 568 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(100000000, 1)':

            22999,143194 task-clock                #    0,998 CPUs utilized
                      42 context-switches          #    0,002 K/sec
                       7 cpu-migrations            #    0,000 K/sec
                 981.836 page-faults               #    0,043 M/sec
          76.349.236.183 cycles                    #    3,320 GHz                     [83,32%]
          10.406.912.115 stalled-cycles-frontend   #   13,63% frontend cycles idle    [83,33%]
          10.835.792.921 stalled-cycles-backend    #   14,19% backend  cycles idle    [66,67%]
         172.964.539.876 instructions              #    2,27  insns per cycle
                                                   #    0,06  stalled cycles per insn [83,34%]
          40.617.505.047 branches                  # 1766,044 M/sec                   [83,34%]
              40.139.981 branch-misses             #    0,10% of all branches         [83,34%]

            23,052829889 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(10000000, 10)"
      10 loops, best of 3: 100 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(10000000, 10)':

             4054,416410 task-clock                #    0,998 CPUs utilized
                      10 context-switches          #    0,002 K/sec
                       2 cpu-migrations            #    0,000 K/sec
                 981.837 page-faults               #    0,242 M/sec
          13.454.033.035 cycles                    #    3,318 GHz                     [83,27%]
           4.673.909.923 stalled-cycles-frontend   #   34,74% frontend cycles idle    [83,36%]
           3.979.510.755 stalled-cycles-backend    #   29,58% backend  cycles idle    [66,73%]
          21.056.769.254 instructions              #    1,57  insns per cycle
                                                   #    0,22  stalled cycles per insn [83,36%]
           4.568.603.085 branches                  # 1126,821 M/sec                   [83,37%]
              40.179.017 branch-misses             #    0,88% of all branches         [83,31%]

             4,064132486 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(1000000, 100)"
      10 loops, best of 3: 53.9 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(1000000, 100)':

             2187,384714 task-clock                #    0,998 CPUs utilized
                       7 context-switches          #    0,003 K/sec
                       3 cpu-migrations            #    0,001 K/sec
                 981.836 page-faults               #    0,449 M/sec
           7.258.120.628 cycles                    #    3,318 GHz                     [83,21%]
           4.674.011.310 stalled-cycles-frontend   #   64,40% frontend cycles idle    [83,37%]
           2.885.745.957 stalled-cycles-backend    #   39,76% backend  cycles idle    [66,80%]
           5.729.720.330 instructions              #    0,79  insns per cycle
                                                   #    0,82  stalled cycles per insn [83,40%]
             967.537.770 branches                  #  442,326 M/sec                   [83,40%]
              19.793.026 branch-misses             #    2,05% of all branches         [83,34%]

             2,192747954 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(100000, 1000)"
      10 loops, best of 3: 51.5 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(100000, 1000)':

             2091,117089 task-clock                #    0,998 CPUs utilized
                       7 context-switches          #    0,003 K/sec
                       1 cpu-migrations            #    0,000 K/sec
                 981.837 page-faults               #    0,470 M/sec
           6.937.524.817 cycles                    #    3,318 GHz                     [83,21%]
           4.872.916.390 stalled-cycles-frontend   #   70,24% frontend cycles idle    [83,39%]
           3.386.904.371 stalled-cycles-backend    #   48,82% backend  cycles idle    [66,79%]
           4.556.276.082 instructions              #    0,66  insns per cycle
                                                   #    1,07  stalled cycles per insn [83,40%]
             646.935.853 branches                  #  309,373 M/sec                   [83,40%]
               9.473.741 branch-misses             #    1,46% of all branches         [83,23%]

             2,096271655 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(10000, 10000)"
      10 loops, best of 3: 50.8 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(10000, 10000)':

             2065,892296 task-clock                #    0,998 CPUs utilized
                       5 context-switches          #    0,002 K/sec
                       0 cpu-migrations            #    0,000 K/sec
                 981.840 page-faults               #    0,475 M/sec
           6.855.113.284 cycles                    #    3,318 GHz                     [83,19%]
           4.915.424.358 stalled-cycles-frontend   #   71,70% frontend cycles idle    [83,38%]
           3.371.544.123 stalled-cycles-backend    #   49,18% backend  cycles idle    [66,77%]
           4.232.073.717 instructions              #    0,62  insns per cycle
                                                   #    1,16  stalled cycles per insn [83,39%]
             608.009.119 branches                  #  294,308 M/sec                   [83,39%]
               9.214.666 branch-misses             #    1,52% of all branches         [83,28%]

             2,071013192 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(1000, 100000)"
      10 loops, best of 3: 50.9 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(1000, 100000)':

             2069,153661 task-clock                #    0,997 CPUs utilized
                       6 context-switches          #    0,003 K/sec
                       0 cpu-migrations            #    0,000 K/sec
                 981.880 page-faults               #    0,475 M/sec
           6.865.759.003 cycles                    #    3,318 GHz                     [83,22%]
           4.848.262.934 stalled-cycles-frontend   #   70,62% frontend cycles idle    [83,22%]
           2.891.221.676 stalled-cycles-backend    #   42,11% backend  cycles idle    [66,83%]
           4.325.962.747 instructions              #    0,63  insns per cycle
                                                   #    1,12  stalled cycles per insn [83,41%]
             600.758.284 branches                  #  290,340 M/sec                   [83,41%]
               8.836.929 branch-misses             #    1,47% of all branches         [83,32%]

             2,074399751 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(100, 1000000)"
      10 loops, best of 3: 50.8 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(100, 1000000)':

             2098,209221 task-clock                #    0,998 CPUs utilized
                       5 context-switches          #    0,002 K/sec
                       1 cpu-migrations            #    0,000 K/sec
                 982.814 page-faults               #    0,468 M/sec
           6.962.432.883 cycles                    #    3,318 GHz                     [83,26%]
           4.927.617.478 stalled-cycles-frontend   #   70,77% frontend cycles idle    [83,27%]
           3.313.428.169 stalled-cycles-backend    #   47,59% backend  cycles idle    [66,71%]
           4.336.431.110 instructions              #    0,62  insns per cycle
                                                   #    1,14  stalled cycles per insn [83,45%]
             608.851.622 branches                  #  290,177 M/sec                   [83,45%]
               8.757.185 branch-misses             #    1,44% of all branches         [83,33%]

             2,103374100 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(10, 10000000)"
      10 loops, best of 3: 52.6 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(10, 10000000)':

             2160,786550 task-clock                #    0,998 CPUs utilized
                       6 context-switches          #    0,003 K/sec
                       3 cpu-migrations            #    0,001 K/sec
                 991.552 page-faults               #    0,459 M/sec
           7.152.367.654 cycles                    #    3,310 GHz                     [83,35%]
           5.027.834.797 stalled-cycles-frontend   #   70,30% frontend cycles idle    [83,38%]
           3.250.538.435 stalled-cycles-backend    #   45,45% backend  cycles idle    [66,76%]
           4.478.910.597 instructions              #    0,63  insns per cycle
                                                   #    1,12  stalled cycles per insn [83,38%]
             631.368.892 branches                  #  292,194 M/sec                   [83,38%]
               8.514.755 branch-misses             #    1,35% of all branches         [83,28%]

             2,166123028 seconds time elapsed

      perf stat /home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit "from test_stringbuilder1 import test" "test(1, 100000000)"
      10 loops, best of 3: 103 msec per loop

       Performance counter stats for '/home/oberstet/pypy-c-jit-67861-20b7b762dbed-linux64/bin/pypy -m timeit from test_stringbuilder1 import test test(1, 100000000)':

             4208,596687 task-clock                #    0,998 CPUs utilized
                       9 context-switches          #    0,002 K/sec
                       2 cpu-migrations            #    0,000 K/sec
               1.958.385 page-faults               #    0,465 M/sec
          13.965.502.617 cycles                    #    3,318 GHz                     [83,31%]
           9.710.596.242 stalled-cycles-frontend   #   69,53% frontend cycles idle    [83,31%]
           7.118.714.720 stalled-cycles-backend    #   50,97% backend  cycles idle    [66,69%]
           9.001.902.521 instructions              #    0,64  insns per cycle
                                                   #    1,08  stalled cycles per insn [83,39%]
           1.398.700.718 branches                  #  332,344 M/sec                   [83,41%]
              16.832.510 branch-misses             #    1,20% of all branches         [83,34%]

             4,218679276 seconds time elapsed

