# etcd

## Resources

* https://www.heise.de/developer/artikel/Verteilte-Systeme-mit-Etcd-in-der-Praxis-2845358.html
* https://coreos.com/etcd/docs/latest/rfc/v3api.html
* https://github.com/coreos/etcd/tree/master/contrib/recipes
* https://github.com/coreos/etcd/blob/master/Documentation/dev-guide/api_grpc_gateway.md


## Installation

> You will need at least etcd v3.1.0 (because we want v3, and because only 3.1+ has a working HTTP bridge).

```console
ETCD_VER=v3.1.0
DOWNLOAD_URL=https://github.com/coreos/etcd/releases/download
curl -L ${DOWNLOAD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
mkdir -p /opt/etcd && tar xzvf /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz -C /opt/etcd --strip-components=1
/opt/etcd/etcd --version
```

## Test using etcdctl and the v3 API

In a first terminal, scratch and run etcd:

```console
rm -rf /default.etcd/
/opt/etcd/etcd
```

You can check the status of the cluster like this:

```console
ETCDCTL_API=3 /opt/etcd/etcdctl endpoint --write-out="json" status
```

In a second terminal, write a key

```console
ETCDCTL_API=3 /opt/etcd/etcdctl put foo hello
```

or read a key

```console
ETCDCTL_API=3 /opt/etcd/etcdctl get --write-out="json" foo
```

In a third terminal, watch a key

```console
ETCDCTL_API=3 /opt/etcd/etcdctl watch --write-out="json" foo
```

and modify the key from the second terminal like above.


## Test using curl

Write "hello" to key "foo" (both Base64 encoded):

```console
curl -L http://localhost:2379/v3alpha/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'
```

Do a key range request:

```console
curl -L http://localhost:2379/v3alpha/kv/range -X POST -d '{"key": "Zm9v"}'
```

Watch a key:

```console
curl -L http://localhost:2379/v3alpha/watch -X POST -d '{"create_request": {"key": "Zm9v"}}'
```

Watch a key beginning from a revision:

```console
curl -L http://localhost:2379/v3alpha/watch -X POST -d '{"create_request": {"key": "Zm9v", "start_revision": 1}}'
```

Get cluster status:

```console
curl -L http://localhost:2379/v3alpha/maintenance/status -X POST -d '{}'
```
