# Building a Kernel

```
cd /usr/src/sys/amd64/conf
cp GENERIC BRUMMER_KERNEL_10_1
cd /usr/src
make buildkernel KERNCONF=BRUMMER_KERNEL_10_1
make installkernel KERNCONF=BRUMMER_KERNEL_10_1
```
