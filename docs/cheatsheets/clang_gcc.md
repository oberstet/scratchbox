# Make Variables

See [here](http://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html) and:

	CC			C compiler executable
	CXX			C++ compiler executable
	CPP			C/C++ preprocessor executable
	CFLAGS		C compiler flags
	CXXFLAGS	C++ compiler flags
	CPPFLAGS	C/C++ preprocessor flags
	LDFLAGS     Extra flags to give to compilers when they are supposed to invoke the linker
	LDLIBS		Library flags or names given to compilers when they are supposed to invoke the linker

# Check predefined symbols:

	clang -dM -E -x c /dev/null
	gcc -dM -E -x c /dev/null


