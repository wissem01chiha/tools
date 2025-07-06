#ifndef RTE_H
#define RTE_H

#include "Std_Types.h"
#include "Rte_Type.h"

typedef struct {
    
} Rte_Instance;

{% for port in ports %}
{% if port.kind() == "ClientServer" %}
#define Rte_Call_{{ port.name }}_a(instance, arg) ((instance)->{{ port.name }}.Call_a(arg))
{% else %}
#define Rte_Write_{{ port.name }}_{{ port.signal }}(instance, data) \
    ((instance)->{{ port.name }}.{{ port.signal }} = (data), E_OK)
{% endif %}
{% endfor %}

{% for pim in pims %}
#define Rte_Pim_{{ pim.name }}(instance) ((instance)->{{ pim.name }})
{% endfor %}

{% for irv in irvs %}
#define Rte_IrvIWrite_{{ irv.runnable }}_{{ irv.name }}(instance, value) \
    ((instance)->irv_{{ irv.name }} = (value))
#define Rte_IrvIRead_{{ irv.runnable }}_{{ irv.name }}(instance) \
    ((instance)->irv_{{ irv.name }})
{% endfor %}

{% for mode in modes %}
#define Rte_Mode_{{ mode.name }}(instance) ((instance)->{{ mode.name }})
{% endfor %}

{% for trigger in triggers %}
#define Rte_Trigger_{{ trigger.name }}(instance) ((instance)->{{ trigger.name }}())
{% endfor %}

{% for func in functions %}
void {{ func.name }}({{ func.args }});
{% endfor %}

{% for var in variables %}
extern {{ var.ctype }} {{ var.name }};
{% endfor %}

#endif // RTE_H
