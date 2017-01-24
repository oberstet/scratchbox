# psync engine on individual NVMes

## FIO results

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio individual-nvmes-psync.fio
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 978 (f=14484): [_(1),f(11),_(1),f(33),_(1),f(3),_(1),f(11),_(1),f(3),_(1),f(5),_(1),f(2),_(1),f(6),_(1),f(18),_(1),f(6),_(1),f(4),_(4),f(8),_(3),f(24),_(1),f(24),_(1),f(4),_(1),f(28),_(1),f(3),_(2),f(1),_(1),f(59),_(1),f(7),_(1),f(25),_(1),f(19),_(1),f(19),_(1),f(188),_(1),f(15),_(1),f(85),_(1),f(29),_(1),f(31),_(1),f(34),_(1),f(3),_(1),f(1),_(1),f(10),_(1),f(88),_(1),f(7),_(1),f(6),_(1),f(4),_(1),f(43),_(1),f(15),_(1),f(9),_(1),f(87)][100.0%][r=7213MiB/s,w=0KiB/s][r=1847k,w=0 IOPS][eta 00m:00s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=139023: Tue Jan 24 10:09:17 2017
   read: IOPS=1934k, BW=7554MiB/s (7920MB/s)(222GiB/30039msec)
  cpu          : usr=0.84%, sys=10.31%, ctx=57446889, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=58086592,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=7554MiB/s (7920MB/s), 7554MiB/s-7554MiB/s (7920MB/s-7920MB/s), io=222GiB (238GB), run=30039-30039msec

Disk stats (read/write):
  nvme0n1: ios=3604964/0, merge=0/0, ticks=1033264/0, in_queue=1058812, util=96.43%
  nvme1n1: ios=3630540/0, merge=0/0, ticks=1056124/0, in_queue=1125096, util=96.06%
  nvme2n1: ios=3630540/0, merge=0/0, ticks=843440/0, in_queue=891648, util=95.81%
  nvme3n1: ios=3630540/0, merge=0/0, ticks=935988/0, in_queue=961044, util=96.10%
  nvme4n1: ios=3630540/0, merge=0/0, ticks=894116/0, in_queue=961700, util=96.77%
  nvme5n1: ios=3630540/0, merge=0/0, ticks=1014896/0, in_queue=1028872, util=95.78%
  nvme6n1: ios=3630540/0, merge=0/0, ticks=778676/0, in_queue=788636, util=95.77%
  nvme7n1: ios=3630540/0, merge=0/0, ticks=915704/0, in_queue=928388, util=95.71%
  nvme8n1: ios=3630540/0, merge=0/0, ticks=1052056/0, in_queue=1067676, util=95.94%
  nvme9n1: ios=3630540/0, merge=0/0, ticks=941632/0, in_queue=1004344, util=97.01%
  nvme10n1: ios=3630540/0, merge=0/0, ticks=992980/0, in_queue=1008096, util=96.19%
  nvme11n1: ios=3630540/0, merge=0/0, ticks=1034104/0, in_queue=1113432, util=97.34%
  nvme12n1: ios=3630540/0, merge=0/0, ticks=1018456/0, in_queue=1031436, util=96.28%
  nvme13n1: ios=3630540/0, merge=0/0, ticks=817216/0, in_queue=856888, util=97.12%
  nvme14n1: ios=3629516/0, merge=0/0, ticks=999216/0, in_queue=1012312, util=96.48%
  nvme15n1: ios=3629516/0, merge=0/0, ticks=872840/0, in_queue=887024, util=96.54%
[ perf record: Woken up 49 times to write data ]
Warning:
2 out of order events recorded.
[ perf record: Captured and wrote 497.745 MB perf.data (13030902 samples) ]
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$
```

## perf results

```console
Samples: 13M of event 'cycles:ppp', Event count (approx.): 62615976949699281
Overhead  Command  Shared Object       Symbol
  39.33%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   4.45%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   3.59%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   2.93%  fio      [kernel.kallsyms]   [k] finish_task_switch
   1.62%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   1.45%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   1.39%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   1.33%  fio      [kernel.kallsyms]   [k] native_write_msr
   1.30%  fio      fio                 [.] get_io_u
   1.26%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   1.16%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   1.13%  fio      [kernel.kallsyms]   [k] __fget
   0.99%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.88%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   0.87%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.73%  fio      fio                 [.] fio_psyncio_queue
   0.69%  fio      fio                 [.] thread_main
   0.67%  fio      [kernel.kallsyms]   [k] _raw_spin_trylock
   0.66%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.63%  fio      [kernel.kallsyms]   [k] new_sync_read
   0.60%  fio      [kernel.kallsyms]   [k] __switch_to
   0.59%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   0.58%  fio      [kernel.kallsyms]   [k] enqueue_entity
   0.57%  fio      fio                 [.] td_io_queue
   0.56%  fio      [kernel.kallsyms]   [k] dio_bio_complete
   0.55%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.55%  fio      [kernel.kallsyms]   [k] dequeue_entity
   0.51%  fio      [kernel.kallsyms]   [k] blk_rq_map_sg
   0.50%  fio      [kernel.kallsyms]   [k] __schedule
   0.50%  fio      [kernel.kallsyms]   [k] blk_mq_complete_request
   0.48%  fio      [kernel.kallsyms]   [k] load_balance
   0.48%  fio      fio                 [.] io_u_sync_complete
   0.48%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.46%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.44%  fio      [kernel.kallsyms]   [k] blk_mq_start_request
   0.44%  fio      [kernel.kallsyms]   [k] kmem_cache_alloc
   0.44%  fio      [kernel.kallsyms]   [k] ___cache_free
   0.44%  fio      fio                 [.] clock_thread_fn
   0.42%  fio      libpthread-2.19.so  [.] __pthread_disable_asynccancel
   0.40%  fio      libpthread-2.19.so  [.] 0x000000000000f273
   0.37%  fio      [kernel.kallsyms]   [k] blk_mq_hctx_mark_pending
   0.36%  fio      [kernel.kallsyms]   [k] blk_rq_bio_prep
   0.36%  fio      [kernel.kallsyms]   [k] __do_softirq
   0.35%  fio      [kernel.kallsyms]   [k] set_page_dirty_lock
   0.34%  fio      [kernel.kallsyms]   [k] blk_mq_make_request
   0.34%  fio      [kernel.kallsyms]   [k] osq_lock
```
