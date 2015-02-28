# Building

From ports:

```
cd /usr/ports/emulators/virtualbox-ose
make config
```

Unselect all but VNC support. Then:

```
make install
```

Then check the installed files

```
pkg info -l virtualbox-ose | less
```

And load required kernel modules at boot time

```
echo 'vboxdrv_load="YES"' >> /boot/loader.conf
```

Add user to VBox group:

```
 pw groupmod vboxusers -m jerry
```

and reboot.

Management:

```
/usr/local/etc/rc.d/vboxheadless
/usr/local/etc/rc.d/vboxwatchdog
```

and

```
/usr/local/bin/VBoxHeadless
/usr/local/bin/VBoxManage
```
