# ZFS

```
oberstet@matterhorn:~$ sudo zfs destroy tank/docker-root
oberstet@matterhorn:~$ sudo zfs create -o mountpoint=/var/lib/docker tank/docker-root
oberstet@matterhorn:~$ sudo zfs create -o mountpoint=/var/lib/docker/volumes tank/docker-volumes
oberstet@matterhorn:~$ sudo chmod 700 /var/lib/docker/volumes
```

```
oberstet@matterhorn:~$ cat /etc/docker/daemon.json 
{"storage-driver": "zfs"}
```

* https://wiki.kobol.io/helios64/software/zfs/docker-zfs/
* https://docs.docker.com/storage/storagedriver/zfs-driver/

# Prune everything

```
docker system prune --volumes --force
```

See [here](https://docs.docker.com/config/pruning/).

# Remove all images

```
docker rmi --force $(docker images -a -q)
```

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
