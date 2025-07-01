// ser defined impl data tyes 
#include "Rte.h" 

// The RTE Types Header File includes the RTE specific type declarations derived from
// the ImplementationDataTypes created from the definitions of AUTOSAR meta-
// model classes within the RTE generator’s input.
#define RTE_E_OK 0
// mplementationDataTypes are generated in the RTE Types Header file

{% for attribute in PrimitiveImplementationDataType %}
typedef {% attribute %} PrimitiveImplementationDataType;
{% endfor %}

typedef <nativeDeclaration> <name>[<size 1>]{[<size 2>]...[<size n>]};