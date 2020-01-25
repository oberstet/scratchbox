## Clone disk

Identify source and target block device:

```
oberstet@intel-nuci7:~$ hwinfo --block --short
disk:                                                           
  /dev/nvme0n1         Intel Disk
  /dev/nvme1n1         Intel Disk
partition:
  /dev/nvme0n1p1       Partition
  /dev/nvme0n1p2       Partition
```

Update the system and reboot into **single-user mode**:

```
sudo apt update
sudo apt dist-upgrade
sudo ap autoremove
sudo reboot
```

> You want to do the disk copy in single-user mode, since the copy is not synchronized with filesystem writes. This might result in a corrupt root filesystem, which may in turn require first booting into single-user/recovery mode to do a 'fsck /dev/nvme0p2` or similar.

Copy block device **from** `/dev/nvme0n1` **to** `/dev/nvme1n1`:

```
oberstet@intel-nuci7:~$ sudo ddrescue -vf /dev/nvme0n1 /dev/nvme1n1
GNU ddrescue 1.22
About to copy 128035 MBytes from '/dev/nvme0n1' to '/dev/nvme1n1'
    Starting positions: infile = 0 B,  outfile = 0 B
    Copy block size: 128 sectors       Initial skip size: 2560 sectors
Sector size: 512 Bytes

     ipos:  128035 MB, non-trimmed:        0 B,  current rate:  23683 kB/s
     opos:  128035 MB, non-scraped:        0 B,  average rate:    128 MB/s
non-tried:        0 B,  bad-sector:        0 B,    error rate:       0 B/s
  rescued:  128035 MB,   bad areas:        0,        run time:     16m 32s
pct rescued:  100.00%, read errors:        0,  remaining time:         n/a
                              time since last successful read:         n/a
Finished                                     
```

Now use gparted to enlarge the root partition to include the new free disk space.

Check free space

```
oberstet@intel-nuci7:~$ df -h /
Dateisystem    Größe Benutzt Verf. Verw% Eingehängt auf
/dev/nvme0n1p2  469G    108G  342G   24% /
```

## Profiling
 * https://wiki.freebsd.org/DTrace
 * https://wiki.freebsd.org/PmcTools


### Linux (SO_REUSEPORT)

 * https://lwn.net/Articles/542629/


### Linux (perf)


http://www.berniepope.id.au/linuxPerfEvents.html



	sudo perf record -g -e cycles,cache-misses,branch-misses,stalled-cycles-frontend,stalled-cycles-backend `which wstest` -m testeeserver -w ws://127.0.0.1:9000

	sudo perf report

#### Install from package

	sudo apt-get install linux-tools-common 
	sudo apt-get install linux-tools
	sudo apt-get install linux-tools-3.8.0-32

#### Build from source

	sudo apt-get install -y libelf-dev
	sudo apt-get install -y binutils-dev
	sudo apt-get install -y libdwarf-dev
	sudo apt-get install -y flex
	sudo apt-get install -y bison
	sudo apt-get install -y libunwind-dev
	sudo apt-get install -y elfutils
	sudo apt-get install -y libdw-dev
	sudo apt-get install -y libaudit-dev
	sudo apt-get install -y libslang-dev
	sudo apt-get install -y libgtk2.0-dev
	sudo apt-get install -y libnuma-dev

	wget https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.11.tar.bz2
	cd linux-3.11/tools/perf/

	export PREFIX=$HOME/local
	export PYTHON=$HOME/local/bin/python2.7
	export LD_LIBRARY_PATH=$HOME/local/lib

	make
	make install


sudo /home/oberstet/build/linux-3.11/tools/perf/perf record ..
sudo /home/oberstet/build/linux-3.11/tools/perf/perf script -g python



Record:
sudo ~/build/linux-3.11/tools/perf/perf record -a --event raw_syscalls:sys_enter

Generate template:
sudo ~/build/linux-3.11/tools/perf/perf script -g python

Analyze:
sudo ~/build/linux-3.11/tools/perf/perf script -s perf-script.py




 * http://www.jauu.net/data/pdf/cpu-profiling.pdf

 * http://www.linuxtag.org/2013/fileadmin/www.linuxtag.org/slides/Arnaldo_Melo_-_Linux__perf__tools__Overview_and_Current_Developments.e323.pdf
 * http://en.wikipedia.org/wiki/Perf_%28Linux%29
 * https://perf.wiki.kernel.org/index.php/Main_Page
 * https://perf.wiki.kernel.org/index.php/Tutorial
 * http://www.pixelbeat.org/programming/profiling/
 * http://penberg.blogspot.co.uk/2009/06/jato-has-profiler.html
 * http://lists.freedesktop.org/archives/mesa-dev/2013-April/037952.html
 * http://web.eece.maine.edu/~vweaver/projects/perf_events/
 * http://stackoverflow.com/questions/12697028/profiling-output-of-jit-on-linux-with-perf-events-oprofile
 * http://stackoverflow.com/questions/tagged/perf
 * http://git.kernel.org/cgit/linux/kernel/git/tip/tip.git/tree/tools/perf
 * http://git.kernel.org/cgit/linux/kernel/git/tip/tip.git/tree/tools/perf/Documentation/perf-script-python.txt
 * http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=80d496be89ed7dede5abee5c057634e80a31c82d

## Health Monitoring

 * http://dtrace.org/blogs/brendan/2012/02/29/the-use-method/
 * http://dtrace.org/blogs/brendan/2012/03/07/the-use-method-linux-performance-checklist/
 * http://dtrace.org/blogs/brendan/2013/09/25/the-use-method-freebsd-performance-checklist/

