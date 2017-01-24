# sync engine on individual NVMes

## FIO results

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio individual-nvmes-sync.fio
randread-individual-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1023 (f=16368): [_(1),r(1023)][51.6%][r=7276MiB/s,w=0KiB/s][r=1863k,w=0 IOPS][eta 00m:30s]
randread-individual-nvmes: (groupid=0, jobs=1024): err= 0: pid=137705: Tue Jan 24 10:05:53 2017
   read: IOPS=1859k, BW=7262MiB/s (7614MB/s)(213GiB/30073msec)
  cpu          : usr=0.88%, sys=10.56%, ctx=55300698, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=55905088,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=7262MiB/s (7614MB/s), 7262MiB/s-7262MiB/s (7614MB/s-7614MB/s), io=213GiB (229GB), run=30073-30073msec

Disk stats (read/write):
  nvme0n1: ios=3476092/0, merge=0/0, ticks=1008104/0, in_queue=1020140, util=95.73%
  nvme1n1: ios=3494196/0, merge=0/0, ticks=976544/0, in_queue=1039472, util=96.41%
  nvme2n1: ios=3494196/0, merge=0/0, ticks=803312/0, in_queue=853296, util=95.95%
  nvme3n1: ios=3494196/0, merge=0/0, ticks=884300/0, in_queue=897344, util=95.07%
  nvme4n1: ios=3494196/0, merge=0/0, ticks=871268/0, in_queue=930932, util=96.05%
  nvme5n1: ios=3494196/0, merge=0/0, ticks=992224/0, in_queue=1005296, util=95.32%
  nvme6n1: ios=3494196/0, merge=0/0, ticks=780636/0, in_queue=792184, util=95.44%
  nvme7n1: ios=3494196/0, merge=0/0, ticks=895436/0, in_queue=906724, util=95.30%
  nvme8n1: ios=3494196/0, merge=0/0, ticks=1002456/0, in_queue=1023564, util=95.91%
  nvme9n1: ios=3494196/0, merge=0/0, ticks=869748/0, in_queue=934428, util=96.43%
  nvme10n1: ios=3494196/0, merge=0/0, ticks=927836/0, in_queue=936820, util=95.31%
  nvme11n1: ios=3494196/0, merge=0/0, ticks=953348/0, in_queue=1021528, util=96.79%
  nvme12n1: ios=3494196/0, merge=0/0, ticks=988628/0, in_queue=1002512, util=95.93%
  nvme13n1: ios=3494196/0, merge=0/0, ticks=780084/0, in_queue=824556, util=96.75%
  nvme14n1: ios=3493172/0, merge=0/0, ticks=947268/0, in_queue=957056, util=95.96%
  nvme15n1: ios=3493172/0, merge=0/0, ticks=804580/0, in_queue=813984, util=95.78%
[ perf record: Woken up 405 times to write data ]
Warning:
41 out of order events recorded.
[ perf record: Captured and wrote 487.676 MB perf.data (12757742 samples) ]
```

## perf results

```console
Samples: 12M of event 'cycles:ppp', Event count (approx.): 142828545602519333
Overhead  Command  Shared Object       Symbol
  27.56%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   7.04%  fio      [kernel.kallsyms]   [k] osq_lock
   6.60%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   4.95%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   3.71%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   2.11%  fio      [kernel.kallsyms]   [k] finish_task_switch
   2.08%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   1.58%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   1.58%  fio      [kernel.kallsyms]   [k] __fget
   1.48%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   1.38%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   1.33%  fio      [kernel.kallsyms]   [k] _raw_spin_trylock
   1.30%  fio      [kernel.kallsyms]   [k] down_write
   1.04%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   1.03%  fio      fio                 [.] get_io_u
   1.03%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.96%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.94%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.88%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.87%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   0.83%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.72%  fio      fio                 [.] td_io_queue
   0.70%  fio      [kernel.kallsyms]   [k] switch_mm_irqs_off
   0.52%  fio      [kernel.kallsyms]   [.] native_irq_return_iret
   0.51%  fio      [kernel.kallsyms]   [k] __bt_get.isra.7
   0.48%  fio      [kernel.kallsyms]   [k] __do_softirq
   0.45%  fio      [kernel.kallsyms]   [k] blk_rq_map_sg
   0.44%  fio      [kernel.kallsyms]   [k] __switch_to
   0.44%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.42%  fio      [kernel.kallsyms]   [k] __schedule
   0.42%  fio      [kernel.kallsyms]   [k] nvme_complete_rq
   0.42%  fio      fio                 [.] fio_syncio_queue
   0.40%  fio      [kernel.kallsyms]   [k] dio_bio_complete
   0.39%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.37%  fio      [kernel.kallsyms]   [k] cpuacct_charge
   0.36%  fio      [kernel.kallsyms]   [k] __blk_mq_run_hw_queue
   0.36%  fio      [kernel.kallsyms]   [k] block_llseek
   0.35%  fio      [kernel.kallsyms]   [k] __perf_event_task_sched_out
   0.35%  fio      [kernel.kallsyms]   [k] pick_next_task_fair
   0.35%  fio      fio                 [.] thread_main
   0.32%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.32%  fio      fio                 [.] get_next_rand_offset
   0.30%  fio      [kernel.kallsyms]   [k] bt_clear_tag
   0.29%  fio      [kernel.kallsyms]   [k] blk_throtl_bio
   0.29%  fio      [kernel.kallsyms]   [k] nvme_setup_cmd
   0.29%  fio      [kernel.kallsyms]   [k] blk_rq_bio_prep
```
