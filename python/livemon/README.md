# Usage

Start Crossbar.io:

    crossbar start

Start Monitor backend:

    sudo `which python` monitor.py

# CPU Stats

CPU statistics are published to the topic `de.parcit.adr.livemon.on_cpu_stats`. The event payload consists of a single (positional) value being a dictionary:

```
{
    "timestamp": "2015-07-15T12:37:42.258Z",
    "sockets": [
        {
            "id": 0,
            "physical_id": 0,
            "temperature": null,
            "cores": [
                {
                    "id": 0,
                    "physical_id": 0,
                    "frequency": 3399.96,
                    "temperature": 49,

                    "user": 0,
                    "nice": 0,
                    "system": 0,
                    "total": 0,

                    "idle": 0.98,
                    "iowait": 0,
                    "softirq": 0
                    "irq": 0,
                    "steal": 0,
                }
            ]
        }
    ]
}
```

For convenience, the event contains `total` CPU which is the sum of `user`, `nice` and `system`.

