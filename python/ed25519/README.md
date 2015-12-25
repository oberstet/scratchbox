# Generate Ed25519 Keys using OpenSSH

To generate a new Ed25519 private key using OpenSSH:

```
ssh-keygen -t ed25519 -N '' -f node_ed25519
```

To get the raw key from above OpenSSH key file, we use [this](https://github.com/mk-fg/fgtk/blob/master/ssh-keyparse) (which is copied here, licensed [under](http://www.wtfpl.net/txt/copying/)):

```
./ssh-keyparse --hex node_ed25519 > node_ed25519.hex
```

To load and verify the key from PyNaCl:

```
python load_key.py
```

Actually, with Ed25519, the secret stored isn't the private key itself, but the seed value. And the seed value is simply a 32 byte random value. Hence we can "generate a new key" like so:

```
dd if=/dev/urandom of=node_ed25519.bin count=1 bs=32
```

This is nice, because it provides the user with maximum flexibility and control over the key generation process. And if the user prefers convenience, we provide auto-generate for keys.
