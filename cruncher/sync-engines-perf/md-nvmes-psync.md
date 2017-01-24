# psync engine on individual NVMes

## FIO results

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio md-nvmes-psync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=psync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=8350MiB/s,w=0KiB/s][r=2138k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=141654: Tue Jan 24 10:15:44 2017
   read: IOPS=2131k, BW=8326MiB/s (8730MB/s)(244GiB/30066msec)
  cpu          : usr=0.80%, sys=12.22%, ctx=63358199, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=64081664,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=8326MiB/s (8730MB/s), 8326MiB/s-8326MiB/s (8730MB/s-8730MB/s), io=244GiB (262GB), run=30066-30066msec

Disk stats (read/write):
    md1: ios=64063277/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=4005104/0, aggrmerge=0/0, aggrticks=894525/0, aggrin_queue=917950, aggrutil=99.01%
  nvme15n1: ios=4004543/0, merge=0/0, ticks=798088/0, in_queue=805660, util=97.89%
  nvme6n1: ios=4003085/0, merge=0/0, ticks=813820/0, in_queue=822528, util=98.05%
  nvme9n1: ios=4000635/0, merge=0/0, ticks=845000/0, in_queue=892984, util=99.01%
  nvme11n1: ios=4006064/0, merge=0/0, ticks=929328/0, in_queue=978972, util=98.86%
  nvme2n1: ios=4004596/0, merge=0/0, ticks=843140/0, in_queue=887768, util=98.88%
  nvme14n1: ios=4007342/0, merge=0/0, ticks=950624/0, in_queue=958484, util=98.02%
  nvme5n1: ios=4005224/0, merge=0/0, ticks=997340/0, in_queue=1009052, util=98.18%
  nvme8n1: ios=4008310/0, merge=0/0, ticks=953852/0, in_queue=963708, util=98.17%
  nvme10n1: ios=4003055/0, merge=0/0, ticks=894936/0, in_queue=904016, util=98.16%
  nvme1n1: ios=4007011/0, merge=0/0, ticks=916952/0, in_queue=959748, util=98.91%
  nvme13n1: ios=4006076/0, merge=0/0, ticks=808728/0, in_queue=844388, util=98.69%
  nvme4n1: ios=4004984/0, merge=0/0, ticks=851624/0, in_queue=899228, util=99.00%
  nvme7n1: ios=4006141/0, merge=0/0, ticks=908060/0, in_queue=916832, util=98.05%
  nvme0n1: ios=4002291/0, merge=0/0, ticks=981448/0, in_queue=997420, util=98.43%
  nvme12n1: ios=4007259/0, merge=0/0, ticks=928732/0, in_queue=938384, util=98.35%
  nvme3n1: ios=4005048/0, merge=0/0, ticks=890732/0, in_queue=908040, util=98.39%
[ perf record: Woken up 90 times to write data ]
Warning:
17 out of order events recorded.
[ perf record: Captured and wrote 607.092 MB perf.data (15898515 samples) ]
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$
```

## perf results

```console
Samples: 15M of event 'cycles:ppp', Event count (approx.): 78757338785604787
Overhead  Command  Shared Object       Symbol
  25.87%  fio      [kernel.kallsyms]   [k] md_make_request
  25.33%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   3.75%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   2.21%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   1.78%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   1.60%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   1.57%  fio      [kernel.kallsyms]   [k] raid0_make_request
   1.13%  fio      fio                 [.] get_io_u
   1.04%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   1.03%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   1.03%  fio      [kernel.kallsyms]   [k] finish_task_switch
   0.87%  fio      [kernel.kallsyms]   [k] native_write_msr
   0.87%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.75%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   0.68%  fio      [kernel.kallsyms]   [k] nvme_queue_rq
   0.61%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.56%  fio      [kernel.kallsyms]   [k] __switch_to
   0.56%  fio      [kernel.kallsyms]   [k] blk_mq_map_queue
   0.52%  fio      [kernel.kallsyms]   [k] bt_clear_tag
   0.51%  fio      fio                 [.] td_io_queue
   0.51%  fio      [kernel.kallsyms]   [k] __sched_text_start
   0.50%  fio      fio                 [.] thread_main
   0.50%  fio      [kernel.kallsyms]   [k] __do_softirq
   0.49%  fio      [kernel.kallsyms]   [k] update_curr
   0.49%  fio      [kernel.kallsyms]   [k] blk_queue_split
   0.48%  fio      [kernel.kallsyms]   [k] __blk_mq_alloc_request
   0.46%  fio      [kernel.kallsyms]   [k] osq_lock
   0.45%  fio      [kernel.kallsyms]   [k] blk_rq_map_sg
   0.43%  fio      [kernel.kallsyms]   [k] __schedule
   0.43%  fio      [kernel.kallsyms]   [k] blk_mq_make_request
   0.43%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.42%  fio      [kernel.kallsyms]   [k] gup_pte_range
   0.39%  fio      [kernel.kallsyms]   [k] _raw_spin_trylock
   0.39%  fio      [kernel.kallsyms]   [k] dequeue_entity
   0.39%  fio      [kernel.kallsyms]   [k] __percpu_counter_add
   0.38%  fio      [kernel.kallsyms]   [k] switch_mm_irqs_off
   0.38%  fio      [kernel.kallsyms]   [k] __fget
   0.36%  fio      [kernel.kallsyms]   [k] enqueue_entity
   0.35%  fio      fio                 [.] fio_psyncio_queue
   0.35%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.34%  fio      [kernel.kallsyms]   [k] blk_account_io_done
   0.34%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.34%  fio      [kernel.kallsyms]   [k] blk_mq_start_request
   0.34%  fio      [kernel.kallsyms]   [k] bio_alloc_bioset
   0.32%  fio      [kernel.kallsyms]   [k] blk_throtl_bio
   0.32%  fio      fio                 [.] io_u_sync_complete
```
