# JSON and MsgPack Serializer Performance

## Test System

* Intel(R) Xeon(R) CPU E3-1240 v3 @ 3.40GHz
* Ubuntu 14.04.3 LTS and FreeBSD 10.1
* PyPy 4.0.0 and PyPy 2.6.1

## Requirements

```
pip install autobahn[all]
```

## Testing

```
pypy speed.py
```

## Results

### Linux / PyPy 4.0.0

```
Linux-3.19.0-25-generic-x86_64-with-debian-jessie-sid
2.7.10 (850edf14b2c7, Oct 26 2015, 06:41:12)
[PyPy 4.0.0 with GCC 4.8.4]

{'ser': {'JsonObjectSerializer': 460373, 'MsgPackObjectSerializer': 1445008},
 'unser': {'JsonObjectSerializer': 351437, 'MsgPackObjectSerializer': 579613}}
```

### Linux / PyPy 2.6.1

```
Linux-3.19.0-25-generic-x86_64-with-debian-jessie-sid
2.7.10 (f3ad1e1e1d62, Aug 28 2015, 10:45:29)
[PyPy 2.6.1 with GCC 4.8.4]

{'ser': {'JsonObjectSerializer': 438520, 'MsgPackObjectSerializer': 1509394},
 'unser': {'JsonObjectSerializer': 351903, 'MsgPackObjectSerializer': 956219}}
```

### FreeBSD / PyPy 2.6.1

```
2.7.10 (f3ad1e1e1d6215e20d34bb65ab85ff9188c9f559, Sep 01 2015, 01:15:42)
[PyPy 2.6.1 with GCC 4.2.1 Compatible FreeBSD Clang 3.4.1 (tags/RELEASE_34/dot1-final 208032)]
{'ser': {'JsonObjectSerializer': 273311, 'MsgPackObjectSerializer': 886687},
 'unser': {'JsonObjectSerializer': 206810, 'MsgPackObjectSerializer': 610964}}
```
