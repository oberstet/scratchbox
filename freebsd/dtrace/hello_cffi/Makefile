all:
	cc -c -Wall -Werror -fpic foo.c
	cc -shared -l dtrace -l proc -l ctf -l elf -l z -l rtld_db -l pthread -l util -o libfoo.so foo.o
