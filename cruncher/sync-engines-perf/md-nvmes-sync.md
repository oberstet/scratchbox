# sync engine on MD

## without perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo /opt/fio/bin/fio md-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 1024 (f=1024): [r(1024)][100.0%][r=6130MiB/s,w=0KiB/s][r=1569k,w=0 IOPS][eta 00m:00s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=120370: Wed Jan 25 12:21:36 2017
   read: IOPS=1562k, BW=6101MiB/s (6397MB/s)(180GiB/30152msec)
  cpu          : usr=0.13%, sys=15.84%, ctx=48042122, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=47091584,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=6101MiB/s (6397MB/s), 6101MiB/s-6101MiB/s (6397MB/s-6397MB/s), io=180GiB (193GB), run=30152-30152msec

Disk stats (read/write):
    md1: ios=46785655/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=2943224/0, aggrmerge=0/0, aggrticks=22810/0, aggrin_queue=22296, aggrutil=52.33%
  nvme15n1: ios=2941215/0, merge=0/0, ticks=22944/0, in_queue=22312, util=51.84%
  nvme6n1: ios=2945254/0, merge=0/0, ticks=22828/0, in_queue=22268, util=51.86%
  nvme9n1: ios=2943695/0, merge=0/0, ticks=22500/0, in_queue=22296, util=51.16%
  nvme11n1: ios=2940946/0, merge=0/0, ticks=22512/0, in_queue=22148, util=51.29%
  nvme2n1: ios=2942602/0, merge=0/0, ticks=23192/0, in_queue=22832, util=52.33%
  nvme14n1: ios=2943102/0, merge=0/0, ticks=22816/0, in_queue=22176, util=51.40%
  nvme5n1: ios=2945415/0, merge=0/0, ticks=22960/0, in_queue=22364, util=51.69%
  nvme8n1: ios=2940100/0, merge=0/0, ticks=22904/0, in_queue=22200, util=51.51%
  nvme10n1: ios=2941776/0, merge=0/0, ticks=22908/0, in_queue=22268, util=51.56%
  nvme1n1: ios=2944039/0, merge=0/0, ticks=22036/0, in_queue=21744, util=50.12%
  nvme13n1: ios=2943624/0, merge=0/0, ticks=22520/0, in_queue=22136, util=50.83%
  nvme4n1: ios=2942718/0, merge=0/0, ticks=23176/0, in_queue=22804, util=52.20%
  nvme7n1: ios=2945415/0, merge=0/0, ticks=22748/0, in_queue=22160, util=51.89%
  nvme0n1: ios=2946256/0, merge=0/0, ticks=22792/0, in_queue=22284, util=51.99%
  nvme12n1: ios=2940946/0, merge=0/0, ticks=22784/0, in_queue=22048, util=52.01%
  nvme3n1: ios=2944481/0, merge=0/0, ticks=23340/0, in_queue=22704, util=52.06%
```

## with perf

```console
oberstet@svr-psql19:~/scm/parcit/RA/user/oberstet/sync-engines-perf$ sudo perf record /opt/fio/bin/fio md-nvmes-sync.fio
randread-md-nvmes: (g=0): rw=randread, bs=4096B-4096B,4096B-4096B,4096B-4096B, ioengine=sync, iodepth=1
...
fio-2.17-17-g9cf1
Starting 1024 threads
Jobs: 999 (f=999): [r(2),_(1),r(3),_(3),r(10),_(1),r(5),_(2),r(1),_(1),r(1),_(3),r(3),_(1),r(1),_(1),r(1),_(1),r(2),_(2),r(2),_(1),r(1),_(2),r(1),_(4),r(92),_(1),r(821),_(1),r(53)][4.1%][r=6523MiB/s,w=0KiB/s][r=1670k,w=0 IOPS][eta 12m:30s]
randread-md-nvmes: (groupid=0, jobs=1024): err= 0: pid=119153: Wed Jan 25 12:19:30 2017
   read: IOPS=1661k, BW=6486MiB/s (6802MB/s)(191GiB/30164msec)
  cpu          : usr=0.16%, sys=15.19%, ctx=50918579, majf=0, minf=1024
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=50088256,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=6486MiB/s (6802MB/s), 6486MiB/s-6486MiB/s (6802MB/s-6802MB/s), io=191GiB (205GB), run=30164-30164msec

