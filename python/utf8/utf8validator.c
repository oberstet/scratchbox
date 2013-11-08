#include "utf8validator.h"

#define USE_GCC_OPTS

#ifdef USE_GCC_OPTS
// cat /proc/cpuinfo | grep cache_alignment
static const uint8_t UTF8VALIDATOR_DFA[] __attribute__((aligned(64))) =
#else
static const uint8_t UTF8VALIDATOR_DFA[] =
//static const int UTF8VALIDATOR_DFA[] =
#endif
{
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, // 00..1f
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, // 20..3f
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, // 40..5f
   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, // 60..7f
   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9, // 80..9f
   7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7, // a0..bf
   8,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, // c0..df

   0xa,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x3,0x4,0x3,0x3, // e0..ef
   0xb,0x6,0x6,0x6,0x5,0x8,0x8,0x8,0x8,0x8,0x8,0x8,0x8,0x8,0x8,0x8, // f0..ff
   0x0,0x1,0x2,0x3,0x5,0x8,0x7,0x1,0x1,0x1,0x4,0x6,0x1,0x1,0x1,0x1, // s0..s0
   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1, // s1..s2
   1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1, // s3..s4
   1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,1,1,1, // s5..s6
   1,3,1,1,1,1,1,3,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1  // s7..s8
};

#define UTF8_ACCEPT 0
#define UTF8_REJECT 1

void utf8vld_reset (utf8_validator_t* validator) {
   validator->state = UTF8_ACCEPT;
   validator->current_index = 0;
   validator->total_index = 0;
   validator->is_valid = 1;
   validator->ends_on_codepoint = 1;
}

#if 0
void utf8vld_validate (utf8_validator_t* validator, const uint8_t* data, size_t offset, size_t length) {

   int state = validator->state;

#ifdef USE_GCC_OPTS
   __builtin_prefetch(&UTF8VALIDATOR_DFA[0],   0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[64],  0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[128], 0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[192], 0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[256], 0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[320], 0, 3);
   __builtin_prefetch(&UTF8VALIDATOR_DFA[384], 0, 3);
#endif

   for (size_t i = offset; i < length + offset; ++i) {

      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[data[i]]];

#ifdef USE_GCC_OPTS
      if (__builtin_expect(state == UTF8_REJECT, 0))
#else
      if (state == UTF8_REJECT)
#endif
      {
         validator->state = state;
         validator->current_index = i - offset;
         validator->total_index += i - offset;
         validator->is_valid = 0;
         validator->ends_on_codepoint = 0;
         return;
      }
   }

   validator->state = state;
   validator->current_index = length;
   validator->total_index += length;
   validator->is_valid = 1;
   validator->ends_on_codepoint = validator->state == UTF8_ACCEPT;
}

#else

#define SSE_SIZE 16

#include <xmmintrin.h>

// SSE2
#include <emmintrin.h>
#include <mmintrin.h>

// SSE3
#include <pmmintrin.h>
#include <immintrin.h>   // (Meta-header)

// SSE4
//#include <smmintrin.h>

#include <stdio.h>

//#define DEBUG_LOG

void utf8vld_validate (utf8_validator_t* validator, const uint8_t* data, size_t offset, size_t length) {

   //return;

   //int state = validator->state;
   __m128i state = _mm_cvtsi32_si128(validator->state);

/*
   for (size_t i = offset; i < length + offset; ++i) {

      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[data[i]]];

      if (state == UTF8_REJECT) {
         validator->state = state;
         validator->current_index = i - offset;
         validator->total_index += i - offset;
         validator->is_valid = 0;
         validator->ends_on_codepoint = 0;
         return;
      }
   }
*/
#ifdef DEBUG_LOG
   printf("data:     %p\n", data);
   printf("offset:   %zd\n", offset);
   printf("length:   %zd\n", length);
   printf("data+o+l: %p\n", data + offset + length);
   //data += 1;
   //printf("data:     %p\n", data);
#endif
   size_t cnt_pre = SSE_SIZE - ((size_t) (data + offset)) % SSE_SIZE;
   size_t cnt_post = ((size_t) data + offset + length) % SSE_SIZE;

#if 0
   const uint8_t* begin = data + offset + cnt_pre;
   const uint8_t* end = data + offset + length - cnt_post;
#else
   const uint8_t* ptr = data + offset;
   const uint8_t* end = data + offset + length;
#endif

#ifdef DEBUG_LOG
   printf("cnt_pre:  %zd\n", cnt_pre);
   printf("cnt_post: %zd\n", cnt_post);
   printf("ptr:      %p\n", ptr);
   printf("end:      %p\n", end);
#endif

   // http://stackoverflow.com/questions/12913451/mm-extract-epi8-intrinsic-that-takes-a-non-literal-integer-as-argument

   uint8_t type;

   __m128i reg2 = _mm_cvtsi32_si128(0);
   __m128i reg3 = _mm_cvtsi32_si128(256);

   while (ptr < end) {
      __builtin_prefetch(ptr + SSE_SIZE, 0, 3);
      __m128i reg1 = _mm_load_si128((void *) ptr);

/*
      //reg2 = _mm_xor_si128(reg1, reg2);
      //_mm_cvtsi128_si32(state)
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  1)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  2)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  3)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  4)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  5)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  6)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  7)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  8)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  9)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 10)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 11)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 12)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 13)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 14)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + _mm_cvtsi128_si32(state) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 15)]]);
*/
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  1)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  2)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  3)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  4)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  5)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  6)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  7)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  8)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  9)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 10)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 11)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 12)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 13)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 14)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 15)]];

//      reg2 = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]);
//      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + state + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]]);

//      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]]);
/*
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  1)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  2)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  3)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  4)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  5)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  6)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  7)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  8)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  9)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 10)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 11)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 12)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 13)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 14)]]);
      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 15)]]);
*/
//      state = _mm_cvtsi32_si128(UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  0)]]);
/*
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  1)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  2)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  3)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  4)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  5)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  6)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  7)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  8)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1,  9)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 10)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 11)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 12)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 13)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 14)]];
      state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[_mm_extract_epi8(reg1, 15)]];
*/
/*
      for (int i = 0; i < SSE_SIZE; ++i) {
         _mm_shuffle_epi8(reg1, _mm_set1_epi8(i));
         uint8_t type = _mm_extract_epi8(reg1, 0);
         state = UTF8VALIDATOR_DFA[256 + (state << 4) + UTF8VALIDATOR_DFA[type]];

         if (state == UTF8_REJECT) {
            validator->state = state;
            validator->current_index = i - offset;
            validator->total_index += i - offset;
            validator->is_valid = 0;
            validator->ends_on_codepoint = 0;
            return;
         }
      }
*/
      ptr += SSE_SIZE;
   }

   //validator->state = _mm_cvtsi128_si32(reg2);
   //validator->state = _mm_cvtsi128_si32(state);
   validator->state = state;

   validator->current_index = length;
   //validator->current_index = state;
   validator->total_index += length;
   validator->is_valid = 1;
   validator->ends_on_codepoint = validator->state == UTF8_ACCEPT;
}
#endif
