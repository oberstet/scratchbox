all:
	cc \
	 -I /usr/src/cddl/compat/opensolaris/include \
	 -I /usr/src/cddl/contrib/opensolaris/lib/libdtrace/common/ \
	 -I /usr/src/sys/cddl/compat/opensolaris \
	 -I /usr/src/sys/cddl/contrib/opensolaris/uts/common/ \
	 hello_dtrace.c \
	 -l dtrace -l proc -l ctf -l elf -l z -l rtld_db -l pthread -l util \
	 -o hello_dtrace

test: all
	sudo ./hello_dtrace