Disk stats (read/write):
    md1: ios=49990970/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=3130516/0, aggrmerge=0/0, aggrticks=31945/0, aggrin_queue=31421, aggrutil=63.32%
  nvme15n1: ios=3131567/0, merge=0/0, ticks=32348/0, in_queue=31756, util=62.56%
  nvme6n1: ios=3128627/0, merge=0/0, ticks=32188/0, in_queue=31568, util=62.41%
  nvme9n1: ios=3136488/0, merge=0/0, ticks=31868/0, in_queue=31480, util=62.91%
  nvme11n1: ios=3129245/0, merge=0/0, ticks=31620/0, in_queue=31272, util=61.95%
  nvme2n1: ios=3130592/0, merge=0/0, ticks=32008/0, in_queue=31660, util=61.84%
  nvme14n1: ios=3127730/0, merge=0/0, ticks=32388/0, in_queue=31708, util=62.93%
  nvme5n1: ios=3125669/0, merge=0/0, ticks=32532/0, in_queue=31800, util=62.57%
  nvme8n1: ios=3132626/0, merge=0/0, ticks=32024/0, in_queue=31504, util=62.22%
  nvme10n1: ios=3127565/0, merge=0/0, ticks=32336/0, in_queue=31764, util=63.32%
  nvme1n1: ios=3130847/0, merge=0/0, ticks=31236/0, in_queue=30920, util=61.43%
  nvme13n1: ios=3133052/0, merge=0/0, ticks=31544/0, in_queue=31088, util=61.63%
  nvme4n1: ios=3130700/0, merge=0/0, ticks=31984/0, in_queue=31524, util=62.64%
  nvme7n1: ios=3130978/0, merge=0/0, ticks=32072/0, in_queue=31604, util=61.93%
  nvme0n1: ios=3130488/0, merge=0/0, ticks=31508/0, in_queue=30920, util=61.71%
  nvme12n1: ios=3131768/0, merge=0/0, ticks=31804/0, in_queue=31064, util=61.99%
  nvme3n1: ios=3130314/0, merge=0/0, ticks=31664/0, in_queue=31108, util=61.73%
[ perf record: Woken up 291 times to write data ]
[ perf record: Captured and wrote 723.049 MB perf.data (18839617 samples) ]
```

## perf results

```console
Samples: 18M of event 'cycles:ppp', Event count (approx.): 234837748285505976
Overhead  Command  Shared Object       Symbol
  82.77%  fio      [kernel.kallsyms]   [k] osq_lock
   3.12%  fio      [kernel.kallsyms]   [k] nohz_balance_exit_idle
   1.40%  fio      [kernel.kallsyms]   [k] trigger_load_balance
   1.01%  fio      [kernel.kallsyms]   [k] native_queued_spin_lock_slowpath
   0.67%  fio      [kernel.kallsyms]   [k] try_to_wake_up
   0.47%  fio      [kernel.kallsyms]   [k] md_make_request
   0.46%  fio      [kernel.kallsyms]   [k] _raw_spin_lock_irqsave
   0.37%  fio      [kernel.kallsyms]   [k] down_write
   0.36%  fio      [kernel.kallsyms]   [k] _raw_spin_lock
   0.28%  fio      [kernel.kallsyms]   [k] do_blockdev_direct_IO
   0.26%  fio      [kernel.kallsyms]   [k] get_user_pages_fast
   0.23%  fio      [kernel.kallsyms]   [k] finish_task_switch
   0.22%  fio      [kernel.kallsyms]   [k] rwsem_down_write_failed
   0.19%  fio      [kernel.kallsyms]   [k] rwsem_spin_on_owner
   0.18%  fio      [kernel.kallsyms]   [k] up_write
   0.17%  fio      [kernel.kallsyms]   [k] _raw_spin_trylock
   0.16%  fio      [kernel.kallsyms]   [k] generic_make_request_checks
   0.15%  fio      [kernel.kallsyms]   [k] __nvme_process_cq
   0.14%  fio      fio                 [.] get_io_u
   0.14%  fio      [kernel.kallsyms]   [k] idle_cpu
   0.13%  fio      [kernel.kallsyms]   [.] native_irq_return_iret
   0.12%  fio      [kernel.kallsyms]   [k] blk_account_io_start
   0.12%  fio      [kernel.kallsyms]   [k] blk_account_io_completion
   0.11%  fio      [kernel.kallsyms]   [k] __schedule
   0.11%  fio      [kernel.kallsyms]   [k] _raw_spin_unlock_irqrestore
   0.11%  fio      fio                 [.] clock_thread_fn
```
