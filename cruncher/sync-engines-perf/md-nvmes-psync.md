# psync engine on MD

## without perf

```console
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=15.8GiB/s,w=0KiB/s][r=4126k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=116700: Wed Jan 25 12:13:46 2017
   read: IOPS=4117k, BW=15.8GiB/s (16.9GB/s)(472GiB/30033msec)
  cpu          : usr=1.11%, sys=16.04%, ctx=121285370, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=123659072,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=15.8GiB/s (16.9GB/s), 15.8GiB/s-15.8GiB/s (16.9GB/s-16.9GB/s), io=472GiB (507GB), run=30033-30033msec

Disk stats (read/write):
    md1: ios=122989770/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=7728692/0, aggrmerge=0/0, aggrticks=189179/0, aggrin_queue=202496, aggrutil=100.00%
  nvme15n1: ios=7728727/0, merge=0/0, ticks=187876/0, in_queue=193784, util=100.00%
  nvme6n1: ios=7726094/0, merge=0/0, ticks=190884/0, in_queue=195920, util=100.00%
  nvme9n1: ios=7728475/0, merge=0/0, ticks=201220/0, in_queue=227468, util=100.00%
  nvme11n1: ios=7723831/0, merge=0/0, ticks=190780/0, in_queue=217444, util=100.00%
  nvme2n1: ios=7727241/0, merge=0/0, ticks=192108/0, in_queue=217948, util=100.00%
  nvme14n1: ios=7731469/0, merge=0/0, ticks=179948/0, in_queue=186904, util=100.00%
  nvme5n1: ios=7728983/0, merge=0/0, ticks=204124/0, in_queue=210816, util=100.00%
  nvme8n1: ios=7730201/0, merge=0/0, ticks=195632/0, in_queue=201212, util=100.00%
  nvme10n1: ios=7731963/0, merge=0/0, ticks=207280/0, in_queue=214804, util=100.00%
  nvme1n1: ios=7728372/0, merge=0/0, ticks=184308/0, in_queue=208228, util=100.00%
  nvme13n1: ios=7728035/0, merge=0/0, ticks=177780/0, in_queue=199184, util=100.00%
  nvme4n1: ios=7732290/0, merge=0/0, ticks=191416/0, in_queue=217612, util=100.00%
  nvme7n1: ios=7726779/0, merge=0/0, ticks=186528/0, in_queue=193880, util=100.00%
  nvme0n1: ios=7731120/0, merge=0/0, ticks=173764/0, in_queue=178672, util=100.00%
  nvme12n1: ios=7730233/0, merge=0/0, ticks=174596/0, in_queue=180448, util=100.00%
  nvme3n1: ios=7725259/0, merge=0/0, ticks=188628/0, in_queue=195616, util=100.00%
```

## with perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio md-nvmes-psync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 974 (f=968): [_(1),r(11),_(1),r(11),_(1),r(1),E(1),r(2),_(1),r(4),_(1),r(6),_(1),r(22),_(2),r(12),_(1),r(11),_(1),r(4),_(1),r(4),_(1),r(1),_(1),r(27),_(1),r(1),_(1),r(4),_(1),r(15),E(1),r(29),E(1),r(2),E(1),r(2),_(1),r(100),_(1),r(57),_(1),r(51),_(1),r(27),_(1),r(8),_(1),r(8),_(1),r(71),_(1),r(37),E(1),r(70),_(1),r(67),_(1),r(20),_(1),r(37),E(1),r(43),_(1),r(32),E(1),r(10),f(1),r(16),E(1),r(11),_(1),r(6),f(1),r(7),E(1),r(12),E(1),_(1),r(1),f(1),r(9),f(1),r(12),_(1),r(4),_(1),r(3),_(1),r(18),E(1),r(21),E(1),r(2),E(1),r(1),f(1),r(4),f(1),E(1),r(25),E(1),_(1),r(6),_(1),r(3)][1.5%][r=15.7GiB/s,w=0KiB/s][r=3950k,w=0 IOPS][eta 34m:30s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=117921: Wed Jan 25 12:14:50 2017
   read: IOPS=3987k, BW=15.3GiB/s (16.4GB/s)(458GiB/30130msec)
  cpu          : usr=1.07%, sys=16.05%, ctx=117576722, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=120113792,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=15.3GiB/s (16.4GB/s), 15.3GiB/s-15.3GiB/s (16.4GB/s-16.4GB/s), io=458GiB (492GB), run=30130-30130msec

