rustup update
rustup target add thumbv7m-none-eabi

cargo build --target armv7a-none-eabi

```
(base) oberstet@intel-nuci7:~/scm/oberstet/scratchbox/rust/tuttests/rtic1$ qemu-system-aarch64 --machine help | grep lm3s6965
lm3s6965evb          Stellaris LM3S6965EVB (Cortex-M3)
```


qemu-system-arm --machine lm3s6965evb ./target/thumbv7m-none-eabi/debug/bluepill_blinky
