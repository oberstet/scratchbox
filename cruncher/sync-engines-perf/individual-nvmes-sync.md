# sync engine on individual NVMes

## without perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio individual-nvmes-sync.fio
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 965 (f=14729): [f(2),_(1),f(2),_(1),f(2),_(2),f(3),_(1),f(8),_(4),f(1),_(2),f(2),_(1),f(22),_(1),f(1),_(2),f(1),_(8),f(2),_(1),f(1),_(3),f(1),_(5),f(1),_(3),f(6),_(1),f(4),_(1),f(4),_(1),f(11),_(1),f(4),_(1),f(21),_(2),f(13),_(1),f(2),_(2),f(2),_(2),f(9),_(1),f(9),_(1),f(42),_(1),f(10),_(1),f(18),_(1),f(3),_(1),f(141),_(1),f(19),_(1),f(134),_(1),f(41),_(1),f(44),_(1),f(355),_(1),f(24)][100.0%][r=34.9GiB/s,w=0KiB/s][r=9132k,w=0 IOPS][eta 00m:00s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=110607: Wed Jan 25 10:51:34 2017
   read: IOPS=9191k, BW=35.7GiB/s (37.7GB/s)(1054GiB/30050msec)
  cpu          : usr=1.28%, sys=14.52%, ctx=281884710, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=276196416,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=35.7GiB/s (37.7GB/s), 35.7GiB/s-35.7GiB/s (37.7GB/s-37.7GB/s), io=1054GiB (1131GB), run=30050-30050msec

Disk stats (read/write):
  nvme0n1: ios=17262404/0, merge=0/0, ticks=406284/0, in_queue=414604, util=97.93%
  nvme1n1: ios=17262404/0, merge=0/0, ticks=419236/0, in_queue=456104, util=98.82%
  nvme2n1: ios=17262404/0, merge=0/0, ticks=410744/0, in_queue=448008, util=98.95%
  nvme3n1: ios=17262404/0, merge=0/0, ticks=421256/0, in_queue=431996, util=98.58%
  nvme4n1: ios=17262404/0, merge=0/0, ticks=410056/0, in_queue=455868, util=99.41%
  nvme5n1: ios=17262404/0, merge=0/0, ticks=450164/0, in_queue=460268, util=99.17%
  nvme6n1: ios=17262404/0, merge=0/0, ticks=485232/0, in_queue=496104, util=98.84%
  nvme7n1: ios=17262404/0, merge=0/0, ticks=453944/0, in_queue=464876, util=98.86%
  nvme8n1: ios=17262404/0, merge=0/0, ticks=414768/0, in_queue=426652, util=99.48%
  nvme9n1: ios=17262404/0, merge=0/0, ticks=433608/0, in_queue=471944, util=100.00%
  nvme10n1: ios=17262404/0, merge=0/0, ticks=1051484/0, in_queue=1086232, util=99.53%
  nvme11n1: ios=17262404/0, merge=0/0, ticks=744816/0, in_queue=818732, util=100.00%
  nvme12n1: ios=17262404/0, merge=0/0, ticks=2945728/0, in_queue=3056388, util=99.49%
  nvme13n1: ios=17262404/0, merge=0/0, ticks=1925196/0, in_queue=2103264, util=100.00%
  nvme14n1: ios=17261380/0, merge=0/0, ticks=377904/0, in_queue=385296, util=99.48%
  nvme15n1: ios=17261380/0, merge=0/0, ticks=402852/0, in_queue=413512, util=100.00%
```

## with perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio individual-nvmes-sync.fio
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 997 (f=15945): [_(1),r(75),_(1),r(12),_(1),r(3),_(1),r(7),_(1),r(2),_(2),E(1),r(2),_(1),r(11),_(1),r(6),_(1),r(1),_(1),r(1),_(1),r(1),_(2),E(1),r(6),_(1),r(59),_(1),r(12),_(1),r(76),E(1),r(145),_(1),r(20),E(1),r(78),_(1),r(50),_(1),r(76),_(1),r(27),_(1),r(181),_(1),r(26),f(1),r(119)][3.7%][r=23.6GiB/s,w=0KiB/s][r=6169k,w=0 IOPS][eta 14m:00s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=111813: Wed Jan 25 10:53:35 2017
   read: IOPS=6052k, BW=23.9GiB/s (24.8GB/s)(694GiB/30076msec)
  cpu          : usr=0.89%, sys=12.97%, ctx=167804357, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=182021248,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=23.9GiB/s (24.8GB/s), 23.9GiB/s-23.9GiB/s (24.8GB/s-24.8GB/s), io=694GiB (746GB), run=30076-30076msec

Disk stats (read/write):
  nvme0n1: ios=11367911/0, merge=0/0, ticks=459808/0, in_queue=466248, util=95.63%
  nvme1n1: ios=11376456/0, merge=0/0, ticks=479788/0, in_queue=509820, util=95.87%
  nvme2n1: ios=11376456/0, merge=0/0, ticks=489660/0, in_queue=517936, util=95.79%
  nvme3n1: ios=11376456/0, merge=0/0, ticks=482068/0, in_queue=488472, util=94.79%
  nvme4n1: ios=11376456/0, merge=0/0, ticks=465844/0, in_queue=495676, util=95.31%
  nvme5n1: ios=11376456/0, merge=0/0, ticks=510884/0, in_queue=514688, util=94.78%
  nvme6n1: ios=11376456/0, merge=0/0, ticks=495044/0, in_queue=499164, util=94.72%
  nvme7n1: ios=11376456/0, merge=0/0, ticks=464380/0, in_queue=470272, util=95.32%
  nvme8n1: ios=11376456/0, merge=0/0, ticks=489768/0, in_queue=494996, util=95.32%
  nvme9n1: ios=11376456/0, merge=0/0, ticks=487244/0, in_queue=519384, util=96.12%
  nvme10n1: ios=11376456/0, merge=0/0, ticks=541164/0, in_queue=546180, util=95.25%
  nvme11n1: ios=11376456/0, merge=0/0, ticks=516424/0, in_queue=542036, util=96.11%
  nvme12n1: ios=11376456/0, merge=0/0, ticks=453396/0, in_queue=458184, util=95.49%
  nvme13n1: ios=11376456/0, merge=0/0, ticks=466576/0, in_queue=489852, util=96.12%
  nvme14n1: ios=11375432/0, merge=0/0, ticks=439512/0, in_queue=444172, util=96.17%
  nvme15n1: ios=11375432/0, merge=0/0, ticks=455952/0, in_queue=462048, util=96.03%
[ perf record: Woken up 365 times to write data ]
Warning:
58 out of order events recorded.
[ perf record: Captured and wrote 616.779 MB perf.data (16078710 samples) ]
```

## perf results

```console
Samples: 16M of event 'cycles:ppp', Event count (approx.): 238119694043716848
Overhead  Command  Shared Object       Symbol
  23.73%  fio      [kernel.kallsyms]   [k] osq_lock
  18.61%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   4.92%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   2.23%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   2.14%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   2.04%  fio      [kernel.kallsyms]   [k] finish_task_switch
   1.85%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   1.46%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   1.15%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   1.10%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   1.07%  fio      [kernel.kallsyms]   [k] __fget
   1.01%  fio      fio                 [.] get_io_u
   0.97%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   0.89%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.88%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.83%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   0.73%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.71%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.70%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   0.69%  fio      [kernel.kallsyms]   [k] __switch_to
   0.69%  fio      [kernel.kallsyms]   [k] down_write
   0.67%  fio      [kernel.kallsyms]   [k] __schedule
   0.62%  fio      [kernel.kallsyms]   [k] blk_rq_map_sg
   0.57%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.54%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.52%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
```
