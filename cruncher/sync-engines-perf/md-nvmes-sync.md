# psync engine on individual NVMes

## FIO results

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio md-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=5742MiB/s,w=0KiB/s][r=1470k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=140350: Tue Jan 24 10:12:45 2017
   read: IOPS=1464k, BW=5718MiB/s (5996MB/s)(168GiB/30099msec)
  cpu          : usr=0.19%, sys=10.05%, ctx=45090496, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=44059392,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=5718MiB/s (5996MB/s), 5718MiB/s-5718MiB/s (5996MB/s-5996MB/s), io=168GiB (180GB), run=30099-30099msec

Disk stats (read/write):
    md1: ios=44046954/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=2753712/0, aggrmerge=0/0, aggrticks=276407/0, aggrin_queue=279556, aggrutil=98.35%
  nvme15n1: ios=2753931/0, merge=0/0, ticks=283360/0, in_queue=285472, util=97.82%
  nvme6n1: ios=2752987/0, merge=0/0, ticks=269672/0, in_queue=271524, util=97.94%
  nvme9n1: ios=2753816/0, merge=0/0, ticks=273484/0, in_queue=277976, util=98.03%
  nvme11n1: ios=2756095/0, merge=0/0, ticks=286796/0, in_queue=293088, util=98.34%
  nvme2n1: ios=2753639/0, merge=0/0, ticks=270156/0, in_queue=274176, util=97.81%
  nvme14n1: ios=2752786/0, merge=0/0, ticks=301204/0, in_queue=302976, util=97.90%
  nvme5n1: ios=2752563/0, merge=0/0, ticks=267016/0, in_queue=269432, util=98.14%
  nvme8n1: ios=2753362/0, merge=0/0, ticks=277100/0, in_queue=278920, util=97.97%
  nvme10n1: ios=2754452/0, merge=0/0, ticks=269808/0, in_queue=271640, util=98.01%
  nvme1n1: ios=2754344/0, merge=0/0, ticks=279604/0, in_queue=284584, util=98.32%
  nvme13n1: ios=2753068/0, merge=0/0, ticks=280256/0, in_queue=284664, util=98.15%
  nvme4n1: ios=2754080/0, merge=0/0, ticks=278680/0, in_queue=285020, util=98.35%
  nvme7n1: ios=2753482/0, merge=0/0, ticks=277408/0, in_queue=280192, util=98.16%
  nvme0n1: ios=2754091/0, merge=0/0, ticks=269240/0, in_queue=271364, util=97.89%
  nvme12n1: ios=2753664/0, merge=0/0, ticks=269556/0, in_queue=270540, util=97.91%
  nvme3n1: ios=2753032/0, merge=0/0, ticks=269172/0, in_queue=271340, util=98.01%
[ perf record: Woken up 1501 times to write data ]
Warning:
1 out of order events recorded.
[ perf record: Captured and wrote 595.841 MB perf.data (15527198 samples) ]
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$
```

## perf results

```console
Samples: 15M of event 'cycles:ppp', Event count (approx.): 228278046116764448
Overhead  Command  Shared Object       Symbol
  73.48%  fio      [kernel.kallsyms]   [k] osq_lock
   4.44%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   3.49%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   1.19%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   0.70%  fio      [kernel.kallsyms]   [k] down_write
   0.70%  fio      [kernel.kallsyms]   [k] md_make_request
   0.60%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   0.56%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   0.44%  fio      [kernel.kallsyms]   [k] rwsem_spin_on_owner
   0.35%  fio      [kernel.kallsyms]   [k] up_write
   0.34%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   0.32%  fio      [kernel.kallsyms]   [k] finish_task_switch
   0.32%  fio      [kernel.kallsyms]   [k] rwsem_down_write_failed
   0.28%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.27%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   0.26%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.26%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.26%  fio      fio                 [.] get_io_u
   0.25%  fio      [kernel.kallsyms]   [k] _raw_spin_trylock
   0.23%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.22%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   0.19%  fio      [kernel.kallsyms]   [k] find_first_bit
   0.19%  fio      [kernel.kallsyms]   [k] wake_q_add
   0.18%  fio      [kernel.kallsyms]   [k] dequeue_entity
   0.18%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.18%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.17%  fio      [kernel.kallsyms]   [k] _raw_spin_unlock_irqrestore
   0.17%  fio      fio                 [.] td_io_queue
   0.16%  fio      [kernel.kallsyms]   [k] raid0_make_request
   0.16%  fio      [kernel.kallsyms]   [.] native_irq_return_iret
   0.15%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   0.15%  fio      [kernel.kallsyms]   [k] blk_mq_get_tag
   0.15%  fio      [kernel.kallsyms]   [k] __blk_mq_run_hw_queue
   0.14%  fio      [kernel.kallsyms]   [k] gup_pte_range
   0.14%  fio      [kernel.kallsyms]   [k] blk_throtl_bio
   0.14%  fio      [kernel.kallsyms]   [k] select_idle_sibling
   0.13%  fio      [kernel.kallsyms]   [k] dio_bio_complete
   0.13%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.13%  fio      [kernel.kallsyms]   [k] blk_queue_split
   0.13%  fio      [kernel.kallsyms]   [k] update_curr
   0.12%  fio      [kernel.kallsyms]   [k] system_call_fast_compare_end
   0.12%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   0.12%  fio      [kernel.kallsyms]   [k] iov_iter_advance
   0.12%  fio      [kernel.kallsyms]   [k] __bitmap_intersects
   0.12%  fio      [kernel.kallsyms]   [k] update_blocked_averages
   0.12%  fio      [kernel.kallsyms]   [k] block_llseek
```
