
## Get version

```console
extern107:~/oberstet # isdct version
- Version Information -
Name: Intel(R) Data Center Tool
Version: 2.2.1
Description: Interact and configure Intel SSDs.


extern107:~/oberstet # which isdct
/usr/bin/isdct
extern107:~/oberstet # ls -la ~/isdct-2.2.1.400-10.x86_64.rpm 
-rw-r--r-- 1 root root 5161465 Mär 31 13:04 /root/isdct-2.2.1.400-10.x86_64.rpm
extern107:~/oberstet # isdct version
- Version Information -
Name: Intel(R) Data Center Tool
Version: 2.2.1
Description: Interact and configure Intel SSDs.
```

## List all Intel SSDs

```console
extern107:~/oberstet # isdct show -intelssd
- IntelSSD Index 0 -
DevicePath: /dev/sg1
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 0
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV447601C6800JGN

- IntelSSD Index 1 -
DevicePath: /dev/sg2
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 1
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV447601AK800JGN

- IntelSSD Index 2 -
DevicePath: /dev/sg3
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 2
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV44800082800JGN

- IntelSSD Index 3 -
DevicePath: /dev/sg33
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 3
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV447601BK800JGN

- IntelSSD Index 4 -
DevicePath: /dev/sg34
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 4
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV449503TE800JGN

- IntelSSD Index 5 -
DevicePath: /dev/sg35
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 5
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV4480006G800JGN

- IntelSSD Index 6 -
DevicePath: /dev/sg4
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 6
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV447601CC800JGN

- IntelSSD Index 7 -
DevicePath: /dev/sg5
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 7
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV4476016K800JGN

- IntelSSD Index 8 -
DevicePath: /dev/sg6
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 8
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV447600ZN800JGN

- IntelSSD Index 9 -
DevicePath: /dev/sg7
DeviceStatus: Healthy
Firmware: 5DV10270
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 9
ProductFamily: Intel SSD DC S3700 Series
ModelNumber: INTEL SSDSC2BA800G3
SerialNumber: BTTV44800089800JGN

- IntelSSD Index 10 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme0n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 10
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT4476002A2P0EGN

- IntelSSD Index 11 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme1n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 11
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT448000302P0EGN

- IntelSSD Index 12 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme2n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 12
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT447600072P0EGN

- IntelSSD Index 13 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme3n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 13
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT448000442P0EGN

- IntelSSD Index 14 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme4n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 14
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT4476002C2P0EGN

- IntelSSD Index 15 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme5n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 15
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT448000162P0EGN

- IntelSSD Index 16 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme6n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 16
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT4480007S2P0EGN

- IntelSSD Index 17 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme7n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 17
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT4480001U2P0EGN
```


## Show device info

Short device info:

```console
extern107:~/oberstet # isdct show -intelssd 10
- IntelSSD Index 10 -
Bootloader: 8B1B012E
DevicePath: /dev/nvme0n1
DeviceStatus: Healthy
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
Index: 10
ProductFamily: Intel SSD DC P3700 Series
ModelNumber: INTEL SSDPEDMD020T4
SerialNumber: CVFT4476002A2P0EGN
```

Long device info:

```console
extern107:~/oberstet # isdct show -all -intelssd 10
- IntelSSD Index 10 -
AggregationThreshold: 0
Aggregation Time: 0
ArbitrationBurst: 0
AsynchronousEventConfiguration: 0
Bootloader: 8B1B012E
DevicePath: /dev/nvme0n1
DeviceStatus: Healthy
EnduranceAnalyzer: Media Workload Indicators have reset values. Run 60+ minute workload prior to running the endurance analyzer.
ErrorString: 
Firmware: 8DV10131
FirmwareUpdateAvailable: Firmware is up to date as of this tool release.
HighPriorityWeightArbitration: 0
Index: 10
IOCompletionQueuesRequested: 30
IOSubmissionQueuesRequested: 30
LBAFormat: 0
LowPriorityWeightArbitration: 0
ProductFamily: Intel SSD DC P3700 Series
MaximumLBA: 3907029167
MediumPriorityWeightArbitration: 0
MetadataSetting: 0
ModelNumber: INTEL SSDPEDMD020T4
NativeMaxLBA: 3907029167
NumErrorLogPageEntries: 63
NumLBAFormats: 6
NVMePowerState: 0
PCILinkGenSpeed: 3
PCILinkWidth: 4
PhysicalSize: 2000398934016
PowerGovernorMode: 0 (25W)
ProtectionInformation: 0
ProtectionInformationLocation: 0
RAIDMember: False
SectorSize: 512
SerialNumber: CVFT4476002A2P0EGN
SystemTrimEnabled: 
TempThreshold: 85 degree C
TimeLimitedErrorRecovery: 0
TrimSupported: True
WriteAtomicityDisableNormal: 0
```


## Get Temperature

To get the current device temperature, [this post](https://communities.intel.com/thread/55412) explains how to do:

```console
extern107:~/oberstet # isdct dump -intelssd 10 datatype=nvmelog logid=197
- Temperature Statistics (Log ID = 197) -
Current Temperature: 38
Highest Temperature: 46
Lowest Temperature: 23
Maximum operating temperature: 85
Minimum operating temperature: 0
Estimated offset in Celsius: -5
```
