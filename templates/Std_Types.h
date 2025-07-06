#ifndef STD_TYPES_H
#define STD_TYPES_H

#include "Platform_Types.h"
#include "Compiler.h"

#define STD_TYPES_AR_RELEASE_MAJOR_VERSION 4
#define STD_TYPES_AR_RELEASE_MINOR_VERSION 3
#define STD_TYPES_AR_RELEASE_REVISION_VERSION 1

#define STD_TYPES_SW_MAJOR_VERSION 1
#define STD_TYPES_SW_MINOR_VERSION 0
#define STD_TYPES_SW_PATCH_VERSION 0

#ifndef NULL_PTR
#define NULL_PTR ((void*)0)
#endif

typedef uint8 Std_ReturnType;

#define E_OK                    0u
#define E_NOT_OK                (Std_ReturnType)1u

#define E_NO_DTC_AVAILABLE      (Std_ReturnType)2u
#define E_SESSION_NOT_ALLOWED   (Std_ReturnType)4u
#define E_PROTOCOL_NOT_ALLOWED  (Std_ReturnType)5u
#define E_REQUEST_NOT_ACCEPTED  (Std_ReturnType)8u
#define E_REQUEST_ENV_NOK       (Std_ReturnType)9u
#define E_PENDING               (Std_ReturnType)10u
#define E_COMPARE_KEY_FAILED    (Std_ReturnType)11u
#define E_FORCE_RCRRP           (Std_ReturnType)12u

#define STD_HIGH                0x01u
#define STD_LOW                 0x00u

#define STD_ACTIVE              0x01u
#define STD_IDLE                0x00u

#define STD_ON                  0x01u
#define STD_OFF                 0x00u

typedef struct {
    uint16 vendorID;
    uint16 moduleID;
    uint8 sw_major_version;
    uint8 sw_minor_version;
    uint8 sw_patch_version;

} Std_VersionInfoType;

typedef struct {
    uint8 Std_TransformerErrorCode;
    uint8 Std_TransformerClass;

} Std_TransformerError;

typedef struct {
    uint8 ForwardedStatus;
    uint8 TransformerClass;

} Std_TransformerForward;

#endif // STD_TYPES_H 
