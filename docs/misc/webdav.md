# WebDAV

Install WebDAV user-mode filesystem

```console
sudo apt-get install davfs2
```

Edit WebDAV configuration (see [Option 2: Mount your Drive on the command line](https://support-en.mailbox.org/knowledge-base/article/webdav-linux)):

```console
sudo vim /etc/davfs2/davfs2.conf
```

and add the following

```
if_match_bug 1
use_locks 0
cache_size 1
table_size 4096
delay_upload 1
gui_optimize 1
```

Then allow yourself mounting without `sudo`:

```console
sudo usermod -a -G davfs2 oberstet
```

and apply all changes

```console
sudo dpkg-reconfigure davfs2
```

Create a mount point (here, we create the mountpouint within our own HOME):

```console
mkdir ${HOME/files}
```

To mount manually

```console
mount.davfs https://dav.mailbox.org/servlet/webdav.infostore ${HOME}/files
``` 

To make mounting more comfortable, edit

```console
sudo vim /etc/fstab
```

and add the follwoing line

```console
https://dav.mailbox.org/servlet/webdav.infostore /home/oberstet/files/ davfs noauto,user 0 0
```

Here are some shortcuts:

```console
vim ~/.bashrc

alias files_mount='mount ${HOME}/files'
alias files_umount='umount -f ${HOME}/files'
alias files_down='rsync -rutv ${HOME}/files/ ${HOME}/Dokumente/'
alias files_up='rsync -rutv ${HOME}/Dokumente/ ${HOME}/files/'
```



References:

* https://support-en.mailbox.org/knowledge-base/article/webdav-linux
* http://ajclarkson.co.uk/blog/auto-mount-webdav-raspberry-pi/
* https://blog.storagemadeeasy.com/syncing-folders-to-any-remote-cloud-storage-from-a-headless-linux-server/
