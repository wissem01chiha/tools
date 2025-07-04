#ifndef RTE_H
#define RTE_H

// rte tyes wch$ic not configu)red not gne 
#include "Std_Types.h"

// client-server port ‘p1’ with operation ‘a’ with a single argument,

{% for port in ports %}
#define Rte_Call_{{ port.name }}_a(s,v) ((s)->{{ port.name }}.Call_a(v))
{% endfor %}

// in compatiblty mode : 
#define Rte_Pim
#define Rte_IRead
#define Rte_IWrite
#define Rte_IWriteRef
#define Rte_IStatus
#define Rte_IrvIRead
#define Rte_Send_p1_a(s,a) (<var> = (a), RTE_E_OK)

// Generated function prototypes
{% for func in functions %}
void {{ func.name }}({{ func.args }});
{% endfor %}

// Global variables
{% for var in variables %}
extern {{ var.ctype }} {{ var.name }};
{% endfor %}


// Std_ReturnType
// Rte_Write_<p>_<o>([IN Rte_Instance <instance>],
// IN <data>)
// Where <p> is the port name and <o> the VariableDataPro-
// totype within the sender-receiver interface categorizing the port.
// c(BSW00310, RTE00098, RTE00028, RTE00131)

#endif // RTE_H
