#ifndef PLATFORM_TYPES_H
#define PLATFORM_TYPES_H

#include <stdbool.h>
#include <stdint.h>

#define PLATFORM_TYPES_AR_RELEASE_MAJOR_VERSION 4
#define PLATFORM_TYPES_AR_RELEASE_MINOR_VERSION 3
#define PLATFORM_TYPES_AR_RELEASE_REVISION_VERSION 1

#define CPU_TYPE            CPU_TYPE_32 
#define CPU_BIT_ORDER       MSB_FIRST

#define HIGH_BYTE_FIRST     0U
#define LOW_BYTE_FIRST      1U

#ifndef FALSE
#define FALSE		        0  
#endif
#ifndef TRUE
#define TRUE		        1  
#endif

typedef uint8_t      		boolean; 

typedef int8_t         		sint8;
typedef uint8_t       		uint8;
typedef int16_t        		sint16;
typedef uint16_t      		uint16;
typedef uint16_t			ucs2;
typedef int32_t         	sint32;
typedef uint32_t       		uint32;
typedef int64_t  			sint64;
typedef uint64_t  			uint64;
typedef uint_least8_t       uint8_least;
typedef uint_least16_t      uint16_least;
typedef uint_least32_t      uint32_least;
typedef int_least8_t        sint8_least;
typedef int_least16_t       sint16_least;
typedef int_least32_t       sint32_least;
typedef float               float32; 
typedef double              float64; 

#if defined(__GNUC__)
#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__ 
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                     
#elif __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__ 
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                                  
#else
#error No endian defined by compiler.
#endif

#elif defined(__ghs__)
#if defined(__LITTLE_ENDIAN__)
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                    
#elif defined(__BIG_ENDIAN__)
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                                   
#else
#error No endian defined by compiler.
#endif

#elif defined(__CWCC__)
#if __option(little_endian)
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                    
#else
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                                   
#endif

#elif defined(__DCC__)
#if defined(__LITTLE_ENDIAN__)
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                     
#elif defined(__BIG_ENDIAN__)
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                                   
#else
#error No endian defined by compiler.
#endif

#elif defined(__ARMCC_VERSION)
#if defined(__BIG_ENDIAN)
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                               
#else
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                     
#endif
#elif defined(_WIN32)
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                     

#elif defined(__IAR_SYSTEMS_ICC__)
#if defined(__LITTLE_ENDIAN__)
#define CPU_BYTE_ORDER LOW_BYTE_FIRST                                     
#elif defined(__BIG_ENDIAN__)
#define CPU_BYTE_ORDER HIGH_BYTE_FIRST                                    
#else
#error No endian defined by compiler.
#endif
#else
#error Compiler not defined
#endif

#endif // PLATFORM_TYPES_H