Disk stats (read/write):
    md1: ios=119863339/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=7507112/0, aggrmerge=0/0, aggrticks=177221/0, aggrin_queue=184277, aggrutil=99.84%
  nvme15n1: ios=7504563/0, merge=0/0, ticks=174536/0, in_queue=175836, util=97.94%
  nvme6n1: ios=7507041/0, merge=0/0, ticks=180224/0, in_queue=182204, util=98.29%
  nvme9n1: ios=7508227/0, merge=0/0, ticks=189496/0, in_queue=205852, util=99.57%
  nvme11n1: ios=7503793/0, merge=0/0, ticks=178408/0, in_queue=196228, util=99.35%
  nvme2n1: ios=7508485/0, merge=0/0, ticks=181008/0, in_queue=198360, util=99.84%
  nvme14n1: ios=7512075/0, merge=0/0, ticks=168860/0, in_queue=170444, util=98.12%
  nvme5n1: ios=7503127/0, merge=0/0, ticks=191044/0, in_queue=192464, util=98.04%
  nvme8n1: ios=7509972/0, merge=0/0, ticks=184192/0, in_queue=185996, util=98.25%
  nvme10n1: ios=7504821/0, merge=0/0, ticks=192344/0, in_queue=193884, util=98.08%
  nvme1n1: ios=7505466/0, merge=0/0, ticks=171108/0, in_queue=186836, util=99.65%
  nvme13n1: ios=7504494/0, merge=0/0, ticks=164836/0, in_queue=179856, util=99.45%
  nvme4n1: ios=7509727/0, merge=0/0, ticks=179352/0, in_queue=195928, util=99.76%
  nvme7n1: ios=7511858/0, merge=0/0, ticks=175648/0, in_queue=176980, util=98.26%
  nvme0n1: ios=7508853/0, merge=0/0, ticks=161940/0, in_queue=163024, util=98.09%
  nvme12n1: ios=7505481/0, merge=0/0, ticks=164696/0, in_queue=165444, util=97.89%
  nvme3n1: ios=7505809/0, merge=0/0, ticks=177848/0, in_queue=179100, util=97.98%
[ perf record: Woken up 3 times to write data ]

[ perf record: Captured and wrote 755.931 MB perf.data (19811853 samples) ]
```

## perf results

```console
Samples: 19M of event 'cycles:ppp', Event count (approx.): 15414018203159307
Overhead  Command  Shared Object       Symbol
  45.56%  fio      [kernel.kallsyms]   [k] md_make_request
   4.33%  fio      [kernel.kallsyms]   [k] osq_lock
   3.40%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   3.23%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   2.21%  fio      [kernel.kallsyms]   [k] raid0_make_request
   2.11%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   1.96%  fio      fio                 [.] clock_thread_fn
   1.79%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   1.41%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.88%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.85%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   0.80%  fio      [kernel.kallsyms]   [k] __switch_to
   0.80%  fio      [kernel.kallsyms]   [k] _find_next_bit.part.0
   0.71%  fio      [kernel.kallsyms]   [k] gup_pte_range
   0.70%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.67%  fio      [kernel.kallsyms]   [k] update_curr
   0.64%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.64%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   0.63%  fio      [kernel.kallsyms]   [k] blk_mq_map_queue
   0.59%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.58%  fio      [kernel.kallsyms]   [k] bt_clear_tag
   0.56%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.54%  fio      fio                 [.] get_io_u
   0.54%  fio      [kernel.kallsyms]   [k] __blk_mq_free_request
   0.53%  fio      fio                 [.] io_queue_event
   0.52%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   0.51%  fio      [kernel.kallsyms]   [k] bio_advance
```
