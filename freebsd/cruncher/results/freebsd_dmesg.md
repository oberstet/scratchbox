```console
root@s4l-zfs:~ # dmesg
Copyright (c) 1992-2015 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
    The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 11.0-CURRENT #0 r280797+e9f6590(strndup)-dirty: Mon Mar 30 09:27:52 CEST 2015
    root@s4l-zfs:/usr/obj/root/src/sys/X amd64
FreeBSD clang version 3.4.1 (tags/RELEASE_34/dot1-final 208032) 20140512
CPU: Intel(R) Xeon(R) CPU E7-8857 v2 @ 3.00GHz (2992.85-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x306e7  Family=0x6  Model=0x3e  Stepping=7
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x7fbee3ff<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,SMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,PCID,DCA,SSE4.1,SSE4.2,x2APIC,POPCNT,TSCDLT,AESNI,XSAVE,OSXSAVE,AVX,F16C,RDRAND>
  AMD Features=0x2c100800<SYSCALL,NX,Page1GB,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  Structured Extended Features=0x281<FSGSBASE,SMEP,ERMS>
  XSAVE Features=0x1<XSAVEOPT>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID,VID,PostIntr
  TSC: P-state invariant, performance statistics
real memory  = 3298434220032 (3145632 MB)
avail memory = 3211526279168 (3062750 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <ALASKA A M I >
FreeBSD/SMP: Multiprocessor System Detected: 48 CPUs
FreeBSD/SMP: 4 package(s) x 12 core(s)
 cpu0 (BSP): APIC ID:  0
 cpu1 (AP): APIC ID:  2
 cpu2 (AP): APIC ID:  4
 cpu3 (AP): APIC ID:  6
 cpu4 (AP): APIC ID:  8
 cpu5 (AP): APIC ID: 10
 cpu6 (AP): APIC ID: 16
 cpu7 (AP): APIC ID: 18
 cpu8 (AP): APIC ID: 20
 cpu9 (AP): APIC ID: 22
 cpu10 (AP): APIC ID: 24
 cpu11 (AP): APIC ID: 26
 cpu12 (AP): APIC ID: 32
 cpu13 (AP): APIC ID: 34
 cpu14 (AP): APIC ID: 36
 cpu15 (AP): APIC ID: 38
 cpu16 (AP): APIC ID: 40
 cpu17 (AP): APIC ID: 42
 cpu18 (AP): APIC ID: 48
 cpu19 (AP): APIC ID: 50
 cpu20 (AP): APIC ID: 52
 cpu21 (AP): APIC ID: 54
 cpu22 (AP): APIC ID: 56
 cpu23 (AP): APIC ID: 58
 cpu24 (AP): APIC ID: 64
 cpu25 (AP): APIC ID: 66
 cpu26 (AP): APIC ID: 68
 cpu27 (AP): APIC ID: 70
 cpu28 (AP): APIC ID: 72
 cpu29 (AP): APIC ID: 74
 cpu30 (AP): APIC ID: 80
 cpu31 (AP): APIC ID: 82
 cpu32 (AP): APIC ID: 84
 cpu33 (AP): APIC ID: 86
 cpu34 (AP): APIC ID: 88
 cpu35 (AP): APIC ID: 90
 cpu36 (AP): APIC ID: 96
 cpu37 (AP): APIC ID: 98
 cpu38 (AP): APIC ID: 100
 cpu39 (AP): APIC ID: 102
 cpu40 (AP): APIC ID: 104
 cpu41 (AP): APIC ID: 106
 cpu42 (AP): APIC ID: 112
 cpu43 (AP): APIC ID: 114
 cpu44 (AP): APIC ID: 116
 cpu45 (AP): APIC ID: 118
 cpu46 (AP): APIC ID: 120
 cpu47 (AP): APIC ID: 122
ioapic0 <Version 2.0> irqs 0-23 on motherboard
ioapic1 <Version 2.0> irqs 24-47 on motherboard
ioapic2 <Version 2.0> irqs 48-71 on motherboard
ioapic3 <Version 2.0> irqs 72-95 on motherboard
ioapic4 <Version 2.0> irqs 96-119 on motherboard
random: entropy device infrastructure driver
random: selecting highest priority adaptor <Dummy>
random: SOFT: yarrow init()
random: selecting highest priority adaptor <Yarrow>
random: live provider: "Intel Secure Key RNG"
acpi0: <ALASKA A M I > on motherboard
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
cpu1: <ACPI CPU> on acpi0
cpu2: <ACPI CPU> on acpi0
cpu3: <ACPI CPU> on acpi0
cpu4: <ACPI CPU> on acpi0
cpu5: <ACPI CPU> on acpi0
cpu6: <ACPI CPU> on acpi0
cpu7: <ACPI CPU> on acpi0
cpu8: <ACPI CPU> on acpi0
cpu9: <ACPI CPU> on acpi0
cpu10: <ACPI CPU> on acpi0
cpu11: <ACPI CPU> on acpi0
cpu12: <ACPI CPU> on acpi0
cpu13: <ACPI CPU> on acpi0
cpu14: <ACPI CPU> on acpi0
cpu15: <ACPI CPU> on acpi0
cpu16: <ACPI CPU> on acpi0
cpu17: <ACPI CPU> on acpi0
cpu18: <ACPI CPU> on acpi0
cpu19: <ACPI CPU> on acpi0
cpu20: <ACPI CPU> on acpi0
cpu21: <ACPI CPU> on acpi0
cpu22: <ACPI CPU> on acpi0
cpu23: <ACPI CPU> on acpi0
cpu24: <ACPI CPU> on acpi0
cpu25: <ACPI CPU> on acpi0
cpu26: <ACPI CPU> on acpi0
cpu27: <ACPI CPU> on acpi0
cpu28: <ACPI CPU> on acpi0
cpu29: <ACPI CPU> on acpi0
cpu30: <ACPI CPU> on acpi0
cpu31: <ACPI CPU> on acpi0
cpu32: <ACPI CPU> on acpi0
cpu33: <ACPI CPU> on acpi0
cpu34: <ACPI CPU> on acpi0
cpu35: <ACPI CPU> on acpi0
cpu36: <ACPI CPU> on acpi0
cpu37: <ACPI CPU> on acpi0
cpu38: <ACPI CPU> on acpi0
cpu39: <ACPI CPU> on acpi0
cpu40: <ACPI CPU> on acpi0
cpu41: <ACPI CPU> on acpi0
cpu42: <ACPI CPU> on acpi0
cpu43: <ACPI CPU> on acpi0
cpu44: <ACPI CPU> on acpi0
cpu45: <ACPI CPU> on acpi0
cpu46: <ACPI CPU> on acpi0
cpu47: <ACPI CPU> on acpi0
dmar0: <DMA remap> iomem 0xc7ffc000-0xc7ffcfff on acpi0
dmar1: <DMA remap> iomem 0xe3ffc000-0xe3ffcfff on acpi0
dmar2: <DMA remap> iomem 0xfbffc000-0xfbffcfff on acpi0
dmar3: <DMA remap> iomem 0xabffc000-0xabffcfff on acpi0
dmar3: programming irte[0] rid 0xf0ff high 0x4f0ff low 0x300011
atrtc0: <AT realtime clock> port 0x70-0x71,0x74-0x77 irq 8 on acpi0
dmar3: programming irte[1] rid 0xf0ff high 0x4f0ff low 0x390001
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
dmar3: programming irte[2] rid 0xf0ff high 0x4f0ff low 0x3a0001
Event timer "i8254" frequency 1193182 Hz quality 100
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Event timer "HPET" frequency 14318180 Hz quality 350
Event timer "HPET1" frequency 14318180 Hz quality 340
Event timer "HPET2" frequency 14318180 Hz quality 340
Event timer "HPET3" frequency 14318180 Hz quality 340
Event timer "HPET4" frequency 14318180 Hz quality 340
Event timer "HPET5" frequency 14318180 Hz quality 340
Event timer "HPET6" frequency 14318180 Hz quality 340
Event timer "HPET7" frequency 14318180 Hz quality 340
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x408-0x40b on acpi0
pcib0: <ACPI Host-PCI bridge> on acpi0
pci255: <ACPI PCI bus> on pcib0
pcib1: <ACPI Host-PCI bridge> on acpi0
pci191: <ACPI PCI bus> on pcib1
pcib2: <ACPI Host-PCI bridge> on acpi0
pci127: <ACPI PCI bus> on pcib2
pcib3: <ACPI Host-PCI bridge> on acpi0
pci63: <ACPI PCI bus> on pcib3
pcib4: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib4
pcib5: <ACPI PCI-PCI bridge> irq 32 at device 2.0 on pci0
pci1: <ACPI PCI bus> on pcib5
ix0: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 2.7.4> port 0x4020-0x403f mem 0xaac00000-0xaadfffff,0xaae04000-0xaae07fff irq 32 at device 0.0 on pci1
ix0: Using MSIX interrupts with 49 vectors
unknown: dmar3 pci0:0:29:0 rid e8 domain 0 mgaw 48 agaw 48 re-mapped
unknown: dmar3 pci0:0:26:0 rid d0 domain 1 mgaw 48 agaw 48 re-mapped
ix0: dmar3 pci0:1:0:0 rid 100 domain 2 mgaw 48 agaw 48 re-mapped
dmar3: programming irte[3] rid 0x100 high 0x40100 low 0x430001
dmar3: programming irte[4] rid 0x100 high 0x40100 low 0x440001
dmar3: programming irte[5] rid 0x100 high 0x40100 low 0x450001
dmar3: programming irte[6] rid 0x100 high 0x40100 low 0x460001
dmar3: programming irte[7] rid 0x100 high 0x40100 low 0x470001
dmar3: programming irte[8] rid 0x100 high 0x40100 low 0x480001
dmar3: programming irte[9] rid 0x100 high 0x40100 low 0x490001
dmar3: programming irte[10] rid 0x100 high 0x40100 low 0x4a0001
dmar3: programming irte[11] rid 0x100 high 0x40100 low 0x4b0001
dmar3: programming irte[12] rid 0x100 high 0x40100 low 0x4c0001
dmar3: programming irte[13] rid 0x100 high 0x40100 low 0x4d0001
dmar3: programming irte[14] rid 0x100 high 0x40100 low 0x4e0001
dmar3: programming irte[15] rid 0x100 high 0x40100 low 0x4f0001
dmar3: programming irte[16] rid 0x100 high 0x40100 low 0x500001
dmar3: programming irte[17] rid 0x100 high 0x40100 low 0x510001
dmar3: programming irte[18] rid 0x100 high 0x40100 low 0x520001
dmar3: programming irte[19] rid 0x100 high 0x40100 low 0x530001
dmar3: programming irte[20] rid 0x100 high 0x40100 low 0x540001
dmar3: programming irte[21] rid 0x100 high 0x40100 low 0x550001
dmar3: programming irte[22] rid 0x100 high 0x40100 low 0x560001
dmar3: programming irte[23] rid 0x100 high 0x40100 low 0x570001
dmar3: programming irte[24] rid 0x100 high 0x40100 low 0x580001
dmar3: programming irte[25] rid 0x100 high 0x40100 low 0x590001
dmar3: programming irte[26] rid 0x100 high 0x40100 low 0x5a0001
dmar3: programming irte[27] rid 0x100 high 0x40100 low 0x5b0001
dmar3: programming irte[28] rid 0x100 high 0x40100 low 0x5c0001
dmar3: programming irte[29] rid 0x100 high 0x40100 low 0x5d0001
dmar3: programming irte[30] rid 0x100 high 0x40100 low 0x5e0001
dmar3: programming irte[31] rid 0x100 high 0x40100 low 0x5f0001
dmar3: programming irte[32] rid 0x100 high 0x40100 low 0x600001
dmar3: programming irte[33] rid 0x100 high 0x40100 low 0x610001
dmar3: programming irte[34] rid 0x100 high 0x40100 low 0x620001
dmar3: programming irte[35] rid 0x100 high 0x40100 low 0x630001
dmar3: programming irte[36] rid 0x100 high 0x40100 low 0x640001
dmar3: programming irte[37] rid 0x100 high 0x40100 low 0x650001
dmar3: programming irte[38] rid 0x100 high 0x40100 low 0x660001
dmar3: programming irte[39] rid 0x100 high 0x40100 low 0x670001
dmar3: programming irte[40] rid 0x100 high 0x40100 low 0x680001
dmar3: programming irte[41] rid 0x100 high 0x40100 low 0x690001
dmar3: programming irte[42] rid 0x100 high 0x40100 low 0x6a0001
dmar3: programming irte[43] rid 0x100 high 0x40100 low 0x6b0001
dmar3: programming irte[44] rid 0x100 high 0x40100 low 0x6c0001
dmar3: programming irte[45] rid 0x100 high 0x40100 low 0x6d0001
dmar3: programming irte[46] rid 0x100 high 0x40100 low 0x6e0001
dmar3: programming irte[47] rid 0x100 high 0x40100 low 0x6f0001
dmar3: programming irte[48] rid 0x100 high 0x40100 low 0x700001
dmar3: programming irte[49] rid 0x100 high 0x40100 low 0x710001
dmar3: programming irte[50] rid 0x100 high 0x40100 low 0x720001
dmar3: programming irte[51] rid 0x100 high 0x40100 low 0x730001
ix0: Ethernet address: c4:54:44:92:73:d2
ix0: PCI Express Bus: Speed 5.0GT/s Width x8
ix1: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 2.7.4> port 0x4000-0x401f mem 0xaaa00000-0xaabfffff,0xaae00000-0xaae03fff irq 36 at device 0.1 on pci1
ix1: Using MSIX interrupts with 49 vectors
ix1: dmar3 pci0:1:0:1 rid 101 domain 3 mgaw 48 agaw 48 re-mapped
dmar3: programming irte[52] rid 0x101 high 0x40101 low 0x740001
dmar3: programming irte[53] rid 0x101 high 0x40101 low 0x750001
dmar3: programming irte[54] rid 0x101 high 0x40101 low 0x760001
dmar3: programming irte[55] rid 0x101 high 0x40101 low 0x770001
dmar3: programming irte[56] rid 0x101 high 0x40101 low 0x780001
dmar3: programming irte[57] rid 0x101 high 0x40101 low 0x790001
dmar3: programming irte[58] rid 0x101 high 0x40101 low 0x7a0001
dmar3: programming irte[59] rid 0x101 high 0x40101 low 0x7b0001
dmar3: programming irte[60] rid 0x101 high 0x40101 low 0x7c0001
dmar3: programming irte[61] rid 0x101 high 0x40101 low 0x7d0001
dmar3: programming irte[62] rid 0x101 high 0x40101 low 0x7e0001
dmar3: programming irte[63] rid 0x101 high 0x40101 low 0x7f0001
dmar3: programming irte[64] rid 0x101 high 0x40101 low 0x810001
dmar3: programming irte[65] rid 0x101 high 0x40101 low 0x820001
dmar3: programming irte[66] rid 0x101 high 0x40101 low 0x830001
dmar3: programming irte[67] rid 0x101 high 0x40101 low 0x840001
dmar3: programming irte[68] rid 0x101 high 0x40101 low 0x850001
dmar3: programming irte[69] rid 0x101 high 0x40101 low 0x860001
dmar3: programming irte[70] rid 0x101 high 0x40101 low 0x870001
dmar3: programming irte[71] rid 0x101 high 0x40101 low 0x880001
dmar3: programming irte[72] rid 0x101 high 0x40101 low 0x890001
dmar3: programming irte[73] rid 0x101 high 0x40101 low 0x8a0001
dmar3: programming irte[74] rid 0x101 high 0x40101 low 0x8b0001
dmar3: programming irte[75] rid 0x101 high 0x40101 low 0x8c0001
dmar3: programming irte[76] rid 0x101 high 0x40101 low 0x8d0001
dmar3: programming irte[77] rid 0x101 high 0x40101 low 0x8e0001
dmar3: programming irte[78] rid 0x101 high 0x40101 low 0x8f0001
dmar3: programming irte[79] rid 0x101 high 0x40101 low 0x900001
dmar3: programming irte[80] rid 0x101 high 0x40101 low 0x910001
dmar3: programming irte[81] rid 0x101 high 0x40101 low 0x920001
dmar3: programming irte[82] rid 0x101 high 0x40101 low 0x930001
dmar3: programming irte[83] rid 0x101 high 0x40101 low 0x940001
dmar3: programming irte[84] rid 0x101 high 0x40101 low 0x950001
dmar3: programming irte[85] rid 0x101 high 0x40101 low 0x960001
dmar3: programming irte[86] rid 0x101 high 0x40101 low 0x970001
dmar3: programming irte[87] rid 0x101 high 0x40101 low 0x980001
dmar3: programming irte[88] rid 0x101 high 0x40101 low 0x990001
dmar3: programming irte[89] rid 0x101 high 0x40101 low 0x9a0001
dmar3: programming irte[90] rid 0x101 high 0x40101 low 0x9b0001
dmar3: programming irte[91] rid 0x101 high 0x40101 low 0x9c0001
dmar3: programming irte[92] rid 0x101 high 0x40101 low 0x9d0001
dmar3: programming irte[93] rid 0x101 high 0x40101 low 0x9e0001
dmar3: programming irte[94] rid 0x101 high 0x40101 low 0x9f0001
dmar3: programming irte[95] rid 0x101 high 0x40101 low 0xa00001
dmar3: programming irte[96] rid 0x101 high 0x40101 low 0xa10001
dmar3: programming irte[97] rid 0x101 high 0x40101 low 0xa20001
dmar3: programming irte[98] rid 0x101 high 0x40101 low 0xa30001
dmar3: programming irte[99] rid 0x101 high 0x40101 low 0xa40001
dmar3: programming irte[100] rid 0x101 high 0x40101 low 0xa50001
ix1: Ethernet address: c4:54:44:92:73:d3
ix1: PCI Express Bus: Speed 5.0GT/s Width x8
pcib6: <ACPI PCI-PCI bridge> irq 32 at device 2.2 on pci0
pci2: <ACPI PCI bus> on pcib6
pcib7: <ACPI PCI-PCI bridge> irq 40 at device 3.0 on pci0
pci3: <ACPI PCI bus> on pcib7
pcib8: <ACPI PCI-PCI bridge> irq 40 at device 3.2 on pci0
pci4: <ACPI PCI bus> on pcib8
mpr0: <LSI SAS3008> port 0x3000-0x30ff mem 0xaba00000-0xaba0ffff irq 42 at device 0.0 on pci4
mpr0: dmar3 pci0:4:0:0 rid 400 domain 4 mgaw 48 agaw 48 re-mapped
mpr0: IOCFacts  :
    MsgVersion: 0x205
    HeaderVersion: 0x2300
    IOCNumber: 0
    IOCExceptions: 0x0
    MaxChainDepth: 128
    NumberOfPorts: 1
    RequestCredit: 10240
    ProductID: 0x2221
    IOCRequestFrameSize: 32
    MaxInitiators: 32
    MaxTargets: 1024
    MaxSasExpanders: 42
    MaxEnclosures: 43
    HighPriorityCredit: 128
    MaxReplyDescriptorPostQueueDepth: 65504
    ReplyFrameSize: 32
    MaxVolumes: 0
    MaxDevHandle: 1106
    MaxPersistentEntries: 128
mpr0: Firmware: 07.00.01.00, Driver: 05.255.05.00-fbsd
mpr0: IOCCapabilities: 7a85c<ScsiTaskFull,DiagTrace,SnapBuf,EEDP,TransRetry,EventReplay,MSIXIndex,HostDisc>
dmar3: programming irte[101] rid 0x400 high 0x40400 low 0xa60001
pcib9: <ACPI PCI-PCI bridge> irq 16 at device 17.0 on pci0
pci5: <ACPI PCI bus> on pcib9
pci0: <simple comms> at device 22.0 (no driver attached)
pci0: <simple comms> at device 22.1 (no driver attached)
pci0: <serial bus, USB> at device 26.0 (no driver attached)
pcib10: <ACPI PCI-PCI bridge> irq 16 at device 28.0 on pci0
pci6: <ACPI PCI bus> on pcib10
pcib11: <ACPI PCI-PCI bridge> irq 19 at device 28.7 on pci0
pci7: <ACPI PCI bus> on pcib11
pcib12: <ACPI PCI-PCI bridge> irq 16 at device 0.0 on pci7
pci8: <ACPI PCI bus> on pcib12
vgapci0: <VGA-compatible display> port 0x2000-0x207f mem 0xab000000-0xab7fffff,0xab800000-0xab81ffff irq 16 at device 0.0 on pci8
vgapci0: Boot video device
pci0: <serial bus, USB> at device 29.0 (no driver attached)
pcib13: <ACPI PCI-PCI bridge> at device 30.0 on pci0
pci9: <ACPI PCI bus> on pcib13
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
pci0: <mass storage, SATA> at device 31.2 (no driver attached)
pcib14: <ACPI Host-PCI bridge> on acpi0
pci64: <ACPI PCI bus> on pcib14
pcib15: <ACPI PCI-PCI bridge> irq 56 at device 2.0 on pci64
pci65: <ACPI PCI bus> on pcib15
nvme0: <Generic NVMe Device> mem 0xc6010000-0xc6013fff irq 56 at device 0.0 on pci65
dmar0: programming irte[0] rid 0x402c high 0x4402c low 0xa70011
nvme0: dmar0 pci0:65:0:0 rid 4100 domain 0 mgaw 48 agaw 48 re-mapped
pcib16: <ACPI PCI-PCI bridge> irq 56 at device 2.2 on pci64
pci67: <ACPI PCI bus> on pcib16
nvme1: <Generic NVMe Device> mem 0xc5010000-0xc5013fff irq 58 at device 0.0 on pci67
dmar0: programming irte[1] rid 0x402c high 0x4402c low 0xa80011
nvme1: dmar0 pci0:67:0:0 rid 4300 domain 1 mgaw 48 agaw 48 re-mapped
pcib17: <ACPI PCI-PCI bridge> irq 64 at device 3.0 on pci64
pci69: <ACPI PCI bus> on pcib17
nvme2: <Generic NVMe Device> mem 0xc7010000-0xc7013fff irq 64 at device 0.0 on pci69
dmar0: programming irte[2] rid 0x402c high 0x4402c low 0xa90011
nvme2: dmar0 pci0:69:0:0 rid 4500 domain 2 mgaw 48 agaw 48 re-mapped
pcib18: <ACPI Host-PCI bridge> on acpi0
pci128: <ACPI PCI bus> on pcib18
pcib19: <ACPI PCI-PCI bridge> irq 80 at device 2.0 on pci128
pci129: <ACPI PCI bus> on pcib19
nvme3: <Generic NVMe Device> mem 0xe2010000-0xe2013fff irq 80 at device 0.0 on pci129
dmar1: programming irte[0] rid 0x802c high 0x4802c low 0xaa0011
nvme3: dmar1 pci0:129:0:0 rid 8100 domain 0 mgaw 48 agaw 48 re-mapped
pcib20: <ACPI PCI-PCI bridge> irq 80 at device 2.2 on pci128
pci131: <ACPI PCI bus> on pcib20
nvme4: <Generic NVMe Device> mem 0xe3010000-0xe3013fff irq 82 at device 0.0 on pci131
dmar1: programming irte[1] rid 0x802c high 0x4802c low 0xab0011
nvme4: dmar1 pci0:131:0:0 rid 8300 domain 1 mgaw 48 agaw 48 re-mapped
pcib21: <ACPI PCI-PCI bridge> irq 89 at device 3.0 on pci128
pci132: <ACPI PCI bus> on pcib21
nvme5: <Generic NVMe Device> mem 0xe1010000-0xe1013fff irq 88 at device 0.0 on pci132
dmar1: programming irte[2] rid 0x802c high 0x4802c low 0xac0011
nvme5: dmar1 pci0:132:0:0 rid 8400 domain 2 mgaw 48 agaw 48 re-mapped
pcib22: <ACPI Host-PCI bridge> on acpi0
pci192: <ACPI PCI bus> on pcib22
pcib23: <ACPI PCI-PCI bridge> irq 105 at device 2.0 on pci192
pci193: <ACPI PCI bus> on pcib23
nvme6: <Generic NVMe Device> mem 0xfb310000-0xfb313fff irq 104 at device 0.0 on pci193
dmar2: programming irte[0] rid 0xc02c high 0x4c02c low 0xad0011
nvme6: dmar2 pci0:193:0:0 rid c100 domain 0 mgaw 48 agaw 48 re-mapped
pcib24: <ACPI PCI-PCI bridge> irq 105 at device 2.2 on pci192
pci194: <ACPI PCI bus> on pcib24
nvme7: <Generic NVMe Device> mem 0xfb210000-0xfb213fff irq 106 at device 0.0 on pci194
dmar2: programming irte[1] rid 0xc02c high 0x4c02c low 0xae0011
nvme7: dmar2 pci0:194:0:0 rid c200 domain 1 mgaw 48 agaw 48 re-mapped
pcib25: <ACPI PCI-PCI bridge> irq 112 at device 3.0 on pci192
pci195: <ACPI PCI bus> on pcib25
mpr1: <LSI SAS3008> port 0xf000-0xf0ff mem 0xfb100000-0xfb10ffff irq 112 at device 0.0 on pci195
mpr1: dmar2 pci0:195:0:0 rid c300 domain 2 mgaw 48 agaw 48 re-mapped
mpr1: IOCFacts  :
    MsgVersion: 0x205
    HeaderVersion: 0x2300
    IOCNumber: 0
    IOCExceptions: 0x0
    MaxChainDepth: 128
    NumberOfPorts: 1
    RequestCredit: 10240
    ProductID: 0x2221
    IOCRequestFrameSize: 32
    MaxInitiators: 32
    MaxTargets: 1024
    MaxSasExpanders: 42
    MaxEnclosures: 43
    HighPriorityCredit: 128
    MaxReplyDescriptorPostQueueDepth: 65504
    ReplyFrameSize: 32
    MaxVolumes: 0
    MaxDevHandle: 1106
    MaxPersistentEntries: 128
mpr1: Firmware: 07.00.01.00, Driver: 05.255.05.00-fbsd
mpr1: IOCCapabilities: 7a85c<ScsiTaskFull,DiagTrace,SnapBuf,EEDP,TransRetry,EventReplay,MSIXIndex,HostDisc>
dmar2: programming irte[2] rid 0xc300 high 0x4c300 low 0xaf0001
pcib26: <ACPI PCI-PCI bridge> irq 112 at device 3.2 on pci192
pci196: <ACPI PCI bus> on pcib26
pcib27: <ACPI PCI-PCI bridge> irq 112 at device 3.3 on pci192
pci198: <ACPI PCI bus> on pcib27
acpi_button0: <Power Button> on acpi0
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart0: console (9600,n,8,1)
dmar3: programming irte[102] rid 0xf0ff high 0x4f0ff low 0xb00001
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
dmar3: programming irte[103] rid 0xf0ff high 0x4f0ff low 0xb10001
ipmi0: <IPMI System Interface> port 0xca2,0xca3 on acpi0
ipmi0: KCS mode found at io 0xca2 on acpi
orm0: <ISA Option ROM> at iomem 0xc0000-0xc7fff on isa0
sc0: <System console> at flags 0x100 on isa0
sc0: CGA <16 virtual consoles, flags=0x300>
vga0: <Generic ISA VGA> at port 0x3d0-0x3db iomem 0xb8000-0xbffff on isa0
acpi_throttle0: <ACPI CPU Throttling> on cpu0
acpi_throttle1: <ACPI CPU Throttling> on cpu1
acpi_throttle1: failed to attach P_CNT
device_attach: acpi_throttle1 attach returned 6
acpi_throttle2: <ACPI CPU Throttling> on cpu2
acpi_throttle2: failed to attach P_CNT
device_attach: acpi_throttle2 attach returned 6
acpi_throttle3: <ACPI CPU Throttling> on cpu3
acpi_throttle3: failed to attach P_CNT
device_attach: acpi_throttle3 attach returned 6
acpi_throttle4: <ACPI CPU Throttling> on cpu4
acpi_throttle4: failed to attach P_CNT
device_attach: acpi_throttle4 attach returned 6
acpi_throttle5: <ACPI CPU Throttling> on cpu5
acpi_throttle5: failed to attach P_CNT
device_attach: acpi_throttle5 attach returned 6
acpi_throttle6: <ACPI CPU Throttling> on cpu6
acpi_throttle6: failed to attach P_CNT
device_attach: acpi_throttle6 attach returned 6
acpi_throttle7: <ACPI CPU Throttling> on cpu7
acpi_throttle7: failed to attach P_CNT
device_attach: acpi_throttle7 attach returned 6
acpi_throttle8: <ACPI CPU Throttling> on cpu8
acpi_throttle8: failed to attach P_CNT
device_attach: acpi_throttle8 attach returned 6
acpi_throttle9: <ACPI CPU Throttling> on cpu9
acpi_throttle9: failed to attach P_CNT
device_attach: acpi_throttle9 attach returned 6
acpi_throttle10: <ACPI CPU Throttling> on cpu10
acpi_throttle10: failed to attach P_CNT
device_attach: acpi_throttle10 attach returned 6
acpi_throttle11: <ACPI CPU Throttling> on cpu11
acpi_throttle11: failed to attach P_CNT
device_attach: acpi_throttle11 attach returned 6
acpi_throttle12: <ACPI CPU Throttling> on cpu12
acpi_throttle12: failed to attach P_CNT
device_attach: acpi_throttle12 attach returned 6
acpi_throttle13: <ACPI CPU Throttling> on cpu13
acpi_throttle13: failed to attach P_CNT
device_attach: acpi_throttle13 attach returned 6
acpi_throttle14: <ACPI CPU Throttling> on cpu14
acpi_throttle14: failed to attach P_CNT
device_attach: acpi_throttle14 attach returned 6
acpi_throttle15: <ACPI CPU Throttling> on cpu15
acpi_throttle15: failed to attach P_CNT
device_attach: acpi_throttle15 attach returned 6
acpi_throttle16: <ACPI CPU Throttling> on cpu16
acpi_throttle16: failed to attach P_CNT
device_attach: acpi_throttle16 attach returned 6
acpi_throttle17: <ACPI CPU Throttling> on cpu17
acpi_throttle17: failed to attach P_CNT
device_attach: acpi_throttle17 attach returned 6
acpi_throttle18: <ACPI CPU Throttling> on cpu18
acpi_throttle18: failed to attach P_CNT
device_attach: acpi_throttle18 attach returned 6
acpi_throttle19: <ACPI CPU Throttling> on cpu19
acpi_throttle19: failed to attach P_CNT
device_attach: acpi_throttle19 attach returned 6
acpi_throttle20: <ACPI CPU Throttling> on cpu20
acpi_throttle20: failed to attach P_CNT
device_attach: acpi_throttle20 attach returned 6
acpi_throttle21: <ACPI CPU Throttling> on cpu21
acpi_throttle21: failed to attach P_CNT
device_attach: acpi_throttle21 attach returned 6
acpi_throttle22: <ACPI CPU Throttling> on cpu22
acpi_throttle22: failed to attach P_CNT
device_attach: acpi_throttle22 attach returned 6
acpi_throttle23: <ACPI CPU Throttling> on cpu23
acpi_throttle23: failed to attach P_CNT
device_attach: acpi_throttle23 attach returned 6
acpi_throttle24: <ACPI CPU Throttling> on cpu24
acpi_throttle24: failed to attach P_CNT
device_attach: acpi_throttle24 attach returned 6
acpi_throttle25: <ACPI CPU Throttling> on cpu25
acpi_throttle25: failed to attach P_CNT
device_attach: acpi_throttle25 attach returned 6
acpi_throttle26: <ACPI CPU Throttling> on cpu26
acpi_throttle26: failed to attach P_CNT
device_attach: acpi_throttle26 attach returned 6
acpi_throttle27: <ACPI CPU Throttling> on cpu27
acpi_throttle27: failed to attach P_CNT
device_attach: acpi_throttle27 attach returned 6
acpi_throttle28: <ACPI CPU Throttling> on cpu28
acpi_throttle28: failed to attach P_CNT
device_attach: acpi_throttle28 attach returned 6
acpi_throttle29: <ACPI CPU Throttling> on cpu29
acpi_throttle29: failed to attach P_CNT
device_attach: acpi_throttle29 attach returned 6
acpi_throttle30: <ACPI CPU Throttling> on cpu30
acpi_throttle30: failed to attach P_CNT
device_attach: acpi_throttle30 attach returned 6
acpi_throttle31: <ACPI CPU Throttling> on cpu31
acpi_throttle31: failed to attach P_CNT
device_attach: acpi_throttle31 attach returned 6
acpi_throttle32: <ACPI CPU Throttling> on cpu32
acpi_throttle32: failed to attach P_CNT
device_attach: acpi_throttle32 attach returned 6
acpi_throttle33: <ACPI CPU Throttling> on cpu33
acpi_throttle33: failed to attach P_CNT
device_attach: acpi_throttle33 attach returned 6
acpi_throttle34: <ACPI CPU Throttling> on cpu34
acpi_throttle34: failed to attach P_CNT
device_attach: acpi_throttle34 attach returned 6
acpi_throttle35: <ACPI CPU Throttling> on cpu35
acpi_throttle35: failed to attach P_CNT
device_attach: acpi_throttle35 attach returned 6
acpi_throttle36: <ACPI CPU Throttling> on cpu36
acpi_throttle36: failed to attach P_CNT
device_attach: acpi_throttle36 attach returned 6
acpi_throttle37: <ACPI CPU Throttling> on cpu37
acpi_throttle37: failed to attach P_CNT
device_attach: acpi_throttle37 attach returned 6
acpi_throttle38: <ACPI CPU Throttling> on cpu38
acpi_throttle38: failed to attach P_CNT
device_attach: acpi_throttle38 attach returned 6
acpi_throttle39: <ACPI CPU Throttling> on cpu39
acpi_throttle39: failed to attach P_CNT
device_attach: acpi_throttle39 attach returned 6
acpi_throttle40: <ACPI CPU Throttling> on cpu40
acpi_throttle40: failed to attach P_CNT
device_attach: acpi_throttle40 attach returned 6
acpi_throttle41: <ACPI CPU Throttling> on cpu41
acpi_throttle41: failed to attach P_CNT
device_attach: acpi_throttle41 attach returned 6
acpi_throttle42: <ACPI CPU Throttling> on cpu42
acpi_throttle42: failed to attach P_CNT
device_attach: acpi_throttle42 attach returned 6
acpi_throttle43: <ACPI CPU Throttling> on cpu43
acpi_throttle43: failed to attach P_CNT
device_attach: acpi_throttle43 attach returned 6
acpi_throttle44: <ACPI CPU Throttling> on cpu44
acpi_throttle44: failed to attach P_CNT
device_attach: acpi_throttle44 attach returned 6
acpi_throttle45: <ACPI CPU Throttling> on cpu45
acpi_throttle45: failed to attach P_CNT
device_attach: acpi_throttle45 attach returned 6
acpi_throttle46: <ACPI CPU Throttling> on cpu46
acpi_throttle46: failed to attach P_CNT
device_attach: acpi_throttle46 attach returned 6
acpi_throttle47: <ACPI CPU Throttling> on cpu47
acpi_throttle47: failed to attach P_CNT
device_attach: acpi_throttle47 attach returned 6
ZFS filesystem version: 5
ZFS storage pool version: features support (5000)
Timecounters tick every 1.000 msec
nvd0: <INTEL SSDPEDMD020T4> NVMe namespace
nvd0: 1907729MB (3907029168 512 byte sectors)
nvd1: <INTEL SSDPEDMD020T4> NVMe namespace
nvd1: 1907729MB (3907029168 512 byte sectors)
nvd2: <INTEL SSDPEDMD020T4> NVMe namespace
nvd2: 1907729MB (3907029168 512 byte sectors)
nvd3: <INTEL SSDPEDMD020T4> NVMe namespace
nvd3: 1907729MB (3907029168 512 byte sectors)
nvd4: <INTEL SSDPEDMD020T4> NVMe namespace
nvd4: 1907729MB (3907029168 512 byte sectors)
nvd5: <INTEL SSDPEDMD020T4> NVMe namespace
nvd5: 1907729MB (3907029168 512 byte sectors)
nvd6: <INTEL SSDPEDMD020T4> NVMe namespace
nvd6: 1907729MB (3907029168 512 byte sectors)
nvd7: <INTEL SSDPEDMD020T4> NVMe namespace
nvd7: 1907729MB (3907029168 512 byte sectors)
ipmi0: IPMI device rev. 1, firmware rev. 0.29, version 2.0
ipmi0: Number of channels 2
ipmi0: Attached watchdog
random: unblocking device.
da0 at mpr0 bus 0 scbus0 target 0 lun 0
da1 at mpr0 bus 0 scbus0 target 1 lun 0
da2 at mpr0 bus 0 scbus0 target 3 lun 0
da3 at mpr0 bus 0 scbus0 target 4 lun 0
da4 at mpr0 bus 0 scbus0 target 5 lun 0
da5 at mpr0 bus 0 scbus0 target 6 lun 0
da6 at mpr0 bus 0 scbus0 target 7 lun 0
da0: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da1: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da2: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da3: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da4: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da5: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da6: da0: Serial Number BTTV447600P8800JGN  
da1: Serial Number BTTV447600T6800JGN  
da2: Serial Number BTTV447601AK800JGN  
da3: Serial Number BTTV4476016K800JGN  
da4: Serial Number BTTV447600ZN800JGN  
da5: Serial Number BTTV447601CC800JGN  
<ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da0: 600.000MB/s transfers
da0: Command Queueing enabled
da1: 600.000MB/s transfers
da1: Command Queueing enabled
da2: 600.000MB/s transfersda3: 600.000MB/s transfersda4: 600.000MB/s transfers
da4: Command Queueing enabled
da5: 600.000MB/s transfers
da5: Command Queueing enabled
da6: Serial Number BTTV44800082800JGN  
da0: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da1: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)

da2: Command Queueing enabled

da3: Command Queueing enabled
da4: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da5: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da6: 600.000MB/s transfers
da6: Command Queueing enabled
da2: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da3: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da7 at mpr1 bus 0 scbus1 target 4 lun 0
da6: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da7: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da7: Serial Number BTTV44800089800JGN  
da7: 600.000MB/s transfers
da7: Command Queueing enabled
da7: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da9 at mpr1 bus 0 scbus1 target 6 lun 0
da8 at mpr1 bus 0 scbus1 target 5 lun 0
da9: da10 at mpr1 bus 0 scbus1 target 7 lun 0
da8: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
<ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da10: <ATA INTEL SSDSC2BA80 0270> Fixed Direct Access SPC-4 SCSI device
da8: Serial Number BTTV4480006G800JGN  
da9: Serial Number BTTV447601BK800JGN  
da10: Serial Number BTTV449503TE800JGN  
da8: 600.000MB/s transfers
da8: Command Queueing enabled
da9: 600.000MB/s transfers
da9: Command Queueing enabled
da10: 600.000MB/s transfers
da8: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da9: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da10: Command Queueing enabled
da10: 763097MB (1562824368 512 byte sectors: 255H 63S/T 97281C)
da11 at mpr1 bus 0 scbus1 target 8 lun 0
da11: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da11: Serial Number Z4D0MPHK0000W513FR5H
da11: 1200.000MB/s transfers
da11: Command Queueing enabled
da11: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da12 at mpr1 bus 0 scbus1 target 9 lun 0
da12: da13 at mpr1 bus 0 scbus1 target 10 lun 0
da14 at mpr1 bus 0 scbus1 target 11 lun 0
<SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da13: da14: da12: Serial Number Z4D0MMEK0000W513FLE9
<SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
<SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da12: 1200.000MB/s transfers
da13: Serial Number Z4D0RSW50000W5185ALZ
da14: Serial Number Z4D0RG8K0000W516TJCT
da12: Command Queueing enabled
da13: 1200.000MB/s transfers
da14: 1200.000MB/s transfers
da12: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da13: Command Queueing enabled
da14: Command Queueing enabled
da13: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da14: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da15 at mpr1 bus 0 scbus1 target 12 lun 0
da15: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da16 at mpr1 bus 0 scbus1 target 13 lun 0
da15: Serial Number Z4D0RT9L0000W5186NBK
da16: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da15: 1200.000MB/s transfers
da16: Serial Number Z4D0PNDA0000W515SC6W
da15: Command Queueing enabled
da16: 1200.000MB/s transfers
da15: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da16: Command Queueing enabled
da16: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da17 at mpr1 bus 0 scbus1 target 14 lun 0
da17: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da18 at mpr1 bus 0 scbus1 target 15 lun 0
da19 at mpr1 bus 0 scbus1 target 16 lun 0
da17: Serial Number Z4D0PND40000W5151N72
da18: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da19: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da17: 1200.000MB/s transfers
da18: Serial Number Z4D0RT6K0000W5186PDA
da19: Serial Number Z4D0RX520000W511BLC4
da17: Command Queueing enabled
da18: 1200.000MB/s transfersda19: 1200.000MB/s transfersda17: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)

da18: Command Queueing enabled

da19: Command Queueing enabled
da18: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da19: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da20 at mpr1 bus 0 scbus1 target 17 lun 0
da21 at mpr1 bus 0 scbus1 target 18 lun 0
da20: da22 at mpr1 bus 0 scbus1 target 19 lun 0
da21: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
<SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da22: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da21: Serial Number Z4D0MQCT0000W513FRLC
da20: Serial Number Z4D0LXFL0000W515SDLG
da22: Serial Number Z4D0N4Z20000W513FR35
da21: 1200.000MB/s transfers
da20: 1200.000MB/s transfersda22: 1200.000MB/s transfersda21: Command Queueing enabled

da20: Command Queueing enabled

da22: Command Queueing enabled
da21: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da20: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da22: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da23 at mpr1 bus 0 scbus1 target 20 lun 0
da24 at mpr1 bus 0 scbus1 target 21 lun 0
da23: da25 at mpr1 bus 0 scbus1 target 22 lun 0
da26 at mpr1 bus 0 scbus1 target 23 lun 0
da24: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
<SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da25: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da26: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da24: Serial Number Z4D0Q0N00000W5073ATY
da23: Serial Number Z4D0RE550000W5186S78
da25: Serial Number Z4D0STC50000W5186PNR
da26: Serial Number Z4D0LV1G0000W516TG1S
da24: 1200.000MB/s transfersda23: 1200.000MB/s transfersda25: 1200.000MB/s transfers
da26: 1200.000MB/s transfers

da24: Command Queueing enabled

da23: Command Queueing enabled
da25: Command Queueing enabled
da26: Command Queueing enabled
da24: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da23: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da25: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da26: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da30 at mpr1 bus 0 scbus1 target 27 lun 0
da27 at mpr1 bus 0 scbus1 target 24 lun 0
da28 at mpr1 bus 0 scbus1 target 25 lun 0
da29 at mpr1 bus 0 scbus1 target 26 lun 0
da31 at mpr1 bus 0 scbus1 target 28 lun 0
da32 at mpr1 bus 0 scbus1 target 29 lun 0
da30: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da33 at mpr1 bus 0 scbus1 target 30 lun 0
da34 at mpr1 bus 0 scbus1 target 31 lun 0
da27: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da28: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da29: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da31: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da32: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da30: Serial Number Z4D0R2NA0000W5185B87
da33: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da34: <SEAGATE ST6000NM0014 K001> Fixed Direct Access SPC-4 SCSI device
da27: Serial Number Z4D0RXD40000W516TQQ7
da28: Serial Number Z4D0SWBR0000W5186MWN
da29: Serial Number Z4D0RT3R0000W5186Q7J
da31: Serial Number Z4D0R2RB0000W5186MBZ
da32: Serial Number Z4D0R2F30000W5186PST
da30: 1200.000MB/s transfers
da33: Serial Number Z4D0Q1YK0000W515SDV3
da34: Serial Number Z4D0R2S50000W5186Q26
da27: 1200.000MB/s transfers
da28: 1200.000MB/s transfers
da29: 1200.000MB/s transfers
da31: 1200.000MB/s transfers
da32: 1200.000MB/s transfers
da30: Command Queueing enabled
da33: 1200.000MB/s transfers
da34: 1200.000MB/s transfersda27: Command Queueing enabled
da28: Command Queueing enabled
da29: Command Queueing enabled
da31: Command Queueing enabled
da32: Command Queueing enabled
da30: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da33: Command Queueing enabled

da34: Command Queueing enabled
da27: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da28: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da29: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da31: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da32: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da33: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
da34: 5723166MB (1465130646 4096 byte sectors: 255H 63S/T 91200C)
ses0 at mpr1 bus 0 scbus1 target 32 lun 0
ses0: <LSI SAS3x40 0601> Fixed Enclosure Services SPC-3 SCSI device
ses0: Serial Number         
ses0: 1200.000MB/s transfers
ses0: Command Queueing enabled
ses0: SCSI-3 ENC Device
SMP: AP CPU #33 Launched!
SMP: AP CPU #7 Launched!
SMP: AP CPU #2 Launched!
SMP: AP CPU #1 Launched!
SMP: AP CPU #28 Launched!
SMP: AP CPU #9 Launched!
SMP: AP CPU #11 Launched!
SMP: AP CPU #42 Launched!
SMP: AP CPU #10 Launched!
SMP: AP CPU #8 Launched!
SMP: AP CPU #6 Launched!
SMP: AP CPU #4 Launched!
SMP: AP CPU #5 Launched!
SMP: AP CPU #47 Launched!
SMP: AP CPU #3 Launched!
SMP: AP CPU #34 Launched!
SMP: AP CPU #22 Launched!
SMP: AP CPU #45 Launched!
SMP: AP CPU #12 Launched!
SMP: AP CPU #37 Launched!
SMP: AP CPU #24 Launched!
SMP: AP CPU #27 Launched!
SMP: AP CPU #39 Launched!
SMP: AP CPU #38 Launched!
SMP: AP CPU #40 Launched!
SMP: AP CPU #25 Launched!
SMP: AP CPU #44 Launched!
SMP: AP CPU #43 Launched!
SMP: AP CPU #41 Launched!
SMP: AP CPU #36 Launched!
SMP: AP CPU #20 Launched!
SMP: AP CPU #46 Launched!
SMP: AP CPU #16 Launched!
SMP: AP CPU #26 Launched!
SMP: AP CPU #29 Launched!
SMP: AP CPU #32 Launched!
SMP: AP CPU #18 Launched!
SMP: AP CPU #35 Launched!
SMP: AP CPU #31 Launched!
SMP: AP CPU #30 Launched!
SMP: AP CPU #15 Launched!
SMP: AP CPU #19 Launched!
SMP: AP CPU #23 Launched!
SMP: AP CPU #17 Launched!
SMP: AP CPU #13 Launched!
SMP: AP CPU #14 Launched!
SMP: AP CPU #21 Launched!
dmar3: programming irte[104] rid 0xf0ff high 0x4f0ff low 0x20000300001
dmar3: programming irte[105] rid 0xf0ff high 0x4f0ff low 0x40000300001
dmar3: programming irte[106] rid 0xf0ff high 0x4f0ff low 0x60000300011
dmar0: programming irte[3] rid 0x402c high 0x4402c low 0x80000300011
dmar0: programming irte[4] rid 0x402c high 0x4402c low 0xa0000300011
dmar0: programming irte[5] rid 0x402c high 0x4402c low 0x100000300011
dmar1: programming irte[3] rid 0x802c high 0x4802c low 0x120000300011
dmar1: programming irte[4] rid 0x802c high 0x4802c low 0x140000300011
dmar1: programming irte[5] rid 0x802c high 0x4802c low 0x160000300011
dmar2: programming irte[3] rid 0xc02c high 0x4c02c low 0x180000300011
dmar2: programming irte[4] rid 0xc02c high 0x4c02c low 0x1a0000300011
dmar3: GEOM: da4: the primary GPT table is corrupt or invalid.
programming irte[4] rid 0x100 high 0x40100 low 0x20000310001
GEOM: da4: using the secondary instead -- recovery strongly advised.
dmar3: programming irte[5] rid 0x100 high 0x40100 low 0x40000310001
dmar3: programming irte[6] rid 0x100 high 0x40100 low 0x60000310001
dmar3: programming irte[7] rid 0x100 high 0x40100 low 0x80000310001
dmar3: programming irte[8] rid 0x100 high 0x40100 low 0xa0000310001
dmar3: programming irte[9] rid 0x100 high 0x40100 low 0x100000310001
dmar3: programming irte[10] rid 0x100 high 0x40100 low 0x120000310001
dmar3: programming irte[11] rid 0x100 high 0x40100 low 0x140000310001
dmar3: programming irte[12] rid 0x100 high 0x40100 low 0x160000310001
dmar3: programming irte[13] rid 0x100 high 0x40100 low 0x180000310001
dmar3: programming irte[14] rid 0x100 high 0x40100 low 0x1a0000310001
dmar3: programming irte[15] rid 0x100 high 0x40100 low 0x200000310001
dmar3: programming irte[16] rid 0x100 high 0x40100 low 0x220000310001
dmar3: programming irte[17] rid 0x100 high 0x40100 low 0x240000310001
dmar3: programming irte[18] rid 0x100 high 0x40100 low 0x260000310001
dmar3: programming irte[19] rid 0x100 high 0x40100 low 0x280000310001
dmar3: programming irte[20] rid 0x100 high 0x40100 low 0x2a0000310001
dmar3: programming irte[21] rid 0x100 high 0x40100 low 0x300000310001
dmar3: programming irte[22] rid 0x100 high 0x40100 low 0x320000310001
dmar3: programming irte[23] rid 0x100 high 0x40100 low 0x340000300001
dmar3: programming irte[24] rid 0x100 high 0x40100 low 0x360000300001
dmar3: programming irte[25] rid 0x100 high 0x40100 low 0x380000300001
dmar3: programming irte[26] rid 0x100 high 0x40100 low 0x3a0000300001
dmar3: programming irte[27] rid 0x100 high 0x40100 low 0x400000300001
dmar3: programming irte[28] rid 0x100 high 0x40100 low 0x420000300001
dmar3: programming irte[29] rid 0x100 high 0x40100 low 0x440000300001
dmar3: programming irte[30] rid 0x100 high 0x40100 low 0x460000300001
dmar3: programming irte[31] rid 0x100 high 0x40100 low 0x480000300001
dmar3: programming irte[32] rid 0x100 high 0x40100 low 0x4a0000300001
dmar3: programming irte[33] rid 0x100 high 0x40100 low 0x500000300001
dmar3: programming irte[34] rid 0x100 high 0x40100 low 0x520000300001
dmar3: programming irte[35] rid 0x100 high 0x40100 low 0x540000300001
dmar3: programming irte[36] rid 0x100 high 0x40100 low 0x560000300001
dmar3: programming irte[37] rid 0x100 high 0x40100 low 0x580000300001
dmar3: programming irte[38] rid 0x100 high 0x40100 low 0x5a0000300001
dmar3: programming irte[39] rid 0x100 high 0x40100 low 0x600000300001
dmar3: programming irte[40] rid 0x100 high 0x40100 low 0x620000300001
dmar3: programming irte[41] rid 0x100 high 0x40100 low 0x640000300001
dmar3: programming irte[42] rid 0x100 high 0x40100 low 0x660000300001
dmar3: programming irte[43] rid 0x100 high 0x40100 low 0x680000300001
dmar3: programming irte[44] rid 0x100 high 0x40100 low 0x6a0000300001
dmar3: programming irte[45] rid 0x100 high 0x40100 low 0x700000300001
dmar3: programming irte[46] rid 0x100 high 0x40100 low 0x720000300001
dmar3: programming irte[47] rid 0x100 high 0x40100 low 0x740000300001
dmar3: programming irte[48] rid 0x100 high 0x40100 low 0x760000300001
dmar3: programming irte[49] rid 0x100 high 0x40100 low 0x780000300001
dmar3: programming irte[50] rid 0x100 high 0x40100 low 0x7a0000300001
dmar3: programming irte[51] rid 0x100 high 0x40100 low 0x340000310001
dmar3: programming irte[53] rid 0x101 high 0x40101 low 0x20000320001
dmar3: programming irte[54] rid 0x101 high 0x40101 low 0x40000320001
dmar3: programming irte[55] rid 0x101 high 0x40101 low 0x60000320001
dmar3: programming irte[56] rid 0x101 high 0x40101 low 0x80000320001
dmar3: programming irte[57] rid 0x101 high 0x40101 low 0xa0000320001
dmar3: programming irte[58] rid 0x101 high 0x40101 low 0x100000320001
dmar3: programming irte[59] rid 0x101 high 0x40101 low 0x120000320001
dmar3: programming irte[60] rid 0x101 high 0x40101 low 0x140000320001
dmar3: programming irte[61] rid 0x101 high 0x40101 low 0x160000320001
dmar3: programming irte[62] rid 0x101 high 0x40101 low 0x180000320001
dmar3: programming irte[63] rid 0x101 high 0x40101 low 0x1a0000320001
dmar3: programming irte[64] rid 0x101 high 0x40101 low 0x200000320001
dmar3: programming irte[65] rid 0x101 high 0x40101 low 0x220000320001
dmar3: programming irte[66] rid 0x101 high 0x40101 low 0x240000320001
dmar3: programming irte[67] rid 0x101 high 0x40101 low 0x260000320001
dmar3: programming irte[68] rid 0x101 high 0x40101 low 0x280000320001
dmar3: programming irte[69] rid 0x101 high 0x40101 low 0x2a0000320001
dmar3: programming irte[70] rid 0x101 high 0x40101 low 0x300000320001
dmar3: programming irte[71] rid 0x101 high 0x40101 low 0x320000320001
dmar3: programming irte[72] rid 0x101 high 0x40101 low 0x340000320001
dmar3: programming irte[73] rid 0x101 high 0x40101 low 0x360000310001
dmar3: programming irte[74] rid 0x101 high 0x40101 low 0x380000310001
dmar3: programming irte[75] rid 0x101 high 0x40101 low 0x3a0000310001
dmar3: programming irte[76] rid 0x101 high 0x40101 low 0x400000310001
dmar3: programming irte[77] rid 0x101 high 0x40101 low 0x420000310001
dmar3: programming irte[78] rid 0x101 high 0x40101 low 0x440000310001
dmar3: programming irte[79] rid 0x101 high 0x40101 low 0x460000310001
dmar3: programming irte[80] rid 0x101 high 0x40101 low 0x480000310001
dmar3: programming irte[81] rid 0x101 high 0x40101 low 0x4a0000310001
dmar3: programming irte[82] rid 0x101 high 0x40101 low 0x500000310001
dmar3: programming irte[83] rid 0x101 high 0x40101 low 0x520000310001
dmar3: programming irte[84] rid 0x101 high 0x40101 low 0x540000310001
dmar3: programming irte[85] rid 0x101 high 0x40101 low 0x560000310001
dmar3: programming irte[86] rid 0x101 high 0x40101 low 0x580000310001
dmar3: programming irte[87] rid 0x101 high 0x40101 low 0x5a0000310001
dmar3: programming irte[88] rid 0x101 high 0x40101 low 0x600000310001
dmar3: programming irte[89] rid 0x101 high 0x40101 low 0x620000310001
dmar3: programming irte[90] rid 0x101 high 0x40101 low 0x640000310001
dmar3: programming irte[91] rid 0x101 high 0x40101 low 0x660000310001
dmar3: programming irte[92] rid 0x101 high 0x40101 low 0x680000310001
dmar3: programming irte[93] rid 0x101 high 0x40101 low 0x6a0000310001
dmar3: programming irte[94] rid 0x101 high 0x40101 low 0x700000310001
dmar3: programming irte[95] rid 0x101 high 0x40101 low 0x720000310001
dmar3: programming irte[96] rid 0x101 high 0x40101 low 0x740000310001
dmar3: programming irte[97] rid 0x101 high 0x40101 low 0x760000310001
dmar3: programming irte[98] rid 0x101 high 0x40101 low 0x780000310001
dmar3: programming irte[99] rid 0x101 high 0x40101 low 0x7a0000310001
dmar3: programming irte[100] rid 0x101 high 0x40101 low 0x360000320001
dmar3: programming irte[101] rid 0x400 high 0x40400 low 0x380000320001
dmar2: programming irte[2] rid 0xc300 high 0x4c300 low 0x3a0000320001
Timecounter "TSC-low" frequency 1496425194 Hz quality 1000
Trying to mount root from zfs:zroot/ROOT/default []...
ix0: link state changed to UP
\000
root@s4l-zfs:~ # 
```
