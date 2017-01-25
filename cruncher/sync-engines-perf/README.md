Test maschine hardware:

* 4 socket NUMA
* Intel(R) Xeon(R) CPU E7-8880 v4 @ 2.20GHz
* 88 cores / 176 threads
* 3TB RAM
* 8 x Intel P3608 4TB NVMe

Software:

* Debian 8 with Kernel 4.8 from backports

```console
oberstet@svr-psql19:~$ uname -r
4.8.0-0.bpo.2-amd64
```

* FIO (upstream master)

```
oberstet@svr-psql19:~$ /opt/fio/bin/fio --version
fio-2.17-17-g9cf1
```
