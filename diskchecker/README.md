Summary: Purchase [Intel DC S3700](http://www.intel.com/content/www/us/en/solid-state-drives/solid-state-drives-dc-s3700-series.html).
______

1.	Use magnetic platter or SSD with power failure protection
2.	Disable write cache on the host disk where VM resides
3.	Use SAS based VirtualBox disks (using the “LSI SAS Controller”)
4.	Disable “use host cache” option in VirtualBox on disks
5.	Use ZFS
6.	Use diskchecker.pl for “pull the plug” testing

________

    ./diskchecker.pl -l
    
    ./diskchecker.pl -s 192.168.1.136 create test_file 500
    
    ./diskchecker.pl -s 192.168.1.136 verify test_file
    
________

I used diskchecker.pl

http://brad.livejournal.com/2116715.html
https://gist.github.com/bradfitz/3172656
http://rhaas.blogspot.de/2010/10/wal-reliability.html

to check if fsyncs from inside the VMs are actually persisting data or only cheating.

Host: Windows 7 Prof. 64 Bit, Oracle VM latest
Guests: FreeBSD 9.1 amd64

"Pull-the-plug" testing was done by 2 methods

A. hard reset of the VM
B. pull power plug of host

Findings:

1) For surviving A., it seems to suffice to use SATA, SCSI or SAS guest controller (not IDE) in VirtualBox _and_ disable the "Use host cache" option on the guest controller.

Note: Its unfortunate that the VirtualBox defaults for e.g. Ubuntu do exactly that (SATA and no host cache), but not for FreeBSD. Default there is IDE with "use host cache" enabled.

2) For surviving B., its more tricky.

2.1) OCZ Vertex 2 SSD : It is _not_ power failure resilant. Disabling write cache does not help. In fact, nothing I tried makes this SSD power failure resilant. Probably no surprise.

2.2) Samsung HD642 magnetic disk: Disabled the write cache .. thats required, but not sufficient.

2.3) Using the VirtualBox IDE or SATA guest controllers: both don't work. Not resilant

2.4) So use SCSI or SAS VirtualBox guest controller.

2.5) Use ZFS (or probably UFS without soft updates)

ZFS seem to be able to robustly tell the disk to just sync at the right moment. It works. Even from inside VMs.

In summary, the following is resilant to repeated power plugs:

- Host disk write cache disabled or disk with power failure protection (or BBU controller)
- file (VDI) backed guest disks
- SCSI/SAS guest controller
- "use host cache" disabled
- ZFS inside guest

The resulting synchronous write performance is ... terrible. diskchecker.pl reports 16/s

For hosting our VMs here in office, we now look at purchasing Intel DC S3700 SSDs.


