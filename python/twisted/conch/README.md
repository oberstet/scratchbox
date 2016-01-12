https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Authentication_Keys


sudo chmod -x /usr/bin/gnome-keyring*


/opt/openssh/bin/ssh-keygen -lvf ~/.ssh/id_ed25519


Ubuntu default SSH agent ("GNOME Keyring" -> `gnome-keyring-daemon`) does [not support Ed25519](https://wiki.archlinux.org/index.php/GNOME_Keyring).

So we need to disable it first:

```console
sudo ln -sf /dev/null /etc/xdg/autostart/gnome-keyring-ssh.desktop
```

```console
oberstet@thinkpad-t430s:~$ cat /etc/xdg/autostart/gnome-keyring-ssh.desktop
[Desktop Entry]
Type=Application
Name=SSH Key Agent
Comment=GNOME Keyring: SSH Agent
Exec=/usr/bin/gnome-keyring-daemon --start --components=ssh
OnlyShowIn=GNOME;Unity;MATE;
X-GNOME-Autostart-Phase=Initialization
X-GNOME-AutoRestart=false
X-GNOME-Autostart-Notify=true
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-Bugzilla-Product=gnome-keyring
X-GNOME-Bugzilla-Component=general
X-GNOME-Bugzilla-Version=3.10.1
X-Ubuntu-Gettext-Domain=gnome-keyring
```

and [use OpenSSH agent](https://wiki.archlinux.org/index.php/SSH_keys#SSH_agents):


~/.bashrc

eval $(keychain --eval --quiet id_ed25519 id_rsa ~/.keys/my_custom_key)



~/.bash_profile

eval `keychain --eval --agents ssh id_rsa`





36.) Stop the stupid GNOME SSH agent thing from working.

NOTE: This is a stupid hack to get around the fact that, apparently,
the gnome keyring is started unconditionally with all components if
any gnome services are run (and we would like to run them, just not
this specific one).

To fix, do:

cd /usr/bin
sudo mv gnome-keyring-daemon gnome-keyring-daemon-wrapped

Then create a new gnome-keyring-daemon and set its contents to:

#!/bin/sh
exec /usr/bin/gnome-keyring-daemon-wrapped --components=pkcs11,secrets,gpg "$@"

and make it executable:

sudo chmod a+rx /usr/bin/gnome-keyring-daemon

Also, you need to go into ~/.config/autostart/gnome-keyring-ssh.desktop and add:

[Desktop Entry]
X-GNOME-Autostart-enabled=false

so that it doesn't get started by the ancillary (and likely redundant)
separate invoker.
