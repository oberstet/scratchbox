#include <stdlib.h>
#include <stdint.h>
#include <assert.h>

#include <xmmintrin.h>

// SSE2
#include <emmintrin.h>
#include <mmintrin.h>

// SSE3
#include <pmmintrin.h>
#include <immintrin.h>   // (Meta-header)

// SSE4
//#include <smmintrin.h>

// http://gcc.gnu.org/onlinedocs/gcc/i386-and-x86_002d64-Options.html

static uint32_t coeffs[4] __attribute__((aligned(16))) = {
//  0x00000000, 0x00000000, 0x00000000, 0x00000000,
  0x00112233, 0x44556677, 0x8899aabb, 0xccddeeff,
};

void xor (char* data, size_t len)
{
//   __m128i shuffle = _mm_set_epi8(12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3);
//   __m128i shuffle = _mm_set_epi8(15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0);
   __m128i shuffle = _mm_set_epi8(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15);

   //__m128i val;
   __m128i mask = _mm_load_si128((void *) coeffs);

   __m128i* p = (__m128i*) data;
   __m128i* p_end = (__m128i*) (data + len);

   while (p < p_end) {
     //val = _mm_load_si128(p);
     //_mm_store_si128(p, _mm_xor_si128(val, mask));
     _mm_store_si128(p, _mm_shuffle_epi8(_mm_load_si128(p), shuffle));

     //_mm_store_si128(p, val);
     ++p;
   }
/*
   for (size_t i = 0; i < len; ++i) {
      data[i] = 66;
   }
*/
}

/*
const __m128i* pa = (__m128i*)a;
const __m128i* pend = (__m128i*)(a + arr_size);
__m128i* pb = (__m128i*)b;
__m128i xmm1, xmm2;
while (pa < pend) {
  xmm1 = _mm_loadu_si128(pa); // must use unaligned access
  xmm2 = _mm_load_si128(pb); // numpy will align at 16 byte boundaries
  _mm_store_si128(pb, _mm_xor_si128(xmm1, xmm2));
  ++pa;
  ++pb;
}
*/
