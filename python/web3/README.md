This code shows how to use Web3 (a blocking library) with Twisted to interact with a contract on the blockchain.

The test program has a single command line option: when you provide `--blocked`, Web3 will be used on the main thread and hence block the Twisted reactor. When used without this option, the actual Web3 use is only from a background thread from the default Twisted threadpool.

You can see the different outcome: https://asciinema.org/a/EkvFILXPicCeBh0oN81rlCeSQ
