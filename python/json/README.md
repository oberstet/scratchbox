Python 2.7.10 (850edf14b2c7, Oct 26 2015, 06:41:12)
[PyPy 4.0.0 with GCC 4.8.4]
testing serializing using <class 'autobahn.wamp.serializer.JsonObjectSerializer'>
serializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
425091 objs/sec
444283 objs/sec
444239 objs/sec
440620 objs/sec
443004 objs/sec
444340 objs/sec
439054 objs/sec
442359 objs/sec
446334 objs/sec
451420 objs/sec

testing serializing using <class 'autobahn.wamp.serializer.MsgPackObjectSerializer'>
serializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
1343792 objs/sec
1443676 objs/sec
1466015 objs/sec
1444788 objs/sec
1465423 objs/sec
1442820 objs/sec
1465900 objs/sec
1445250 objs/sec
1466104 objs/sec
1444805 objs/sec

testing unserializing using <class 'autobahn.wamp.serializer.JsonObjectSerializer'>
unserializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
360664 objs/sec
364473 objs/sec
364226 objs/sec
364149 objs/sec
363775 objs/sec
363827 objs/sec
363010 objs/sec
365121 objs/sec
365198 objs/sec
365193 objs/sec

testing unserializing using <class 'autobahn.wamp.serializer.MsgPackObjectSerializer'>
unserializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
19759753 objs/sec
22837330 objs/sec
22825275 objs/sec
22676204 objs/sec
22860357 objs/sec
22895297 objs/sec
22807650 objs/sec
23765378 objs/sec
23705070 objs/sec
23642935 objs/sec

Python 2.7.10 (f3ad1e1e1d62, Aug 28 2015, 10:45:29)
[PyPy 2.6.1 with GCC 4.8.4]
testing serializing using <class 'autobahn.wamp.serializer.JsonObjectSerializer'>
serializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
432824 objs/sec
445158 objs/sec
446719 objs/sec
449159 objs/sec
448142 objs/sec
446124 objs/sec
448279 objs/sec
447698 objs/sec
447274 objs/sec
449157 objs/sec

testing serializing using <class 'autobahn.wamp.serializer.MsgPackObjectSerializer'>
serializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
1358594 objs/sec
1506746 objs/sec
1498358 objs/sec
1503128 objs/sec
1505219 objs/sec
1506962 objs/sec
1481521 objs/sec
1500272 objs/sec
1500886 objs/sec
1504846 objs/sec

testing unserializing using <class 'autobahn.wamp.serializer.JsonObjectSerializer'>
unserializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
329695 objs/sec
331565 objs/sec
330429 objs/sec
331138 objs/sec
331374 objs/sec
331539 objs/sec
331559 objs/sec
330872 objs/sec
330074 objs/sec
331139 objs/sec

testing unserializing using <class 'autobahn.wamp.serializer.MsgPackObjectSerializer'>
unserializing object [48, 1, {u'receive_progress': True}, u'com.example.add2', (1, 2), {u'foo': 23, u'bar': u'baz'}]
23686596 objs/sec
31039488 objs/sec
31628628 objs/sec
32113930 objs/sec
32091324 objs/sec
32076108 objs/sec
32128443 objs/sec
32052332 objs/sec
32115159 objs/sec
32081015 objs/sec

Linux brummer2 3.19.0-25-generic #26~14.04.1-Ubuntu SMP Fri Jul 24 21:16:20 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 803.648
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 833.664
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 1
cpu cores	: 4
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 2
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 810.421
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 2
cpu cores	: 4
apicid		: 4
initial apicid	: 4
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 900.070
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 3
cpu cores	: 4
apicid		: 6
initial apicid	: 6
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 4
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 821.445
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 5
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 814.671
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 1
cpu cores	: 4
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 6
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 852.656
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 2
cpu cores	: 4
apicid		: 5
initial apicid	: 5
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

processor	: 7
vendor_id	: GenuineIntel
cpu family	: 6
model		: 60
model name	: Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
stepping	: 3
microcode	: 0x9
cpu MHz		: 837.914
cache size	: 8192 KB
physical id	: 0
siblings	: 8
core id		: 3
cpu cores	: 4
apicid		: 7
initial apicid	: 7
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm xsaveopt
bugs		:
bogomips	: 6785.05
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

