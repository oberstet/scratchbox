

```console
/usr/local/etc/rc.d/isc-dhcpd status
```

```console
/usr/local/etc/rc.d/isc-dhcpd configtest
```

```console
root@wachtmeister:/home/oberstet # cat /usr/local/etc/dhcpd.conf
option domain-name "office.tavendo.de";
option domain-name-servers 192.168.1.1, 8.8.8.8;

# Wolke Cluster
#
subnet 10.0.1.0 netmask 255.255.255.0 {
   range 10.0.1.10 10.0.1.199;
   option subnet-mask 255.255.255.0;
   option broadcast-address 10.0.1.255;
   option routers 10.0.1.1;
}

# Wolke Cluster Block A
#
host w1a1 {
  hardware ethernet 70:71:bc:b1:8e:53;
  fixed-address 10.0.1.10;
}

host w1a2 {
  hardware ethernet 70:71:bc:b1:8e:77;
  fixed-address 10.0.1.11;
}

host w1a3 {
  hardware ethernet 70:71:bc:b1:8c:ff;
  fixed-address 10.0.1.12;
}

host w1a4 {
  hardware ethernet 70:71:bc:b1:8e:61;
  fixed-address 10.0.1.13;
}

host w1a5 {
  hardware ethernet 70:71:bc:b1:8c:af;
  fixed-address 10.0.1.14;
}

host w1a6 {
  hardware ethernet 70:71:bc:b1:8c:66;
  fixed-address 10.0.1.15;
}


# Wolke Cluster Block B
#
host w1b1 {
  hardware ethernet 70:71:bc:ad:1e:d4;
  fixed-address 10.0.1.16;
}

host w1b2 {
  hardware ethernet 70:71:bc:ad:1e:f1;
  fixed-address 10.0.1.17;
}

host w1b3 {
  hardware ethernet 70:71:bc:dc:80:4a;
  fixed-address 10.0.1.18;
}

host w1b4 {
  hardware ethernet 70:71:bc:dc:80:3b;
  fixed-address 10.0.1.19;
}

host w1b5 {
  hardware ethernet 70:71:bc:b1:8d:8d;
  fixed-address 10.0.1.20;
}

host w1b6 {
  hardware ethernet 70:71:bc:b1:8c:37;
  fixed-address 10.0.1.21;
}


# Wolke Cluster Block C
#
host w1c1 {
  hardware ethernet 70:71:bc:b1:8e:6c;
  fixed-address 10.0.1.22;
}

host w1c2 {
  hardware ethernet 70:71:bc:b1:8e:69;
  fixed-address 10.0.1.23;
}

host w1c3 {
  hardware ethernet 70:71:bc:b1:8d:99;
  fixed-address 10.0.1.24;
}

host w1c4 {
  hardware ethernet 70:71:bc:b1:8c:e7;
  fixed-address 10.0.1.25;
}

host w1c5 {
  hardware ethernet 70:71:bc:b1:90:4f;
  fixed-address 10.0.1.26;
}

host w1c6 {
  hardware ethernet 70:71:bc:b1:8e:64;
  fixed-address 10.0.1.27;
}
```
