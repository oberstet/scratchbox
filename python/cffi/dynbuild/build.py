from cffi import FFI
ffi = FFI()

ffi.cdef(
"""
    int foo (int x);
""")

if __name__ == "__main__":
    ffi.set_source("_example",
        """
        #include <x86intrin.h>

        const __m128i* ptr = 0;

        int foo (int x) {
            ptr += 1;
            return x + ((int) ptr);
        };
        """,
        libraries=[])

    ffi.compile()
