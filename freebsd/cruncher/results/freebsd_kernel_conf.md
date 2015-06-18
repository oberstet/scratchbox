```console
root@s4l-zfs:~/src/sys/amd64/conf # uname -a
FreeBSD s4l-zfs 11.0-CURRENT FreeBSD 11.0-CURRENT #0 r280797+e9f6590(strndup)-dirty: Mon Mar 30 09:27:52 CEST 2015     root@s4l-zfs:/usr/obj/root/src/sys/X  amd64
root@s4l-zfs:~/src/sys/amd64/conf # pwd
/root/src/sys/amd64/conf
root@s4l-zfs:~/src/sys/amd64/conf # cat X
cpu     HAMMER
options     PREEMPTION
options     SMP
options         HWPMC_HOOKS
device      acpi
options     ACPI_DMAR

options     INVARIANTS
options     INVARIANT_SUPPORT
#options        WITNESS
#options    WITNESS_SKIPSPIN
#options        DEBUG_LOCKS
#options        DEBUG_VFS_LOCKS
#options        DIAGNOSTIC
#options        DEBUG_MEMGUARD
#options        BUS_DEBUG

ident       X
nooptions   INCLUDE_CONFIG_FILE

makeoptions DEBUG=-gdwarf-2

#options    KDB
#options    KDB_TRACE
#options    DDB
#options    DDB_NUMSYM
#options        GDB
#options        KTR
#options        KTR_ENTRIES=131072
#options    BREAK_TO_DEBUGGER
#options    ALT_BREAK_TO_DEBUGGER

options     INET
options     INET6
options     SCTP
options     SCHED_ULE
options     SOFTUPDATES
options     QUOTA
options     UFS_DIRHASH
options     UFS_ACL
options     UFS_EXTATTR
options     UFS_EXTATTR_AUTOSTART
options     SUIDDIR
options     NFS_ROOT
options     COMPAT_43
options     COMPAT_FREEBSD4
options     COMPAT_43TTY
options     COMPAT_FREEBSD32
options     SCSI_DELAY=15000
options     KTRACE
options     _KPOSIX_PRIORITY_SCHEDULING
options     KBD_INSTALL_CDEV
options     CAPABILITY_MODE
options     CAPABILITIES
options     MAC
options     PRINTF_BUFR_SIZE=128
options     COMPAT_43TTY
options     COMPAT_FREEBSD4
options     COMPAT_FREEBSD5
options     COMPAT_FREEBSD6
options     COMPAT_FREEBSD7
options     COMPAT_FREEBSD9
options     COMPAT_FREEBSD10

device      isa
device      pci

device      atkbdc
device      atkbd
device      psm

device      vga

# syscons is the default console driver, resembling an SCO console
device      sc
options     SC_NO_CUTPASTE
#options        SC_NO_SYSMOUSE
#options        SC_DISABLE_REBOOT

device      loop        # Network loopback
device      ether       # Ethernet support
device      mem
device      io
device      bpf
device      uart
root@s4l-zfs:~/src/sys/amd64/conf # 
```
