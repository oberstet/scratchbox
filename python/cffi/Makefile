test:
	dd if=/dev/zero of=shm.map bs=1024 count=1
#	dd if=/dev/urandom of=shm.map bs=1024 count=1
	python test3.py -w
	python test3.py
	hexdump shm.map
