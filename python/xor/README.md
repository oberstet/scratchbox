## CPython/wsaccel

### Starting ..

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/xor$ python test.py

      !!! Skipping pure Python maskers when running CPython [way too slow]

### Param Set 1

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (1 frames, 1 chops, 100000000 chop size, 100000000 total length)
      Processing 10 messages (1000000000 total payload)..
      Runtime 2.0496711731

### Param Set 2

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (100 frames, 100 chops, 1000 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 2.04835295677

### Param Set 3

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (10 frames, 10000 chops, 100 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 4.24687600136

### Param Set 4

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (1 frames, 1 chops, 100 chop size, 100 total length)
      Processing 10000000 messages (1000000000 total payload)..
      Runtime 11.3152461052

## PyPy

### Starting ..

      oberstet@corei7-ubuntu:~/scm/scratchbox/python/xor$ pypy test.py

### Param Set 1

      Using XOR masker xormasker.XorMaskerSimple
      WebSocket Message (1 frames, 1 chops, 100000000 chop size, 100000000 total length)
      Processing 10 messages (1000000000 total payload)..
      Runtime 8.47873497009

      Using XOR masker xormasker.XorMaskerShifted1
      WebSocket Message (1 frames, 1 chops, 100000000 chop size, 100000000 total length)
      Processing 10 messages (1000000000 total payload)..
      Runtime 5.07598400116

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (1 frames, 1 chops, 100000000 chop size, 100000000 total length)
      Processing 10 messages (1000000000 total payload)..
      Runtime 3.96876502037

### Param Set 2

      Using XOR masker xormasker.XorMaskerSimple
      WebSocket Message (100 frames, 100 chops, 1000 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 9.05049014091

      Using XOR masker xormasker.XorMaskerShifted1
      WebSocket Message (100 frames, 100 chops, 1000 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 5.69222211838

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (100 frames, 100 chops, 1000 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 5.73332905769

### Param Set 3

      Using XOR masker xormasker.XorMaskerSimple
      WebSocket Message (10 frames, 10000 chops, 100 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 13.2506849766

      Using XOR masker xormasker.XorMaskerShifted1
      WebSocket Message (10 frames, 10000 chops, 100 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 10.0598080158

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (10 frames, 10000 chops, 100 chop size, 10000000 total length)
      Processing 100 messages (1000000000 total payload)..
      Runtime 26.1088609695

### Param Set 4

      Using XOR masker xormasker.XorMaskerSimple
      WebSocket Message (1 frames, 1 chops, 100 chop size, 100 total length)
      Processing 10000000 messages (1000000000 total payload)..
      Runtime 13.815171957

      Using XOR masker xormasker.XorMaskerShifted1
      WebSocket Message (1 frames, 1 chops, 100 chop size, 100 total length)
      Processing 10000000 messages (1000000000 total payload)..
      Runtime 17.3883159161

      Using XOR masker <type 'wsaccel.xormask.XorMaskerSimple'>
      WebSocket Message (1 frames, 1 chops, 100 chop size, 100 total length)
      Processing 10000000 messages (1000000000 total payload)..
      Runtime 111.565964937

