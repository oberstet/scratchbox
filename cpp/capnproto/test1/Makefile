version:
	g++ --version
	capnp --version

requirements:
	sudo apt install -y capnproto libcapnp-dev

generate:
	capnp compile -oc++ addressbook.capnp

compile: generate
	g++ -std=c++11 -c test.cpp

link_dynamic:
	g++ test.o -lcapnp -lkj -o test
	file ./test
	ldd ./test

link_static:
	#g++ test.o -Wl,-Bstatic -lcapnp -lkj -o test
	#g++ test.o /usr/lib/x86_64-linux-gnu/libcapnp.a /usr/lib/x86_64-linux-gnu/libkj.a -o test
	#g++ -static -static-libgcc -static-libstdc++ test.o -lcapnp -lkj -o test
	g++ -static test.o -lcapnp -lkj -o test
	file ./test
	-ldd ./test
	nm ./test | grep " U "

build_dynamic: compile link_dynamic

build_static: compile link_static

clean:
	rm -f addressbook.capnp.c++
	rm -f addressbook.capnp.h
	rm -f test
	rm -f test.o

build: clean build_static build_dynamic
