# psync engine on individual NVMes

## without perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio individual-nvmes-psync.fio
[sudo] password for oberstet:
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 928 (f=6261): [_(1),f(2),_(1),f(1),_(1),f(4),_(3),f(6),_(1),f(2),_(1),f(2),_(1),f(3),_(1),f(2),_(1),f(1),_(2),f(3),_(1),f(1),_(1),f(1),_(1),f(3),_(1),f(4),_(1),f(6),_(2),f(3),_(1),f(1),_(1),f(3),_(1),f(1),_(1),f(2),_(1),f(6),_(1),f(14),_(1),f(12),_(1),f(2),_(1),f(15),_(1),f(38),_(1),f(36),_(1),f(2),_(1),f(6),_(1),f(1),E(1),f(20),E(1),f(10),_(1),f(10),_(1),f(3),_(1),f(3),_(1),f(16),E(1),f(15),_(1),f(20),_(1),f(3),_(1),f(11),_(1),f(51),_(1),f(15),_(1),f(28),_(1),f(10),_(1),f(15),_(1),f(13),E(1),f(8),_(1),f(17),_(1),f(17),_(1),f(5),E(1),f(27),_(1),f(3),_(2),f(2),_(1),f(3),E(1),_(1),f(3),_(1),f(3),_(1),f(40),_(1),f(74),E(2),f(3),_(1),f(24),_(1),f(19),_(1),f(23),_(1),f(29),_(2),f(8),E(1),f(5),_(1),f(25),_(1),f(9),_(1),f(2),_(1),f(20),_(1),f(1),_(2),f(10),_(1),f(15),_(1),f(12),_(1),f(9),_(2),f(6),_(1),f(18),_(1),f(2),_(1),f(15),_(1),f(8),_(1),f(9),_(1),f(4),_(1),f(2),E(1),f(9),_(1),f(4),_(1),f(3),_(1),f(6)][100.0%][r=30.9GiB/s,w=0KiB/s][r=8084k,w=0 IOPS][eta 00m:00s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=108170: Wed Jan 25 10:45:36 2017
   read: IOPS=9395k, BW=35.9GiB/s (38.5GB/s)(1078GiB/30087msec)
  cpu          : usr=1.43%, sys=13.15%, ctx=284932261, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=282661760,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=35.9GiB/s (38.5GB/s), 35.9GiB/s-35.9GiB/s (38.5GB/s-38.5GB/s), io=1078GiB (1158GB), run=30087-30087msec

Disk stats (read/write):
  nvme0n1: ios=17605082/0, merge=0/0, ticks=465164/0, in_queue=478992, util=98.67%
  nvme1n1: ios=17605185/0, merge=0/0, ticks=490384/0, in_queue=529988, util=99.39%
  nvme2n1: ios=17666488/0, merge=0/0, ticks=511960/0, in_queue=561284, util=99.67%
  nvme3n1: ios=17666488/0, merge=0/0, ticks=516484/0, in_queue=533508, util=98.81%
  nvme4n1: ios=17666488/0, merge=0/0, ticks=512832/0, in_queue=571080, util=99.63%
  nvme5n1: ios=17666488/0, merge=0/0, ticks=567960/0, in_queue=586476, util=99.18%
  nvme6n1: ios=17666488/0, merge=0/0, ticks=573688/0, in_queue=590964, util=98.77%
  nvme7n1: ios=17666488/0, merge=0/0, ticks=531636/0, in_queue=548824, util=99.01%
  nvme8n1: ios=17666488/0, merge=0/0, ticks=499668/0, in_queue=512624, util=99.02%
  nvme9n1: ios=17666488/0, merge=0/0, ticks=547316/0, in_queue=605544, util=100.00%
  nvme10n1: ios=17666488/0, merge=0/0, ticks=723076/0, in_queue=746888, util=99.33%
  nvme11n1: ios=17666488/0, merge=0/0, ticks=662284/0, in_queue=732452, util=100.00%
  nvme12n1: ios=17666488/0, merge=0/0, ticks=3260900/0, in_queue=3378328, util=99.72%
  nvme13n1: ios=17666488/0, merge=0/0, ticks=6242132/0, in_queue=6803000, util=100.00%
  nvme14n1: ios=17665464/0, merge=0/0, ticks=456736/0, in_queue=471436, util=99.86%
  nvme15n1: ios=17665464/0, merge=0/0, ticks=490120/0, in_queue=504476, util=99.62%
```

## under perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio individual-nvmes-psync.fio
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=16384): [r(1024)][100.0%][r=26.4GiB/s,w=0KiB/s][r=6826k,w=0 IOPS][eta 00m:00s]
Message from syslogd@svr-psql19 at Jan 25 10:48:10 ...
 kernel:[503419.732516] NMI watchdog: BUG: soft lockup - CPU#0 stuck for 23s! [kworker/0:1H:5226]
Jobs: 965 (f=13787): [_(1),f(7),_(3),f(10),_(1),f(5),_(2),f(9),_(1),f(9),_(1),f(2),_(4),f(1),_(1),f(1),_(1),f(1),_(1),f(1),_(5),f(4),_(1),f(11),_(1),f(3),_(5),f(1),_(1),f(4),_(1),f(5),_(3),f(16),_(1),f(6),_(2),f(2),_(1),f(10),_(1),f(19),_(1),f(114),_(2),f(61),_(1),f(45),_(1),f(4),_(1),f(21),_(1),f(19),_(1),f(84),_(1),f(121),_(1),f(73),_(1),f(2),_(1),f(8),_(1),f(4),_(1),f(88),_(1),f(7),_(1),f(22),_(1),f(12),_(2),f(57),_(1),f(48),_(1),f(48)][100.0%][r=24.5GiB/s,w=0KiB/s][r=6303k,w=0 IOPS][eta 00m:00s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=109377: Wed Jan 25 10:48:11 2017
   read: IOPS=6636k, BW=25.4GiB/s (27.2GB/s)(761GiB/30065msec)
  cpu          : usr=0.90%, sys=12.08%, ctx=172710220, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=199499392,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=25.4GiB/s (27.2GB/s), 25.4GiB/s-25.4GiB/s (27.2GB/s-27.2GB/s), io=761GiB (817GB), run=30065-30065msec

Disk stats (read/write):
  nvme0n1: ios=12389268/0, merge=0/0, ticks=561612/0, in_queue=569416, util=95.74%
  nvme1n1: ios=12468840/0, merge=0/0, ticks=592076/0, in_queue=630384, util=96.06%
  nvme2n1: ios=12468840/0, merge=0/0, ticks=610428/0, in_queue=651840, util=95.65%
  nvme3n1: ios=12468840/0, merge=0/0, ticks=607832/0, in_queue=618044, util=95.45%
  nvme4n1: ios=12468840/0, merge=0/0, ticks=580252/0, in_queue=628372, util=96.40%
  nvme5n1: ios=12468840/0, merge=0/0, ticks=636768/0, in_queue=644636, util=95.50%
  nvme6n1: ios=12468840/0, merge=0/0, ticks=629336/0, in_queue=635992, util=95.36%
  nvme7n1: ios=12468840/0, merge=0/0, ticks=576864/0, in_queue=585352, util=95.66%
  nvme8n1: ios=12468840/0, merge=0/0, ticks=611784/0, in_queue=621152, util=95.73%
  nvme9n1: ios=12468840/0, merge=0/0, ticks=604140/0, in_queue=650676, util=96.64%
  nvme10n1: ios=12468840/0, merge=0/0, ticks=669452/0, in_queue=677408, util=95.66%
  nvme11n1: ios=12468840/0, merge=0/0, ticks=637876/0, in_queue=690564, util=97.03%
  nvme12n1: ios=12468840/0, merge=0/0, ticks=572028/0, in_queue=579296, util=95.96%
  nvme13n1: ios=12468840/0, merge=0/0, ticks=586724/0, in_queue=618964, util=96.76%
  nvme14n1: ios=12467816/0, merge=0/0, ticks=546156/0, in_queue=554208, util=96.13%
  nvme15n1: ios=12467816/0, merge=0/0, ticks=568072/0, in_queue=575656, util=96.32%
[ perf record: Woken up 138 times to write data ]
Warning:
38 out of order events recorded.
[ perf record: Captured and wrote 642.510 MB perf.data (16771515 samples) ]
```

## perf results

```console
Samples: 16M of event 'cycles:ppp', Event count (approx.): 82293785158374025
Overhead  Command  Shared Object       Symbol
  26.54%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   6.59%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   3.51%  fio      [kernel.kallsyms]   [k] finish_task_switch
   2.86%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   2.84%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   2.37%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   2.26%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   1.55%  fio      [kernel.kallsyms]   [k] __fget
   1.53%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   1.38%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   1.37%  fio      fio                 [.] get_io_u
   1.34%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   1.23%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   1.08%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.96%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.95%  fio      [kernel.kallsyms]   [k] blk_rq_map_sg
   0.93%  fio      fio                 [.] fio_psyncio_queue
   0.82%  fio      [kernel.kallsyms]   [k] __schedule
   0.78%  fio      [kernel.kallsyms]   [k] __bt_get.isra.7
   0.78%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.78%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   0.77%  fio      [kernel.kallsyms]   [k] __switch_to
   0.74%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.73%  fio      [kernel.kallsyms]   [k] osq_lock
   0.69%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.64%  fio      fio                 [.] thread_main
   0.62%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.60%  fio      [kernel.kallsyms]   [k] kmem_cache_alloc
   0.60%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.60%  fio      [kernel.kallsyms]   [k] dio_bio_complete
   0.58%  fio      [kernel.kallsyms]   [k] gup_pte_range
   0.54%  fio      [kernel.kallsyms]   [k] __blk_mq_run_hw_queue
   0.53%  fio      [kernel.kallsyms]   [k] _find_next_bit.part.0
   0.53%  fio      fio                 [.] td_io_queue
   0.53%  fio      [kernel.kallsyms]   [k] new_sync_read
   0.50%  fio      [kernel.kallsyms]   [k] blk_throtl_bio
   0.50%  fio      [kernel.kallsyms]   [k] blk_mq_make_request
   0.50%  fio      libpthread-2.19.so  [.] 0x000000000000f273
```
