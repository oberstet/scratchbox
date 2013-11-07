#ifndef UTF8_VALIDATOR_H
#define UTF8_VALIDATOR_H

#include <stdlib.h>
#include <stdint.h>

typedef struct {
   int state;
   int current_index;
   int total_index;
   int is_valid;
   int ends_on_codepoint;
} utf8_validator_t;

extern void utf8vld_reset (utf8_validator_t* validator);

extern void utf8vld_validate (utf8_validator_t* validator, const char* data, size_t offset, size_t length);

#endif // UTF8_VALIDATOR_H
