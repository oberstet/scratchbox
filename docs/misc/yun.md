# Arduino Yun - Random Notes

## YunBridge

The `/dev/ttyATH0` device is attached at boot to a console (via `/etc/inittab` line `ttyATH0::askfirst:/bin/ash --login`).

When the MCU calls `Bridge.begin()`, this will send a command to the console on the Linux side which starts a Python script (the "YunBridge") which talks then over `stdio` over serial. 

 * https://github.com/arduino/linino/blob/master/trunk/target/linux/ar71xx/base-files/etc/uci-defaults/00_inittab-console-fixup
 * https://github.com/arduino/linino/tree/master/trunk/package/linino/yun-scripts/files/usr/bin
 * https://github.com/arduino/linino/blob/master/trunk/package/linino/yun-scripts/files/usr/bin/run-bridge
 * https://github.com/arduino/YunBridge

## Building Packages

 * http://wiki.openwrt.org/doc/devel/crosscompile
 * http://wiki.openwrt.org/doc/devel/packages
 * http://eggie5.com/40-cross-compile-mips-openwrt

## My Yun

 * Wifi AP-Mode Default IP: 192.168.240.1
 * yun1_wlan0	192.168.1.150	90:A2:DA:F0:0C:4E
 * yun1_eth1	192.168.1.151	90:A2:DA:F8:0C:4E

## ASUS RT-AC66U

	SoC 	Broadcom BCM4706
	RAM 	256 MB
	Flash 	128 MB

The SoC has a 600 MHz MIPS32 74K core. 

### Resources

 * http://www.broadcom.com/products/Wireless-LAN/802.11-Wireless-LAN-Solutions/BCM4706
 * http://www.smallnetbuilder.com/wireless/wireless-reviews/31841-asus-rt-ac66u-80211ac-dual-band-wireless-ac1750-gigabit-router-reviewed
