# Bandwidth

Download [Bandwidth](https://zsmith.co/bandwidth.html) tarball and build.

Install GCC

```console
sudo pkg install -y gcc gmake nasm
```

Edit `Makefile` and adjust paths for GCC:

```
CC=gcc48
LD=gcc48
```

Build

```console
gmake bandwidth64
```

Run

```console
./bandwidth64
``` 

## Results (small Xeon machine)

```console
[oberstet@brummer2 ~/bandwidth-1.1]$ uname -a
FreeBSD brummer2 10.1-RELEASE-p6 FreeBSD 10.1-RELEASE-p6 #0: Tue Feb 24 19:00:21 UTC 2015     root@amd64-builder.daemonology.net:/usr/obj/usr/src/sys/GENERIC  amd64
[oberstet@brummer2 ~/bandwidth-1.1]$ sysctl hw.model
hw.model: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
[oberstet@brummer2 ~/bandwidth-1.1]$ sysctl hw.ncpu 
hw.ncpu: 8
[oberstet@brummer2 ~/bandwidth-1.1]$ ./bandwidth64 
This is bandwidth version 1.1.
Copyright (C) 2005-2014 by Zack T Smith.

This software is covered by the GNU Public License.
It is provided AS-IS, use at your own risk.
See the file COPYING for more information.

CPU family: GenuineIntel
CPU features: MMX SSE SSE2 SSE3 SSSE3 SSE4.1 SSE4.2 AES AVX AVX2 XD Intel64 

Cache 0: L1 data cache,        line size 64,  8-ways,    64 sets, size 32k 
Cache 1: L1 instruction cache, line size 64,  8-ways,    64 sets, size 32k 
Cache 2: L2 unified cache,     line size 64,  8-ways,   512 sets, size 256k 
Cache 3: L3 unified cache,     line size 64, 16-ways,  8192 sets, size 8192k 

Notation: B = byte, kB = 1024 B, MB = 1048576 B.

Sequential read (128-bit), size = 128 B, loops = 4236771328, 103429.6 MB/s
Sequential read (128-bit), size = 256 B, loops = 2118385664, 103435.2 MB/s
Sequential read (128-bit), size = 384 B, loops = 1325220246, 97056.5 MB/s
Sequential read (128-bit), size = 512 B, loops = 1059192832, 103435.4 MB/s
Sequential read (128-bit), size = 640 B, loops = 847139703, 103406.6 MB/s
Sequential read (128-bit), size = 768 B, loops = 705863718, 103398.0 MB/s
Sequential read (128-bit), size = 896 B, loops = 605100942, 103401.4 MB/s
Sequential read (128-bit), size = 1024 B, loops = 529399808, 103387.9 MB/s
Sequential read (128-bit), size = 1280 B, loops = 423356100, 103347.3 MB/s
Sequential read (128-bit), size = 2 kB, loops = 264732672, 103407.8 MB/s
Sequential read (128-bit), size = 3 kB, loops = 176485755, 103409.4 MB/s
Sequential read (128-bit), size = 4 kB, loops = 132366336, 103408.2 MB/s
Sequential read (128-bit), size = 6 kB, loops = 87987632, 103109.3 MB/s
Sequential read (128-bit), size = 8 kB, loops = 65814528, 102832.2 MB/s
Sequential read (128-bit), size = 12 kB, loops = 42268140, 99061.0 MB/s
Sequential read (128-bit), size = 16 kB, loops = 31944704, 99816.8 MB/s
Sequential read (128-bit), size = 20 kB, loops = 25703496, 100395.9 MB/s
Sequential read (128-bit), size = 24 kB, loops = 21476910, 100671.6 MB/s
Sequential read (128-bit), size = 28 kB, loops = 18476640, 101036.3 MB/s
Sequential read (128-bit), size = 32 kB, loops = 16097280, 100597.2 MB/s
Sequential read (128-bit), size = 34 kB, loops = 10409654, 69122.8 MB/s
Sequential read (128-bit), size = 36 kB, loops = 8153600, 57329.3 MB/s
Sequential read (128-bit), size = 40 kB, loops = 7321860, 57200.1 MB/s
Sequential read (128-bit), size = 48 kB, loops = 6112470, 57291.7 MB/s
Sequential read (128-bit), size = 64 kB, loops = 4577280, 57209.1 MB/s
Sequential read (128-bit), size = 128 kB, loops = 2282496, 57051.3 MB/s
Sequential read (128-bit), size = 192 kB, loops = 1510289, 56628.0 MB/s
Sequential read (128-bit), size = 256 kB, loops = 1124352, 56205.3 MB/s
Sequential read (128-bit), size = 320 kB, loops = 627096, 39189.4 MB/s
Sequential read (128-bit), size = 384 kB, loops = 520710, 39049.5 MB/s
Sequential read (128-bit), size = 512 kB, loops = 390016, 38991.3 MB/s
Sequential read (128-bit), size = 768 kB, loops = 260950, 39137.1 MB/s
Sequential read (128-bit), size = 1 MB, loops = 194944, 38978.7 MB/s
Sequential read (128-bit), size = 1.25 MB, loops = 156009, 38989.7 MB/s
Sequential read (128-bit), size = 1.5 MB, loops = 130032, 39001.1 MB/s
Sequential read (128-bit), size = 1.75 MB, loops = 111456, 39002.2 MB/s
Sequential read (128-bit), size = 2 MB, loops = 97536, 39003.3 MB/s
Sequential read (128-bit), size = 2.25 MB, loops = 87164, 39215.1 MB/s
Sequential read (128-bit), size = 2.5 MB, loops = 78025, 39004.8 MB/s
Sequential read (128-bit), size = 2.75 MB, loops = 70932, 39006.0 MB/s
Sequential read (128-bit), size = 3 MB, loops = 65373, 39221.8 MB/s
Sequential read (128-bit), size = 3.25 MB, loops = 60249, 39161.5 MB/s
Sequential read (128-bit), size = 3.5 MB, loops = 55728, 39004.4 MB/s
Sequential read (128-bit), size = 4 MB, loops = 49152, 39317.3 MB/s
Sequential read (128-bit), size = 5 MB, loops = 39396, 39392.9 MB/s
Sequential read (128-bit), size = 6 MB, loops = 32980, 39566.6 MB/s
Sequential read (128-bit), size = 7 MB, loops = 28233, 39519.0 MB/s
Sequential read (128-bit), size = 8 MB, loops = 23632, 37810.7 MB/s
Sequential read (128-bit), size = 9 MB, loops = 15799, 28432.5 MB/s
Sequential read (128-bit), size = 10 MB, loops = 12894, 25785.5 MB/s
Sequential read (128-bit), size = 12 MB, loops = 8835, 21194.8 MB/s
Sequential read (128-bit), size = 14 MB, loops = 6840, 19142.8 MB/s
Sequential read (128-bit), size = 15 MB, loops = 6272, 18813.3 MB/s
Sequential read (128-bit), size = 16 MB, loops = 5804, 18571.6 MB/s
Sequential read (128-bit), size = 20 MB, loops = 4482, 17918.0 MB/s
Sequential read (128-bit), size = 21 MB, loops = 4242, 17809.3 MB/s
Sequential read (128-bit), size = 32 MB, loops = 2698, 17266.2 MB/s
Sequential read (128-bit), size = 48 MB, loops = 1765, 16944.0 MB/s
Sequential read (128-bit), size = 64 MB, loops = 1315, 16821.4 MB/s
Sequential read (128-bit), size = 72 MB, loops = 1173, 16882.4 MB/s
Sequential read (128-bit), size = 96 MB, loops = 877, 16836.4 MB/s
Sequential read (128-bit), size = 128 MB, loops = 657, 16799.6 MB/s

Sequential read (256-bit), size = 256 B, loops = 4235198464, 206785.3 MB/s
Sequential read (256-bit), size = 512 B, loops = 1693843456, 165410.4 MB/s
Sequential read (256-bit), size = 768 B, loops = 1411203150, 206709.4 MB/s
Sequential read (256-bit), size = 1024 B, loops = 1057947648, 206619.9 MB/s
Sequential read (256-bit), size = 1280 B, loops = 846712200, 206716.0 MB/s
Sequential read (256-bit), size = 2 kB, loops = 529235968, 206720.7 MB/s
Sequential read (256-bit), size = 3 kB, loops = 352818595, 206722.9 MB/s
Sequential read (256-bit), size = 4 kB, loops = 264617984, 206722.9 MB/s
Sequential read (256-bit), size = 6 kB, loops = 176412144, 206721.6 MB/s
Sequential read (256-bit), size = 8 kB, loops = 131645440, 205689.3 MB/s
Sequential read (256-bit), size = 12 kB, loops = 81587340, 191219.9 MB/s
Sequential read (256-bit), size = 16 kB, loops = 61759488, 192996.7 MB/s
Sequential read (256-bit), size = 20 kB, loops = 49916412, 194973.3 MB/s
Sequential read (256-bit), size = 24 kB, loops = 41992860, 196831.4 MB/s
Sequential read (256-bit), size = 28 kB, loops = 36134280, 197607.0 MB/s
Sequential read (256-bit), size = 32 kB, loops = 31461376, 196622.5 MB/s
Sequential read (256-bit), size = 34 kB, loops = 17522211, 116352.2 MB/s
Sequential read (256-bit), size = 36 kB, loops = 12488840, 87801.8 MB/s
Sequential read (256-bit), size = 40 kB, loops = 11203920, 87519.2 MB/s
Sequential read (256-bit), size = 48 kB, loops = 9302475, 87209.9 MB/s
Sequential read (256-bit), size = 64 kB, loops = 6979584, 87234.1 MB/s
Sequential read (256-bit), size = 128 kB, loops = 3460608, 86507.0 MB/s
Sequential read (256-bit), size = 192 kB, loops = 2254010, 84516.4 MB/s
Sequential read (256-bit), size = 256 kB, loops = 1655552, 82771.6 MB/s
Sequential read (256-bit), size = 320 kB, loops = 666060, 41625.6 MB/s
Sequential read (256-bit), size = 384 kB, loops = 556580, 41732.3 MB/s
Sequential read (256-bit), size = 512 kB, loops = 416256, 41624.7 MB/s
Sequential read (256-bit), size = 768 kB, loops = 277525, 41618.6 MB/s
Sequential read (256-bit), size = 1 MB, loops = 208128, 41615.5 MB/s
Sequential read (256-bit), size = 1.25 MB, loops = 166566, 41629.5 MB/s
Sequential read (256-bit), size = 1.5 MB, loops = 139104, 41728.6 MB/s
Sequential read (256-bit), size = 1.75 MB, loops = 118944, 41627.8 MB/s
Sequential read (256-bit), size = 2 MB, loops = 104288, 41713.8 MB/s
Sequential read (256-bit), size = 2.25 MB, loops = 92680, 41703.2 MB/s
Sequential read (256-bit), size = 2.5 MB, loops = 83450, 41724.8 MB/s
Sequential read (256-bit), size = 2.75 MB, loops = 75716, 41637.8 MB/s
Sequential read (256-bit), size = 3 MB, loops = 69615, 41756.6 MB/s
Sequential read (256-bit), size = 3.25 MB, loops = 64258, 41756.1 MB/s
Sequential read (256-bit), size = 3.5 MB, loops = 59670, 41757.0 MB/s
Sequential read (256-bit), size = 4 MB, loops = 52192, 41744.9 MB/s
Sequential read (256-bit), size = 5 MB, loops = 41616, 41611.9 MB/s
Sequential read (256-bit), size = 6 MB, loops = 34790, 41744.2 MB/s
Sequential read (256-bit), size = 7 MB, loops = 29835, 41762.1 MB/s
Sequential read (256-bit), size = 8 MB, loops = 25496, 40792.2 MB/s
Sequential read (256-bit), size = 9 MB, loops = 17115, 30796.2 MB/s
Sequential read (256-bit), size = 10 MB, loops = 13128, 26246.5 MB/s
Sequential read (256-bit), size = 12 MB, loops = 8705, 20886.4 MB/s
Sequential read (256-bit), size = 14 MB, loops = 6708, 18782.3 MB/s
Sequential read (256-bit), size = 15 MB, loops = 6088, 18263.7 MB/s
Sequential read (256-bit), size = 16 MB, loops = 5612, 17948.3 MB/s
Sequential read (256-bit), size = 20 MB, loops = 4311, 17239.1 MB/s
Sequential read (256-bit), size = 21 MB, loops = 4080, 17127.2 MB/s
Sequential read (256-bit), size = 32 MB, loops = 2616, 16741.6 MB/s
Sequential read (256-bit), size = 48 MB, loops = 1734, 16642.8 MB/s
Sequential read (256-bit), size = 64 MB, loops = 1301, 16649.1 MB/s
Sequential read (256-bit), size = 72 MB, loops = 1154, 16613.3 MB/s
Sequential read (256-bit), size = 96 MB, loops = 865, 16599.6 MB/s
Sequential read (256-bit), size = 128 MB, loops = 648, 16563.9 MB/s

Random read (128-bit), size = 256 B, loops = 1303904256, 63658.9 MB/s
Random read (128-bit), size = 512 B, loops = 651952128, 63660.0 MB/s
Random read (128-bit), size = 768 B, loops = 434545713, 63646.4 MB/s
Random read (128-bit), size = 1024 B, loops = 325910528, 63646.8 MB/s
Random read (128-bit), size = 1280 B, loops = 260619588, 63624.5 MB/s
Random read (128-bit), size = 2 kB, loops = 162955264, 63648.7 MB/s
Random read (128-bit), size = 3 kB, loops = 108635185, 63648.1 MB/s
Random read (128-bit), size = 4 kB, loops = 81461248, 63629.7 MB/s
Random read (128-bit), size = 6 kB, loops = 54315106, 63648.3 MB/s
Random read (128-bit), size = 8 kB, loops = 40738816, 63648.1 MB/s
Random read (128-bit), size = 12 kB, loops = 26824432, 62866.0 MB/s
Random read (128-bit), size = 16 kB, loops = 20180992, 63060.6 MB/s
Random read (128-bit), size = 20 kB, loops = 16173612, 63175.4 MB/s
Random read (128-bit), size = 24 kB, loops = 13494390, 63251.7 MB/s
Random read (128-bit), size = 28 kB, loops = 11508120, 62928.6 MB/s
Random read (128-bit), size = 32 kB, loops = 9551872, 59688.8 MB/s
Random read (128-bit), size = 34 kB, loops = 8272611, 54934.0 MB/s
Random read (128-bit), size = 36 kB, loops = 6841380, 48101.9 MB/s
Random read (128-bit), size = 40 kB, loops = 5918094, 46229.9 MB/s
Random read (128-bit), size = 48 kB, loops = 4803435, 45025.5 MB/s
Random read (128-bit), size = 64 kB, loops = 3525632, 44066.0 MB/s
Random read (128-bit), size = 128 kB, loops = 1731072, 43274.2 MB/s
Random read (128-bit), size = 192 kB, loops = 1142009, 42824.7 MB/s
Random read (128-bit), size = 256 kB, loops = 777984, 38898.4 MB/s
Random read (128-bit), size = 320 kB, loops = 460836, 28801.9 MB/s
Random read (128-bit), size = 384 kB, loops = 364480, 27327.4 MB/s
Random read (128-bit), size = 512 kB, loops = 261760, 26172.5 MB/s
Random read (128-bit), size = 768 kB, loops = 168215, 25224.0 MB/s
Random read (128-bit), size = 1 MB, loops = 123776, 24744.3 MB/s
Random read (128-bit), size = 1.25 MB, loops = 98532, 24626.9 MB/s
Random read (128-bit), size = 1.5 MB, loops = 81522, 24456.5 MB/s
Random read (128-bit), size = 1.75 MB, loops = 69552, 24333.4 MB/s
Random read (128-bit), size = 2 MB, loops = 60896, 24347.3 MB/s
Random read (128-bit), size = 2.25 MB, loops = 53788, 24203.8 MB/s
Random read (128-bit), size = 2.5 MB, loops = 48425, 24209.1 MB/s
Random read (128-bit), size = 2.75 MB, loops = 43792, 24079.6 MB/s
Random read (128-bit), size = 3 MB, loops = 40089, 24046.0 MB/s
Random read (128-bit), size = 3.25 MB, loops = 36936, 23998.6 MB/s
Random read (128-bit), size = 3.5 MB, loops = 34272, 23990.0 MB/s
Random read (128-bit), size = 4 MB, loops = 34352, 27474.8 MB/s
Random read (128-bit), size = 5 MB, loops = 26808, 26804.6 MB/s
Random read (128-bit), size = 6 MB, loops = 22850, 27412.3 MB/s
Random read (128-bit), size = 7 MB, loops = 18810, 26329.0 MB/s
Random read (128-bit), size = 8 MB, loops = 11576, 18514.4 MB/s
Random read (128-bit), size = 9 MB, loops = 7217, 12982.7 MB/s
Random read (128-bit), size = 10 MB, loops = 5898, 11789.3 MB/s
Random read (128-bit), size = 12 MB, loops = 4240, 10165.9 MB/s
Random read (128-bit), size = 14 MB, loops = 3284, 9187.0 MB/s
Random read (128-bit), size = 15 MB, loops = 2940, 8815.1 MB/s
Random read (128-bit), size = 16 MB, loops = 2676, 8561.0 MB/s
Random read (128-bit), size = 20 MB, loops = 1938, 7745.6 MB/s
Random read (128-bit), size = 21 MB, loops = 1821, 7638.0 MB/s
Random read (128-bit), size = 32 MB, loops = 1066, 6813.1 MB/s
Random read (128-bit), size = 48 MB, loops = 657, 6303.3 MB/s
Random read (128-bit), size = 64 MB, loops = 473, 6045.4 MB/s
Random read (128-bit), size = 72 MB, loops = 413, 5939.0 MB/s
Random read (128-bit), size = 96 MB, loops = 300, 5751.3 MB/s
Random read (128-bit), size = 128 MB, loops = 220, 5624.0 MB/s

Sequential write (128-bit), size = 128 B, loops = 2118647808, 51724.4 MB/s
Sequential write (128-bit), size = 256 B, loops = 1059586048, 51725.4 MB/s
Sequential write (128-bit), size = 384 B, loops = 705863718, 51692.2 MB/s
Sequential write (128-bit), size = 512 B, loops = 529399808, 51696.7 MB/s
Sequential write (128-bit), size = 640 B, loops = 423727137, 51714.9 MB/s
Sequential write (128-bit), size = 768 B, loops = 353106621, 51714.5 MB/s
Sequential write (128-bit), size = 896 B, loops = 302662818, 51715.1 MB/s
Sequential write (128-bit), size = 1024 B, loops = 264830976, 51714.8 MB/s
Sequential write (128-bit), size = 1280 B, loops = 211861548, 51714.6 MB/s
Sequential write (128-bit), size = 2 kB, loops = 132415488, 51715.0 MB/s
Sequential write (128-bit), size = 3 kB, loops = 88275645, 51715.0 MB/s
Sequential write (128-bit), size = 4 kB, loops = 66207744, 51715.3 MB/s
Sequential write (128-bit), size = 6 kB, loops = 44135802, 51715.0 MB/s
Sequential write (128-bit), size = 8 kB, loops = 33087488, 51691.9 MB/s
Sequential write (128-bit), size = 12 kB, loops = 22007830, 51578.7 MB/s
Sequential write (128-bit), size = 16 kB, loops = 16523264, 51631.5 MB/s
Sequential write (128-bit), size = 20 kB, loops = 13221936, 51646.0 MB/s
Sequential write (128-bit), size = 24 kB, loops = 11021010, 51652.1 MB/s
Sequential write (128-bit), size = 28 kB, loops = 9444240, 51639.7 MB/s
Sequential write (128-bit), size = 32 kB, loops = 8263680, 51638.9 MB/s
Sequential write (128-bit), size = 34 kB, loops = 6549873, 43488.6 MB/s
Sequential write (128-bit), size = 36 kB, loops = 4875780, 34281.4 MB/s
Sequential write (128-bit), size = 40 kB, loops = 4365270, 34098.0 MB/s
Sequential write (128-bit), size = 48 kB, loops = 3643185, 34151.6 MB/s
Sequential write (128-bit), size = 64 kB, loops = 2740224, 34252.6 MB/s
Sequential write (128-bit), size = 128 kB, loops = 1364480, 34101.8 MB/s
Sequential write (128-bit), size = 192 kB, loops = 909106, 34084.3 MB/s
Sequential write (128-bit), size = 256 kB, loops = 679168, 33950.6 MB/s
Sequential write (128-bit), size = 320 kB, loops = 425136, 26562.8 MB/s
Sequential write (128-bit), size = 384 kB, loops = 338640, 25396.5 MB/s
Sequential write (128-bit), size = 512 kB, loops = 253824, 25371.5 MB/s
Sequential write (128-bit), size = 768 kB, loops = 169405, 25405.2 MB/s
Sequential write (128-bit), size = 1 MB, loops = 127040, 25405.4 MB/s
Sequential write (128-bit), size = 1.25 MB, loops = 101643, 25405.5 MB/s
Sequential write (128-bit), size = 1.5 MB, loops = 84714, 25405.6 MB/s
Sequential write (128-bit), size = 1.75 MB, loops = 72576, 25400.9 MB/s
Sequential write (128-bit), size = 2 MB, loops = 63520, 25401.8 MB/s
Sequential write (128-bit), size = 2.25 MB, loops = 56476, 25405.3 MB/s
Sequential write (128-bit), size = 2.5 MB, loops = 50800, 25392.9 MB/s
Sequential write (128-bit), size = 2.75 MB, loops = 46092, 25349.1 MB/s
Sequential write (128-bit), size = 3 MB, loops = 42252, 25349.0 MB/s
Sequential write (128-bit), size = 3.25 MB, loops = 39007, 25343.8 MB/s
Sequential write (128-bit), size = 3.5 MB, loops = 36252, 25372.7 MB/s
Sequential write (128-bit), size = 4 MB, loops = 31760, 25397.6 MB/s
Sequential write (128-bit), size = 5 MB, loops = 25356, 25351.6 MB/s
Sequential write (128-bit), size = 6 MB, loops = 21120, 25338.4 MB/s
Sequential write (128-bit), size = 7 MB, loops = 18099, 25334.5 MB/s
Sequential write (128-bit), size = 8 MB, loops = 15456, 24720.5 MB/s
Sequential write (128-bit), size = 9 MB, loops = 10906, 19619.2 MB/s
Sequential write (128-bit), size = 10 MB, loops = 8544, 17076.4 MB/s
Sequential write (128-bit), size = 12 MB, loops = 5945, 14266.8 MB/s
Sequential write (128-bit), size = 14 MB, loops = 4616, 12915.5 MB/s
Sequential write (128-bit), size = 15 MB, loops = 4092, 12272.9 MB/s
Sequential write (128-bit), size = 16 MB, loops = 3708, 11862.1 MB/s
Sequential write (128-bit), size = 20 MB, loops = 2694, 10770.4 MB/s
Sequential write (128-bit), size = 21 MB, loops = 2565, 10762.2 MB/s
Sequential write (128-bit), size = 32 MB, loops = 1578, 10087.4 MB/s
Sequential write (128-bit), size = 48 MB, loops = 1037, 9948.6 MB/s
Sequential write (128-bit), size = 64 MB, loops = 778, 9946.3 MB/s
Sequential write (128-bit), size = 72 MB, loops = 686, 9868.8 MB/s
Sequential write (128-bit), size = 96 MB, loops = 511, 9795.2 MB/s
Sequential write (128-bit), size = 128 MB, loops = 381, 9736.6 MB/s

Sequential write (256-bit), size = 256 B, loops = 2118385664, 103428.6 MB/s
Sequential write (256-bit), size = 512 B, loops = 1058799616, 103391.8 MB/s
Sequential write (256-bit), size = 768 B, loops = 706125861, 103435.4 MB/s
Sequential write (256-bit), size = 1024 B, loops = 529465344, 103406.1 MB/s
Sequential write (256-bit), size = 1280 B, loops = 423565812, 103406.5 MB/s
Sequential write (256-bit), size = 2 kB, loops = 264732672, 103407.9 MB/s
Sequential write (256-bit), size = 3 kB, loops = 176420220, 103360.6 MB/s
Sequential write (256-bit), size = 4 kB, loops = 132366336, 103409.9 MB/s
Sequential write (256-bit), size = 6 kB, loops = 88206072, 103362.2 MB/s
Sequential write (256-bit), size = 8 kB, loops = 65896448, 102957.1 MB/s
Sequential write (256-bit), size = 12 kB, loops = 44010199, 103136.5 MB/s
Sequential write (256-bit), size = 16 kB, loops = 33013760, 103156.5 MB/s
Sequential write (256-bit), size = 20 kB, loops = 26381628, 103052.3 MB/s
Sequential write (256-bit), size = 24 kB, loops = 22028370, 103252.4 MB/s
Sequential write (256-bit), size = 28 kB, loops = 18874440, 103218.9 MB/s
Sequential write (256-bit), size = 32 kB, loops = 16496640, 103101.9 MB/s
Sequential write (256-bit), size = 34 kB, loops = 8266830, 54890.5 MB/s
Sequential write (256-bit), size = 36 kB, loops = 4903080, 34468.6 MB/s
Sequential write (256-bit), size = 40 kB, loops = 4412772, 34473.3 MB/s
Sequential write (256-bit), size = 48 kB, loops = 3677310, 34474.0 MB/s
Sequential write (256-bit), size = 64 kB, loops = 2758656, 34473.1 MB/s
Sequential write (256-bit), size = 128 kB, loops = 1377280, 34428.7 MB/s
Sequential write (256-bit), size = 192 kB, loops = 915926, 34335.5 MB/s
Sequential write (256-bit), size = 256 kB, loops = 685568, 34278.2 MB/s
Sequential write (256-bit), size = 320 kB, loops = 425136, 26564.8 MB/s
Sequential write (256-bit), size = 384 kB, loops = 339150, 25424.3 MB/s
Sequential write (256-bit), size = 512 kB, loops = 254080, 25406.7 MB/s
Sequential write (256-bit), size = 768 kB, loops = 169405, 25406.3 MB/s
Sequential write (256-bit), size = 1 MB, loops = 127040, 25406.1 MB/s
Sequential write (256-bit), size = 1.25 MB, loops = 101643, 25406.0 MB/s
Sequential write (256-bit), size = 1.5 MB, loops = 84714, 25406.4 MB/s
Sequential write (256-bit), size = 1.75 MB, loops = 72612, 25406.1 MB/s
Sequential write (256-bit), size = 2 MB, loops = 63520, 25406.2 MB/s
Sequential write (256-bit), size = 2.25 MB, loops = 56476, 25406.0 MB/s
Sequential write (256-bit), size = 2.5 MB, loops = 50825, 25402.2 MB/s
Sequential write (256-bit), size = 2.75 MB, loops = 46207, 25401.9 MB/s
Sequential write (256-bit), size = 3 MB, loops = 42357, 25405.8 MB/s
Sequential write (256-bit), size = 3.25 MB, loops = 39102, 25405.3 MB/s
Sequential write (256-bit), size = 3.5 MB, loops = 36288, 25400.4 MB/s
Sequential write (256-bit), size = 4 MB, loops = 31760, 25397.6 MB/s
Sequential write (256-bit), size = 5 MB, loops = 25392, 25387.6 MB/s
Sequential write (256-bit), size = 6 MB, loops = 21160, 25385.8 MB/s
Sequential write (256-bit), size = 7 MB, loops = 18126, 25368.6 MB/s
Sequential write (256-bit), size = 8 MB, loops = 15504, 24794.5 MB/s
Sequential write (256-bit), size = 9 MB, loops = 11011, 19814.0 MB/s
Sequential write (256-bit), size = 10 MB, loops = 8592, 17176.9 MB/s
Sequential write (256-bit), size = 12 MB, loops = 6015, 14424.2 MB/s
Sequential write (256-bit), size = 14 MB, loops = 4592, 12847.0 MB/s
Sequential write (256-bit), size = 15 MB, loops = 4072, 12207.6 MB/s
Sequential write (256-bit), size = 16 MB, loops = 3708, 11865.3 MB/s
Sequential write (256-bit), size = 20 MB, loops = 2733, 10924.6 MB/s
Sequential write (256-bit), size = 21 MB, loops = 2559, 10741.9 MB/s
Sequential write (256-bit), size = 32 MB, loops = 1590, 10167.3 MB/s
Sequential write (256-bit), size = 48 MB, loops = 1036, 9939.7 MB/s
Sequential write (256-bit), size = 64 MB, loops = 776, 9932.3 MB/s
Sequential write (256-bit), size = 72 MB, loops = 689, 9919.9 MB/s
Sequential write (256-bit), size = 96 MB, loops = 512, 9817.9 MB/s
Sequential write (256-bit), size = 128 MB, loops = 382, 9765.5 MB/s

Random write (128-bit), size = 256 B, loops = 1059061760, 51700.5 MB/s
Random write (128-bit), size = 512 B, loops = 529661952, 51718.3 MB/s
Random write (128-bit), size = 768 B, loops = 353106621, 51714.9 MB/s
Random write (128-bit), size = 1024 B, loops = 264699904, 51690.9 MB/s
Random write (128-bit), size = 1280 B, loops = 211756692, 51690.8 MB/s
Random write (128-bit), size = 2 kB, loops = 132349952, 51691.8 MB/s
Random write (128-bit), size = 3 kB, loops = 86921255, 50920.4 MB/s
Random write (128-bit), size = 4 kB, loops = 65241088, 50962.1 MB/s
Random write (128-bit), size = 6 kB, loops = 43666156, 51169.5 MB/s
Random write (128-bit), size = 8 kB, loops = 32260096, 50402.9 MB/s
Random write (128-bit), size = 12 kB, loops = 21439886, 50243.4 MB/s
Random write (128-bit), size = 16 kB, loops = 16154624, 50480.6 MB/s
Random write (128-bit), size = 20 kB, loops = 12573288, 49103.8 MB/s
Random write (128-bit), size = 24 kB, loops = 10794420, 50588.9 MB/s
Random write (128-bit), size = 28 kB, loops = 9252360, 50594.2 MB/s
Random write (128-bit), size = 32 kB, loops = 5117952, 31977.6 MB/s
Random write (128-bit), size = 34 kB, loops = 3460892, 22969.8 MB/s
Random write (128-bit), size = 36 kB, loops = 2165800, 15225.7 MB/s
Random write (128-bit), size = 40 kB, loops = 1941030, 15154.7 MB/s
Random write (128-bit), size = 48 kB, loops = 1607970, 15069.8 MB/s
Random write (128-bit), size = 64 kB, loops = 1208320, 15101.9 MB/s
Random write (128-bit), size = 128 kB, loops = 606208, 15150.6 MB/s
Random write (128-bit), size = 192 kB, loops = 403403, 15115.5 MB/s
Random write (128-bit), size = 256 kB, loops = 281088, 14049.9 MB/s
Random write (128-bit), size = 320 kB, loops = 107712, 6719.7 MB/s
Random write (128-bit), size = 384 kB, loops = 84830, 6359.1 MB/s
Random write (128-bit), size = 512 kB, loops = 62976, 6295.3 MB/s
Random write (128-bit), size = 768 kB, loops = 41990, 6286.0 MB/s
Random write (128-bit), size = 1 MB, loops = 31424, 6277.6 MB/s
Random write (128-bit), size = 1.25 MB, loops = 25143, 6280.4 MB/s
Random write (128-bit), size = 1.5 MB, loops = 20916, 6267.3 MB/s
Random write (128-bit), size = 1.75 MB, loops = 17964, 6285.0 MB/s
Random write (128-bit), size = 2 MB, loops = 15584, 6221.9 MB/s
Random write (128-bit), size = 2.25 MB, loops = 13972, 6281.4 MB/s
Random write (128-bit), size = 2.5 MB, loops = 12575, 6281.8 MB/s
Random write (128-bit), size = 2.75 MB, loops = 11431, 6281.0 MB/s
Random write (128-bit), size = 3 MB, loops = 10395, 6227.9 MB/s
Random write (128-bit), size = 3.25 MB, loops = 9633, 6253.3 MB/s
Random write (128-bit), size = 3.5 MB, loops = 8928, 6241.2 MB/s
Random write (128-bit), size = 4 MB, loops = 7840, 6261.7 MB/s
Random write (128-bit), size = 5 MB, loops = 6264, 6252.8 MB/s
Random write (128-bit), size = 6 MB, loops = 5240, 6279.2 MB/s
Random write (128-bit), size = 7 MB, loops = 4437, 6205.2 MB/s
Random write (128-bit), size = 8 MB, loops = 3824, 6112.6 MB/s
Random write (128-bit), size = 9 MB, loops = 3262, 5870.3 MB/s
Random write (128-bit), size = 10 MB, loops = 2874, 5747.3 MB/s
Random write (128-bit), size = 12 MB, loops = 2325, 5578.5 MB/s
Random write (128-bit), size = 14 MB, loops = 1952, 5463.4 MB/s
Random write (128-bit), size = 15 MB, loops = 1808, 5420.3 MB/s
Random write (128-bit), size = 16 MB, loops = 1684, 5378.2 MB/s
Random write (128-bit), size = 20 MB, loops = 1317, 5266.1 MB/s
Random write (128-bit), size = 21 MB, loops = 1251, 5243.7 MB/s
Random write (128-bit), size = 32 MB, loops = 822, 5260.2 MB/s
Random write (128-bit), size = 48 MB, loops = 529, 5074.7 MB/s
Random write (128-bit), size = 64 MB, loops = 398, 5088.3 MB/s
Random write (128-bit), size = 72 MB, loops = 354, 5085.5 MB/s
Random write (128-bit), size = 96 MB, loops = 257, 4934.3 MB/s
Random write (128-bit), size = 128 MB, loops = 197, 5028.3 MB/s

Sequential read bypassing cache (128-bit), size = 128 B, loops = 4236771328, 103434.2 MB/s
Sequential read bypassing cache (128-bit), size = 256 B, loops = 2118385664, 103434.3 MB/s
Sequential read bypassing cache (128-bit), size = 384 B, loops = 1349861688, 98866.6 MB/s
Sequential read bypassing cache (128-bit), size = 512 B, loops = 1059192832, 103432.7 MB/s
Sequential read bypassing cache (128-bit), size = 640 B, loops = 846720275, 103353.7 MB/s
Sequential read bypassing cache (128-bit), size = 768 B, loops = 705951099, 103408.1 MB/s
Sequential read bypassing cache (128-bit), size = 896 B, loops = 604501758, 103298.6 MB/s
Sequential read bypassing cache (128-bit), size = 1024 B, loops = 529203200, 103357.2 MB/s
Sequential read bypassing cache (128-bit), size = 1280 B, loops = 423565812, 103401.0 MB/s
Sequential read bypassing cache (128-bit), size = 2 kB, loops = 264732672, 103399.1 MB/s
Sequential read bypassing cache (128-bit), size = 3 kB, loops = 176398375, 103356.4 MB/s
Sequential read bypassing cache (128-bit), size = 4 kB, loops = 132235264, 103302.9 MB/s
Sequential read bypassing cache (128-bit), size = 6 kB, loops = 87889334, 102991.4 MB/s
Sequential read bypassing cache (128-bit), size = 8 kB, loops = 65650688, 102568.9 MB/s
Sequential read bypassing cache (128-bit), size = 12 kB, loops = 42137076, 98748.2 MB/s
Sequential read bypassing cache (128-bit), size = 16 kB, loops = 31928320, 99768.9 MB/s
Sequential read bypassing cache (128-bit), size = 20 kB, loops = 25674012, 100277.1 MB/s
Sequential read bypassing cache (128-bit), size = 24 kB, loops = 21490560, 100728.9 MB/s
Sequential read bypassing cache (128-bit), size = 28 kB, loops = 18453240, 100913.6 MB/s
Sequential read bypassing cache (128-bit), size = 32 kB, loops = 16093184, 100573.6 MB/s
Sequential read bypassing cache (128-bit), size = 34 kB, loops = 10407727, 69112.9 MB/s
Sequential read bypassing cache (128-bit), size = 36 kB, loops = 8104460, 56979.5 MB/s
Sequential read bypassing cache (128-bit), size = 40 kB, loops = 7289100, 56940.7 MB/s
Sequential read bypassing cache (128-bit), size = 48 kB, loops = 6082440, 57012.9 MB/s
Sequential read bypassing cache (128-bit), size = 64 kB, loops = 4577280, 57214.7 MB/s
Sequential read bypassing cache (128-bit), size = 128 kB, loops = 2280448, 57006.5 MB/s
Sequential read bypassing cache (128-bit), size = 192 kB, loops = 1509266, 56588.6 MB/s
Sequential read bypassing cache (128-bit), size = 256 kB, loops = 1124608, 56217.8 MB/s
Sequential read bypassing cache (128-bit), size = 320 kB, loops = 626076, 39128.2 MB/s
Sequential read bypassing cache (128-bit), size = 384 kB, loops = 519690, 38964.9 MB/s
Sequential read bypassing cache (128-bit), size = 512 kB, loops = 390912, 39082.0 MB/s
Sequential read bypassing cache (128-bit), size = 768 kB, loops = 260270, 39028.1 MB/s
Sequential read bypassing cache (128-bit), size = 1 MB, loops = 195264, 39046.0 MB/s
Sequential read bypassing cache (128-bit), size = 1.25 MB, loops = 156570, 39137.7 MB/s
Sequential read bypassing cache (128-bit), size = 1.5 MB, loops = 130032, 39004.8 MB/s
Sequential read bypassing cache (128-bit), size = 1.75 MB, loops = 111456, 39006.6 MB/s
Sequential read bypassing cache (128-bit), size = 2 MB, loops = 97536, 39008.7 MB/s
Sequential read bypassing cache (128-bit), size = 2.25 MB, loops = 86688, 39008.1 MB/s
Sequential read bypassing cache (128-bit), size = 2.5 MB, loops = 78225, 39110.0 MB/s
Sequential read bypassing cache (128-bit), size = 2.75 MB, loops = 71346, 39232.3 MB/s
Sequential read bypassing cache (128-bit), size = 3 MB, loops = 65415, 39243.3 MB/s
Sequential read bypassing cache (128-bit), size = 3.25 MB, loops = 60363, 39231.7 MB/s
Sequential read bypassing cache (128-bit), size = 3.5 MB, loops = 56052, 39231.6 MB/s
Sequential read bypassing cache (128-bit), size = 4 MB, loops = 49472, 39566.4 MB/s
Sequential read bypassing cache (128-bit), size = 5 MB, loops = 39468, 39463.8 MB/s
Sequential read bypassing cache (128-bit), size = 6 MB, loops = 32820, 39373.3 MB/s
Sequential read bypassing cache (128-bit), size = 7 MB, loops = 28152, 39400.7 MB/s
Sequential read bypassing cache (128-bit), size = 8 MB, loops = 23616, 37779.3 MB/s
Sequential read bypassing cache (128-bit), size = 9 MB, loops = 15890, 28599.9 MB/s
Sequential read bypassing cache (128-bit), size = 10 MB, loops = 12954, 25905.0 MB/s
Sequential read bypassing cache (128-bit), size = 12 MB, loops = 8855, 21243.1 MB/s
Sequential read bypassing cache (128-bit), size = 14 MB, loops = 6832, 19124.2 MB/s
Sequential read bypassing cache (128-bit), size = 15 MB, loops = 6284, 18848.4 MB/s
Sequential read bypassing cache (128-bit), size = 16 MB, loops = 5808, 18585.2 MB/s
Sequential read bypassing cache (128-bit), size = 20 MB, loops = 4494, 17968.5 MB/s
Sequential read bypassing cache (128-bit), size = 21 MB, loops = 4254, 17860.3 MB/s
Sequential read bypassing cache (128-bit), size = 32 MB, loops = 2692, 17219.2 MB/s
Sequential read bypassing cache (128-bit), size = 48 MB, loops = 1772, 17007.0 MB/s
Sequential read bypassing cache (128-bit), size = 64 MB, loops = 1319, 16875.4 MB/s
Sequential read bypassing cache (128-bit), size = 72 MB, loops = 1169, 16824.2 MB/s
Sequential read bypassing cache (128-bit), size = 96 MB, loops = 872, 16729.1 MB/s
Sequential read bypassing cache (128-bit), size = 128 MB, loops = 655, 16756.3 MB/s

Random read bypassing cache (128-bit), size = 256 B, loops = 1303904256, 63659.3 MB/s
Random read bypassing cache (128-bit), size = 512 B, loops = 651952128, 63659.5 MB/s
Random read bypassing cache (128-bit), size = 768 B, loops = 434458332, 63628.8 MB/s
Random read bypassing cache (128-bit), size = 1024 B, loops = 325910528, 63643.9 MB/s
Random read bypassing cache (128-bit), size = 1280 B, loops = 260724444, 63644.0 MB/s
Random read bypassing cache (128-bit), size = 2 kB, loops = 162955264, 63645.2 MB/s
Random read bypassing cache (128-bit), size = 3 kB, loops = 108635185, 63644.4 MB/s
Random read bypassing cache (128-bit), size = 4 kB, loops = 81477632, 63646.5 MB/s
Random read bypassing cache (128-bit), size = 6 kB, loops = 54315106, 63647.2 MB/s
Random read bypassing cache (128-bit), size = 8 kB, loops = 41000960, 64052.3 MB/s
Random read bypassing cache (128-bit), size = 12 kB, loops = 26671524, 62504.5 MB/s
Random read bypassing cache (128-bit), size = 16 kB, loops = 20242432, 63247.3 MB/s
Random read bypassing cache (128-bit), size = 20 kB, loops = 16137576, 63026.6 MB/s
Random read bypassing cache (128-bit), size = 24 kB, loops = 13548990, 63504.2 MB/s
Random read bypassing cache (128-bit), size = 28 kB, loops = 11594700, 63399.9 MB/s
Random read bypassing cache (128-bit), size = 32 kB, loops = 9396224, 58716.4 MB/s
Random read bypassing cache (128-bit), size = 34 kB, loops = 8133867, 54008.1 MB/s
Random read bypassing cache (128-bit), size = 36 kB, loops = 6799520, 47808.4 MB/s
Random read bypassing cache (128-bit), size = 40 kB, loops = 5831280, 45556.4 MB/s
Random read bypassing cache (128-bit), size = 48 kB, loops = 4732455, 44356.0 MB/s
Random read bypassing cache (128-bit), size = 64 kB, loops = 3490816, 43632.0 MB/s
Random read bypassing cache (128-bit), size = 128 kB, loops = 1719296, 42970.2 MB/s
Random read bypassing cache (128-bit), size = 192 kB, loops = 1138599, 42688.4 MB/s
Random read bypassing cache (128-bit), size = 256 kB, loops = 774912, 38736.2 MB/s
Random read bypassing cache (128-bit), size = 320 kB, loops = 452676, 28286.3 MB/s
Random read bypassing cache (128-bit), size = 384 kB, loops = 363460, 27258.8 MB/s
Random read bypassing cache (128-bit), size = 512 kB, loops = 261632, 26150.8 MB/s
Random read bypassing cache (128-bit), size = 768 kB, loops = 167195, 25073.7 MB/s
Random read bypassing cache (128-bit), size = 1 MB, loops = 124096, 24815.2 MB/s
Random read bypassing cache (128-bit), size = 1.25 MB, loops = 98583, 24635.2 MB/s
Random read bypassing cache (128-bit), size = 1.5 MB, loops = 81648, 24483.2 MB/s
Random read bypassing cache (128-bit), size = 1.75 MB, loops = 69372, 24280.1 MB/s
Random read bypassing cache (128-bit), size = 2 MB, loops = 60864, 24334.9 MB/s
Random read bypassing cache (128-bit), size = 2.25 MB, loops = 53900, 24249.7 MB/s
Random read bypassing cache (128-bit), size = 2.5 MB, loops = 48475, 24225.6 MB/s
Random read bypassing cache (128-bit), size = 2.75 MB, loops = 43792, 24085.4 MB/s
Random read bypassing cache (128-bit), size = 3 MB, loops = 40257, 24153.8 MB/s
Random read bypassing cache (128-bit), size = 3.25 MB, loops = 37145, 24138.4 MB/s
Random read bypassing cache (128-bit), size = 3.5 MB, loops = 34434, 24102.1 MB/s
Random read bypassing cache (128-bit), size = 4 MB, loops = 34576, 27654.5 MB/s
Random read bypassing cache (128-bit), size = 5 MB, loops = 26952, 26941.5 MB/s
Random read bypassing cache (128-bit), size = 6 MB, loops = 23010, 27607.4 MB/s
Random read bypassing cache (128-bit), size = 7 MB, loops = 18783, 26289.3 MB/s
Random read bypassing cache (128-bit), size = 8 MB, loops = 11472, 18353.9 MB/s
Random read bypassing cache (128-bit), size = 9 MB, loops = 7343, 13205.4 MB/s
Random read bypassing cache (128-bit), size = 10 MB, loops = 5964, 11916.7 MB/s
Random read bypassing cache (128-bit), size = 12 MB, loops = 4285, 10278.7 MB/s
Random read bypassing cache (128-bit), size = 14 MB, loops = 3328, 9314.8 MB/s
Random read bypassing cache (128-bit), size = 15 MB, loops = 2984, 8943.8 MB/s
Random read bypassing cache (128-bit), size = 16 MB, loops = 2708, 8658.4 MB/s
Random read bypassing cache (128-bit), size = 20 MB, loops = 1956, 7819.2 MB/s
Random read bypassing cache (128-bit), size = 21 MB, loops = 1842, 7727.4 MB/s
Random read bypassing cache (128-bit), size = 32 MB, loops = 1072, 6852.2 MB/s
Random read bypassing cache (128-bit), size = 48 MB, loops = 659, 6325.6 MB/s
Random read bypassing cache (128-bit), size = 64 MB, loops = 473, 6053.1 MB/s
Random read bypassing cache (128-bit), size = 72 MB, loops = 412, 5924.7 MB/s
Random read bypassing cache (128-bit), size = 96 MB, loops = 298, 5715.5 MB/s
Random read bypassing cache (128-bit), size = 128 MB, loops = 219, 5591.7 MB/s

Sequential write bypassing cache (128-bit), size = 128 B, loops = 166723584, 4059.6 MB/s
Sequential write bypassing cache (128-bit), size = 256 B, loops = 170917888, 8340.2 MB/s
Sequential write bypassing cache (128-bit), size = 384 B, loops = 166373424, 12185.4 MB/s
Sequential write bypassing cache (128-bit), size = 512 B, loops = 164626432, 16076.6 MB/s
Sequential write bypassing cache (128-bit), size = 640 B, loops = 150260081, 18331.0 MB/s
Sequential write bypassing cache (128-bit), size = 768 B, loops = 124867449, 18280.3 MB/s
Sequential write bypassing cache (128-bit), size = 896 B, loops = 109650672, 18730.4 MB/s
Sequential write bypassing cache (128-bit), size = 1024 B, loops = 96337920, 18808.1 MB/s
Sequential write bypassing cache (128-bit), size = 1280 B, loops = 77069160, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 2 kB, loops = 48168960, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 3 kB, loops = 32112150, 18806.4 MB/s
Sequential write bypassing cache (128-bit), size = 4 kB, loops = 24084480, 18806.2 MB/s
Sequential write bypassing cache (128-bit), size = 6 kB, loops = 16055340, 18808.3 MB/s
Sequential write bypassing cache (128-bit), size = 8 kB, loops = 12042240, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 12 kB, loops = 8027670, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 16 kB, loops = 6021120, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 20 kB, loops = 4815720, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 24 kB, loops = 4013100, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 28 kB, loops = 3439800, 18808.2 MB/s
Sequential write bypassing cache (128-bit), size = 32 kB, loops = 3010560, 18808.1 MB/s
Sequential write bypassing cache (128-bit), size = 34 kB, loops = 2832690, 18808.4 MB/s
Sequential write bypassing cache (128-bit), size = 36 kB, loops = 2675400, 18808.4 MB/s
Sequential write bypassing cache (128-bit), size = 40 kB, loops = 2407860, 18808.5 MB/s
Sequential write bypassing cache (128-bit), size = 48 kB, loops = 2006550, 18808.5 MB/s
Sequential write bypassing cache (128-bit), size = 64 kB, loops = 1505280, 18808.3 MB/s
Sequential write bypassing cache (128-bit), size = 128 kB, loops = 752640, 18809.0 MB/s
Sequential write bypassing cache (128-bit), size = 192 kB, loops = 501611, 18809.5 MB/s
Sequential write bypassing cache (128-bit), size = 256 kB, loops = 376320, 18810.3 MB/s
Sequential write bypassing cache (128-bit), size = 320 kB, loops = 301104, 18810.5 MB/s
Sequential write bypassing cache (128-bit), size = 384 kB, loops = 250920, 18810.6 MB/s
Sequential write bypassing cache (128-bit), size = 512 kB, loops = 188160, 18810.6 MB/s
Sequential write bypassing cache (128-bit), size = 768 kB, loops = 125460, 18810.6 MB/s
Sequential write bypassing cache (128-bit), size = 1 MB, loops = 94080, 18808.7 MB/s
Sequential write bypassing cache (128-bit), size = 1.25 MB, loops = 75276, 18810.6 MB/s
Sequential write bypassing cache (128-bit), size = 1.5 MB, loops = 62706, 18810.5 MB/s
Sequential write bypassing cache (128-bit), size = 1.75 MB, loops = 53748, 18810.5 MB/s
Sequential write bypassing cache (128-bit), size = 2 MB, loops = 47040, 18808.7 MB/s
Sequential write bypassing cache (128-bit), size = 2.25 MB, loops = 41804, 18810.3 MB/s
Sequential write bypassing cache (128-bit), size = 2.5 MB, loops = 37625, 18810.3 MB/s
Sequential write bypassing cache (128-bit), size = 2.75 MB, loops = 34201, 18809.4 MB/s
Sequential write bypassing cache (128-bit), size = 3 MB, loops = 31353, 18808.4 MB/s
Sequential write bypassing cache (128-bit), size = 3.25 MB, loops = 28937, 18808.4 MB/s
Sequential write bypassing cache (128-bit), size = 3.5 MB, loops = 26874, 18808.3 MB/s
Sequential write bypassing cache (128-bit), size = 4 MB, loops = 23520, 18805.9 MB/s
Sequential write bypassing cache (128-bit), size = 5 MB, loops = 18816, 18804.4 MB/s
Sequential write bypassing cache (128-bit), size = 6 MB, loops = 15680, 18805.3 MB/s
Sequential write bypassing cache (128-bit), size = 7 MB, loops = 13437, 18804.5 MB/s
Sequential write bypassing cache (128-bit), size = 8 MB, loops = 11752, 18801.8 MB/s
Sequential write bypassing cache (128-bit), size = 9 MB, loops = 10451, 18802.6 MB/s
Sequential write bypassing cache (128-bit), size = 10 MB, loops = 9402, 18801.7 MB/s
Sequential write bypassing cache (128-bit), size = 12 MB, loops = 7835, 18799.7 MB/s
Sequential write bypassing cache (128-bit), size = 14 MB, loops = 6716, 18797.3 MB/s
Sequential write bypassing cache (128-bit), size = 15 MB, loops = 6268, 18797.1 MB/s
Sequential write bypassing cache (128-bit), size = 16 MB, loops = 5876, 18796.4 MB/s
Sequential write bypassing cache (128-bit), size = 20 MB, loops = 4701, 18792.6 MB/s
Sequential write bypassing cache (128-bit), size = 21 MB, loops = 4476, 18789.9 MB/s
Sequential write bypassing cache (128-bit), size = 32 MB, loops = 2936, 18781.2 MB/s
Sequential write bypassing cache (128-bit), size = 48 MB, loops = 1955, 18766.3 MB/s
Sequential write bypassing cache (128-bit), size = 64 MB, loops = 1465, 18750.4 MB/s
Sequential write bypassing cache (128-bit), size = 72 MB, loops = 1302, 18744.4 MB/s
Sequential write bypassing cache (128-bit), size = 96 MB, loops = 976, 18722.1 MB/s
Sequential write bypassing cache (128-bit), size = 128 MB, loops = 731, 18692.7 MB/s

Sequential write bypassing cache (256-bit), size = 256 B, loops = 2117337088, 103383.9 MB/s
Sequential write bypassing cache (256-bit), size = 512 B, loops = 1058930688, 103399.1 MB/s
Sequential write bypassing cache (256-bit), size = 768 B, loops = 40020498, 5851.7 MB/s
Sequential write bypassing cache (256-bit), size = 1024 B, loops = 21299200, 4158.3 MB/s
Sequential write bypassing cache (256-bit), size = 1280 B, loops = 17091528, 4162.3 MB/s
Sequential write bypassing cache (256-bit), size = 2 kB, loops = 10321920, 4025.3 MB/s
Sequential write bypassing cache (256-bit), size = 3 kB, loops = 7012245, 4105.7 MB/s
Sequential write bypassing cache (256-bit), size = 4 kB, loops = 5210112, 4065.0 MB/s
Sequential write bypassing cache (256-bit), size = 6 kB, loops = 3505962, 4105.9 MB/s
Sequential write bypassing cache (256-bit), size = 8 kB, loops = 2564096, 4004.5 MB/s
Sequential write bypassing cache (256-bit), size = 12 kB, loops = 1758442, 4117.0 MB/s
Sequential write bypassing cache (256-bit), size = 16 kB, loops = 1302528, 4061.5 MB/s
Sequential write bypassing cache (256-bit), size = 20 kB, loops = 1061424, 4139.3 MB/s
Sequential write bypassing cache (256-bit), size = 24 kB, loops = 868140, 4059.1 MB/s
Sequential write bypassing cache (256-bit), size = 28 kB, loops = 753480, 4117.7 MB/s
Sequential write bypassing cache (256-bit), size = 32 kB, loops = 643072, 4017.3 MB/s
Sequential write bypassing cache (256-bit), size = 34 kB, loops = 614713, 4077.1 MB/s
Sequential write bypassing cache (256-bit), size = 36 kB, loops = 591500, 4150.9 MB/s
Sequential write bypassing cache (256-bit), size = 40 kB, loops = 532350, 4150.6 MB/s
Sequential write bypassing cache (256-bit), size = 48 kB, loops = 431340, 4042.9 MB/s
Sequential write bypassing cache (256-bit), size = 64 kB, loops = 322560, 4023.6 MB/s
Sequential write bypassing cache (256-bit), size = 128 kB, loops = 161280, 4026.1 MB/s
Sequential write bypassing cache (256-bit), size = 192 kB, loops = 110484, 4135.8 MB/s
Sequential write bypassing cache (256-bit), size = 256 kB, loops = 82944, 4143.3 MB/s
Sequential write bypassing cache (256-bit), size = 320 kB, loops = 66300, 4142.5 MB/s
Sequential write bypassing cache (256-bit), size = 384 kB, loops = 55250, 4140.8 MB/s
Sequential write bypassing cache (256-bit), size = 512 kB, loops = 41472, 4142.0 MB/s
Sequential write bypassing cache (256-bit), size = 768 kB, loops = 26860, 4026.8 MB/s
Sequential write bypassing cache (256-bit), size = 1 MB, loops = 20160, 4024.0 MB/s
Sequential write bypassing cache (256-bit), size = 1.25 MB, loops = 16269, 4066.7 MB/s
Sequential write bypassing cache (256-bit), size = 1.5 MB, loops = 13902, 4161.4 MB/s
Sequential write bypassing cache (256-bit), size = 1.75 MB, loops = 11916, 4161.3 MB/s
Sequential write bypassing cache (256-bit), size = 2 MB, loops = 10368, 4143.3 MB/s
Sequential write bypassing cache (256-bit), size = 2.25 MB, loops = 9212, 4139.8 MB/s
Sequential write bypassing cache (256-bit), size = 2.5 MB, loops = 8300, 4140.0 MB/s
Sequential write bypassing cache (256-bit), size = 2.75 MB, loops = 7452, 4096.5 MB/s
Sequential write bypassing cache (256-bit), size = 3 MB, loops = 6783, 4066.2 MB/s
Sequential write bypassing cache (256-bit), size = 3.25 MB, loops = 6289, 4076.5 MB/s
Sequential write bypassing cache (256-bit), size = 3.5 MB, loops = 5904, 4130.7 MB/s
Sequential write bypassing cache (256-bit), size = 4 MB, loops = 5056, 4039.1 MB/s
Sequential write bypassing cache (256-bit), size = 5 MB, loops = 4152, 4141.0 MB/s
Sequential write bypassing cache (256-bit), size = 6 MB, loops = 3470, 4158.6 MB/s
Sequential write bypassing cache (256-bit), size = 7 MB, loops = 2970, 4154.6 MB/s
Sequential write bypassing cache (256-bit), size = 8 MB, loops = 2608, 4160.2 MB/s
Sequential write bypassing cache (256-bit), size = 9 MB, loops = 2317, 4160.0 MB/s
Sequential write bypassing cache (256-bit), size = 10 MB, loops = 2082, 4162.8 MB/s
Sequential write bypassing cache (256-bit), size = 12 MB, loops = 1710, 4102.7 MB/s
Sequential write bypassing cache (256-bit), size = 14 MB, loops = 1476, 4126.3 MB/s
Sequential write bypassing cache (256-bit), size = 15 MB, loops = 1376, 4119.9 MB/s
Sequential write bypassing cache (256-bit), size = 16 MB, loops = 1260, 4021.2 MB/s
Sequential write bypassing cache (256-bit), size = 20 MB, loops = 1011, 4037.2 MB/s
Sequential write bypassing cache (256-bit), size = 21 MB, loops = 987, 4135.9 MB/s
Sequential write bypassing cache (256-bit), size = 32 MB, loops = 632, 4032.0 MB/s
Sequential write bypassing cache (256-bit), size = 48 MB, loops = 419, 4018.9 MB/s
Sequential write bypassing cache (256-bit), size = 64 MB, loops = 322, 4111.6 MB/s
Sequential write bypassing cache (256-bit), size = 72 MB, loops = 287, 4130.1 MB/s
Sequential write bypassing cache (256-bit), size = 96 MB, loops = 213, 4083.3 MB/s
Sequential write bypassing cache (256-bit), size = 128 MB, loops = 159, 4069.7 MB/s

Random write bypassing cache (128-bit), size = 256 B, loops = 169869312, 8287.4 MB/s
Random write bypassing cache (128-bit), size = 512 B, loops = 134217728, 13104.3 MB/s
Random write bypassing cache (128-bit), size = 768 B, loops = 90701478, 13276.5 MB/s
Random write bypassing cache (128-bit), size = 1024 B, loops = 67239936, 13129.0 MB/s
Random write bypassing cache (128-bit), size = 1280 B, loops = 57303804, 13979.6 MB/s
Random write bypassing cache (128-bit), size = 2 kB, loops = 37584896, 14676.5 MB/s
Random write bypassing cache (128-bit), size = 3 kB, loops = 25143595, 14724.3 MB/s
Random write bypassing cache (128-bit), size = 4 kB, loops = 18841600, 14715.9 MB/s
Random write bypassing cache (128-bit), size = 6 kB, loops = 12538456, 14681.0 MB/s
Random write bypassing cache (128-bit), size = 8 kB, loops = 9412608, 14704.6 MB/s
Random write bypassing cache (128-bit), size = 12 kB, loops = 6274689, 14699.1 MB/s
Random write bypassing cache (128-bit), size = 16 kB, loops = 4710400, 14716.9 MB/s
Random write bypassing cache (128-bit), size = 20 kB, loops = 3767400, 14704.8 MB/s
Random write bypassing cache (128-bit), size = 24 kB, loops = 3139500, 14704.6 MB/s
Random write bypassing cache (128-bit), size = 28 kB, loops = 2688660, 14693.3 MB/s
Random write bypassing cache (128-bit), size = 32 kB, loops = 2353152, 14698.7 MB/s
Random write bypassing cache (128-bit), size = 34 kB, loops = 2216050, 14708.8 MB/s
Random write bypassing cache (128-bit), size = 36 kB, loops = 2091180, 14700.0 MB/s
Random write bypassing cache (128-bit), size = 40 kB, loops = 1883700, 14709.9 MB/s
Random write bypassing cache (128-bit), size = 48 kB, loops = 1568385, 14697.9 MB/s
Random write bypassing cache (128-bit), size = 64 kB, loops = 1176576, 14698.4 MB/s
Random write bypassing cache (128-bit), size = 128 kB, loops = 588800, 14709.0 MB/s
Random write bypassing cache (128-bit), size = 192 kB, loops = 392150, 14705.4 MB/s
Random write bypassing cache (128-bit), size = 256 kB, loops = 294400, 14708.9 MB/s
Random write bypassing cache (128-bit), size = 320 kB, loops = 235416, 14703.1 MB/s
Random write bypassing cache (128-bit), size = 384 kB, loops = 196010, 14699.1 MB/s
Random write bypassing cache (128-bit), size = 512 kB, loops = 147072, 14703.7 MB/s
Random write bypassing cache (128-bit), size = 768 kB, loops = 97920, 14680.7 MB/s
Random write bypassing cache (128-bit), size = 1 MB, loops = 73536, 14706.2 MB/s
Random write bypassing cache (128-bit), size = 1.25 MB, loops = 58854, 14708.6 MB/s
Random write bypassing cache (128-bit), size = 1.5 MB, loops = 49056, 14708.8 MB/s
Random write bypassing cache (128-bit), size = 1.75 MB, loops = 42048, 14706.5 MB/s
Random write bypassing cache (128-bit), size = 2 MB, loops = 36800, 14709.8 MB/s
Random write bypassing cache (128-bit), size = 2.25 MB, loops = 32676, 14702.4 MB/s
Random write bypassing cache (128-bit), size = 2.5 MB, loops = 29425, 14703.0 MB/s
Random write bypassing cache (128-bit), size = 2.75 MB, loops = 26726, 14694.7 MB/s
Random write bypassing cache (128-bit), size = 3 MB, loops = 24507, 14693.1 MB/s
Random write bypassing cache (128-bit), size = 3.25 MB, loops = 22629, 14706.7 MB/s
Random write bypassing cache (128-bit), size = 3.5 MB, loops = 21006, 14696.0 MB/s
Random write bypassing cache (128-bit), size = 4 MB, loops = 18384, 14700.8 MB/s
Random write bypassing cache (128-bit), size = 5 MB, loops = 14712, 14700.8 MB/s
Random write bypassing cache (128-bit), size = 6 MB, loops = 12260, 14700.1 MB/s
Random write bypassing cache (128-bit), size = 7 MB, loops = 10494, 14686.3 MB/s
Random write bypassing cache (128-bit), size = 8 MB, loops = 9184, 14686.6 MB/s
Random write bypassing cache (128-bit), size = 9 MB, loops = 8155, 14677.7 MB/s
Random write bypassing cache (128-bit), size = 10 MB, loops = 7350, 14691.6 MB/s
Random write bypassing cache (128-bit), size = 12 MB, loops = 6120, 14687.8 MB/s
Random write bypassing cache (128-bit), size = 14 MB, loops = 5248, 14684.0 MB/s
Random write bypassing cache (128-bit), size = 15 MB, loops = 4892, 14672.2 MB/s
Random write bypassing cache (128-bit), size = 16 MB, loops = 4584, 14665.8 MB/s
Random write bypassing cache (128-bit), size = 20 MB, loops = 3672, 14680.0 MB/s
Random write bypassing cache (128-bit), size = 21 MB, loops = 3498, 14681.6 MB/s
Random write bypassing cache (128-bit), size = 32 MB, loops = 2294, 14672.1 MB/s
Random write bypassing cache (128-bit), size = 48 MB, loops = 1527, 14654.3 MB/s
Random write bypassing cache (128-bit), size = 64 MB, loops = 1144, 14639.2 MB/s
Random write bypassing cache (128-bit), size = 72 MB, loops = 1016, 14626.8 MB/s
Random write bypassing cache (128-bit), size = 96 MB, loops = 761, 14597.5 MB/s
Random write bypassing cache (128-bit), size = 128 MB, loops = 570, 14576.0 MB/s

Sequential read (64-bit), size = 128 B, loops = 2117074944, 51683.5 MB/s
Sequential read (64-bit), size = 256 B, loops = 1059586048, 51725.7 MB/s
Sequential read (64-bit), size = 384 B, loops = 706213242, 51714.1 MB/s
Sequential read (64-bit), size = 512 B, loops = 529661952, 51714.7 MB/s
Sequential read (64-bit), size = 640 B, loops = 423727137, 51713.9 MB/s
Sequential read (64-bit), size = 768 B, loops = 353106621, 51714.5 MB/s
Sequential read (64-bit), size = 896 B, loops = 302662818, 51713.5 MB/s
Sequential read (64-bit), size = 1024 B, loops = 264830976, 51714.7 MB/s
Sequential read (64-bit), size = 1280 B, loops = 211756692, 51690.2 MB/s
Sequential read (64-bit), size = 2 kB, loops = 132349952, 51690.1 MB/s
Sequential read (64-bit), size = 3 kB, loops = 88275645, 51715.2 MB/s
Sequential read (64-bit), size = 4 kB, loops = 66207744, 51714.8 MB/s
Sequential read (64-bit), size = 6 kB, loops = 44103036, 51677.9 MB/s
Sequential read (64-bit), size = 8 kB, loops = 33021952, 51587.4 MB/s
Sequential read (64-bit), size = 12 kB, loops = 21603716, 50622.3 MB/s
Sequential read (64-bit), size = 16 kB, loops = 16269312, 50841.4 MB/s
Sequential read (64-bit), size = 20 kB, loops = 12999168, 50770.6 MB/s
Sequential read (64-bit), size = 24 kB, loops = 10895430, 51062.2 MB/s
Sequential read (64-bit), size = 28 kB, loops = 9348300, 51122.9 MB/s
Sequential read (64-bit), size = 32 kB, loops = 8138752, 50865.9 MB/s
Sequential read (64-bit), size = 34 kB, loops = 6694398, 44443.2 MB/s
Sequential read (64-bit), size = 36 kB, loops = 6027840, 42375.5 MB/s
Sequential read (64-bit), size = 40 kB, loops = 5411952, 42274.2 MB/s
Sequential read (64-bit), size = 48 kB, loops = 4522245, 42387.7 MB/s
Sequential read (64-bit), size = 64 kB, loops = 3387392, 42332.6 MB/s
Sequential read (64-bit), size = 128 kB, loops = 1696768, 42411.7 MB/s
Sequential read (64-bit), size = 192 kB, loops = 1126664, 42243.4 MB/s
Sequential read (64-bit), size = 256 kB, loops = 840192, 42002.7 MB/s
Sequential read (64-bit), size = 320 kB, loops = 544272, 34005.1 MB/s
Sequential read (64-bit), size = 384 kB, loops = 453560, 34010.0 MB/s
Sequential read (64-bit), size = 512 kB, loops = 340096, 33998.2 MB/s
Sequential read (64-bit), size = 768 kB, loops = 226695, 33995.3 MB/s
Sequential read (64-bit), size = 1 MB, loops = 169984, 33992.3 MB/s
Sequential read (64-bit), size = 1.25 MB, loops = 136782, 34184.2 MB/s
Sequential read (64-bit), size = 1.5 MB, loops = 113400, 34010.0 MB/s
Sequential read (64-bit), size = 1.75 MB, loops = 97524, 34131.1 MB/s
Sequential read (64-bit), size = 2 MB, loops = 84992, 33991.9 MB/s
Sequential read (64-bit), size = 2.25 MB, loops = 75544, 33990.5 MB/s
Sequential read (64-bit), size = 2.5 MB, loops = 68000, 33992.1 MB/s
Sequential read (64-bit), size = 2.75 MB, loops = 61824, 33992.7 MB/s
Sequential read (64-bit), size = 3 MB, loops = 56658, 33994.0 MB/s
Sequential read (64-bit), size = 3.25 MB, loops = 52307, 33989.0 MB/s
Sequential read (64-bit), size = 3.5 MB, loops = 48564, 33988.5 MB/s
Sequential read (64-bit), size = 4 MB, loops = 42288, 33821.7 MB/s
Sequential read (64-bit), size = 5 MB, loops = 33852, 33849.5 MB/s
Sequential read (64-bit), size = 6 MB, loops = 28190, 33823.0 MB/s
Sequential read (64-bit), size = 7 MB, loops = 24183, 33844.5 MB/s
Sequential read (64-bit), size = 8 MB, loops = 20216, 32342.0 MB/s
Sequential read (64-bit), size = 9 MB, loops = 12873, 23165.1 MB/s
Sequential read (64-bit), size = 10 MB, loops = 11142, 22279.2 MB/s
Sequential read (64-bit), size = 12 MB, loops = 8530, 20460.1 MB/s
Sequential read (64-bit), size = 14 MB, loops = 6768, 18943.2 MB/s
Sequential read (64-bit), size = 15 MB, loops = 6140, 18413.4 MB/s
Sequential read (64-bit), size = 16 MB, loops = 5664, 18120.7 MB/s
Sequential read (64-bit), size = 20 MB, loops = 4398, 17583.5 MB/s
Sequential read (64-bit), size = 21 MB, loops = 4170, 17502.7 MB/s
Sequential read (64-bit), size = 32 MB, loops = 2648, 16941.1 MB/s
Sequential read (64-bit), size = 48 MB, loops = 1742, 16717.9 MB/s
Sequential read (64-bit), size = 64 MB, loops = 1296, 16587.6 MB/s
Sequential read (64-bit), size = 72 MB, loops = 1146, 16488.9 MB/s
Sequential read (64-bit), size = 96 MB, loops = 858, 16469.0 MB/s
Sequential read (64-bit), size = 128 MB, loops = 642, 16417.8 MB/s

Random read (64-bit), size = 256 B, loops = 807141376, 39410.3 MB/s
Random read (64-bit), size = 512 B, loops = 403570688, 39403.5 MB/s
Random read (64-bit), size = 768 B, loops = 268958718, 39388.5 MB/s
Random read (64-bit), size = 1024 B, loops = 201719808, 39387.7 MB/s
Random read (64-bit), size = 1280 B, loops = 161425812, 39402.2 MB/s
Random read (64-bit), size = 2 kB, loops = 100892672, 39402.3 MB/s
Random read (64-bit), size = 3 kB, loops = 67260755, 39403.6 MB/s
Random read (64-bit), size = 4 kB, loops = 50446336, 39403.6 MB/s
Random read (64-bit), size = 6 kB, loops = 33628838, 39403.5 MB/s
Random read (64-bit), size = 8 kB, loops = 25133056, 39262.3 MB/s
Random read (64-bit), size = 12 kB, loops = 16612362, 38922.8 MB/s
Random read (64-bit), size = 16 kB, loops = 12484608, 39013.2 MB/s
Random read (64-bit), size = 20 kB, loops = 9985248, 38992.7 MB/s
Random read (64-bit), size = 24 kB, loops = 8342880, 39101.0 MB/s
Random read (64-bit), size = 28 kB, loops = 7134660, 39008.3 MB/s
Random read (64-bit), size = 32 kB, loops = 5705728, 35658.7 MB/s
Random read (64-bit), size = 34 kB, loops = 4780887, 31739.7 MB/s
Random read (64-bit), size = 36 kB, loops = 3892980, 27369.0 MB/s
Random read (64-bit), size = 40 kB, loops = 3474198, 27133.7 MB/s
Random read (64-bit), size = 48 kB, loops = 2809170, 26326.6 MB/s
Random read (64-bit), size = 64 kB, loops = 2083840, 26045.8 MB/s
Random read (64-bit), size = 128 kB, loops = 1036288, 25901.4 MB/s
Random read (64-bit), size = 192 kB, loops = 687115, 25760.4 MB/s
Random read (64-bit), size = 256 kB, loops = 469504, 23472.2 MB/s
Random read (64-bit), size = 320 kB, loops = 276828, 17292.7 MB/s
Random read (64-bit), size = 384 kB, loops = 215560, 16165.1 MB/s
Random read (64-bit), size = 512 kB, loops = 153472, 15343.0 MB/s
Random read (64-bit), size = 768 kB, loops = 97580, 14627.5 MB/s
Random read (64-bit), size = 1 MB, loops = 70464, 14081.7 MB/s
Random read (64-bit), size = 1.25 MB, loops = 56100, 14014.8 MB/s
Random read (64-bit), size = 1.5 MB, loops = 45948, 13777.0 MB/s
Random read (64-bit), size = 1.75 MB, loops = 39096, 13676.4 MB/s
Random read (64-bit), size = 2 MB, loops = 34304, 13714.6 MB/s
Random read (64-bit), size = 2.25 MB, loops = 29988, 13484.1 MB/s
Random read (64-bit), size = 2.5 MB, loops = 27200, 13593.2 MB/s
Random read (64-bit), size = 2.75 MB, loops = 24702, 13577.4 MB/s
Random read (64-bit), size = 3 MB, loops = 22575, 13543.4 MB/s
Random read (64-bit), size = 3.25 MB, loops = 20824, 13524.6 MB/s
Random read (64-bit), size = 3.5 MB, loops = 19314, 13511.7 MB/s
Random read (64-bit), size = 4 MB, loops = 18960, 15161.1 MB/s
Random read (64-bit), size = 5 MB, loops = 14700, 14692.1 MB/s
Random read (64-bit), size = 6 MB, loops = 12570, 15076.0 MB/s
Random read (64-bit), size = 7 MB, loops = 10314, 14432.7 MB/s
Random read (64-bit), size = 8 MB, loops = 7352, 11760.1 MB/s
Random read (64-bit), size = 9 MB, loops = 4676, 8413.3 MB/s
Random read (64-bit), size = 10 MB, loops = 3774, 7537.0 MB/s
Random read (64-bit), size = 12 MB, loops = 2720, 6527.8 MB/s
Random read (64-bit), size = 14 MB, loops = 2120, 5930.6 MB/s
Random read (64-bit), size = 15 MB, loops = 1904, 5711.8 MB/s
Random read (64-bit), size = 16 MB, loops = 1740, 5556.3 MB/s
Random read (64-bit), size = 20 MB, loops = 1260, 5034.4 MB/s
Random read (64-bit), size = 21 MB, loops = 1182, 4957.7 MB/s
Random read (64-bit), size = 32 MB, loops = 672, 4290.4 MB/s
Random read (64-bit), size = 48 MB, loops = 400, 3833.7 MB/s
Random read (64-bit), size = 64 MB, loops = 280, 3580.3 MB/s
Random read (64-bit), size = 72 MB, loops = 244, 3506.7 MB/s
Random read (64-bit), size = 96 MB, loops = 173, 3316.0 MB/s
Random read (64-bit), size = 128 MB, loops = 124, 3160.8 MB/s

Sequential write (64-bit), size = 128 B, loops = 1059586048, 25864.3 MB/s
Sequential write (64-bit), size = 256 B, loops = 529793024, 25864.7 MB/s
Sequential write (64-bit), size = 384 B, loops = 353194002, 25860.7 MB/s
Sequential write (64-bit), size = 512 B, loops = 264896512, 25858.7 MB/s
Sequential write (64-bit), size = 640 B, loops = 211915997, 25856.6 MB/s
Sequential write (64-bit), size = 768 B, loops = 176509620, 25855.6 MB/s
Sequential write (64-bit), size = 896 B, loops = 151368858, 25858.3 MB/s
Sequential write (64-bit), size = 1024 B, loops = 132448256, 25859.1 MB/s
Sequential write (64-bit), size = 1280 B, loops = 105956988, 25860.2 MB/s
Sequential write (64-bit), size = 2 kB, loops = 66191360, 25848.4 MB/s
Sequential write (64-bit), size = 3 kB, loops = 44148745, 25860.1 MB/s
Sequential write (64-bit), size = 4 kB, loops = 33112064, 25860.3 MB/s
Sequential write (64-bit), size = 6 kB, loops = 22073362, 25860.1 MB/s
Sequential write (64-bit), size = 8 kB, loops = 16556032, 25856.9 MB/s
Sequential write (64-bit), size = 12 kB, loops = 11020298, 25828.5 MB/s
Sequential write (64-bit), size = 16 kB, loops = 8273920, 25846.3 MB/s
Sequential write (64-bit), size = 20 kB, loops = 6614244, 25831.9 MB/s
Sequential write (64-bit), size = 24 kB, loops = 5514600, 25849.4 MB/s
Sequential write (64-bit), size = 28 kB, loops = 4726800, 25846.1 MB/s
Sequential write (64-bit), size = 32 kB, loops = 4136960, 25843.7 MB/s
Sequential write (64-bit), size = 34 kB, loops = 3609271, 23962.7 MB/s
Sequential write (64-bit), size = 36 kB, loops = 3263260, 22936.6 MB/s
Sequential write (64-bit), size = 40 kB, loops = 2941848, 22982.3 MB/s
Sequential write (64-bit), size = 48 kB, loops = 2452905, 22983.3 MB/s
Sequential write (64-bit), size = 64 kB, loops = 1839104, 22984.2 MB/s
Sequential write (64-bit), size = 128 kB, loops = 919552, 22985.4 MB/s
Sequential write (64-bit), size = 192 kB, loops = 612777, 22977.7 MB/s
Sequential write (64-bit), size = 256 kB, loops = 459520, 22975.1 MB/s
Sequential write (64-bit), size = 320 kB, loops = 331296, 20704.9 MB/s
Sequential write (64-bit), size = 384 kB, loops = 275570, 20667.3 MB/s
Sequential write (64-bit), size = 512 kB, loops = 206720, 20667.2 MB/s
Sequential write (64-bit), size = 768 kB, loops = 137785, 20667.2 MB/s
Sequential write (64-bit), size = 1 MB, loops = 103360, 20667.5 MB/s
Sequential write (64-bit), size = 1.25 MB, loops = 82671, 20667.5 MB/s
Sequential write (64-bit), size = 1.5 MB, loops = 68922, 20667.6 MB/s
Sequential write (64-bit), size = 1.75 MB, loops = 59076, 20667.7 MB/s
Sequential write (64-bit), size = 2 MB, loops = 51680, 20667.7 MB/s
Sequential write (64-bit), size = 2.25 MB, loops = 45948, 20667.6 MB/s
Sequential write (64-bit), size = 2.5 MB, loops = 41350, 20667.6 MB/s
Sequential write (64-bit), size = 2.75 MB, loops = 37582, 20660.4 MB/s
Sequential write (64-bit), size = 3 MB, loops = 34461, 20667.5 MB/s
Sequential write (64-bit), size = 3.25 MB, loops = 31806, 20667.4 MB/s
Sequential write (64-bit), size = 3.5 MB, loops = 29538, 20665.4 MB/s
Sequential write (64-bit), size = 4 MB, loops = 25840, 20660.8 MB/s
Sequential write (64-bit), size = 5 MB, loops = 20664, 20660.3 MB/s
Sequential write (64-bit), size = 6 MB, loops = 17220, 20660.1 MB/s
Sequential write (64-bit), size = 7 MB, loops = 14751, 20648.8 MB/s
Sequential write (64-bit), size = 8 MB, loops = 12752, 20396.4 MB/s
Sequential write (64-bit), size = 9 MB, loops = 9821, 17670.3 MB/s
Sequential write (64-bit), size = 10 MB, loops = 8046, 16090.5 MB/s
Sequential write (64-bit), size = 12 MB, loops = 5795, 13898.6 MB/s
Sequential write (64-bit), size = 14 MB, loops = 4464, 12490.1 MB/s
Sequential write (64-bit), size = 15 MB, loops = 4004, 12009.6 MB/s
Sequential write (64-bit), size = 16 MB, loops = 3648, 11672.3 MB/s
Sequential write (64-bit), size = 20 MB, loops = 2712, 10840.2 MB/s
Sequential write (64-bit), size = 21 MB, loops = 2547, 10685.6 MB/s
Sequential write (64-bit), size = 32 MB, loops = 1600, 10229.7 MB/s
Sequential write (64-bit), size = 48 MB, loops = 1050, 10076.8 MB/s
Sequential write (64-bit), size = 64 MB, loops = 781, 9988.6 MB/s
Sequential write (64-bit), size = 72 MB, loops = 692, 9962.6 MB/s
Sequential write (64-bit), size = 96 MB, loops = 519, 9963.7 MB/s
Sequential write (64-bit), size = 128 MB, loops = 386, 9868.5 MB/s

Random write (64-bit), size = 256 B, loops = 529793024, 25864.5 MB/s
Random write (64-bit), size = 512 B, loops = 264896512, 25860.6 MB/s
Random write (64-bit), size = 768 B, loops = 176597001, 25860.5 MB/s
Random write (64-bit), size = 1024 B, loops = 132448256, 25860.4 MB/s
Random write (64-bit), size = 1280 B, loops = 105956988, 25860.0 MB/s
Random write (64-bit), size = 2 kB, loops = 66224128, 25860.0 MB/s
Random write (64-bit), size = 3 kB, loops = 44148745, 25860.5 MB/s
Random write (64-bit), size = 4 kB, loops = 31866880, 24888.4 MB/s
Random write (64-bit), size = 6 kB, loops = 21865844, 25620.2 MB/s
Random write (64-bit), size = 8 kB, loops = 16023552, 25034.4 MB/s
Random write (64-bit), size = 12 kB, loops = 10698099, 25061.7 MB/s
Random write (64-bit), size = 16 kB, loops = 8249344, 25766.5 MB/s
Random write (64-bit), size = 20 kB, loops = 6538896, 25542.6 MB/s
Random write (64-bit), size = 24 kB, loops = 5492760, 25743.1 MB/s
Random write (64-bit), size = 28 kB, loops = 4600440, 25151.7 MB/s
Random write (64-bit), size = 32 kB, loops = 3289088, 20547.9 MB/s
Random write (64-bit), size = 34 kB, loops = 2445363, 16237.5 MB/s
Random write (64-bit), size = 36 kB, loops = 1727180, 12141.7 MB/s
Random write (64-bit), size = 40 kB, loops = 1556100, 12152.5 MB/s
Random write (64-bit), size = 48 kB, loops = 1287195, 12062.3 MB/s
Random write (64-bit), size = 64 kB, loops = 965632, 12059.1 MB/s
Random write (64-bit), size = 128 kB, loops = 482816, 12060.6 MB/s
Random write (64-bit), size = 192 kB, loops = 321904, 12063.3 MB/s
Random write (64-bit), size = 256 kB, loops = 227840, 11384.4 MB/s
Random write (64-bit), size = 320 kB, loops = 96288, 6015.0 MB/s
Random write (64-bit), size = 384 kB, loops = 76330, 5722.2 MB/s
Random write (64-bit), size = 512 kB, loops = 57088, 5701.3 MB/s
Random write (64-bit), size = 768 kB, loops = 37995, 5688.5 MB/s
Random write (64-bit), size = 1 MB, loops = 28480, 5692.2 MB/s
Random write (64-bit), size = 1.25 MB, loops = 22797, 5688.4 MB/s
Random write (64-bit), size = 1.5 MB, loops = 18984, 5689.3 MB/s
Random write (64-bit), size = 1.75 MB, loops = 16272, 5688.4 MB/s
Random write (64-bit), size = 2 MB, loops = 14240, 5692.9 MB/s
Random write (64-bit), size = 2.25 MB, loops = 12656, 5691.5 MB/s
Random write (64-bit), size = 2.5 MB, loops = 11400, 5690.4 MB/s
Random write (64-bit), size = 2.75 MB, loops = 10350, 5690.2 MB/s
Random write (64-bit), size = 3 MB, loops = 9492, 5688.7 MB/s
Random write (64-bit), size = 3.25 MB, loops = 8759, 5688.9 MB/s
Random write (64-bit), size = 3.5 MB, loops = 8100, 5659.0 MB/s
Random write (64-bit), size = 4 MB, loops = 7040, 5619.9 MB/s
Random write (64-bit), size = 5 MB, loops = 5688, 5678.1 MB/s
Random write (64-bit), size = 6 MB, loops = 4700, 5628.3 MB/s
Random write (64-bit), size = 7 MB, loops = 4059, 5681.6 MB/s
Random write (64-bit), size = 8 MB, loops = 3480, 5556.6 MB/s
Random write (64-bit), size = 9 MB, loops = 3010, 5410.6 MB/s
Random write (64-bit), size = 10 MB, loops = 2622, 5236.1 MB/s
Random write (64-bit), size = 12 MB, loops = 2145, 5142.2 MB/s
Random write (64-bit), size = 14 MB, loops = 1836, 5140.3 MB/s
Random write (64-bit), size = 15 MB, loops = 1704, 5104.0 MB/s
Random write (64-bit), size = 16 MB, loops = 1588, 5078.3 MB/s
Random write (64-bit), size = 20 MB, loops = 1275, 5090.0 MB/s
Random write (64-bit), size = 21 MB, loops = 1182, 4961.8 MB/s
Random write (64-bit), size = 32 MB, loops = 744, 4752.5 MB/s
Random write (64-bit), size = 48 MB, loops = 515, 4942.6 MB/s
Random write (64-bit), size = 64 MB, loops = 387, 4942.5 MB/s
Random write (64-bit), size = 72 MB, loops = 336, 4824.9 MB/s
Random write (64-bit), size = 96 MB, loops = 246, 4719.6 MB/s
Random write (64-bit), size = 128 MB, loops = 178, 4540.8 MB/s

Sequential copy (128-bit), size = 128 B, loops = 2119172096, 51725.4 MB/s
Sequential copy (128-bit), size = 256 B, loops = 1059586048, 51725.5 MB/s
Sequential copy (128-bit), size = 384 B, loops = 706213242, 51714.5 MB/s
Sequential copy (128-bit), size = 512 B, loops = 529661952, 51714.3 MB/s
Sequential copy (128-bit), size = 640 B, loops = 423727137, 51714.6 MB/s
Sequential copy (128-bit), size = 768 B, loops = 353106621, 51714.6 MB/s
Sequential copy (128-bit), size = 896 B, loops = 302662818, 51714.0 MB/s
Sequential copy (128-bit), size = 1024 B, loops = 264830976, 51715.2 MB/s
Sequential copy (128-bit), size = 1280 B, loops = 211861548, 51714.4 MB/s
Sequential copy (128-bit), size = 2 kB, loops = 132415488, 51714.9 MB/s
Sequential copy (128-bit), size = 3 kB, loops = 88275645, 51716.5 MB/s
Sequential copy (128-bit), size = 4 kB, loops = 66207744, 51715.6 MB/s
Sequential copy (128-bit), size = 6 kB, loops = 44113958, 51690.2 MB/s
Sequential copy (128-bit), size = 8 kB, loops = 33103872, 51715.6 MB/s
Sequential copy (128-bit), size = 12 kB, loops = 22024213, 51614.8 MB/s
Sequential copy (128-bit), size = 16 kB, loops = 15405056, 48140.0 MB/s
Sequential copy (128-bit), size = 20 kB, loops = 6650280, 25971.7 MB/s
Sequential copy (128-bit), size = 24 kB, loops = 5536440, 25940.3 MB/s
Sequential copy (128-bit), size = 28 kB, loops = 4747860, 25963.1 MB/s
Sequential copy (128-bit), size = 32 kB, loops = 4157440, 25980.6 MB/s
Sequential copy (128-bit), size = 34 kB, loops = 3909883, 25958.0 MB/s
Sequential copy (128-bit), size = 36 kB, loops = 3694600, 25975.0 MB/s
Sequential copy (128-bit), size = 40 kB, loops = 3323502, 25959.0 MB/s
Sequential copy (128-bit), size = 48 kB, loops = 2768220, 25944.9 MB/s
Sequential copy (128-bit), size = 64 kB, loops = 2076672, 25949.1 MB/s
Sequential copy (128-bit), size = 128 kB, loops = 1030656, 25756.2 MB/s
Sequential copy (128-bit), size = 192 kB, loops = 429660, 16111.6 MB/s
Sequential copy (128-bit), size = 256 kB, loops = 321536, 16074.2 MB/s
Sequential copy (128-bit), size = 320 kB, loops = 257040, 16059.9 MB/s
Sequential copy (128-bit), size = 384 kB, loops = 214370, 16076.8 MB/s
Sequential copy (128-bit), size = 512 kB, loops = 160768, 16075.4 MB/s
Sequential copy (128-bit), size = 768 kB, loops = 107185, 16077.2 MB/s
Sequential copy (128-bit), size = 1 MB, loops = 80448, 16078.2 MB/s
Sequential copy (128-bit), size = 1.25 MB, loops = 64209, 16047.2 MB/s
Sequential copy (128-bit), size = 1.5 MB, loops = 53172, 15947.0 MB/s
Sequential copy (128-bit), size = 1.75 MB, loops = 45576, 15950.2 MB/s
Sequential copy (128-bit), size = 2 MB, loops = 39872, 15944.9 MB/s
Sequential copy (128-bit), size = 2.25 MB, loops = 35336, 15898.3 MB/s
Sequential copy (128-bit), size = 2.5 MB, loops = 31850, 15923.9 MB/s
Sequential copy (128-bit), size = 2.75 MB, loops = 29118, 16011.9 MB/s
Sequential copy (128-bit), size = 3 MB, loops = 26523, 15907.6 MB/s
Sequential copy (128-bit), size = 3.25 MB, loops = 24491, 15915.7 MB/s
Sequential copy (128-bit), size = 3.5 MB, loops = 22716, 15895.2 MB/s
Sequential copy (128-bit), size = 4 MB, loops = 19520, 15604.0 MB/s
Sequential copy (128-bit), size = 5 MB, loops = 10644, 10642.3 MB/s
Sequential copy (128-bit), size = 6 MB, loops = 7310, 8764.1 MB/s
Sequential copy (128-bit), size = 7 MB, loops = 4680, 6544.9 MB/s
Sequential copy (128-bit), size = 8 MB, loops = 3808, 6092.0 MB/s
Sequential copy (128-bit), size = 9 MB, loops = 3745, 6733.8 MB/s
Sequential copy (128-bit), size = 10 MB, loops = 3282, 6560.1 MB/s
Sequential copy (128-bit), size = 12 MB, loops = 2780, 6670.0 MB/s
Sequential copy (128-bit), size = 14 MB, loops = 2356, 6589.7 MB/s
Sequential copy (128-bit), size = 15 MB, loops = 1920, 5756.0 MB/s
Sequential copy (128-bit), size = 16 MB, loops = 1776, 5680.0 MB/s
Sequential copy (128-bit), size = 20 MB, loops = 1653, 6611.5 MB/s
Sequential copy (128-bit), size = 21 MB, loops = 1560, 6551.1 MB/s
Sequential copy (128-bit), size = 32 MB, loops = 870, 5566.1 MB/s
Sequential copy (128-bit), size = 48 MB, loops = 584, 5605.8 MB/s
Sequential copy (128-bit), size = 64 MB, loops = 441, 5638.2 MB/s
Sequential copy (128-bit), size = 72 MB, loops = 388, 5581.4 MB/s
Sequential copy (128-bit), size = 96 MB, loops = 292, 5602.1 MB/s
Sequential copy (128-bit), size = 128 MB, loops = 219, 5605.4 MB/s

Sequential copy (256-bit), size = 256 B, loops = 2118385664, 103432.3 MB/s
Sequential copy (256-bit), size = 512 B, loops = 1059192832, 103435.3 MB/s
Sequential copy (256-bit), size = 768 B, loops = 705601575, 103355.1 MB/s
Sequential copy (256-bit), size = 1024 B, loops = 529465344, 103406.0 MB/s
Sequential copy (256-bit), size = 1280 B, loops = 423565812, 103408.8 MB/s
Sequential copy (256-bit), size = 2 kB, loops = 264601600, 103355.3 MB/s
Sequential copy (256-bit), size = 3 kB, loops = 176398375, 103349.2 MB/s
Sequential copy (256-bit), size = 4 kB, loops = 132366336, 103403.5 MB/s
Sequential copy (256-bit), size = 6 kB, loops = 88238838, 103395.7 MB/s
Sequential copy (256-bit), size = 8 kB, loops = 66183168, 103399.0 MB/s
Sequential copy (256-bit), size = 12 kB, loops = 43917362, 102926.7 MB/s
Sequential copy (256-bit), size = 16 kB, loops = 28700672, 89684.7 MB/s
Sequential copy (256-bit), size = 20 kB, loops = 6705972, 26190.8 MB/s
Sequential copy (256-bit), size = 24 kB, loops = 5588310, 26194.7 MB/s
Sequential copy (256-bit), size = 28 kB, loops = 4792320, 26198.1 MB/s
Sequential copy (256-bit), size = 32 kB, loops = 4190208, 26188.6 MB/s
Sequential copy (256-bit), size = 34 kB, loops = 3946496, 26200.8 MB/s
Sequential copy (256-bit), size = 36 kB, loops = 3725540, 26190.5 MB/s
Sequential copy (256-bit), size = 40 kB, loops = 3351348, 26175.8 MB/s
Sequential copy (256-bit), size = 48 kB, loops = 2792790, 26179.2 MB/s
Sequential copy (256-bit), size = 64 kB, loops = 2094080, 26170.2 MB/s
Sequential copy (256-bit), size = 128 kB, loops = 1040384, 26008.4 MB/s
Sequential copy (256-bit), size = 192 kB, loops = 430683, 16138.9 MB/s
Sequential copy (256-bit), size = 256 kB, loops = 322048, 16097.0 MB/s
Sequential copy (256-bit), size = 320 kB, loops = 257652, 16096.7 MB/s
Sequential copy (256-bit), size = 384 kB, loops = 216410, 16228.1 MB/s
Sequential copy (256-bit), size = 512 kB, loops = 161408, 16136.3 MB/s
Sequential copy (256-bit), size = 768 kB, loops = 108035, 16203.2 MB/s
Sequential copy (256-bit), size = 1 MB, loops = 80704, 16136.2 MB/s
Sequential copy (256-bit), size = 1.25 MB, loops = 64923, 16229.7 MB/s
Sequential copy (256-bit), size = 1.5 MB, loops = 53970, 16188.9 MB/s
Sequential copy (256-bit), size = 1.75 MB, loops = 46044, 16112.7 MB/s
Sequential copy (256-bit), size = 2 MB, loops = 40352, 16130.8 MB/s
Sequential copy (256-bit), size = 2.25 MB, loops = 35952, 16169.5 MB/s
Sequential copy (256-bit), size = 2.5 MB, loops = 32150, 16071.6 MB/s
Sequential copy (256-bit), size = 2.75 MB, loops = 29141, 16024.7 MB/s
Sequential copy (256-bit), size = 3 MB, loops = 26733, 16027.2 MB/s
Sequential copy (256-bit), size = 3.25 MB, loops = 24662, 16029.1 MB/s
Sequential copy (256-bit), size = 3.5 MB, loops = 22914, 16030.4 MB/s
Sequential copy (256-bit), size = 4 MB, loops = 19888, 15906.2 MB/s
Sequential copy (256-bit), size = 5 MB, loops = 11256, 11254.5 MB/s
Sequential copy (256-bit), size = 6 MB, loops = 7080, 8495.7 MB/s
Sequential copy (256-bit), size = 7 MB, loops = 5616, 7854.5 MB/s
Sequential copy (256-bit), size = 8 MB, loops = 4168, 6660.2 MB/s
Sequential copy (256-bit), size = 9 MB, loops = 3570, 6420.6 MB/s
Sequential copy (256-bit), size = 10 MB, loops = 3198, 6395.0 MB/s
Sequential copy (256-bit), size = 12 MB, loops = 2470, 5918.4 MB/s
Sequential copy (256-bit), size = 14 MB, loops = 2288, 6399.4 MB/s
Sequential copy (256-bit), size = 15 MB, loops = 2156, 6468.0 MB/s
Sequential copy (256-bit), size = 16 MB, loops = 2104, 6722.0 MB/s
Sequential copy (256-bit), size = 20 MB, loops = 1476, 5897.4 MB/s
Sequential copy (256-bit), size = 21 MB, loops = 1503, 6309.2 MB/s
Sequential copy (256-bit), size = 32 MB, loops = 944, 6039.7 MB/s
Sequential copy (256-bit), size = 48 MB, loops = 614, 5889.0 MB/s
Sequential copy (256-bit), size = 64 MB, loops = 454, 5810.6 MB/s
Sequential copy (256-bit), size = 72 MB, loops = 403, 5794.1 MB/s
Sequential copy (256-bit), size = 96 MB, loops = 300, 5754.1 MB/s
Sequential copy (256-bit), size = 128 MB, loops = 224, 5729.7 MB/s

Sequential read (64-bit LODSQ), size = 128 B, loops = 214958080, 5247.2 MB/s
Sequential read (64-bit LODSQ), size = 256 B, loops = 154402816, 7532.0 MB/s
Sequential read (64-bit LODSQ), size = 384 B, loops = 119537208, 8751.4 MB/s
Sequential read (64-bit LODSQ), size = 512 B, loops = 97517568, 9520.2 MB/s
Sequential read (64-bit LODSQ), size = 640 B, loops = 82312745, 10039.9 MB/s
Sequential read (64-bit LODSQ), size = 768 B, loops = 71302896, 10437.8 MB/s
Sequential read (64-bit LODSQ), size = 896 B, loops = 62839422, 10732.5 MB/s
Sequential read (64-bit LODSQ), size = 1024 B, loops = 55967744, 10929.8 MB/s
Sequential read (64-bit LODSQ), size = 1280 B, loops = 46346352, 11305.3 MB/s
Sequential read (64-bit LODSQ), size = 2 kB, loops = 30408704, 11865.9 MB/s
Sequential read (64-bit LODSQ), size = 3 kB, loops = 20840130, 12202.0 MB/s
Sequential read (64-bit LODSQ), size = 4 kB, loops = 15843328, 12376.2 MB/s
Sequential read (64-bit LODSQ), size = 6 kB, loops = 10714482, 12555.8 MB/s
Sequential read (64-bit LODSQ), size = 8 kB, loops = 8093696, 12641.4 MB/s
Sequential read (64-bit LODSQ), size = 12 kB, loops = 5439156, 12739.8 MB/s
Sequential read (64-bit LODSQ), size = 16 kB, loops = 4096000, 12787.3 MB/s
Sequential read (64-bit LODSQ), size = 20 kB, loops = 3282552, 12816.3 MB/s
Sequential read (64-bit LODSQ), size = 24 kB, loops = 2740920, 12835.8 MB/s
Sequential read (64-bit LODSQ), size = 28 kB, loops = 2351700, 12849.4 MB/s
Sequential read (64-bit LODSQ), size = 32 kB, loops = 2058240, 12859.5 MB/s
Sequential read (64-bit LODSQ), size = 34 kB, loops = 1938562, 12863.3 MB/s
Sequential read (64-bit LODSQ), size = 36 kB, loops = 1830920, 12865.9 MB/s
Sequential read (64-bit LODSQ), size = 40 kB, loops = 1647828, 12872.3 MB/s
Sequential read (64-bit LODSQ), size = 48 kB, loops = 1374555, 12881.8 MB/s
Sequential read (64-bit LODSQ), size = 64 kB, loops = 1032192, 12894.1 MB/s
Sequential read (64-bit LODSQ), size = 128 kB, loops = 516608, 12912.4 MB/s
Sequential read (64-bit LODSQ), size = 192 kB, loops = 344751, 12918.5 MB/s
Sequential read (64-bit LODSQ), size = 256 kB, loops = 258560, 12920.5 MB/s
Sequential read (64-bit LODSQ), size = 320 kB, loops = 206856, 12922.1 MB/s
Sequential read (64-bit LODSQ), size = 384 kB, loops = 172380, 12923.7 MB/s
Sequential read (64-bit LODSQ), size = 512 kB, loops = 129280, 12925.2 MB/s
Sequential read (64-bit LODSQ), size = 768 kB, loops = 86190, 12926.8 MB/s
Sequential read (64-bit LODSQ), size = 1 MB, loops = 64640, 12927.6 MB/s
Sequential read (64-bit LODSQ), size = 1.25 MB, loops = 51714, 12927.9 MB/s
Sequential read (64-bit LODSQ), size = 1.5 MB, loops = 43134, 12928.2 MB/s
Sequential read (64-bit LODSQ), size = 1.75 MB, loops = 36936, 12922.6 MB/s
Sequential read (64-bit LODSQ), size = 2 MB, loops = 32320, 12922.7 MB/s
Sequential read (64-bit LODSQ), size = 2.25 MB, loops = 28756, 12928.7 MB/s
Sequential read (64-bit LODSQ), size = 2.5 MB, loops = 25850, 12922.8 MB/s
Sequential read (64-bit LODSQ), size = 2.75 MB, loops = 23506, 12916.8 MB/s
Sequential read (64-bit LODSQ), size = 3 MB, loops = 21567, 12928.9 MB/s
Sequential read (64-bit LODSQ), size = 3.25 MB, loops = 19893, 12922.8 MB/s
Sequential read (64-bit LODSQ), size = 3.5 MB, loops = 18468, 12922.5 MB/s
Sequential read (64-bit LODSQ), size = 4 MB, loops = 16160, 12927.0 MB/s
Sequential read (64-bit LODSQ), size = 5 MB, loops = 12924, 12921.2 MB/s
Sequential read (64-bit LODSQ), size = 6 MB, loops = 10780, 12928.7 MB/s
Sequential read (64-bit LODSQ), size = 7 MB, loops = 9234, 12927.4 MB/s
Sequential read (64-bit LODSQ), size = 8 MB, loops = 7976, 12758.5 MB/s
Sequential read (64-bit LODSQ), size = 9 MB, loops = 6720, 12092.6 MB/s
Sequential read (64-bit LODSQ), size = 10 MB, loops = 6018, 12035.7 MB/s
Sequential read (64-bit LODSQ), size = 12 MB, loops = 5020, 12040.6 MB/s
Sequential read (64-bit LODSQ), size = 14 MB, loops = 4356, 12195.4 MB/s
Sequential read (64-bit LODSQ), size = 15 MB, loops = 4108, 12319.4 MB/s
Sequential read (64-bit LODSQ), size = 16 MB, loops = 3872, 12379.5 MB/s
Sequential read (64-bit LODSQ), size = 20 MB, loops = 3108, 12426.7 MB/s
Sequential read (64-bit LODSQ), size = 21 MB, loops = 2958, 12423.3 MB/s
Sequential read (64-bit LODSQ), size = 32 MB, loops = 1938, 12392.1 MB/s
Sequential read (64-bit LODSQ), size = 48 MB, loops = 1286, 12337.5 MB/s
Sequential read (64-bit LODSQ), size = 64 MB, loops = 965, 12340.9 MB/s
Sequential read (64-bit LODSQ), size = 72 MB, loops = 860, 12371.7 MB/s
Sequential read (64-bit LODSQ), size = 96 MB, loops = 644, 12356.5 MB/s
Sequential read (64-bit LODSQ), size = 128 MB, loops = 483, 12363.1 MB/s

Sequential read (32-bit LODSD), size = 128 B, loops = 154664960, 3766.6 MB/s
Sequential read (32-bit LODSD), size = 256 B, loops = 97517568, 4760.1 MB/s
Sequential read (32-bit LODSD), size = 384 B, loops = 71302896, 5218.9 MB/s
Sequential read (32-bit LODSD), size = 512 B, loops = 55967744, 5465.0 MB/s
Sequential read (32-bit LODSD), size = 640 B, loops = 46346794, 5654.4 MB/s
Sequential read (32-bit LODSD), size = 768 B, loops = 39496212, 5775.4 MB/s
Sequential read (32-bit LODSD), size = 896 B, loops = 34303284, 5862.0 MB/s
Sequential read (32-bit LODSD), size = 1024 B, loops = 30408704, 5933.9 MB/s
Sequential read (32-bit LODSD), size = 1280 B, loops = 24746016, 6030.5 MB/s
Sequential read (32-bit LODSD), size = 2 kB, loops = 15859712, 6188.1 MB/s
Sequential read (32-bit LODSD), size = 3 kB, loops = 10725895, 6277.7 MB/s
Sequential read (32-bit LODSD), size = 4 kB, loops = 8093696, 6320.8 MB/s
Sequential read (32-bit LODSD), size = 6 kB, loops = 5439156, 6367.6 MB/s
Sequential read (32-bit LODSD), size = 8 kB, loops = 4096000, 6394.1 MB/s
Sequential read (32-bit LODSD), size = 12 kB, loops = 2741422, 6417.9 MB/s
Sequential read (32-bit LODSD), size = 16 kB, loops = 2060288, 6429.7 MB/s
Sequential read (32-bit LODSD), size = 20 kB, loops = 1647828, 6433.4 MB/s
Sequential read (32-bit LODSD), size = 24 kB, loops = 1375920, 6441.4 MB/s
Sequential read (32-bit LODSD), size = 28 kB, loops = 1179360, 6445.4 MB/s
Sequential read (32-bit LODSD), size = 32 kB, loops = 1032192, 6447.7 MB/s
Sequential read (32-bit LODSD), size = 34 kB, loops = 971208, 6445.8 MB/s
Sequential read (32-bit LODSD), size = 36 kB, loops = 919100, 6449.8 MB/s
Sequential read (32-bit LODSD), size = 40 kB, loops = 827190, 6451.4 MB/s
Sequential read (32-bit LODSD), size = 48 kB, loops = 689325, 6453.9 MB/s
Sequential read (32-bit LODSD), size = 64 kB, loops = 517120, 6456.9 MB/s
Sequential read (32-bit LODSD), size = 128 kB, loops = 258560, 6461.4 MB/s
Sequential read (32-bit LODSD), size = 192 kB, loops = 172546, 6462.8 MB/s
Sequential read (32-bit LODSD), size = 256 kB, loops = 129280, 6459.9 MB/s
Sequential read (32-bit LODSD), size = 320 kB, loops = 103428, 6460.4 MB/s
Sequential read (32-bit LODSD), size = 384 kB, loops = 86190, 6460.7 MB/s
Sequential read (32-bit LODSD), size = 512 kB, loops = 64640, 6464.0 MB/s
Sequential read (32-bit LODSD), size = 768 kB, loops = 43095, 6464.2 MB/s
Sequential read (32-bit LODSD), size = 1 MB, loops = 32320, 6461.5 MB/s
Sequential read (32-bit LODSD), size = 1.25 MB, loops = 25908, 6464.4 MB/s
Sequential read (32-bit LODSD), size = 1.5 MB, loops = 21588, 6464.6 MB/s
Sequential read (32-bit LODSD), size = 1.75 MB, loops = 18504, 6464.7 MB/s
Sequential read (32-bit LODSD), size = 2 MB, loops = 16192, 6464.7 MB/s
Sequential read (32-bit LODSD), size = 2.25 MB, loops = 14392, 6464.7 MB/s
Sequential read (32-bit LODSD), size = 2.5 MB, loops = 12950, 6464.7 MB/s
Sequential read (32-bit LODSD), size = 2.75 MB, loops = 11776, 6464.8 MB/s
Sequential read (32-bit LODSD), size = 3 MB, loops = 10794, 6464.1 MB/s
Sequential read (32-bit LODSD), size = 3.25 MB, loops = 9956, 6464.5 MB/s
Sequential read (32-bit LODSD), size = 3.5 MB, loops = 9252, 6464.5 MB/s
Sequential read (32-bit LODSD), size = 4 MB, loops = 8096, 6464.5 MB/s
Sequential read (32-bit LODSD), size = 5 MB, loops = 6468, 6461.7 MB/s
Sequential read (32-bit LODSD), size = 6 MB, loops = 5390, 6461.7 MB/s
Sequential read (32-bit LODSD), size = 7 MB, loops = 4626, 6463.9 MB/s
Sequential read (32-bit LODSD), size = 8 MB, loops = 4008, 6411.8 MB/s
Sequential read (32-bit LODSD), size = 9 MB, loops = 3493, 6286.9 MB/s
Sequential read (32-bit LODSD), size = 10 MB, loops = 3138, 6264.3 MB/s
Sequential read (32-bit LODSD), size = 12 MB, loops = 2620, 6278.6 MB/s
Sequential read (32-bit LODSD), size = 14 MB, loops = 2252, 6297.7 MB/s
Sequential read (32-bit LODSD), size = 15 MB, loops = 2100, 6295.6 MB/s
Sequential read (32-bit LODSD), size = 16 MB, loops = 1972, 6300.5 MB/s
Sequential read (32-bit LODSD), size = 20 MB, loops = 1578, 6306.4 MB/s
Sequential read (32-bit LODSD), size = 21 MB, loops = 1506, 6312.4 MB/s
Sequential read (32-bit LODSD), size = 32 MB, loops = 990, 6328.2 MB/s
Sequential read (32-bit LODSD), size = 48 MB, loops = 665, 6376.5 MB/s
Sequential read (32-bit LODSD), size = 64 MB, loops = 499, 6387.0 MB/s
Sequential read (32-bit LODSD), size = 72 MB, loops = 445, 6394.9 MB/s
Sequential read (32-bit LODSD), size = 96 MB, loops = 334, 6405.2 MB/s
Sequential read (32-bit LODSD), size = 128 MB, loops = 251, 6413.7 MB/s

Sequential read (16-bit LODSW), size = 128 B, loops = 97517568, 2380.0 MB/s
Sequential read (16-bit LODSW), size = 256 B, loops = 56098816, 2732.5 MB/s
Sequential read (16-bit LODSW), size = 384 B, loops = 39496212, 2887.9 MB/s
Sequential read (16-bit LODSW), size = 512 B, loops = 30408704, 2967.0 MB/s
Sequential read (16-bit LODSW), size = 640 B, loops = 24746252, 3016.6 MB/s
Sequential read (16-bit LODSW), size = 768 B, loops = 20884059, 3049.1 MB/s
Sequential read (16-bit LODSW), size = 896 B, loops = 18050418, 3074.9 MB/s
Sequential read (16-bit LODSW), size = 1024 B, loops = 15859712, 3094.0 MB/s
Sequential read (16-bit LODSW), size = 1280 B, loops = 12792432, 3120.8 MB/s
Sequential read (16-bit LODSW), size = 2 kB, loops = 8093696, 3160.4 MB/s
Sequential read (16-bit LODSW), size = 3 kB, loops = 5439405, 3183.9 MB/s
Sequential read (16-bit LODSW), size = 4 kB, loops = 4096000, 3197.1 MB/s
Sequential read (16-bit LODSW), size = 6 kB, loops = 2741422, 3209.0 MB/s
Sequential read (16-bit LODSW), size = 8 kB, loops = 2064384, 3214.9 MB/s
Sequential read (16-bit LODSW), size = 12 kB, loops = 1376172, 3220.7 MB/s
Sequential read (16-bit LODSW), size = 16 kB, loops = 1032192, 3223.8 MB/s
Sequential read (16-bit LODSW), size = 20 kB, loops = 828828, 3225.8 MB/s
Sequential read (16-bit LODSW), size = 24 kB, loops = 690690, 3227.1 MB/s
Sequential read (16-bit LODSW), size = 28 kB, loops = 592020, 3227.9 MB/s
Sequential read (16-bit LODSW), size = 32 kB, loops = 518144, 3228.4 MB/s
Sequential read (16-bit LODSW), size = 34 kB, loops = 487531, 3228.8 MB/s
Sequential read (16-bit LODSW), size = 36 kB, loops = 460460, 3228.9 MB/s
Sequential read (16-bit LODSW), size = 40 kB, loops = 414414, 3229.3 MB/s
Sequential read (16-bit LODSW), size = 48 kB, loops = 345345, 3230.0 MB/s
Sequential read (16-bit LODSW), size = 64 kB, loops = 259072, 3230.7 MB/s
Sequential read (16-bit LODSW), size = 128 kB, loops = 129536, 3230.4 MB/s
Sequential read (16-bit LODSW), size = 192 kB, loops = 86273, 3232.3 MB/s
Sequential read (16-bit LODSW), size = 256 kB, loops = 64768, 3230.5 MB/s
Sequential read (16-bit LODSW), size = 320 kB, loops = 51816, 3232.1 MB/s
Sequential read (16-bit LODSW), size = 384 kB, loops = 43180, 3232.2 MB/s
Sequential read (16-bit LODSW), size = 512 kB, loops = 32384, 3232.3 MB/s
Sequential read (16-bit LODSW), size = 768 kB, loops = 21590, 3232.4 MB/s
Sequential read (16-bit LODSW), size = 1 MB, loops = 16192, 3232.4 MB/s
Sequential read (16-bit LODSW), size = 1.25 MB, loops = 12954, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 1.5 MB, loops = 10794, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 1.75 MB, loops = 9252, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 2 MB, loops = 8096, 3231.0 MB/s
Sequential read (16-bit LODSW), size = 2.25 MB, loops = 7196, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 2.5 MB, loops = 6475, 3232.1 MB/s
Sequential read (16-bit LODSW), size = 2.75 MB, loops = 5888, 3229.5 MB/s
Sequential read (16-bit LODSW), size = 3 MB, loops = 5397, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 3.25 MB, loops = 4978, 3232.4 MB/s
Sequential read (16-bit LODSW), size = 3.5 MB, loops = 4626, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 4 MB, loops = 4048, 3232.5 MB/s
Sequential read (16-bit LODSW), size = 5 MB, loops = 3240, 3230.8 MB/s
Sequential read (16-bit LODSW), size = 6 MB, loops = 2700, 3230.6 MB/s
Sequential read (16-bit LODSW), size = 7 MB, loops = 2313, 3230.5 MB/s
Sequential read (16-bit LODSW), size = 8 MB, loops = 2016, 3219.3 MB/s
Sequential read (16-bit LODSW), size = 9 MB, loops = 1785, 3205.7 MB/s
Sequential read (16-bit LODSW), size = 10 MB, loops = 1608, 3207.8 MB/s
Sequential read (16-bit LODSW), size = 12 MB, loops = 1340, 3207.3 MB/s
Sequential read (16-bit LODSW), size = 14 MB, loops = 1148, 3210.7 MB/s
Sequential read (16-bit LODSW), size = 15 MB, loops = 1072, 3210.0 MB/s
Sequential read (16-bit LODSW), size = 16 MB, loops = 1004, 3211.8 MB/s
Sequential read (16-bit LODSW), size = 20 MB, loops = 804, 3212.8 MB/s
Sequential read (16-bit LODSW), size = 21 MB, loops = 768, 3214.2 MB/s
Sequential read (16-bit LODSW), size = 32 MB, loops = 504, 3213.3 MB/s
Sequential read (16-bit LODSW), size = 48 MB, loops = 335, 3208.4 MB/s
Sequential read (16-bit LODSW), size = 64 MB, loops = 251, 3212.7 MB/s
Sequential read (16-bit LODSW), size = 72 MB, loops = 224, 3212.6 MB/s
Sequential read (16-bit LODSW), size = 96 MB, loops = 168, 3213.1 MB/s
Sequential read (16-bit LODSW), size = 128 MB, loops = 126, 3210.2 MB/s

Sequential read (8-bit LODSB), size = 128 B, loops = 56098816, 1366.3 MB/s
Sequential read (8-bit LODSB), size = 256 B, loops = 30408704, 1483.5 MB/s
Sequential read (8-bit LODSB), size = 384 B, loops = 20971440, 1525.2 MB/s
Sequential read (8-bit LODSB), size = 512 B, loops = 15859712, 1546.9 MB/s
Sequential read (8-bit LODSB), size = 640 B, loops = 12792554, 1560.3 MB/s
Sequential read (8-bit LODSB), size = 768 B, loops = 10747863, 1569.3 MB/s
Sequential read (8-bit LODSB), size = 896 B, loops = 9287352, 1576.1 MB/s
Sequential read (8-bit LODSB), size = 1024 B, loops = 8126464, 1579.5 MB/s
Sequential read (8-bit LODSB), size = 1280 B, loops = 6553500, 1587.9 MB/s
Sequential read (8-bit LODSB), size = 2 kB, loops = 4096000, 1598.6 MB/s
Sequential read (8-bit LODSB), size = 3 kB, loops = 2752470, 1603.8 MB/s
Sequential read (8-bit LODSB), size = 4 kB, loops = 2064384, 1606.8 MB/s
Sequential read (8-bit LODSB), size = 6 kB, loops = 1376172, 1610.5 MB/s
Sequential read (8-bit LODSB), size = 8 kB, loops = 1032192, 1610.6 MB/s
Sequential read (8-bit LODSB), size = 12 kB, loops = 693547, 1613.5 MB/s
Sequential read (8-bit LODSB), size = 16 kB, loops = 520192, 1613.5 MB/s
Sequential read (8-bit LODSB), size = 20 kB, loops = 416052, 1614.0 MB/s
Sequential read (8-bit LODSB), size = 24 kB, loops = 346710, 1615.0 MB/s
Sequential read (8-bit LODSB), size = 28 kB, loops = 297180, 1615.2 MB/s
Sequential read (8-bit LODSB), size = 32 kB, loops = 260096, 1614.6 MB/s
Sequential read (8-bit LODSB), size = 34 kB, loops = 244729, 1615.3 MB/s
Sequential read (8-bit LODSB), size = 36 kB, loops = 231140, 1614.8 MB/s
Sequential read (8-bit LODSB), size = 40 kB, loops = 208026, 1615.6 MB/s
Sequential read (8-bit LODSB), size = 48 kB, loops = 173355, 1615.7 MB/s
Sequential read (8-bit LODSB), size = 64 kB, loops = 130048, 1615.9 MB/s
Sequential read (8-bit LODSB), size = 128 kB, loops = 65024, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 192 kB, loops = 43307, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 256 kB, loops = 32512, 1615.5 MB/s
Sequential read (8-bit LODSB), size = 320 kB, loops = 25908, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 384 kB, loops = 21590, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 512 kB, loops = 16256, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 768 kB, loops = 10795, 1615.5 MB/s
Sequential read (8-bit LODSB), size = 1 MB, loops = 8128, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 1.25 MB, loops = 6477, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 1.5 MB, loops = 5418, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 1.75 MB, loops = 4644, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 2 MB, loops = 4064, 1616.1 MB/s
Sequential read (8-bit LODSB), size = 2.25 MB, loops = 3612, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 2.5 MB, loops = 3250, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 2.75 MB, loops = 2944, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 3 MB, loops = 2709, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 3.25 MB, loops = 2489, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 3.5 MB, loops = 2322, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 4 MB, loops = 2032, 1615.5 MB/s
Sequential read (8-bit LODSB), size = 5 MB, loops = 1620, 1616.3 MB/s
Sequential read (8-bit LODSB), size = 6 MB, loops = 1350, 1615.4 MB/s
Sequential read (8-bit LODSB), size = 7 MB, loops = 1161, 1616.2 MB/s
Sequential read (8-bit LODSB), size = 8 MB, loops = 1008, 1611.9 MB/s
Sequential read (8-bit LODSB), size = 9 MB, loops = 896, 1610.8 MB/s
Sequential read (8-bit LODSB), size = 10 MB, loops = 810, 1612.2 MB/s
Sequential read (8-bit LODSB), size = 12 MB, loops = 675, 1612.5 MB/s
Sequential read (8-bit LODSB), size = 14 MB, loops = 576, 1611.0 MB/s
Sequential read (8-bit LODSB), size = 15 MB, loops = 540, 1612.0 MB/s
Sequential read (8-bit LODSB), size = 16 MB, loops = 504, 1608.1 MB/s
Sequential read (8-bit LODSB), size = 20 MB, loops = 405, 1611.3 MB/s
Sequential read (8-bit LODSB), size = 21 MB, loops = 384, 1607.3 MB/s
Sequential read (8-bit LODSB), size = 32 MB, loops = 252, 1610.3 MB/s
Sequential read (8-bit LODSB), size = 48 MB, loops = 168, 1610.3 MB/s
Sequential read (8-bit LODSB), size = 64 MB, loops = 126, 1600.4 MB/s
Sequential read (8-bit LODSB), size = 72 MB, loops = 112, 1611.6 MB/s
Sequential read (8-bit LODSB), size = 96 MB, loops = 84, 1609.2 MB/s
Sequential read (8-bit LODSB), size = 128 MB, loops = 63, 1608.8 MB/s

Main register to main register transfers (64-bit) 91347.3 MB/s
Main register to vector register transfers (64-bit) 25726.8 MB/s
Vector register to main register transfers (64-bit) 25727.2 MB/s
Vector register to vector register transfers (128-bit) 88081.7 MB/s
Vector register to vector register transfers (256-bit) 268755.6 MB/s
Vector 8-bit datum to main register transfers 403.9 MB/s
Vector 16-bit datum to main register transfers 1614.8 MB/s
Vector 32-bit datum to main register transfers 6452.4 MB/s
Vector 64-bit datum to main register transfers 12881.1 MB/s
Main register 8-bit datum to vector register transfers 403.9 MB/s
Main register 16-bit datum to vector register transfers 1614.9 MB/s
Main register 32-bit datum to vector register transfers 6453.6 MB/s
Main register 64-bit datum to vector register transfers 6453.4 MB/s

Stack-to-register transfers (64-bit) 51536.4 MB/s
Register-to-stack transfers (64-bit) 25804.6 MB/s

Library: memset 23478.7 MB/s
Library: memcpy 9206.2 MB/s

Wrote graph to bandwidth.bmp.

Done.
[oberstet@brummer2 ~/bandwidth-1.1]$ 
```

## Results (48 core NUMA machine)

```console
root@s4l-zfs:~/oberstet/bandwidth-1.1 # sysctl hw.model
hw.model: Intel(R) Xeon(R) CPU E7-8857 v2 @ 3.00GHz
root@s4l-zfs:~/oberstet/bandwidth-1.1 # sysctl hw.ncpu
hw.ncpu: 48
root@s4l-zfs:~/oberstet/bandwidth-1.1 # uname -a
FreeBSD s4l-zfs 11.0-CURRENT FreeBSD 11.0-CURRENT #1 r280797+e9f6590(strndup)-dirty: Thu Apr  2 11:58:58 CEST 2015     root@s4l-zfs:/usr/obj/root/src/sys/X  amd64
root@s4l-zfs:~/oberstet/bandwidth-1.1 # ./bandwidth64 
This is bandwidth version 1.1.
Copyright (C) 2005-2014 by Zack T Smith.

This software is covered by the GNU Public License.
It is provided AS-IS, use at your own risk.
See the file COPYING for more information.

CPU family: GenuineIntel
CPU features: MMX SSE SSE2 SSE3 SSSE3 SSE4.1 SSE4.2 AES AVX XD Intel64 

Cache 0: L1 data cache,        line size 64,  8-ways,    64 sets, size 32k 
Cache 1: L1 instruction cache, line size 64,  8-ways,    64 sets, size 32k 
Cache 2: L2 unified cache,     line size 64,  8-ways,   512 sets, size 256k 
Cache 3: L3 unified cache,     line size 64, 20-ways, 24576 sets, size 30720k 

Notation: B = byte, kB = 1024 B, MB = 1048576 B.

Sequential read (128-bit), size = 128 B, loops = 3732930560, 91134.2 MB/s
Sequential read (128-bit), size = 256 B, loops = 1866203136, 91123.1 MB/s
Sequential read (128-bit), size = 384 B, loops = 1244130678, 91118.8 MB/s
Sequential read (128-bit), size = 512 B, loops = 933232640, 91126.7 MB/s
Sequential read (128-bit), size = 640 B, loops = 746372126, 91103.2 MB/s
Sequential read (128-bit), size = 768 B, loops = 622065339, 91117.0 MB/s
Sequential read (128-bit), size = 896 B, loops = 533123964, 91101.8 MB/s
Sequential read (128-bit), size = 1024 B, loops = 466550784, 91112.2 MB/s
Sequential read (128-bit), size = 1280 B, loops = 373234932, 91109.8 MB/s
Sequential read (128-bit), size = 2 kB, loops = 233308160, 91131.4 MB/s
Sequential read (128-bit), size = 3 kB, loops = 155536400, 91130.6 MB/s
Sequential read (128-bit), size = 4 kB, loops = 116637696, 91116.6 MB/s
Sequential read (128-bit), size = 6 kB, loops = 77753718, 91110.4 MB/s
Sequential read (128-bit), size = 8 kB, loops = 58318848, 91116.5 MB/s
Sequential read (128-bit), size = 12 kB, loops = 37386006, 87622.5 MB/s
Sequential read (128-bit), size = 16 kB, loops = 28311552, 88470.8 MB/s
Sequential read (128-bit), size = 20 kB, loops = 22784580, 88996.6 MB/s
Sequential read (128-bit), size = 24 kB, loops = 19060860, 89345.4 MB/s
Sequential read (128-bit), size = 28 kB, loops = 16382340, 89580.1 MB/s
Sequential read (128-bit), size = 32 kB, loops = 14292992, 89328.1 MB/s
Sequential read (128-bit), size = 34 kB, loops = 8411355, 55845.6 MB/s
Sequential read (128-bit), size = 36 kB, loops = 6402760, 45008.3 MB/s
Sequential read (128-bit), size = 40 kB, loops = 5764122, 45022.3 MB/s
Sequential read (128-bit), size = 48 kB, loops = 4796610, 44965.5 MB/s
Sequential read (128-bit), size = 64 kB, loops = 3590144, 44869.4 MB/s
Sequential read (128-bit), size = 128 kB, loops = 1773056, 44324.9 MB/s
Sequential read (128-bit), size = 192 kB, loops = 1170653, 43892.6 MB/s
Sequential read (128-bit), size = 256 kB, loops = 854784, 42728.9 MB/s
Sequential read (128-bit), size = 320 kB, loops = 526116, 32875.4 MB/s
Sequential read (128-bit), size = 384 kB, loops = 348670, 26147.9 MB/s
Sequential read (128-bit), size = 512 kB, loops = 255360, 25524.0 MB/s
Sequential read (128-bit), size = 768 kB, loops = 169915, 25478.6 MB/s
Sequential read (128-bit), size = 1 MB, loops = 127424, 25481.4 MB/s
Sequential read (128-bit), size = 1.25 MB, loops = 101949, 25483.6 MB/s
Sequential read (128-bit), size = 1.5 MB, loops = 84966, 25482.9 MB/s
Sequential read (128-bit), size = 1.75 MB, loops = 72792, 25476.7 MB/s
Sequential read (128-bit), size = 2 MB, loops = 63712, 25478.4 MB/s
Sequential read (128-bit), size = 2.25 MB, loops = 56252, 25303.2 MB/s
Sequential read (128-bit), size = 2.5 MB, loops = 50425, 25204.0 MB/s
Sequential read (128-bit), size = 2.75 MB, loops = 45839, 25200.7 MB/s
Sequential read (128-bit), size = 3 MB, loops = 42021, 25202.3 MB/s
Sequential read (128-bit), size = 3.25 MB, loops = 38779, 25204.6 MB/s
Sequential read (128-bit), size = 3.5 MB, loops = 36018, 25205.2 MB/s
Sequential read (128-bit), size = 4 MB, loops = 32032, 25613.2 MB/s
Sequential read (128-bit), size = 5 MB, loops = 25596, 25590.7 MB/s
Sequential read (128-bit), size = 6 MB, loops = 21350, 25615.8 MB/s
Sequential read (128-bit), size = 7 MB, loops = 18288, 25595.4 MB/s
Sequential read (128-bit), size = 8 MB, loops = 16016, 25615.3 MB/s
Sequential read (128-bit), size = 9 MB, loops = 14224, 25599.7 MB/s
Sequential read (128-bit), size = 10 MB, loops = 12810, 25613.6 MB/s
Sequential read (128-bit), size = 12 MB, loops = 10675, 25612.6 MB/s
Sequential read (128-bit), size = 14 MB, loops = 9148, 25612.2 MB/s
Sequential read (128-bit), size = 15 MB, loops = 8536, 25605.1 MB/s
Sequential read (128-bit), size = 16 MB, loops = 8004, 25612.3 MB/s
Sequential read (128-bit), size = 20 MB, loops = 6405, 25612.5 MB/s
Sequential read (128-bit), size = 21 MB, loops = 6099, 25606.6 MB/s
Sequential read (128-bit), size = 32 MB, loops = 954, 6094.1 MB/s
Sequential read (128-bit), size = 48 MB, loops = 441, 4226.8 MB/s
Sequential read (128-bit), size = 64 MB, loops = 313, 4002.3 MB/s
Sequential read (128-bit), size = 72 MB, loops = 278, 3995.8 MB/s
Sequential read (128-bit), size = 96 MB, loops = 209, 3994.4 MB/s
Sequential read (128-bit), size = 128 MB, loops = 156, 3993.3 MB/s

Sequential read (256-bit), size = 256 B, loops = 1866203136, 91120.3 MB/s
Sequential read (256-bit), size = 512 B, loops = 933101568, 91115.5 MB/s
Sequential read (256-bit), size = 768 B, loops = 622065339, 91117.0 MB/s
Sequential read (256-bit), size = 1024 B, loops = 466550784, 91120.1 MB/s
Sequential read (256-bit), size = 1280 B, loops = 373234932, 91119.7 MB/s
Sequential read (256-bit), size = 2 kB, loops = 233275392, 91120.3 MB/s
Sequential read (256-bit), size = 3 kB, loops = 155514555, 91114.0 MB/s
Sequential read (256-bit), size = 4 kB, loops = 116637696, 91115.5 MB/s
Sequential read (256-bit), size = 6 kB, loops = 77753718, 91110.9 MB/s
Sequential read (256-bit), size = 8 kB, loops = 58310656, 91100.4 MB/s
Sequential read (256-bit), size = 12 kB, loops = 38494589, 90210.2 MB/s
Sequential read (256-bit), size = 16 kB, loops = 28942336, 90433.5 MB/s
Sequential read (256-bit), size = 20 kB, loops = 23187528, 90569.5 MB/s
Sequential read (256-bit), size = 24 kB, loops = 19342050, 90653.5 MB/s
Sequential read (256-bit), size = 28 kB, loops = 16585920, 90702.9 MB/s
Sequential read (256-bit), size = 32 kB, loops = 14514176, 90705.1 MB/s
Sequential read (256-bit), size = 34 kB, loops = 7526862, 49979.0 MB/s
Sequential read (256-bit), size = 36 kB, loops = 5401760, 37975.6 MB/s
Sequential read (256-bit), size = 40 kB, loops = 4850118, 37884.9 MB/s
Sequential read (256-bit), size = 48 kB, loops = 4060875, 38058.1 MB/s
Sequential read (256-bit), size = 64 kB, loops = 3046400, 38078.6 MB/s
Sequential read (256-bit), size = 128 kB, loops = 1499648, 37484.3 MB/s
Sequential read (256-bit), size = 192 kB, loops = 987536, 37029.5 MB/s
Sequential read (256-bit), size = 256 kB, loops = 723712, 36174.3 MB/s
Sequential read (256-bit), size = 320 kB, loops = 464100, 28997.1 MB/s
Sequential read (256-bit), size = 384 kB, loops = 341190, 25580.8 MB/s
Sequential read (256-bit), size = 512 kB, loops = 252672, 25255.7 MB/s
Sequential read (256-bit), size = 768 kB, loops = 168130, 25218.8 MB/s
Sequential read (256-bit), size = 1 MB, loops = 126080, 25214.2 MB/s
Sequential read (256-bit), size = 1.25 MB, loops = 100878, 25212.9 MB/s
Sequential read (256-bit), size = 1.5 MB, loops = 84084, 25213.1 MB/s
Sequential read (256-bit), size = 1.75 MB, loops = 72036, 25205.1 MB/s
Sequential read (256-bit), size = 2 MB, loops = 63040, 25203.6 MB/s
Sequential read (256-bit), size = 2.25 MB, loops = 55440, 24940.5 MB/s
Sequential read (256-bit), size = 2.5 MB, loops = 49575, 24777.4 MB/s
Sequential read (256-bit), size = 2.75 MB, loops = 45057, 24778.4 MB/s
Sequential read (256-bit), size = 3 MB, loops = 41307, 24779.9 MB/s
Sequential read (256-bit), size = 3.25 MB, loops = 38133, 24779.3 MB/s
Sequential read (256-bit), size = 3.5 MB, loops = 35406, 24779.1 MB/s
Sequential read (256-bit), size = 4 MB, loops = 31920, 25533.1 MB/s
Sequential read (256-bit), size = 5 MB, loops = 25476, 25470.1 MB/s
Sequential read (256-bit), size = 6 MB, loops = 21280, 25532.2 MB/s
Sequential read (256-bit), size = 7 MB, loops = 18207, 25485.9 MB/s
Sequential read (256-bit), size = 8 MB, loops = 15960, 25533.4 MB/s
Sequential read (256-bit), size = 9 MB, loops = 14168, 25497.9 MB/s
Sequential read (256-bit), size = 10 MB, loops = 12768, 25531.3 MB/s
Sequential read (256-bit), size = 12 MB, loops = 10640, 25532.5 MB/s
Sequential read (256-bit), size = 14 MB, loops = 9120, 25533.5 MB/s
Sequential read (256-bit), size = 15 MB, loops = 8504, 25509.7 MB/s
Sequential read (256-bit), size = 16 MB, loops = 7980, 25532.1 MB/s
Sequential read (256-bit), size = 20 MB, loops = 6384, 25531.1 MB/s
Sequential read (256-bit), size = 21 MB, loops = 6078, 25515.3 MB/s
Sequential read (256-bit), size = 32 MB, loops = 1144, 7310.0 MB/s
Sequential read (256-bit), size = 48 MB, loops = 454, 4353.1 MB/s
Sequential read (256-bit), size = 64 MB, loops = 329, 4199.3 MB/s
Sequential read (256-bit), size = 72 MB, loops = 292, 4191.5 MB/s
Sequential read (256-bit), size = 96 MB, loops = 219, 4191.8 MB/s
Sequential read (256-bit), size = 128 MB, loops = 164, 4193.5 MB/s

Random read (128-bit), size = 256 B, loops = 829685760, 40505.1 MB/s
Random read (128-bit), size = 512 B, loops = 428736512, 41867.0 MB/s
Random read (128-bit), size = 768 B, loops = 339387804, 49713.3 MB/s
Random read (128-bit), size = 1024 B, loops = 242548736, 47368.2 MB/s
Random read (128-bit), size = 1280 B, loops = 199121544, 48613.0 MB/s
Random read (128-bit), size = 2 kB, loops = 131039232, 51183.8 MB/s
Random read (128-bit), size = 3 kB, loops = 84889670, 49728.9 MB/s
Random read (128-bit), size = 4 kB, loops = 65486848, 51160.5 MB/s
Random read (128-bit), size = 6 kB, loops = 43698922, 51204.2 MB/s
Random read (128-bit), size = 8 kB, loops = 32759808, 51184.8 MB/s
Random read (128-bit), size = 12 kB, loops = 21467191, 50307.4 MB/s
Random read (128-bit), size = 16 kB, loops = 16273408, 50846.3 MB/s
Random read (128-bit), size = 20 kB, loops = 13051584, 50976.3 MB/s
Random read (128-bit), size = 24 kB, loops = 10917270, 51165.7 MB/s
Random read (128-bit), size = 28 kB, loops = 9369360, 51237.5 MB/s
Random read (128-bit), size = 32 kB, loops = 7688192, 48043.8 MB/s
Random read (128-bit), size = 34 kB, loops = 6833142, 45371.9 MB/s
Random read (128-bit), size = 36 kB, loops = 5419960, 38097.8 MB/s
Random read (128-bit), size = 40 kB, loops = 4674852, 36519.3 MB/s
Random read (128-bit), size = 48 kB, loops = 3775590, 35391.7 MB/s
Random read (128-bit), size = 64 kB, loops = 2769920, 34617.2 MB/s
Random read (128-bit), size = 128 kB, loops = 1355264, 33879.6 MB/s
Random read (128-bit), size = 192 kB, loops = 893420, 33495.2 MB/s
Random read (128-bit), size = 256 kB, loops = 621312, 31054.4 MB/s
Random read (128-bit), size = 320 kB, loops = 351492, 21966.9 MB/s
Random read (128-bit), size = 384 kB, loops = 281690, 21118.0 MB/s
Random read (128-bit), size = 512 kB, loops = 204800, 20473.1 MB/s
Random read (128-bit), size = 768 kB, loops = 131835, 19763.4 MB/s
Random read (128-bit), size = 1 MB, loops = 97600, 19510.1 MB/s
Random read (128-bit), size = 1.25 MB, loops = 77571, 19386.2 MB/s
Random read (128-bit), size = 1.5 MB, loops = 64344, 19297.5 MB/s
Random read (128-bit), size = 1.75 MB, loops = 55080, 19277.8 MB/s
Random read (128-bit), size = 2 MB, loops = 47936, 19161.9 MB/s
Random read (128-bit), size = 2.25 MB, loops = 40516, 18222.2 MB/s
Random read (128-bit), size = 2.5 MB, loops = 35175, 17582.4 MB/s
Random read (128-bit), size = 2.75 MB, loops = 31257, 17187.8 MB/s
Random read (128-bit), size = 3 MB, loops = 28119, 16869.9 MB/s
Random read (128-bit), size = 3.25 MB, loops = 25517, 16575.2 MB/s
Random read (128-bit), size = 3.5 MB, loops = 23400, 16372.4 MB/s
Random read (128-bit), size = 4 MB, loops = 25488, 20384.8 MB/s
Random read (128-bit), size = 5 MB, loops = 20124, 20115.2 MB/s
Random read (128-bit), size = 6 MB, loops = 16980, 20366.7 MB/s
Random read (128-bit), size = 7 MB, loops = 14418, 20175.8 MB/s
Random read (128-bit), size = 8 MB, loops = 12720, 20347.9 MB/s
Random read (128-bit), size = 9 MB, loops = 11221, 20197.5 MB/s
Random read (128-bit), size = 10 MB, loops = 10170, 20328.3 MB/s
Random read (128-bit), size = 12 MB, loops = 8470, 20323.9 MB/s
Random read (128-bit), size = 14 MB, loops = 7260, 20326.3 MB/s
Random read (128-bit), size = 15 MB, loops = 6748, 20239.5 MB/s
Random read (128-bit), size = 16 MB, loops = 6352, 20319.6 MB/s
Random read (128-bit), size = 20 MB, loops = 5079, 20315.1 MB/s
Random read (128-bit), size = 21 MB, loops = 4824, 20253.0 MB/s
Random read (128-bit), size = 32 MB, loops = 320, 2041.8 MB/s
Random read (128-bit), size = 48 MB, loops = 181, 1735.8 MB/s
Random read (128-bit), size = 64 MB, loops = 133, 1696.4 MB/s
Random read (128-bit), size = 72 MB, loops = 118, 1685.8 MB/s
Random read (128-bit), size = 96 MB, loops = 87, 1664.7 MB/s
Random read (128-bit), size = 128 MB, loops = 65, 1651.5 MB/s

Sequential write (128-bit), size = 128 B, loops = 1866989568, 45571.6 MB/s
Sequential write (128-bit), size = 256 B, loops = 933494784, 45571.3 MB/s
Sequential write (128-bit), size = 384 B, loops = 622327482, 45568.7 MB/s
Sequential write (128-bit), size = 512 B, loops = 466747392, 45568.8 MB/s
Sequential write (128-bit), size = 640 B, loops = 373395777, 45572.2 MB/s
Sequential write (128-bit), size = 768 B, loops = 311163741, 45572.9 MB/s
Sequential write (128-bit), size = 896 B, loops = 266711778, 45570.2 MB/s
Sequential write (128-bit), size = 1024 B, loops = 233373696, 45572.7 MB/s
Sequential write (128-bit), size = 1280 B, loops = 186696108, 45568.6 MB/s
Sequential write (128-bit), size = 2 kB, loops = 116686848, 45569.5 MB/s
Sequential write (128-bit), size = 3 kB, loops = 77790045, 45570.9 MB/s
Sequential write (128-bit), size = 4 kB, loops = 58343424, 45568.1 MB/s
Sequential write (128-bit), size = 6 kB, loops = 38893242, 45574.1 MB/s
Sequential write (128-bit), size = 8 kB, loops = 29163520, 45567.7 MB/s
Sequential write (128-bit), size = 12 kB, loops = 19266408, 45153.5 MB/s
Sequential write (128-bit), size = 16 kB, loops = 14483456, 45251.1 MB/s
Sequential write (128-bit), size = 20 kB, loops = 11600316, 45310.1 MB/s
Sequential write (128-bit), size = 24 kB, loops = 9675120, 45350.7 MB/s
Sequential write (128-bit), size = 28 kB, loops = 8297640, 45374.0 MB/s
Sequential write (128-bit), size = 32 kB, loops = 7262208, 45380.0 MB/s
Sequential write (128-bit), size = 34 kB, loops = 5807978, 38566.7 MB/s
Sequential write (128-bit), size = 36 kB, loops = 4337060, 30489.0 MB/s
Sequential write (128-bit), size = 40 kB, loops = 3849300, 30070.9 MB/s
Sequential write (128-bit), size = 48 kB, loops = 3244605, 30414.3 MB/s
Sequential write (128-bit), size = 64 kB, loops = 2454528, 30669.3 MB/s
Sequential write (128-bit), size = 128 kB, loops = 1202176, 30050.6 MB/s
Sequential write (128-bit), size = 192 kB, loops = 786005, 29462.7 MB/s
Sequential write (128-bit), size = 256 kB, loops = 573952, 28688.7 MB/s
Sequential write (128-bit), size = 320 kB, loops = 405348, 25324.5 MB/s
Sequential write (128-bit), size = 384 kB, loops = 266730, 20001.0 MB/s
Sequential write (128-bit), size = 512 kB, loops = 186624, 18658.0 MB/s
Sequential write (128-bit), size = 768 kB, loops = 124185, 18623.4 MB/s
Sequential write (128-bit), size = 1 MB, loops = 93184, 18624.7 MB/s
Sequential write (128-bit), size = 1.25 MB, loops = 74511, 18624.3 MB/s
Sequential write (128-bit), size = 1.5 MB, loops = 62076, 18615.7 MB/s
Sequential write (128-bit), size = 1.75 MB, loops = 53208, 18615.0 MB/s
Sequential write (128-bit), size = 2 MB, loops = 46560, 18619.9 MB/s
Sequential write (128-bit), size = 2.25 MB, loops = 41216, 18542.5 MB/s
Sequential write (128-bit), size = 2.5 MB, loops = 37050, 18518.3 MB/s
Sequential write (128-bit), size = 2.75 MB, loops = 33695, 18524.2 MB/s
Sequential write (128-bit), size = 3 MB, loops = 30849, 18506.6 MB/s
Sequential write (128-bit), size = 3.25 MB, loops = 28500, 18522.4 MB/s
Sequential write (128-bit), size = 3.5 MB, loops = 26460, 18520.0 MB/s
Sequential write (128-bit), size = 4 MB, loops = 23264, 18605.4 MB/s
Sequential write (128-bit), size = 5 MB, loops = 18612, 18600.3 MB/s
Sequential write (128-bit), size = 6 MB, loops = 15500, 18595.4 MB/s
Sequential write (128-bit), size = 7 MB, loops = 13284, 18591.5 MB/s
Sequential write (128-bit), size = 8 MB, loops = 11624, 18587.4 MB/s
Sequential write (128-bit), size = 9 MB, loops = 10325, 18584.1 MB/s
Sequential write (128-bit), size = 10 MB, loops = 9294, 18579.7 MB/s
Sequential write (128-bit), size = 12 MB, loops = 7740, 18572.1 MB/s
Sequential write (128-bit), size = 14 MB, loops = 6632, 18561.7 MB/s
Sequential write (128-bit), size = 15 MB, loops = 6188, 18555.0 MB/s
Sequential write (128-bit), size = 16 MB, loops = 5800, 18552.9 MB/s
Sequential write (128-bit), size = 20 MB, loops = 4635, 18536.2 MB/s
Sequential write (128-bit), size = 21 MB, loops = 4413, 18529.1 MB/s
Sequential write (128-bit), size = 32 MB, loops = 514, 3279.1 MB/s
Sequential write (128-bit), size = 48 MB, loops = 256, 2448.1 MB/s
Sequential write (128-bit), size = 64 MB, loops = 186, 2374.5 MB/s
Sequential write (128-bit), size = 72 MB, loops = 165, 2371.2 MB/s
Sequential write (128-bit), size = 96 MB, loops = 123, 2359.1 MB/s
Sequential write (128-bit), size = 128 MB, loops = 92, 2343.1 MB/s

Sequential write (256-bit), size = 256 B, loops = 933494784, 45570.0 MB/s
Sequential write (256-bit), size = 512 B, loops = 466616320, 45563.1 MB/s
Sequential write (256-bit), size = 768 B, loops = 311163741, 45579.1 MB/s
Sequential write (256-bit), size = 1024 B, loops = 233373696, 45571.9 MB/s
Sequential write (256-bit), size = 1280 B, loops = 186696108, 45572.9 MB/s
Sequential write (256-bit), size = 2 kB, loops = 116686848, 45570.2 MB/s
Sequential write (256-bit), size = 3 kB, loops = 77790045, 45569.1 MB/s
Sequential write (256-bit), size = 4 kB, loops = 58343424, 45574.8 MB/s
Sequential write (256-bit), size = 6 kB, loops = 38893242, 45575.3 MB/s
Sequential write (256-bit), size = 8 kB, loops = 28909568, 45169.9 MB/s
Sequential write (256-bit), size = 12 kB, loops = 19211798, 45025.9 MB/s
Sequential write (256-bit), size = 16 kB, loops = 14450688, 45154.6 MB/s
Sequential write (256-bit), size = 20 kB, loops = 11580660, 45234.2 MB/s
Sequential write (256-bit), size = 24 kB, loops = 9661470, 45281.9 MB/s
Sequential write (256-bit), size = 28 kB, loops = 8288280, 45318.2 MB/s
Sequential write (256-bit), size = 32 kB, loops = 7254016, 45326.7 MB/s
Sequential write (256-bit), size = 34 kB, loops = 5802197, 38525.3 MB/s
Sequential write (256-bit), size = 36 kB, loops = 4384380, 30823.0 MB/s
Sequential write (256-bit), size = 40 kB, loops = 3962322, 30950.9 MB/s
Sequential write (256-bit), size = 48 kB, loops = 3301935, 30950.4 MB/s
Sequential write (256-bit), size = 64 kB, loops = 2461696, 30770.5 MB/s
Sequential write (256-bit), size = 128 kB, loops = 1206272, 30152.8 MB/s
Sequential write (256-bit), size = 192 kB, loops = 786687, 29492.2 MB/s
Sequential write (256-bit), size = 256 kB, loops = 573952, 28686.4 MB/s
Sequential write (256-bit), size = 320 kB, loops = 405348, 25326.7 MB/s
Sequential write (256-bit), size = 384 kB, loops = 266730, 20001.2 MB/s
Sequential write (256-bit), size = 512 kB, loops = 186624, 18660.2 MB/s
Sequential write (256-bit), size = 768 kB, loops = 124185, 18623.6 MB/s
Sequential write (256-bit), size = 1 MB, loops = 93184, 18625.0 MB/s
Sequential write (256-bit), size = 1.25 MB, loops = 74562, 18628.6 MB/s
Sequential write (256-bit), size = 1.5 MB, loops = 62118, 18624.6 MB/s
Sequential write (256-bit), size = 1.75 MB, loops = 53208, 18616.5 MB/s
Sequential write (256-bit), size = 2 MB, loops = 46560, 18614.6 MB/s
Sequential write (256-bit), size = 2.25 MB, loops = 41048, 18460.6 MB/s
Sequential write (256-bit), size = 2.5 MB, loops = 36775, 18376.3 MB/s
Sequential write (256-bit), size = 2.75 MB, loops = 33442, 18391.2 MB/s
Sequential write (256-bit), size = 3 MB, loops = 30681, 18401.6 MB/s
Sequential write (256-bit), size = 3.25 MB, loops = 28329, 18407.6 MB/s
Sequential write (256-bit), size = 3.5 MB, loops = 26244, 18366.4 MB/s
Sequential write (256-bit), size = 4 MB, loops = 23264, 18603.6 MB/s
Sequential write (256-bit), size = 5 MB, loops = 18600, 18599.2 MB/s
Sequential write (256-bit), size = 6 MB, loops = 15500, 18595.6 MB/s
Sequential write (256-bit), size = 7 MB, loops = 13284, 18589.6 MB/s
Sequential write (256-bit), size = 8 MB, loops = 11616, 18583.8 MB/s
Sequential write (256-bit), size = 9 MB, loops = 10325, 18579.0 MB/s
Sequential write (256-bit), size = 10 MB, loops = 9294, 18577.2 MB/s
Sequential write (256-bit), size = 12 MB, loops = 7740, 18567.7 MB/s
Sequential write (256-bit), size = 14 MB, loops = 6628, 18557.7 MB/s
Sequential write (256-bit), size = 15 MB, loops = 6184, 18550.4 MB/s
Sequential write (256-bit), size = 16 MB, loops = 5796, 18544.7 MB/s
Sequential write (256-bit), size = 20 MB, loops = 4632, 18522.7 MB/s
Sequential write (256-bit), size = 21 MB, loops = 4413, 18526.2 MB/s
Sequential write (256-bit), size = 32 MB, loops = 532, 3392.2 MB/s
Sequential write (256-bit), size = 48 MB, loops = 256, 2457.5 MB/s
Sequential write (256-bit), size = 64 MB, loops = 186, 2373.9 MB/s
Sequential write (256-bit), size = 72 MB, loops = 165, 2371.5 MB/s
Sequential write (256-bit), size = 96 MB, loops = 124, 2370.8 MB/s
Sequential write (256-bit), size = 128 MB, loops = 92, 2344.6 MB/s

Random write (128-bit), size = 256 B, loops = 933494784, 45570.2 MB/s
Random write (128-bit), size = 512 B, loops = 466747392, 45570.4 MB/s
Random write (128-bit), size = 768 B, loops = 311163741, 45571.9 MB/s
Random write (128-bit), size = 1024 B, loops = 233373696, 45571.2 MB/s
Random write (128-bit), size = 1280 B, loops = 186696108, 45570.4 MB/s
Random write (128-bit), size = 2 kB, loops = 116686848, 45568.6 MB/s
Random write (128-bit), size = 3 kB, loops = 72503555, 42480.6 MB/s
Random write (128-bit), size = 4 kB, loops = 58146816, 45423.5 MB/s
Random write (128-bit), size = 6 kB, loops = 37768276, 44258.8 MB/s
Random write (128-bit), size = 8 kB, loops = 27230208, 42539.6 MB/s
Random write (128-bit), size = 12 kB, loops = 18567400, 43515.3 MB/s
Random write (128-bit), size = 16 kB, loops = 14327808, 44770.8 MB/s
Random write (128-bit), size = 20 kB, loops = 10840284, 42338.7 MB/s
Random write (128-bit), size = 24 kB, loops = 9183720, 43043.7 MB/s
Random write (128-bit), size = 28 kB, loops = 7488000, 40938.6 MB/s
Random write (128-bit), size = 32 kB, loops = 4835328, 30219.6 MB/s
Random write (128-bit), size = 34 kB, loops = 3052368, 20256.9 MB/s
Random write (128-bit), size = 36 kB, loops = 1880060, 13210.8 MB/s
Random write (128-bit), size = 40 kB, loops = 1682226, 13140.2 MB/s
Random write (128-bit), size = 48 kB, loops = 1396395, 13080.7 MB/s
Random write (128-bit), size = 64 kB, loops = 1049600, 13117.6 MB/s
Random write (128-bit), size = 128 kB, loops = 518656, 12956.3 MB/s
Random write (128-bit), size = 192 kB, loops = 340659, 12770.6 MB/s
Random write (128-bit), size = 256 kB, loops = 229632, 11470.0 MB/s
Random write (128-bit), size = 320 kB, loops = 77316, 4826.7 MB/s
Random write (128-bit), size = 384 kB, loops = 58820, 4405.4 MB/s
Random write (128-bit), size = 512 kB, loops = 43136, 4302.4 MB/s
Random write (128-bit), size = 768 kB, loops = 28475, 4271.2 MB/s
Random write (128-bit), size = 1 MB, loops = 21312, 4259.2 MB/s
Random write (128-bit), size = 1.25 MB, loops = 17034, 4256.0 MB/s
Random write (128-bit), size = 1.5 MB, loops = 14196, 4249.6 MB/s
Random write (128-bit), size = 1.75 MB, loops = 12168, 4248.8 MB/s
Random write (128-bit), size = 2 MB, loops = 10624, 4247.8 MB/s
Random write (128-bit), size = 2.25 MB, loops = 9408, 4221.3 MB/s
Random write (128-bit), size = 2.5 MB, loops = 8400, 4195.9 MB/s
Random write (128-bit), size = 2.75 MB, loops = 7613, 4179.4 MB/s
Random write (128-bit), size = 3 MB, loops = 6972, 4173.8 MB/s
Random write (128-bit), size = 3.25 MB, loops = 6403, 4152.7 MB/s
Random write (128-bit), size = 3.5 MB, loops = 5922, 4143.9 MB/s
Random write (128-bit), size = 4 MB, loops = 5296, 4233.5 MB/s
Random write (128-bit), size = 5 MB, loops = 4236, 4229.7 MB/s
Random write (128-bit), size = 6 MB, loops = 3530, 4224.9 MB/s
Random write (128-bit), size = 7 MB, loops = 3024, 4222.5 MB/s
Random write (128-bit), size = 8 MB, loops = 2640, 4218.9 MB/s
Random write (128-bit), size = 9 MB, loops = 2345, 4215.3 MB/s
Random write (128-bit), size = 10 MB, loops = 2112, 4212.3 MB/s
Random write (128-bit), size = 12 MB, loops = 1755, 4204.9 MB/s
Random write (128-bit), size = 14 MB, loops = 1500, 4197.0 MB/s
Random write (128-bit), size = 15 MB, loops = 1400, 4193.8 MB/s
Random write (128-bit), size = 16 MB, loops = 1312, 4191.3 MB/s
Random write (128-bit), size = 20 MB, loops = 1044, 4172.2 MB/s
Random write (128-bit), size = 21 MB, loops = 993, 4167.3 MB/s
Random write (128-bit), size = 32 MB, loops = 62, 390.6 MB/s
Random write (128-bit), size = 48 MB, loops = 32, 303.0 MB/s
Random write (128-bit), size = 64 MB, loops = 23, 293.2 MB/s
Random write (128-bit), size = 72 MB, loops = 21, 292.4 MB/s
Random write (128-bit), size = 96 MB, loops = 16, 290.8 MB/s
Random write (128-bit), size = 128 MB, loops = 12, 288.3 MB/s

Sequential read bypassing cache (128-bit), size = 128 B, loops = 3732406272, 91118.3 MB/s
Sequential read bypassing cache (128-bit), size = 256 B, loops = 1865416704, 91080.4 MB/s
Sequential read bypassing cache (128-bit), size = 384 B, loops = 1244130678, 91118.2 MB/s
Sequential read bypassing cache (128-bit), size = 512 B, loops = 898629632, 87746.8 MB/s
Sequential read bypassing cache (128-bit), size = 640 B, loops = 746476983, 91120.3 MB/s
Sequential read bypassing cache (128-bit), size = 768 B, loops = 620667243, 90906.1 MB/s
Sequential read bypassing cache (128-bit), size = 896 B, loops = 533198862, 91122.0 MB/s
Sequential read bypassing cache (128-bit), size = 1024 B, loops = 447086592, 87313.2 MB/s
Sequential read bypassing cache (128-bit), size = 1280 B, loops = 359813364, 87840.6 MB/s
Sequential read bypassing cache (128-bit), size = 2 kB, loops = 229900288, 89795.9 MB/s
Sequential read bypassing cache (128-bit), size = 3 kB, loops = 154793670, 90687.9 MB/s
Sequential read bypassing cache (128-bit), size = 4 kB, loops = 116277248, 90837.5 MB/s
Sequential read bypassing cache (128-bit), size = 6 kB, loops = 77611732, 90939.4 MB/s
Sequential read bypassing cache (128-bit), size = 8 kB, loops = 58228736, 90976.2 MB/s
Sequential read bypassing cache (128-bit), size = 12 kB, loops = 36768913, 86175.4 MB/s
Sequential read bypassing cache (128-bit), size = 16 kB, loops = 27959296, 87370.2 MB/s
Sequential read bypassing cache (128-bit), size = 20 kB, loops = 22558536, 88118.6 MB/s
Sequential read bypassing cache (128-bit), size = 24 kB, loops = 18910710, 88640.4 MB/s
Sequential read bypassing cache (128-bit), size = 28 kB, loops = 16260660, 88920.5 MB/s
Sequential read bypassing cache (128-bit), size = 32 kB, loops = 14213120, 88823.6 MB/s
Sequential read bypassing cache (128-bit), size = 34 kB, loops = 8332348, 55328.4 MB/s
Sequential read bypassing cache (128-bit), size = 36 kB, loops = 6366360, 44755.6 MB/s
Sequential read bypassing cache (128-bit), size = 40 kB, loops = 5718258, 44665.9 MB/s
Sequential read bypassing cache (128-bit), size = 48 kB, loops = 4787055, 44869.1 MB/s
Sequential read bypassing cache (128-bit), size = 64 kB, loops = 3570688, 44625.1 MB/s
Sequential read bypassing cache (128-bit), size = 128 kB, loops = 1756160, 43892.5 MB/s
Sequential read bypassing cache (128-bit), size = 192 kB, loops = 1161787, 43555.4 MB/s
Sequential read bypassing cache (128-bit), size = 256 kB, loops = 849408, 42462.7 MB/s
Sequential read bypassing cache (128-bit), size = 320 kB, loops = 525504, 32837.2 MB/s
Sequential read bypassing cache (128-bit), size = 384 kB, loops = 348500, 26127.2 MB/s
Sequential read bypassing cache (128-bit), size = 512 kB, loops = 255232, 25512.3 MB/s
Sequential read bypassing cache (128-bit), size = 768 kB, loops = 169915, 25475.4 MB/s
Sequential read bypassing cache (128-bit), size = 1 MB, loops = 127424, 25475.0 MB/s
Sequential read bypassing cache (128-bit), size = 1.25 MB, loops = 101949, 25479.0 MB/s
Sequential read bypassing cache (128-bit), size = 1.5 MB, loops = 84966, 25478.6 MB/s
Sequential read bypassing cache (128-bit), size = 1.75 MB, loops = 72792, 25472.1 MB/s
Sequential read bypassing cache (128-bit), size = 2 MB, loops = 63680, 25471.2 MB/s
Sequential read bypassing cache (128-bit), size = 2.25 MB, loops = 56224, 25297.0 MB/s
Sequential read bypassing cache (128-bit), size = 2.5 MB, loops = 50400, 25198.2 MB/s
Sequential read bypassing cache (128-bit), size = 2.75 MB, loops = 45816, 25197.6 MB/s
Sequential read bypassing cache (128-bit), size = 3 MB, loops = 42021, 25200.4 MB/s
Sequential read bypassing cache (128-bit), size = 3.25 MB, loops = 38779, 25202.0 MB/s
Sequential read bypassing cache (128-bit), size = 3.5 MB, loops = 36018, 25200.1 MB/s
Sequential read bypassing cache (128-bit), size = 4 MB, loops = 32032, 25614.9 MB/s
Sequential read bypassing cache (128-bit), size = 5 MB, loops = 25596, 25588.8 MB/s
Sequential read bypassing cache (128-bit), size = 6 MB, loops = 21350, 25611.2 MB/s
Sequential read bypassing cache (128-bit), size = 7 MB, loops = 18288, 25592.0 MB/s
Sequential read bypassing cache (128-bit), size = 8 MB, loops = 16008, 25612.7 MB/s
Sequential read bypassing cache (128-bit), size = 9 MB, loops = 14224, 25597.7 MB/s
Sequential read bypassing cache (128-bit), size = 10 MB, loops = 12810, 25609.8 MB/s
Sequential read bypassing cache (128-bit), size = 12 MB, loops = 10675, 25610.0 MB/s
Sequential read bypassing cache (128-bit), size = 14 MB, loops = 9148, 25608.6 MB/s
Sequential read bypassing cache (128-bit), size = 15 MB, loops = 8536, 25597.3 MB/s
Sequential read bypassing cache (128-bit), size = 16 MB, loops = 8004, 25607.8 MB/s
Sequential read bypassing cache (128-bit), size = 20 MB, loops = 6402, 25604.9 MB/s
Sequential read bypassing cache (128-bit), size = 21 MB, loops = 6096, 25602.1 MB/s
Sequential read bypassing cache (128-bit), size = 32 MB, loops = 950, 6074.0 MB/s
Sequential read bypassing cache (128-bit), size = 48 MB, loops = 445, 4266.4 MB/s
Sequential read bypassing cache (128-bit), size = 64 MB, loops = 315, 4021.3 MB/s
Sequential read bypassing cache (128-bit), size = 72 MB, loops = 279, 4012.3 MB/s
Sequential read bypassing cache (128-bit), size = 96 MB, loops = 209, 4009.1 MB/s
Sequential read bypassing cache (128-bit), size = 128 MB, loops = 157, 4009.1 MB/s

Random read bypassing cache (128-bit), size = 256 B, loops = 1148715008, 56084.6 MB/s
Random read bypassing cache (128-bit), size = 512 B, loops = 574357504, 56081.2 MB/s
Random read bypassing cache (128-bit), size = 768 B, loops = 377136396, 55235.7 MB/s
Random read bypassing cache (128-bit), size = 1024 B, loops = 283770880, 55418.6 MB/s
Random read bypassing cache (128-bit), size = 1280 B, loops = 226541388, 55299.7 MB/s
Random read bypassing cache (128-bit), size = 2 kB, loops = 130973696, 51151.4 MB/s
Random read bypassing cache (128-bit), size = 3 kB, loops = 89892175, 52666.3 MB/s
Random read bypassing cache (128-bit), size = 4 kB, loops = 65437696, 51116.8 MB/s
Random read bypassing cache (128-bit), size = 6 kB, loops = 43491404, 50966.2 MB/s
Random read bypassing cache (128-bit), size = 8 kB, loops = 32718848, 51117.9 MB/s
Random read bypassing cache (128-bit), size = 12 kB, loops = 21379815, 50098.2 MB/s
Random read bypassing cache (128-bit), size = 16 kB, loops = 16232448, 50719.2 MB/s
Random read bypassing cache (128-bit), size = 20 kB, loops = 13045032, 50946.8 MB/s
Random read bypassing cache (128-bit), size = 24 kB, loops = 10906350, 51122.4 MB/s
Random read bypassing cache (128-bit), size = 28 kB, loops = 9207900, 50343.1 MB/s
Random read bypassing cache (128-bit), size = 32 kB, loops = 7569408, 47303.6 MB/s
Random read bypassing cache (128-bit), size = 34 kB, loops = 6322487, 41973.9 MB/s
Random read bypassing cache (128-bit), size = 36 kB, loops = 5328960, 37465.6 MB/s
Random read bypassing cache (128-bit), size = 40 kB, loops = 4591314, 35861.0 MB/s
Random read bypassing cache (128-bit), size = 48 kB, loops = 3731910, 34982.4 MB/s
Random read bypassing cache (128-bit), size = 64 kB, loops = 2763776, 34545.0 MB/s
Random read bypassing cache (128-bit), size = 128 kB, loops = 1350144, 33748.4 MB/s
Random read bypassing cache (128-bit), size = 192 kB, loops = 895125, 33554.8 MB/s
Random read bypassing cache (128-bit), size = 256 kB, loops = 616960, 30840.5 MB/s
Random read bypassing cache (128-bit), size = 320 kB, loops = 350676, 21914.3 MB/s
Random read bypassing cache (128-bit), size = 384 kB, loops = 281690, 21116.3 MB/s
Random read bypassing cache (128-bit), size = 512 kB, loops = 204416, 20438.0 MB/s
Random read bypassing cache (128-bit), size = 768 kB, loops = 132175, 19815.8 MB/s
Random read bypassing cache (128-bit), size = 1 MB, loops = 97792, 19558.2 MB/s
Random read bypassing cache (128-bit), size = 1.25 MB, loops = 77724, 19422.2 MB/s
Random read bypassing cache (128-bit), size = 1.5 MB, loops = 64428, 19320.2 MB/s
Random read bypassing cache (128-bit), size = 1.75 MB, loops = 55080, 19270.1 MB/s
Random read bypassing cache (128-bit), size = 2 MB, loops = 47936, 19168.2 MB/s
Random read bypassing cache (128-bit), size = 2.25 MB, loops = 40656, 18286.5 MB/s
Random read bypassing cache (128-bit), size = 2.5 MB, loops = 35175, 17579.8 MB/s
Random read bypassing cache (128-bit), size = 2.75 MB, loops = 31349, 17238.2 MB/s
Random read bypassing cache (128-bit), size = 3 MB, loops = 28203, 16921.1 MB/s
Random read bypassing cache (128-bit), size = 3.25 MB, loops = 25707, 16709.4 MB/s
Random read bypassing cache (128-bit), size = 3.5 MB, loops = 23490, 16431.6 MB/s
Random read bypassing cache (128-bit), size = 4 MB, loops = 25600, 20469.3 MB/s
Random read bypassing cache (128-bit), size = 5 MB, loops = 20184, 20181.7 MB/s
Random read bypassing cache (128-bit), size = 6 MB, loops = 17040, 20441.5 MB/s
Random read bypassing cache (128-bit), size = 7 MB, loops = 14463, 20240.4 MB/s
Random read bypassing cache (128-bit), size = 8 MB, loops = 12776, 20430.3 MB/s
Random read bypassing cache (128-bit), size = 9 MB, loops = 11263, 20269.2 MB/s
Random read bypassing cache (128-bit), size = 10 MB, loops = 10206, 20410.3 MB/s
Random read bypassing cache (128-bit), size = 12 MB, loops = 8505, 20405.1 MB/s
Random read bypassing cache (128-bit), size = 14 MB, loops = 7288, 20398.7 MB/s
Random read bypassing cache (128-bit), size = 15 MB, loops = 6768, 20300.3 MB/s
Random read bypassing cache (128-bit), size = 16 MB, loops = 6376, 20391.5 MB/s
Random read bypassing cache (128-bit), size = 20 MB, loops = 5097, 20387.9 MB/s
Random read bypassing cache (128-bit), size = 21 MB, loops = 4839, 20320.4 MB/s
Random read bypassing cache (128-bit), size = 32 MB, loops = 324, 2069.5 MB/s
Random read bypassing cache (128-bit), size = 48 MB, loops = 179, 1709.8 MB/s
Random read bypassing cache (128-bit), size = 64 MB, loops = 131, 1673.0 MB/s
Random read bypassing cache (128-bit), size = 72 MB, loops = 116, 1661.2 MB/s
Random read bypassing cache (128-bit), size = 96 MB, loops = 86, 1638.3 MB/s
Random read bypassing cache (128-bit), size = 128 MB, loops = 64, 1623.6 MB/s

Sequential write bypassing cache (128-bit), size = 128 B, loops = 12058624, 288.8 MB/s
Sequential write bypassing cache (128-bit), size = 256 B, loops = 11796480, 563.8 MB/s
Sequential write bypassing cache (128-bit), size = 384 B, loops = 11184768, 811.9 MB/s
Sequential write bypassing cache (128-bit), size = 512 B, loops = 10878976, 1052.9 MB/s
Sequential write bypassing cache (128-bit), size = 640 B, loops = 10066272, 1226.0 MB/s
Sequential write bypassing cache (128-bit), size = 768 B, loops = 8912862, 1294.6 MB/s
Sequential write bypassing cache (128-bit), size = 896 B, loops = 7639596, 1301.4 MB/s
Sequential write bypassing cache (128-bit), size = 1024 B, loops = 7012352, 1357.1 MB/s
Sequential write bypassing cache (128-bit), size = 1280 B, loops = 5714652, 1392.4 MB/s
Sequential write bypassing cache (128-bit), size = 2 kB, loops = 3637248, 1416.8 MB/s
Sequential write bypassing cache (128-bit), size = 3 kB, loops = 2446640, 1428.4 MB/s
Sequential write bypassing cache (128-bit), size = 4 kB, loops = 1818624, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 6 kB, loops = 1223264, 1421.6 MB/s
Sequential write bypassing cache (128-bit), size = 8 kB, loops = 917504, 1421.6 MB/s
Sequential write bypassing cache (128-bit), size = 12 kB, loops = 611632, 1421.8 MB/s
Sequential write bypassing cache (128-bit), size = 16 kB, loops = 458752, 1421.1 MB/s
Sequential write bypassing cache (128-bit), size = 20 kB, loops = 366912, 1420.9 MB/s
Sequential write bypassing cache (128-bit), size = 24 kB, loops = 305760, 1421.0 MB/s
Sequential write bypassing cache (128-bit), size = 28 kB, loops = 262080, 1421.6 MB/s
Sequential write bypassing cache (128-bit), size = 32 kB, loops = 227328, 1420.3 MB/s
Sequential write bypassing cache (128-bit), size = 34 kB, loops = 215824, 1420.9 MB/s
Sequential write bypassing cache (128-bit), size = 36 kB, loops = 202020, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 40 kB, loops = 183456, 1420.7 MB/s
Sequential write bypassing cache (128-bit), size = 48 kB, loops = 151515, 1420.4 MB/s
Sequential write bypassing cache (128-bit), size = 64 kB, loops = 113664, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 128 kB, loops = 57344, 1420.9 MB/s
Sequential write bypassing cache (128-bit), size = 192 kB, loops = 38192, 1419.6 MB/s
Sequential write bypassing cache (128-bit), size = 256 kB, loops = 28672, 1421.2 MB/s
Sequential write bypassing cache (128-bit), size = 320 kB, loops = 22848, 1420.9 MB/s
Sequential write bypassing cache (128-bit), size = 384 kB, loops = 19040, 1420.8 MB/s
Sequential write bypassing cache (128-bit), size = 512 kB, loops = 14208, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 768 kB, loops = 9520, 1420.6 MB/s
Sequential write bypassing cache (128-bit), size = 1 MB, loops = 7104, 1420.6 MB/s
Sequential write bypassing cache (128-bit), size = 1.25 MB, loops = 5712, 1420.4 MB/s
Sequential write bypassing cache (128-bit), size = 1.5 MB, loops = 4746, 1420.8 MB/s
Sequential write bypassing cache (128-bit), size = 1.75 MB, loops = 4068, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 2 MB, loops = 3552, 1420.3 MB/s
Sequential write bypassing cache (128-bit), size = 2.25 MB, loops = 3164, 1420.3 MB/s
Sequential write bypassing cache (128-bit), size = 2.5 MB, loops = 2850, 1420.0 MB/s
Sequential write bypassing cache (128-bit), size = 2.75 MB, loops = 2599, 1419.9 MB/s
Sequential write bypassing cache (128-bit), size = 3 MB, loops = 2373, 1420.4 MB/s
Sequential write bypassing cache (128-bit), size = 3.25 MB, loops = 2204, 1420.5 MB/s
Sequential write bypassing cache (128-bit), size = 3.5 MB, loops = 2034, 1420.1 MB/s
Sequential write bypassing cache (128-bit), size = 4 MB, loops = 1776, 1419.7 MB/s
Sequential write bypassing cache (128-bit), size = 5 MB, loops = 1428, 1419.3 MB/s
Sequential write bypassing cache (128-bit), size = 6 MB, loops = 1190, 1419.2 MB/s
Sequential write bypassing cache (128-bit), size = 7 MB, loops = 1017, 1418.8 MB/s
Sequential write bypassing cache (128-bit), size = 8 MB, loops = 888, 1418.3 MB/s
Sequential write bypassing cache (128-bit), size = 9 MB, loops = 791, 1417.8 MB/s
Sequential write bypassing cache (128-bit), size = 10 MB, loops = 714, 1417.3 MB/s
Sequential write bypassing cache (128-bit), size = 12 MB, loops = 595, 1417.1 MB/s
Sequential write bypassing cache (128-bit), size = 14 MB, loops = 508, 1416.4 MB/s
Sequential write bypassing cache (128-bit), size = 15 MB, loops = 476, 1416.1 MB/s
Sequential write bypassing cache (128-bit), size = 16 MB, loops = 444, 1415.5 MB/s
Sequential write bypassing cache (128-bit), size = 20 MB, loops = 354, 1414.2 MB/s
Sequential write bypassing cache (128-bit), size = 21 MB, loops = 339, 1414.1 MB/s
Sequential write bypassing cache (128-bit), size = 32 MB, loops = 222, 1410.5 MB/s
Sequential write bypassing cache (128-bit), size = 48 MB, loops = 147, 1405.7 MB/s
Sequential write bypassing cache (128-bit), size = 64 MB, loops = 110, 1400.5 MB/s
Sequential write bypassing cache (128-bit), size = 72 MB, loops = 98, 1398.5 MB/s
Sequential write bypassing cache (128-bit), size = 96 MB, loops = 73, 1391.0 MB/s
Sequential write bypassing cache (128-bit), size = 128 MB, loops = 54, 1380.6 MB/s

Sequential write bypassing cache (256-bit), size = 256 B, loops = 1859387392, 90777.6 MB/s
Sequential write bypassing cache (256-bit), size = 512 B, loops = 929955840, 90805.7 MB/s
Sequential write bypassing cache (256-bit), size = 768 B, loops = 1048572, 144.5 MB/s
Sequential write bypassing cache (256-bit), size = 1024 B, loops = 655360, 116.2 MB/s
Sequential write bypassing cache (256-bit), size = 1280 B, loops = 471852, 114.5 MB/s
Sequential write bypassing cache (256-bit), size = 2 kB, loops = 327680, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 3 kB, loops = 218450, 116.2 MB/s
Sequential write bypassing cache (256-bit), size = 4 kB, loops = 163840, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 6 kB, loops = 109220, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 8 kB, loops = 81920, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 12 kB, loops = 54610, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 16 kB, loops = 40960, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 20 kB, loops = 32760, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 24 kB, loops = 27300, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 28 kB, loops = 23400, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 32 kB, loops = 20480, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 34 kB, loops = 19270, 115.8 MB/s
Sequential write bypassing cache (256-bit), size = 36 kB, loops = 18200, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 40 kB, loops = 16380, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 48 kB, loops = 13650, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 64 kB, loops = 10240, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 128 kB, loops = 5120, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 192 kB, loops = 3410, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 256 kB, loops = 2560, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 320 kB, loops = 2040, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 384 kB, loops = 1700, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 512 kB, loops = 1280, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 768 kB, loops = 850, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 1 MB, loops = 640, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 1.25 MB, loops = 510, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 1.5 MB, loops = 420, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 1.75 MB, loops = 360, 115.9 MB/s
Sequential write bypassing cache (256-bit), size = 2 MB, loops = 320, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 2.25 MB, loops = 280, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 2.5 MB, loops = 250, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 2.75 MB, loops = 230, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 3 MB, loops = 210, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 3.25 MB, loops = 190, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 3.5 MB, loops = 180, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 4 MB, loops = 160, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 5 MB, loops = 120, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 6 MB, loops = 100, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 7 MB, loops = 90, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 8 MB, loops = 80, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 9 MB, loops = 70, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 10 MB, loops = 60, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 12 MB, loops = 50, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 14 MB, loops = 44, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 15 MB, loops = 40, 116.0 MB/s
Sequential write bypassing cache (256-bit), size = 16 MB, loops = 40, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 20 MB, loops = 30, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 21 MB, loops = 30, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 32 MB, loops = 20, 116.1 MB/s
Sequential write bypassing cache (256-bit), size = 48 MB, loops = 13, 116.2 MB/s
Sequential write bypassing cache (256-bit), size = 64 MB, loops = 10, 116.2 MB/s
Sequential write bypassing cache (256-bit), size = 72 MB, loops = 9, 116.3 MB/s
Sequential write bypassing cache (256-bit), size = 96 MB, loops = 7, 116.4 MB/s
Sequential write bypassing cache (256-bit), size = 128 MB, loops = 5, 116.5 MB/s

Random write bypassing cache (128-bit), size = 256 B, loops = 10485760, 508.1 MB/s
Random write bypassing cache (128-bit), size = 512 B, loops = 8912896, 867.3 MB/s
Random write bypassing cache (128-bit), size = 768 B, loops = 4631193, 677.7 MB/s
Random write bypassing cache (128-bit), size = 1024 B, loops = 3997696, 776.6 MB/s
Random write bypassing cache (128-bit), size = 1280 B, loops = 3198108, 778.5 MB/s
Random write bypassing cache (128-bit), size = 2 kB, loops = 2162688, 837.0 MB/s
Random write bypassing cache (128-bit), size = 3 kB, loops = 1463615, 845.0 MB/s
Random write bypassing cache (128-bit), size = 4 kB, loops = 1081344, 844.2 MB/s
Random write bypassing cache (128-bit), size = 6 kB, loops = 731774, 845.2 MB/s
Random write bypassing cache (128-bit), size = 8 kB, loops = 540672, 844.4 MB/s
Random write bypassing cache (128-bit), size = 12 kB, loops = 360426, 840.4 MB/s
Random write bypassing cache (128-bit), size = 16 kB, loops = 270336, 841.6 MB/s
Random write bypassing cache (128-bit), size = 20 kB, loops = 216216, 842.7 MB/s
Random write bypassing cache (128-bit), size = 24 kB, loops = 180180, 841.2 MB/s
Random write bypassing cache (128-bit), size = 28 kB, loops = 154440, 843.4 MB/s
Random write bypassing cache (128-bit), size = 32 kB, loops = 135168, 843.8 MB/s
Random write bypassing cache (128-bit), size = 34 kB, loops = 127182, 843.2 MB/s
Random write bypassing cache (128-bit), size = 36 kB, loops = 120120, 843.9 MB/s
Random write bypassing cache (128-bit), size = 40 kB, loops = 108108, 842.2 MB/s
Random write bypassing cache (128-bit), size = 48 kB, loops = 91455, 846.0 MB/s
Random write bypassing cache (128-bit), size = 64 kB, loops = 67584, 842.0 MB/s
Random write bypassing cache (128-bit), size = 128 kB, loops = 33792, 843.6 MB/s
Random write bypassing cache (128-bit), size = 192 kB, loops = 22506, 841.9 MB/s
Random write bypassing cache (128-bit), size = 256 kB, loops = 16896, 842.7 MB/s
Random write bypassing cache (128-bit), size = 320 kB, loops = 13668, 843.5 MB/s
Random write bypassing cache (128-bit), size = 384 kB, loops = 11390, 842.3 MB/s
Random write bypassing cache (128-bit), size = 512 kB, loops = 8448, 842.7 MB/s
Random write bypassing cache (128-bit), size = 768 kB, loops = 5695, 842.5 MB/s
Random write bypassing cache (128-bit), size = 1 MB, loops = 4224, 842.6 MB/s
Random write bypassing cache (128-bit), size = 1.25 MB, loops = 3417, 843.0 MB/s
Random write bypassing cache (128-bit), size = 1.5 MB, loops = 2814, 843.3 MB/s
Random write bypassing cache (128-bit), size = 1.75 MB, loops = 2412, 843.4 MB/s
Random write bypassing cache (128-bit), size = 2 MB, loops = 2112, 842.8 MB/s
Random write bypassing cache (128-bit), size = 2.25 MB, loops = 1876, 842.7 MB/s
Random write bypassing cache (128-bit), size = 2.5 MB, loops = 1700, 842.3 MB/s
Random write bypassing cache (128-bit), size = 2.75 MB, loops = 1541, 841.6 MB/s
Random write bypassing cache (128-bit), size = 3 MB, loops = 1407, 841.5 MB/s
Random write bypassing cache (128-bit), size = 3.25 MB, loops = 1311, 841.1 MB/s
Random write bypassing cache (128-bit), size = 3.5 MB, loops = 1206, 841.5 MB/s
Random write bypassing cache (128-bit), size = 4 MB, loops = 1056, 842.3 MB/s
Random write bypassing cache (128-bit), size = 5 MB, loops = 852, 842.0 MB/s
Random write bypassing cache (128-bit), size = 6 MB, loops = 710, 842.0 MB/s
Random write bypassing cache (128-bit), size = 7 MB, loops = 603, 841.6 MB/s
Random write bypassing cache (128-bit), size = 8 MB, loops = 528, 841.1 MB/s
Random write bypassing cache (128-bit), size = 9 MB, loops = 469, 841.4 MB/s
Random write bypassing cache (128-bit), size = 10 MB, loops = 426, 841.0 MB/s
Random write bypassing cache (128-bit), size = 12 MB, loops = 355, 840.9 MB/s
Random write bypassing cache (128-bit), size = 14 MB, loops = 304, 840.7 MB/s
Random write bypassing cache (128-bit), size = 15 MB, loops = 284, 840.5 MB/s
Random write bypassing cache (128-bit), size = 16 MB, loops = 264, 839.9 MB/s
Random write bypassing cache (128-bit), size = 20 MB, loops = 210, 839.6 MB/s
Random write bypassing cache (128-bit), size = 21 MB, loops = 201, 839.3 MB/s
Random write bypassing cache (128-bit), size = 32 MB, loops = 132, 837.3 MB/s
Random write bypassing cache (128-bit), size = 48 MB, loops = 87, 834.1 MB/s
Random write bypassing cache (128-bit), size = 64 MB, loops = 65, 831.4 MB/s
Random write bypassing cache (128-bit), size = 72 MB, loops = 58, 830.0 MB/s
Random write bypassing cache (128-bit), size = 96 MB, loops = 43, 824.0 MB/s
Random write bypassing cache (128-bit), size = 128 MB, loops = 32, 817.3 MB/s

Sequential read (64-bit), size = 128 B, loops = 1866989568, 45575.1 MB/s
Sequential read (64-bit), size = 256 B, loops = 933494784, 45574.1 MB/s
Sequential read (64-bit), size = 384 B, loops = 622327482, 45571.7 MB/s
Sequential read (64-bit), size = 512 B, loops = 466747392, 45573.1 MB/s
Sequential read (64-bit), size = 640 B, loops = 373395777, 45574.8 MB/s
Sequential read (64-bit), size = 768 B, loops = 311163741, 45572.2 MB/s
Sequential read (64-bit), size = 896 B, loops = 266711778, 45572.7 MB/s
Sequential read (64-bit), size = 1024 B, loops = 233373696, 45570.9 MB/s
Sequential read (64-bit), size = 1280 B, loops = 186696108, 45572.8 MB/s
Sequential read (64-bit), size = 2 kB, loops = 116686848, 45570.8 MB/s
Sequential read (64-bit), size = 3 kB, loops = 77790045, 45570.6 MB/s
Sequential read (64-bit), size = 4 kB, loops = 58343424, 45571.4 MB/s
Sequential read (64-bit), size = 6 kB, loops = 38893242, 45572.6 MB/s
Sequential read (64-bit), size = 8 kB, loops = 28794880, 44985.6 MB/s
Sequential read (64-bit), size = 12 kB, loops = 19047968, 44642.0 MB/s
Sequential read (64-bit), size = 16 kB, loops = 14360576, 44872.2 MB/s
Sequential read (64-bit), size = 20 kB, loops = 11524968, 45016.1 MB/s
Sequential read (64-bit), size = 24 kB, loops = 9623250, 45108.3 MB/s
Sequential read (64-bit), size = 28 kB, loops = 8260200, 45162.5 MB/s
Sequential read (64-bit), size = 32 kB, loops = 7227392, 45165.7 MB/s
Sequential read (64-bit), size = 34 kB, loops = 5403308, 35879.8 MB/s
Sequential read (64-bit), size = 36 kB, loops = 4571840, 32136.8 MB/s
Sequential read (64-bit), size = 40 kB, loops = 4113018, 32122.1 MB/s
Sequential read (64-bit), size = 48 kB, loops = 3415230, 32011.1 MB/s
Sequential read (64-bit), size = 64 kB, loops = 2566144, 32073.0 MB/s
Sequential read (64-bit), size = 128 kB, loops = 1279488, 31982.6 MB/s
Sequential read (64-bit), size = 192 kB, loops = 849772, 31855.3 MB/s
Sequential read (64-bit), size = 256 kB, loops = 632064, 31600.0 MB/s
Sequential read (64-bit), size = 320 kB, loops = 337416, 21080.2 MB/s
Sequential read (64-bit), size = 384 kB, loops = 276930, 20769.5 MB/s
Sequential read (64-bit), size = 512 kB, loops = 207616, 20749.6 MB/s
Sequential read (64-bit), size = 768 kB, loops = 138380, 20747.1 MB/s
Sequential read (64-bit), size = 1 MB, loops = 103744, 20743.4 MB/s
Sequential read (64-bit), size = 1.25 MB, loops = 82977, 20743.0 MB/s
Sequential read (64-bit), size = 1.5 MB, loops = 69174, 20740.2 MB/s
Sequential read (64-bit), size = 1.75 MB, loops = 59256, 20736.8 MB/s
Sequential read (64-bit), size = 2 MB, loops = 51840, 20732.2 MB/s
Sequential read (64-bit), size = 2.25 MB, loops = 45696, 20561.5 MB/s
Sequential read (64-bit), size = 2.5 MB, loops = 40925, 20461.1 MB/s
Sequential read (64-bit), size = 2.75 MB, loops = 37214, 20455.5 MB/s
Sequential read (64-bit), size = 3 MB, loops = 34104, 20455.6 MB/s
Sequential read (64-bit), size = 3.25 MB, loops = 31483, 20456.0 MB/s
Sequential read (64-bit), size = 3.5 MB, loops = 29232, 20457.4 MB/s
Sequential read (64-bit), size = 4 MB, loops = 26288, 21018.9 MB/s
Sequential read (64-bit), size = 5 MB, loops = 20976, 20968.2 MB/s
Sequential read (64-bit), size = 6 MB, loops = 17520, 21018.3 MB/s
Sequential read (64-bit), size = 7 MB, loops = 14985, 20977.0 MB/s
Sequential read (64-bit), size = 8 MB, loops = 13144, 21020.8 MB/s
Sequential read (64-bit), size = 9 MB, loops = 11662, 20987.4 MB/s
Sequential read (64-bit), size = 10 MB, loops = 10512, 21015.8 MB/s
Sequential read (64-bit), size = 12 MB, loops = 8760, 21019.6 MB/s
Sequential read (64-bit), size = 14 MB, loops = 7508, 21014.7 MB/s
Sequential read (64-bit), size = 15 MB, loops = 7000, 20994.1 MB/s
Sequential read (64-bit), size = 16 MB, loops = 6568, 21014.2 MB/s
Sequential read (64-bit), size = 20 MB, loops = 5256, 21014.2 MB/s
Sequential read (64-bit), size = 21 MB, loops = 5001, 21003.7 MB/s
Sequential read (64-bit), size = 32 MB, loops = 810, 5172.2 MB/s
Sequential read (64-bit), size = 48 MB, loops = 363, 3478.8 MB/s
Sequential read (64-bit), size = 64 MB, loops = 279, 3564.6 MB/s
Sequential read (64-bit), size = 72 MB, loops = 248, 3557.8 MB/s
Sequential read (64-bit), size = 96 MB, loops = 186, 3553.0 MB/s
Sequential read (64-bit), size = 128 MB, loops = 139, 3553.7 MB/s

Random read (64-bit), size = 256 B, loops = 649330688, 31703.1 MB/s
Random read (64-bit), size = 512 B, loops = 327680000, 31989.3 MB/s
Random read (64-bit), size = 768 B, loops = 217666071, 31872.9 MB/s
Random read (64-bit), size = 1024 B, loops = 163053568, 31836.6 MB/s
Random read (64-bit), size = 1280 B, loops = 130807860, 31924.2 MB/s
Random read (64-bit), size = 2 kB, loops = 81264640, 31738.9 MB/s
Random read (64-bit), size = 3 kB, loops = 54306670, 31815.2 MB/s
Random read (64-bit), size = 4 kB, loops = 40681472, 31770.9 MB/s
Random read (64-bit), size = 6 kB, loops = 27130248, 31791.1 MB/s
Random read (64-bit), size = 8 kB, loops = 20357120, 31798.2 MB/s
Random read (64-bit), size = 12 kB, loops = 13532358, 31707.7 MB/s
Random read (64-bit), size = 16 kB, loops = 10166272, 31762.6 MB/s
Random read (64-bit), size = 20 kB, loops = 8140860, 31795.3 MB/s
Random read (64-bit), size = 24 kB, loops = 6857760, 32135.4 MB/s
Random read (64-bit), size = 28 kB, loops = 5791500, 31660.7 MB/s
Random read (64-bit), size = 32 kB, loops = 4608000, 28798.4 MB/s
Random read (64-bit), size = 34 kB, loops = 3854000, 25585.0 MB/s
Random read (64-bit), size = 36 kB, loops = 3161340, 22220.7 MB/s
Random read (64-bit), size = 40 kB, loops = 2791152, 21800.6 MB/s
Random read (64-bit), size = 48 kB, loops = 2293200, 21486.3 MB/s
Random read (64-bit), size = 64 kB, loops = 1698816, 21228.4 MB/s
Random read (64-bit), size = 128 kB, loops = 836096, 20902.4 MB/s
Random read (64-bit), size = 192 kB, loops = 552079, 20699.6 MB/s
Random read (64-bit), size = 256 kB, loops = 375808, 18786.3 MB/s
Random read (64-bit), size = 320 kB, loops = 222972, 13932.0 MB/s
Random read (64-bit), size = 384 kB, loops = 177650, 13318.2 MB/s
Random read (64-bit), size = 512 kB, loops = 126848, 12678.4 MB/s
Random read (64-bit), size = 768 kB, loops = 81175, 12168.7 MB/s
Random read (64-bit), size = 1 MB, loops = 59904, 11973.9 MB/s
Random read (64-bit), size = 1.25 MB, loops = 47532, 11875.1 MB/s
Random read (64-bit), size = 1.5 MB, loops = 39270, 11779.3 MB/s
Random read (64-bit), size = 1.75 MB, loops = 33552, 11740.6 MB/s
Random read (64-bit), size = 2 MB, loops = 29152, 11655.1 MB/s
Random read (64-bit), size = 2.25 MB, loops = 24752, 11129.6 MB/s
Random read (64-bit), size = 2.5 MB, loops = 21525, 10758.3 MB/s
Random read (64-bit), size = 2.75 MB, loops = 19297, 10602.3 MB/s
Random read (64-bit), size = 3 MB, loops = 17388, 10421.3 MB/s
Random read (64-bit), size = 3.25 MB, loops = 15846, 10290.3 MB/s
Random read (64-bit), size = 3.5 MB, loops = 14544, 10174.2 MB/s
Random read (64-bit), size = 4 MB, loops = 15744, 12592.5 MB/s
Random read (64-bit), size = 5 MB, loops = 12384, 12383.3 MB/s
Random read (64-bit), size = 6 MB, loops = 10450, 12538.3 MB/s
Random read (64-bit), size = 7 MB, loops = 8829, 12349.1 MB/s
Random read (64-bit), size = 8 MB, loops = 7832, 12523.9 MB/s
Random read (64-bit), size = 9 MB, loops = 6902, 12412.1 MB/s
Random read (64-bit), size = 10 MB, loops = 6228, 12451.4 MB/s
Random read (64-bit), size = 12 MB, loops = 5190, 12453.6 MB/s
Random read (64-bit), size = 14 MB, loops = 4456, 12471.1 MB/s
Random read (64-bit), size = 15 MB, loops = 4124, 12362.3 MB/s
Random read (64-bit), size = 16 MB, loops = 3896, 12458.0 MB/s
Random read (64-bit), size = 20 MB, loops = 3111, 12436.0 MB/s
Random read (64-bit), size = 21 MB, loops = 2910, 12220.8 MB/s
Random read (64-bit), size = 32 MB, loops = 220, 1398.5 MB/s
Random read (64-bit), size = 48 MB, loops = 115, 1103.9 MB/s
Random read (64-bit), size = 64 MB, loops = 83, 1056.4 MB/s
Random read (64-bit), size = 72 MB, loops = 73, 1039.9 MB/s
Random read (64-bit), size = 96 MB, loops = 53, 1004.3 MB/s
Random read (64-bit), size = 128 MB, loops = 39, 979.8 MB/s

Sequential write (64-bit), size = 128 B, loops = 891813888, 21766.6 MB/s
Sequential write (64-bit), size = 256 B, loops = 452722688, 22097.0 MB/s
Sequential write (64-bit), size = 384 B, loops = 309503502, 22657.3 MB/s
Sequential write (64-bit), size = 512 B, loops = 232128512, 22661.3 MB/s
Sequential write (64-bit), size = 640 B, loops = 185911461, 22687.3 MB/s
Sequential write (64-bit), size = 768 B, loops = 155276037, 22745.1 MB/s
Sequential write (64-bit), size = 896 B, loops = 133018848, 22722.1 MB/s
Sequential write (64-bit), size = 1024 B, loops = 116457472, 22737.9 MB/s
Sequential write (64-bit), size = 1280 B, loops = 93269412, 22763.5 MB/s
Sequential write (64-bit), size = 2 kB, loops = 58294272, 22770.6 MB/s
Sequential write (64-bit), size = 3 kB, loops = 38884100, 22779.4 MB/s
Sequential write (64-bit), size = 4 kB, loops = 29163520, 22781.3 MB/s
Sequential write (64-bit), size = 6 kB, loops = 19452082, 22785.5 MB/s
Sequential write (64-bit), size = 8 kB, loops = 14589952, 22790.0 MB/s
Sequential write (64-bit), size = 12 kB, loops = 9687814, 22697.0 MB/s
Sequential write (64-bit), size = 16 kB, loops = 7274496, 22720.2 MB/s
Sequential write (64-bit), size = 20 kB, loops = 5821452, 22733.1 MB/s
Sequential write (64-bit), size = 24 kB, loops = 4853940, 22742.2 MB/s
Sequential write (64-bit), size = 28 kB, loops = 4160520, 22743.7 MB/s
Sequential write (64-bit), size = 32 kB, loops = 3639296, 22743.0 MB/s
Sequential write (64-bit), size = 34 kB, loops = 3185331, 21142.0 MB/s
Sequential write (64-bit), size = 36 kB, loops = 2881060, 20251.7 MB/s
Sequential write (64-bit), size = 40 kB, loops = 2592954, 20251.3 MB/s
Sequential write (64-bit), size = 48 kB, loops = 2160795, 20250.5 MB/s
Sequential write (64-bit), size = 64 kB, loops = 1620992, 20250.2 MB/s
Sequential write (64-bit), size = 128 kB, loops = 810496, 20254.8 MB/s
Sequential write (64-bit), size = 192 kB, loops = 540144, 20253.3 MB/s
Sequential write (64-bit), size = 256 kB, loops = 404992, 20242.0 MB/s
Sequential write (64-bit), size = 320 kB, loops = 309468, 19336.3 MB/s
Sequential write (64-bit), size = 384 kB, loops = 248540, 18636.9 MB/s
Sequential write (64-bit), size = 512 kB, loops = 173824, 17381.0 MB/s
Sequential write (64-bit), size = 768 kB, loops = 115855, 17374.5 MB/s
Sequential write (64-bit), size = 1 MB, loops = 86912, 17376.0 MB/s
Sequential write (64-bit), size = 1.25 MB, loops = 69564, 17379.0 MB/s
Sequential write (64-bit), size = 1.5 MB, loops = 57918, 17375.1 MB/s
Sequential write (64-bit), size = 1.75 MB, loops = 49644, 17366.4 MB/s
Sequential write (64-bit), size = 2 MB, loops = 43424, 17363.1 MB/s
Sequential write (64-bit), size = 2.25 MB, loops = 38164, 17169.7 MB/s
Sequential write (64-bit), size = 2.5 MB, loops = 34125, 17062.0 MB/s
Sequential write (64-bit), size = 2.75 MB, loops = 31050, 17067.5 MB/s
Sequential write (64-bit), size = 3 MB, loops = 28455, 17067.4 MB/s
Sequential write (64-bit), size = 3.25 MB, loops = 26258, 17066.5 MB/s
Sequential write (64-bit), size = 3.5 MB, loops = 24390, 17067.1 MB/s
Sequential write (64-bit), size = 4 MB, loops = 21712, 17358.3 MB/s
Sequential write (64-bit), size = 5 MB, loops = 17364, 17354.0 MB/s
Sequential write (64-bit), size = 6 MB, loops = 14460, 17349.5 MB/s
Sequential write (64-bit), size = 7 MB, loops = 12393, 17344.8 MB/s
Sequential write (64-bit), size = 8 MB, loops = 10840, 17340.2 MB/s
Sequential write (64-bit), size = 9 MB, loops = 9632, 17337.0 MB/s
Sequential write (64-bit), size = 10 MB, loops = 8670, 17332.9 MB/s
Sequential write (64-bit), size = 12 MB, loops = 7220, 17326.7 MB/s
Sequential write (64-bit), size = 14 MB, loops = 6188, 17317.5 MB/s
Sequential write (64-bit), size = 15 MB, loops = 5772, 17311.5 MB/s
Sequential write (64-bit), size = 16 MB, loops = 5412, 17311.1 MB/s
Sequential write (64-bit), size = 20 MB, loops = 4323, 17289.5 MB/s
Sequential write (64-bit), size = 21 MB, loops = 4116, 17287.0 MB/s
Sequential write (64-bit), size = 32 MB, loops = 514, 3278.4 MB/s
Sequential write (64-bit), size = 48 MB, loops = 261, 2499.6 MB/s
Sequential write (64-bit), size = 64 MB, loops = 190, 2431.8 MB/s
Sequential write (64-bit), size = 72 MB, loops = 169, 2432.4 MB/s
Sequential write (64-bit), size = 96 MB, loops = 126, 2409.3 MB/s
Sequential write (64-bit), size = 128 MB, loops = 94, 2393.1 MB/s

Random write (64-bit), size = 256 B, loops = 466878464, 22790.3 MB/s
Random write (64-bit), size = 512 B, loops = 233439232, 22789.0 MB/s
Random write (64-bit), size = 768 B, loops = 155625561, 22787.2 MB/s
Random write (64-bit), size = 1024 B, loops = 116719616, 22788.3 MB/s
Random write (64-bit), size = 1280 B, loops = 93374268, 22788.8 MB/s
Random write (64-bit), size = 2 kB, loops = 58359808, 22788.1 MB/s
Random write (64-bit), size = 3 kB, loops = 36939895, 21639.1 MB/s
Random write (64-bit), size = 4 kB, loops = 28688384, 22406.8 MB/s
Random write (64-bit), size = 6 kB, loops = 19408394, 22736.6 MB/s
Random write (64-bit), size = 8 kB, loops = 14565376, 22746.0 MB/s
Random write (64-bit), size = 12 kB, loops = 9726041, 22789.5 MB/s
Random write (64-bit), size = 16 kB, loops = 7155712, 22349.8 MB/s
Random write (64-bit), size = 20 kB, loops = 5808348, 22684.3 MB/s
Random write (64-bit), size = 24 kB, loops = 4788420, 22440.9 MB/s
Random write (64-bit), size = 28 kB, loops = 3942900, 21555.4 MB/s
Random write (64-bit), size = 32 kB, loops = 2822144, 17626.4 MB/s
Random write (64-bit), size = 34 kB, loops = 2011788, 13356.0 MB/s
Random write (64-bit), size = 36 kB, loops = 1355900, 9527.9 MB/s
Random write (64-bit), size = 40 kB, loops = 1220310, 9521.1 MB/s
Random write (64-bit), size = 48 kB, loops = 1014195, 9497.3 MB/s
Random write (64-bit), size = 64 kB, loops = 756736, 9446.9 MB/s
Random write (64-bit), size = 128 kB, loops = 381440, 9526.5 MB/s
Random write (64-bit), size = 192 kB, loops = 257114, 9630.2 MB/s
Random write (64-bit), size = 256 kB, loops = 179712, 8983.9 MB/s
Random write (64-bit), size = 320 kB, loops = 68136, 4252.2 MB/s
Random write (64-bit), size = 384 kB, loops = 51850, 3888.2 MB/s
Random write (64-bit), size = 512 kB, loops = 38400, 3832.3 MB/s
Random write (64-bit), size = 768 kB, loops = 25330, 3793.9 MB/s
Random write (64-bit), size = 1 MB, loops = 18944, 3780.1 MB/s
Random write (64-bit), size = 1.25 MB, loops = 15147, 3778.7 MB/s
Random write (64-bit), size = 1.5 MB, loops = 12600, 3776.5 MB/s
Random write (64-bit), size = 1.75 MB, loops = 10800, 3775.5 MB/s
Random write (64-bit), size = 2 MB, loops = 9440, 3774.1 MB/s
Random write (64-bit), size = 2.25 MB, loops = 8372, 3764.7 MB/s
Random write (64-bit), size = 2.5 MB, loops = 7525, 3760.0 MB/s
Random write (64-bit), size = 2.75 MB, loops = 6831, 3753.8 MB/s
Random write (64-bit), size = 3 MB, loops = 6258, 3747.8 MB/s
Random write (64-bit), size = 3.25 MB, loops = 5776, 3745.1 MB/s
Random write (64-bit), size = 3.5 MB, loops = 5346, 3739.9 MB/s
Random write (64-bit), size = 4 MB, loops = 4704, 3762.5 MB/s
Random write (64-bit), size = 5 MB, loops = 3768, 3758.7 MB/s
Random write (64-bit), size = 6 MB, loops = 3130, 3755.7 MB/s
Random write (64-bit), size = 7 MB, loops = 2682, 3753.0 MB/s
Random write (64-bit), size = 8 MB, loops = 2344, 3750.0 MB/s
Random write (64-bit), size = 9 MB, loops = 2086, 3747.3 MB/s
Random write (64-bit), size = 10 MB, loops = 1878, 3744.6 MB/s
Random write (64-bit), size = 12 MB, loops = 1560, 3738.6 MB/s
Random write (64-bit), size = 14 MB, loops = 1336, 3731.2 MB/s
Random write (64-bit), size = 15 MB, loops = 1244, 3727.4 MB/s
Random write (64-bit), size = 16 MB, loops = 1164, 3724.0 MB/s
Random write (64-bit), size = 20 MB, loops = 927, 3707.5 MB/s
Random write (64-bit), size = 21 MB, loops = 882, 3703.8 MB/s
Random write (64-bit), size = 32 MB, loops = 66, 415.3 MB/s
Random write (64-bit), size = 48 MB, loops = 32, 299.6 MB/s
Random write (64-bit), size = 64 MB, loops = 23, 290.6 MB/s
Random write (64-bit), size = 72 MB, loops = 21, 290.1 MB/s
Random write (64-bit), size = 96 MB, loops = 15, 287.9 MB/s
Random write (64-bit), size = 128 MB, loops = 12, 286.0 MB/s

Sequential copy (128-bit), size = 128 B, loops = 1866989568, 45571.9 MB/s
Sequential copy (128-bit), size = 256 B, loops = 933232640, 45566.8 MB/s
Sequential copy (128-bit), size = 384 B, loops = 619007004, 45329.5 MB/s
Sequential copy (128-bit), size = 512 B, loops = 464388096, 45344.0 MB/s
Sequential copy (128-bit), size = 640 B, loops = 372242350, 45427.0 MB/s
Sequential copy (128-bit), size = 768 B, loops = 310289931, 45451.9 MB/s
Sequential copy (128-bit), size = 896 B, loops = 266112594, 45470.1 MB/s
Sequential copy (128-bit), size = 1024 B, loops = 232718336, 45444.9 MB/s
Sequential copy (128-bit), size = 1280 B, loops = 186381540, 45499.4 MB/s
Sequential copy (128-bit), size = 2 kB, loops = 116523008, 45510.9 MB/s
Sequential copy (128-bit), size = 3 kB, loops = 77724510, 45533.9 MB/s
Sequential copy (128-bit), size = 4 kB, loops = 58277888, 45529.2 MB/s
Sequential copy (128-bit), size = 6 kB, loops = 38871398, 45540.4 MB/s
Sequential copy (128-bit), size = 8 kB, loops = 29163520, 45559.4 MB/s
Sequential copy (128-bit), size = 12 kB, loops = 19162649, 44909.1 MB/s
Sequential copy (128-bit), size = 16 kB, loops = 13438976, 41985.3 MB/s
Sequential copy (128-bit), size = 20 kB, loops = 5916456, 23108.1 MB/s
Sequential copy (128-bit), size = 24 kB, loops = 4905810, 22991.3 MB/s
Sequential copy (128-bit), size = 28 kB, loops = 4223700, 23096.1 MB/s
Sequential copy (128-bit), size = 32 kB, loops = 3700736, 23127.8 MB/s
Sequential copy (128-bit), size = 34 kB, loops = 3485943, 23141.8 MB/s
Sequential copy (128-bit), size = 36 kB, loops = 3257800, 22896.0 MB/s
Sequential copy (128-bit), size = 40 kB, loops = 2959866, 23116.6 MB/s
Sequential copy (128-bit), size = 48 kB, loops = 2447445, 22936.9 MB/s
Sequential copy (128-bit), size = 64 kB, loops = 1796096, 22443.7 MB/s
Sequential copy (128-bit), size = 128 kB, loops = 850944, 21262.5 MB/s
Sequential copy (128-bit), size = 192 kB, loops = 317812, 11915.7 MB/s
Sequential copy (128-bit), size = 256 kB, loops = 223232, 11156.9 MB/s
Sequential copy (128-bit), size = 320 kB, loops = 178500, 11148.4 MB/s
Sequential copy (128-bit), size = 384 kB, loops = 148750, 11147.9 MB/s
Sequential copy (128-bit), size = 512 kB, loops = 111488, 11148.1 MB/s
Sequential copy (128-bit), size = 768 kB, loops = 74375, 11145.4 MB/s
Sequential copy (128-bit), size = 1 MB, loops = 55744, 11141.9 MB/s
Sequential copy (128-bit), size = 1.25 MB, loops = 44472, 11110.9 MB/s
Sequential copy (128-bit), size = 1.5 MB, loops = 37044, 11101.4 MB/s
Sequential copy (128-bit), size = 1.75 MB, loops = 31716, 11096.7 MB/s
Sequential copy (128-bit), size = 2 MB, loops = 27744, 11089.4 MB/s
Sequential copy (128-bit), size = 2.25 MB, loops = 24668, 11092.6 MB/s
Sequential copy (128-bit), size = 2.5 MB, loops = 22200, 11093.3 MB/s
Sequential copy (128-bit), size = 2.75 MB, loops = 20171, 11093.6 MB/s
Sequential copy (128-bit), size = 3 MB, loops = 18501, 11095.4 MB/s
Sequential copy (128-bit), size = 3.25 MB, loops = 17081, 11096.4 MB/s
Sequential copy (128-bit), size = 3.5 MB, loops = 15858, 11092.9 MB/s
Sequential copy (128-bit), size = 4 MB, loops = 13920, 11124.6 MB/s
Sequential copy (128-bit), size = 5 MB, loops = 11148, 11147.7 MB/s
Sequential copy (128-bit), size = 6 MB, loops = 9300, 11152.9 MB/s
Sequential copy (128-bit), size = 7 MB, loops = 7956, 11127.5 MB/s
Sequential copy (128-bit), size = 8 MB, loops = 6968, 11142.3 MB/s
Sequential copy (128-bit), size = 9 MB, loops = 6195, 11142.4 MB/s
Sequential copy (128-bit), size = 10 MB, loops = 5574, 11143.0 MB/s
Sequential copy (128-bit), size = 12 MB, loops = 4520, 10847.1 MB/s
Sequential copy (128-bit), size = 14 MB, loops = 1588, 4438.1 MB/s
Sequential copy (128-bit), size = 15 MB, loops = 1196, 3577.1 MB/s
Sequential copy (128-bit), size = 16 MB, loops = 932, 2973.1 MB/s
Sequential copy (128-bit), size = 20 MB, loops = 561, 2232.3 MB/s
Sequential copy (128-bit), size = 21 MB, loops = 519, 2174.6 MB/s
Sequential copy (128-bit), size = 32 MB, loops = 316, 2017.9 MB/s
Sequential copy (128-bit), size = 48 MB, loops = 211, 2017.3 MB/s
Sequential copy (128-bit), size = 64 MB, loops = 158, 2019.3 MB/s
Sequential copy (128-bit), size = 72 MB, loops = 141, 2017.7 MB/s
Sequential copy (128-bit), size = 96 MB, loops = 106, 2019.2 MB/s
Sequential copy (128-bit), size = 128 MB, loops = 79, 2019.7 MB/s

Sequential copy (256-bit), size = 256 B, loops = 933494784, 45570.9 MB/s
Sequential copy (256-bit), size = 512 B, loops = 466747392, 45568.8 MB/s
Sequential copy (256-bit), size = 768 B, loops = 311163741, 45573.6 MB/s
Sequential copy (256-bit), size = 1024 B, loops = 233373696, 45571.4 MB/s
Sequential copy (256-bit), size = 1280 B, loops = 186696108, 45570.8 MB/s
Sequential copy (256-bit), size = 2 kB, loops = 116686848, 45569.0 MB/s
Sequential copy (256-bit), size = 3 kB, loops = 77790045, 45568.8 MB/s
Sequential copy (256-bit), size = 4 kB, loops = 58343424, 45572.1 MB/s
Sequential copy (256-bit), size = 6 kB, loops = 38893242, 45572.2 MB/s
Sequential copy (256-bit), size = 8 kB, loops = 29171712, 45573.4 MB/s
Sequential copy (256-bit), size = 12 kB, loops = 19195415, 44984.5 MB/s
Sequential copy (256-bit), size = 16 kB, loops = 13410304, 41904.7 MB/s
Sequential copy (256-bit), size = 20 kB, loops = 5280912, 20624.9 MB/s
Sequential copy (256-bit), size = 24 kB, loops = 4398030, 20608.2 MB/s
Sequential copy (256-bit), size = 28 kB, loops = 3774420, 20634.6 MB/s
Sequential copy (256-bit), size = 32 kB, loops = 3305472, 20647.3 MB/s
Sequential copy (256-bit), size = 34 kB, loops = 3102470, 20591.8 MB/s
Sequential copy (256-bit), size = 36 kB, loops = 2922920, 20548.1 MB/s
Sequential copy (256-bit), size = 40 kB, loops = 2630628, 20548.2 MB/s
Sequential copy (256-bit), size = 48 kB, loops = 2190825, 20529.8 MB/s
Sequential copy (256-bit), size = 64 kB, loops = 1630208, 20371.7 MB/s
Sequential copy (256-bit), size = 128 kB, loops = 772096, 19293.1 MB/s
Sequential copy (256-bit), size = 192 kB, loops = 336226, 12606.7 MB/s
Sequential copy (256-bit), size = 256 kB, loops = 219648, 10980.3 MB/s
Sequential copy (256-bit), size = 320 kB, loops = 175644, 10972.2 MB/s
Sequential copy (256-bit), size = 384 kB, loops = 146370, 10970.5 MB/s
Sequential copy (256-bit), size = 512 kB, loops = 109824, 10972.2 MB/s
Sequential copy (256-bit), size = 768 kB, loops = 73185, 10969.0 MB/s
Sequential copy (256-bit), size = 1 MB, loops = 54848, 10968.0 MB/s
Sequential copy (256-bit), size = 1.25 MB, loops = 43656, 10903.6 MB/s
Sequential copy (256-bit), size = 1.5 MB, loops = 36414, 10918.7 MB/s
Sequential copy (256-bit), size = 1.75 MB, loops = 31212, 10914.0 MB/s
Sequential copy (256-bit), size = 2 MB, loops = 27264, 10901.4 MB/s
Sequential copy (256-bit), size = 2.25 MB, loops = 24248, 10907.4 MB/s
Sequential copy (256-bit), size = 2.5 MB, loops = 21825, 10910.3 MB/s
Sequential copy (256-bit), size = 2.75 MB, loops = 19849, 10913.2 MB/s
Sequential copy (256-bit), size = 3 MB, loops = 18207, 10915.7 MB/s
Sequential copy (256-bit), size = 3.25 MB, loops = 16796, 10917.3 MB/s
Sequential copy (256-bit), size = 3.5 MB, loops = 15606, 10916.5 MB/s
Sequential copy (256-bit), size = 4 MB, loops = 13712, 10967.0 MB/s
Sequential copy (256-bit), size = 5 MB, loops = 10980, 10973.6 MB/s
Sequential copy (256-bit), size = 6 MB, loops = 9160, 10980.9 MB/s
Sequential copy (256-bit), size = 7 MB, loops = 7839, 10962.3 MB/s
Sequential copy (256-bit), size = 8 MB, loops = 6864, 10971.0 MB/s
Sequential copy (256-bit), size = 9 MB, loops = 6097, 10972.7 MB/s
Sequential copy (256-bit), size = 10 MB, loops = 5490, 10974.7 MB/s
Sequential copy (256-bit), size = 12 MB, loops = 4575, 10969.4 MB/s
Sequential copy (256-bit), size = 14 MB, loops = 1588, 4435.8 MB/s
Sequential copy (256-bit), size = 15 MB, loops = 1192, 3567.7 MB/s
Sequential copy (256-bit), size = 16 MB, loops = 928, 2958.5 MB/s
Sequential copy (256-bit), size = 20 MB, loops = 555, 2218.8 MB/s
Sequential copy (256-bit), size = 21 MB, loops = 513, 2147.9 MB/s
Sequential copy (256-bit), size = 32 MB, loops = 314, 2005.2 MB/s
Sequential copy (256-bit), size = 48 MB, loops = 209, 2004.5 MB/s
Sequential copy (256-bit), size = 64 MB, loops = 157, 2004.3 MB/s
Sequential copy (256-bit), size = 72 MB, loops = 140, 2005.6 MB/s
Sequential copy (256-bit), size = 96 MB, loops = 105, 2004.8 MB/s
Sequential copy (256-bit), size = 128 MB, loops = 79, 2005.4 MB/s

Sequential read (64-bit LODSQ), size = 128 B, loops = 185597952, 4524.1 MB/s
Sequential read (64-bit LODSQ), size = 256 B, loops = 134479872, 6555.8 MB/s
Sequential read (64-bit LODSQ), size = 384 B, loops = 103633866, 7582.7 MB/s
Sequential read (64-bit LODSQ), size = 512 B, loops = 84672512, 8267.4 MB/s
Sequential read (64-bit LODSQ), size = 640 B, loops = 72456187, 8834.2 MB/s
Sequential read (64-bit LODSQ), size = 768 B, loops = 62302653, 9121.1 MB/s
Sequential read (64-bit LODSQ), size = 896 B, loops = 55274724, 9439.2 MB/s
Sequential read (64-bit LODSQ), size = 1024 B, loops = 49348608, 9631.2 MB/s
Sequential read (64-bit LODSQ), size = 1280 B, loops = 40893840, 9975.8 MB/s
Sequential read (64-bit LODSQ), size = 2 kB, loops = 26771456, 10451.9 MB/s
Sequential read (64-bit LODSQ), size = 3 kB, loops = 18349800, 10747.0 MB/s
Sequential read (64-bit LODSQ), size = 4 kB, loops = 13975552, 10909.1 MB/s
Sequential read (64-bit LODSQ), size = 6 kB, loops = 9447530, 11060.2 MB/s
Sequential read (64-bit LODSQ), size = 8 kB, loops = 7135232, 11141.1 MB/s
Sequential read (64-bit LODSQ), size = 12 kB, loops = 4794758, 11226.7 MB/s
Sequential read (64-bit LODSQ), size = 16 kB, loops = 3608576, 11264.2 MB/s
Sequential read (64-bit LODSQ), size = 20 kB, loops = 2892708, 11294.1 MB/s
Sequential read (64-bit LODSQ), size = 24 kB, loops = 2413320, 11304.8 MB/s
Sequential read (64-bit LODSQ), size = 28 kB, loops = 2070900, 11321.7 MB/s
Sequential read (64-bit LODSQ), size = 32 kB, loops = 1814528, 11329.9 MB/s
Sequential read (64-bit LODSQ), size = 34 kB, loops = 1707322, 11334.1 MB/s
Sequential read (64-bit LODSQ), size = 36 kB, loops = 1612520, 11337.3 MB/s
Sequential read (64-bit LODSQ), size = 40 kB, loops = 1452906, 11342.6 MB/s
Sequential read (64-bit LODSQ), size = 48 kB, loops = 1212120, 11351.3 MB/s
Sequential read (64-bit LODSQ), size = 64 kB, loops = 909312, 11359.7 MB/s
Sequential read (64-bit LODSQ), size = 128 kB, loops = 455168, 11378.4 MB/s
Sequential read (64-bit LODSQ), size = 192 kB, loops = 303831, 11382.8 MB/s
Sequential read (64-bit LODSQ), size = 256 kB, loops = 227840, 11381.0 MB/s
Sequential read (64-bit LODSQ), size = 320 kB, loops = 182172, 11381.1 MB/s
Sequential read (64-bit LODSQ), size = 384 kB, loops = 151810, 11382.7 MB/s
Sequential read (64-bit LODSQ), size = 512 kB, loops = 113920, 11384.4 MB/s
Sequential read (64-bit LODSQ), size = 768 kB, loops = 75905, 11384.9 MB/s
Sequential read (64-bit LODSQ), size = 1 MB, loops = 56960, 11385.7 MB/s
Sequential read (64-bit LODSQ), size = 1.25 MB, loops = 45594, 11386.3 MB/s
Sequential read (64-bit LODSQ), size = 1.5 MB, loops = 37968, 11386.4 MB/s
Sequential read (64-bit LODSQ), size = 1.75 MB, loops = 32544, 11386.5 MB/s
Sequential read (64-bit LODSQ), size = 2 MB, loops = 28480, 11386.3 MB/s
Sequential read (64-bit LODSQ), size = 2.25 MB, loops = 25312, 11384.5 MB/s
Sequential read (64-bit LODSQ), size = 2.5 MB, loops = 22775, 11385.1 MB/s
Sequential read (64-bit LODSQ), size = 2.75 MB, loops = 20700, 11384.3 MB/s
Sequential read (64-bit LODSQ), size = 3 MB, loops = 18984, 11384.8 MB/s
Sequential read (64-bit LODSQ), size = 3.25 MB, loops = 17518, 11384.7 MB/s
Sequential read (64-bit LODSQ), size = 3.5 MB, loops = 16272, 11385.2 MB/s
Sequential read (64-bit LODSQ), size = 4 MB, loops = 14240, 11388.7 MB/s
Sequential read (64-bit LODSQ), size = 5 MB, loops = 11388, 11388.0 MB/s
Sequential read (64-bit LODSQ), size = 6 MB, loops = 9500, 11388.9 MB/s
Sequential read (64-bit LODSQ), size = 7 MB, loops = 8136, 11388.4 MB/s
Sequential read (64-bit LODSQ), size = 8 MB, loops = 7120, 11387.5 MB/s
Sequential read (64-bit LODSQ), size = 9 MB, loops = 6328, 11388.2 MB/s
Sequential read (64-bit LODSQ), size = 10 MB, loops = 5700, 11388.7 MB/s
Sequential read (64-bit LODSQ), size = 12 MB, loops = 4750, 11388.4 MB/s
Sequential read (64-bit LODSQ), size = 14 MB, loops = 4068, 11388.4 MB/s
Sequential read (64-bit LODSQ), size = 15 MB, loops = 3796, 11387.7 MB/s
Sequential read (64-bit LODSQ), size = 16 MB, loops = 3560, 11388.2 MB/s
Sequential read (64-bit LODSQ), size = 20 MB, loops = 2847, 11387.5 MB/s
Sequential read (64-bit LODSQ), size = 21 MB, loops = 2712, 11387.2 MB/s
Sequential read (64-bit LODSQ), size = 32 MB, loops = 652, 4166.6 MB/s
Sequential read (64-bit LODSQ), size = 48 MB, loops = 326, 3128.7 MB/s
Sequential read (64-bit LODSQ), size = 64 MB, loops = 232, 2965.8 MB/s
Sequential read (64-bit LODSQ), size = 72 MB, loops = 206, 2962.3 MB/s
Sequential read (64-bit LODSQ), size = 96 MB, loops = 155, 2961.0 MB/s
Sequential read (64-bit LODSQ), size = 128 MB, loops = 116, 2961.0 MB/s

Sequential read (32-bit LODSD), size = 128 B, loops = 134742016, 3277.7 MB/s
Sequential read (32-bit LODSD), size = 256 B, loops = 84672512, 4134.0 MB/s
Sequential read (32-bit LODSD), size = 384 B, loops = 62390034, 4560.2 MB/s
Sequential read (32-bit LODSD), size = 512 B, loops = 49414144, 4815.8 MB/s
Sequential read (32-bit LODSD), size = 640 B, loops = 40894230, 4988.4 MB/s
Sequential read (32-bit LODSD), size = 768 B, loops = 34777638, 5084.5 MB/s
Sequential read (32-bit LODSD), size = 896 B, loops = 30258792, 5160.2 MB/s
Sequential read (32-bit LODSD), size = 1024 B, loops = 26804224, 5225.9 MB/s
Sequential read (32-bit LODSD), size = 1280 B, loops = 21757620, 5300.0 MB/s
Sequential read (32-bit LODSD), size = 2 kB, loops = 13991936, 5455.0 MB/s
Sequential read (32-bit LODSD), size = 3 kB, loops = 9458885, 5530.5 MB/s
Sequential read (32-bit LODSD), size = 4 kB, loops = 7143424, 5570.9 MB/s
Sequential read (32-bit LODSD), size = 6 kB, loops = 4794758, 5613.9 MB/s
Sequential read (32-bit LODSD), size = 8 kB, loops = 3612672, 5632.7 MB/s
Sequential read (32-bit LODSD), size = 12 kB, loops = 2413762, 5652.8 MB/s
Sequential read (32-bit LODSD), size = 16 kB, loops = 1814528, 5664.9 MB/s
Sequential read (32-bit LODSD), size = 20 kB, loops = 1454544, 5670.9 MB/s
Sequential read (32-bit LODSD), size = 24 kB, loops = 1212120, 5676.6 MB/s
Sequential read (32-bit LODSD), size = 28 kB, loops = 1038960, 5678.4 MB/s
Sequential read (32-bit LODSD), size = 32 kB, loops = 909312, 5681.4 MB/s
Sequential read (32-bit LODSD), size = 34 kB, loops = 857515, 5682.2 MB/s
Sequential read (32-bit LODSD), size = 36 kB, loops = 809900, 5682.0 MB/s
Sequential read (32-bit LODSD), size = 40 kB, loops = 728910, 5684.8 MB/s
Sequential read (32-bit LODSD), size = 48 kB, loops = 607425, 5686.7 MB/s
Sequential read (32-bit LODSD), size = 64 kB, loops = 455680, 5689.8 MB/s
Sequential read (32-bit LODSD), size = 128 kB, loops = 227840, 5693.3 MB/s
Sequential read (32-bit LODSD), size = 192 kB, loops = 152086, 5694.4 MB/s
Sequential read (32-bit LODSD), size = 256 kB, loops = 113920, 5693.0 MB/s
Sequential read (32-bit LODSD), size = 320 kB, loops = 91188, 5693.3 MB/s
Sequential read (32-bit LODSD), size = 384 kB, loops = 75990, 5693.3 MB/s
Sequential read (32-bit LODSD), size = 512 kB, loops = 56960, 5694.0 MB/s
Sequential read (32-bit LODSD), size = 768 kB, loops = 37995, 5694.0 MB/s
Sequential read (32-bit LODSD), size = 1 MB, loops = 28480, 5694.6 MB/s
Sequential read (32-bit LODSD), size = 1.25 MB, loops = 22797, 5695.3 MB/s
Sequential read (32-bit LODSD), size = 1.5 MB, loops = 18984, 5695.1 MB/s
Sequential read (32-bit LODSD), size = 1.75 MB, loops = 16272, 5694.4 MB/s
Sequential read (32-bit LODSD), size = 2 MB, loops = 14240, 5694.1 MB/s
Sequential read (32-bit LODSD), size = 2.25 MB, loops = 12656, 5693.7 MB/s
Sequential read (32-bit LODSD), size = 2.5 MB, loops = 11400, 5693.7 MB/s
Sequential read (32-bit LODSD), size = 2.75 MB, loops = 10373, 5693.9 MB/s
Sequential read (32-bit LODSD), size = 3 MB, loops = 9492, 5693.6 MB/s
Sequential read (32-bit LODSD), size = 3.25 MB, loops = 8778, 5693.7 MB/s
Sequential read (32-bit LODSD), size = 3.5 MB, loops = 8136, 5693.7 MB/s
Sequential read (32-bit LODSD), size = 4 MB, loops = 7120, 5694.8 MB/s
Sequential read (32-bit LODSD), size = 5 MB, loops = 5700, 5695.1 MB/s
Sequential read (32-bit LODSD), size = 6 MB, loops = 4750, 5694.4 MB/s
Sequential read (32-bit LODSD), size = 7 MB, loops = 4068, 5694.4 MB/s
Sequential read (32-bit LODSD), size = 8 MB, loops = 3560, 5694.7 MB/s
Sequential read (32-bit LODSD), size = 9 MB, loops = 3164, 5694.6 MB/s
Sequential read (32-bit LODSD), size = 10 MB, loops = 2850, 5694.6 MB/s
Sequential read (32-bit LODSD), size = 12 MB, loops = 2375, 5694.5 MB/s
Sequential read (32-bit LODSD), size = 14 MB, loops = 2036, 5694.7 MB/s
Sequential read (32-bit LODSD), size = 15 MB, loops = 1900, 5695.0 MB/s
Sequential read (32-bit LODSD), size = 16 MB, loops = 1780, 5694.8 MB/s
Sequential read (32-bit LODSD), size = 20 MB, loops = 1425, 5694.6 MB/s
Sequential read (32-bit LODSD), size = 21 MB, loops = 1356, 5694.7 MB/s
Sequential read (32-bit LODSD), size = 32 MB, loops = 534, 3408.8 MB/s
Sequential read (32-bit LODSD), size = 48 MB, loops = 302, 2889.8 MB/s
Sequential read (32-bit LODSD), size = 64 MB, loops = 220, 2814.7 MB/s
Sequential read (32-bit LODSD), size = 72 MB, loops = 196, 2812.2 MB/s
Sequential read (32-bit LODSD), size = 96 MB, loops = 147, 2810.1 MB/s
Sequential read (32-bit LODSD), size = 128 MB, loops = 110, 2808.5 MB/s

Sequential read (16-bit LODSW), size = 128 B, loops = 84934656, 2066.8 MB/s
Sequential read (16-bit LODSW), size = 256 B, loops = 49545216, 2408.0 MB/s
Sequential read (16-bit LODSW), size = 384 B, loops = 34777638, 2542.2 MB/s
Sequential read (16-bit LODSW), size = 512 B, loops = 26869760, 2612.9 MB/s
Sequential read (16-bit LODSW), size = 640 B, loops = 21810256, 2649.7 MB/s
Sequential read (16-bit LODSW), size = 768 B, loops = 18350010, 2687.0 MB/s
Sequential read (16-bit LODSW), size = 896 B, loops = 15878376, 2706.2 MB/s
Sequential read (16-bit LODSW), size = 1024 B, loops = 14024704, 2727.5 MB/s
Sequential read (16-bit LODSW), size = 1280 B, loops = 11272020, 2747.3 MB/s
Sequential read (16-bit LODSW), size = 2 kB, loops = 7143424, 2785.4 MB/s
Sequential read (16-bit LODSW), size = 3 kB, loops = 4805900, 2806.8 MB/s
Sequential read (16-bit LODSW), size = 4 kB, loops = 3620864, 2816.3 MB/s
Sequential read (16-bit LODSW), size = 6 kB, loops = 2413762, 2826.5 MB/s
Sequential read (16-bit LODSW), size = 8 kB, loops = 1818624, 2832.6 MB/s
Sequential read (16-bit LODSW), size = 12 kB, loops = 1212342, 2837.8 MB/s
Sequential read (16-bit LODSW), size = 16 kB, loops = 909312, 2840.4 MB/s
Sequential read (16-bit LODSW), size = 20 kB, loops = 730548, 2841.7 MB/s
Sequential read (16-bit LODSW), size = 24 kB, loops = 608790, 2843.4 MB/s
Sequential read (16-bit LODSW), size = 28 kB, loops = 521820, 2843.8 MB/s
Sequential read (16-bit LODSW), size = 32 kB, loops = 456704, 2844.8 MB/s
Sequential read (16-bit LODSW), size = 34 kB, loops = 429721, 2845.0 MB/s
Sequential read (16-bit LODSW), size = 36 kB, loops = 405860, 2845.2 MB/s
Sequential read (16-bit LODSW), size = 40 kB, loops = 365274, 2845.1 MB/s
Sequential read (16-bit LODSW), size = 48 kB, loops = 304395, 2846.2 MB/s
Sequential read (16-bit LODSW), size = 64 kB, loops = 228352, 2846.1 MB/s
Sequential read (16-bit LODSW), size = 128 kB, loops = 114176, 2847.8 MB/s
Sequential read (16-bit LODSW), size = 192 kB, loops = 76043, 2847.6 MB/s
Sequential read (16-bit LODSW), size = 256 kB, loops = 57088, 2847.0 MB/s
Sequential read (16-bit LODSW), size = 320 kB, loops = 45696, 2847.1 MB/s
Sequential read (16-bit LODSW), size = 384 kB, loops = 38080, 2846.9 MB/s
Sequential read (16-bit LODSW), size = 512 kB, loops = 28544, 2847.0 MB/s
Sequential read (16-bit LODSW), size = 768 kB, loops = 19040, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 1 MB, loops = 14272, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 1.25 MB, loops = 11424, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 1.5 MB, loops = 9492, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 1.75 MB, loops = 8136, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 2 MB, loops = 7136, 2847.2 MB/s
Sequential read (16-bit LODSW), size = 2.25 MB, loops = 6328, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 2.5 MB, loops = 5700, 2847.0 MB/s
Sequential read (16-bit LODSW), size = 2.75 MB, loops = 5198, 2847.1 MB/s
Sequential read (16-bit LODSW), size = 3 MB, loops = 4746, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 3.25 MB, loops = 4389, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 3.5 MB, loops = 4068, 2847.2 MB/s
Sequential read (16-bit LODSW), size = 4 MB, loops = 3568, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 5 MB, loops = 2856, 2847.7 MB/s
Sequential read (16-bit LODSW), size = 6 MB, loops = 2380, 2847.5 MB/s
Sequential read (16-bit LODSW), size = 7 MB, loops = 2034, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 8 MB, loops = 1784, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 9 MB, loops = 1582, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 10 MB, loops = 1428, 2847.6 MB/s
Sequential read (16-bit LODSW), size = 12 MB, loops = 1190, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 14 MB, loops = 1020, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 15 MB, loops = 952, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 16 MB, loops = 892, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 20 MB, loops = 714, 2847.3 MB/s
Sequential read (16-bit LODSW), size = 21 MB, loops = 678, 2847.4 MB/s
Sequential read (16-bit LODSW), size = 32 MB, loops = 374, 2388.9 MB/s
Sequential read (16-bit LODSW), size = 48 MB, loops = 228, 2187.5 MB/s
Sequential read (16-bit LODSW), size = 64 MB, loops = 171, 2182.9 MB/s
Sequential read (16-bit LODSW), size = 72 MB, loops = 152, 2184.0 MB/s
Sequential read (16-bit LODSW), size = 96 MB, loops = 114, 2184.5 MB/s
Sequential read (16-bit LODSW), size = 128 MB, loops = 86, 2184.3 MB/s

Sequential read (8-bit LODSB), size = 128 B, loops = 49807360, 1203.9 MB/s
Sequential read (8-bit LODSB), size = 256 B, loops = 27000832, 1306.4 MB/s
Sequential read (8-bit LODSB), size = 384 B, loops = 18350010, 1343.5 MB/s
Sequential read (8-bit LODSB), size = 512 B, loops = 14024704, 1363.7 MB/s
Sequential read (8-bit LODSB), size = 640 B, loops = 11324556, 1373.6 MB/s
Sequential read (8-bit LODSB), size = 768 B, loops = 9524529, 1382.6 MB/s
Sequential read (8-bit LODSB), size = 896 B, loops = 8163882, 1388.0 MB/s
Sequential read (8-bit LODSB), size = 1024 B, loops = 7143424, 1392.7 MB/s
Sequential read (8-bit LODSB), size = 1280 B, loops = 5767080, 1399.0 MB/s
Sequential read (8-bit LODSB), size = 2 kB, loops = 3637248, 1408.1 MB/s
Sequential read (8-bit LODSB), size = 3 kB, loops = 2424795, 1413.1 MB/s
Sequential read (8-bit LODSB), size = 4 kB, loops = 1818624, 1416.2 MB/s
Sequential read (8-bit LODSB), size = 6 kB, loops = 1212342, 1419.2 MB/s
Sequential read (8-bit LODSB), size = 8 kB, loops = 909312, 1420.4 MB/s
Sequential read (8-bit LODSB), size = 12 kB, loops = 611632, 1421.7 MB/s
Sequential read (8-bit LODSB), size = 16 kB, loops = 458752, 1422.4 MB/s
Sequential read (8-bit LODSB), size = 20 kB, loops = 366912, 1422.7 MB/s
Sequential read (8-bit LODSB), size = 24 kB, loops = 305760, 1423.0 MB/s
Sequential read (8-bit LODSB), size = 28 kB, loops = 262080, 1423.1 MB/s
Sequential read (8-bit LODSB), size = 32 kB, loops = 229376, 1423.4 MB/s
Sequential read (8-bit LODSB), size = 34 kB, loops = 215824, 1423.4 MB/s
Sequential read (8-bit LODSB), size = 36 kB, loops = 203840, 1423.5 MB/s
Sequential read (8-bit LODSB), size = 40 kB, loops = 183456, 1423.6 MB/s
Sequential read (8-bit LODSB), size = 48 kB, loops = 152880, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 64 kB, loops = 114688, 1424.0 MB/s
Sequential read (8-bit LODSB), size = 128 kB, loops = 57344, 1424.2 MB/s
Sequential read (8-bit LODSB), size = 192 kB, loops = 38192, 1424.1 MB/s
Sequential read (8-bit LODSB), size = 256 kB, loops = 28672, 1423.6 MB/s
Sequential read (8-bit LODSB), size = 320 kB, loops = 22848, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 384 kB, loops = 19040, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 512 kB, loops = 14336, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 768 kB, loops = 9520, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 1 MB, loops = 7168, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 1.25 MB, loops = 5712, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 1.5 MB, loops = 4788, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 1.75 MB, loops = 4068, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 2 MB, loops = 3584, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 2.25 MB, loops = 3164, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 2.5 MB, loops = 2850, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 2.75 MB, loops = 2599, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 3 MB, loops = 2373, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 3.25 MB, loops = 2204, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 3.5 MB, loops = 2034, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 4 MB, loops = 1792, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 5 MB, loops = 1428, 1423.6 MB/s
Sequential read (8-bit LODSB), size = 6 MB, loops = 1190, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 7 MB, loops = 1017, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 8 MB, loops = 896, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 9 MB, loops = 791, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 10 MB, loops = 714, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 12 MB, loops = 595, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 14 MB, loops = 512, 1423.8 MB/s
Sequential read (8-bit LODSB), size = 15 MB, loops = 476, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 16 MB, loops = 448, 1423.7 MB/s
Sequential read (8-bit LODSB), size = 20 MB, loops = 357, 1423.9 MB/s
Sequential read (8-bit LODSB), size = 21 MB, loops = 342, 1424.0 MB/s
Sequential read (8-bit LODSB), size = 32 MB, loops = 218, 1383.9 MB/s
Sequential read (8-bit LODSB), size = 48 MB, loops = 140, 1341.3 MB/s
Sequential read (8-bit LODSB), size = 64 MB, loops = 105, 1337.1 MB/s
Sequential read (8-bit LODSB), size = 72 MB, loops = 93, 1337.1 MB/s
Sequential read (8-bit LODSB), size = 96 MB, loops = 70, 1337.3 MB/s
Sequential read (8-bit LODSB), size = 128 MB, loops = 53, 1337.3 MB/s

Main register to main register transfers (64-bit) 80463.5 MB/s
Main register to vector register transfers (64-bit) 21967.0 MB/s
Vector register to main register transfers (64-bit) 22656.8 MB/s
Vector register to vector register transfers (128-bit) 79931.3 MB/s
Vector register to vector register transfers (256-bit) 220750.9 MB/s
Vector 8-bit datum to main register transfers 356.0 MB/s
Vector 16-bit datum to main register transfers 1423.4 MB/s
Vector 32-bit datum to main register transfers 5688.7 MB/s
Vector 64-bit datum to main register transfers 11361.8 MB/s
Main register 8-bit datum to vector register transfers 659.0 MB/s
Main register 16-bit datum to vector register transfers 2634.3 MB/s
Main register 32-bit datum to vector register transfers 10520.4 MB/s
Main register 64-bit datum to vector register transfers 10390.2 MB/s

Stack-to-register transfers (64-bit) 45395.9 MB/s
Register-to-stack transfers (64-bit) 22739.0 MB/s

Library: memset 2039.3 MB/s
Library: memcpy 1611.3 MB/s

Wrote graph to bandwidth.bmp.

Done.
```

# Parallel Bandwidth

Download [PMBW](https://panthema.net/2013/pmbw/) tarball and build.

Unpack the thing, edit `pmbw.cc` and remove the line

```
#include <malloc.h>
```

Now build

```console
./configure --prefix=$HOME/pmbw
gmake
gmake install
```
