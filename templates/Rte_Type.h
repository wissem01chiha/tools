#ifndef RTE_TYPE_H
#define RTE_TYPE_H

#include "Std_Types.h"

#define RTE_E_OK     0
#define RTE_E_NOT_OK 1

{% for type in primitive_types %}
typedef {{ type.base_type }} {{ type.name }};
{% endfor %}

{% for enum in enumerations %}
typedef enum {
    {% for value in enum.values %}
    {{ value.name }} = {{ value.value }},
    {% endfor %}
} {{ enum.name }};
{% endfor %}

{% for record in records %}
typedef struct {
    {% for field in record.fields %}
    {{ field.type }} {{ field.name }};
    {% endfor %}
} {{ record.name }};
{% endfor %}

{% for array in arrays %}
typedef {{ array.base_type }} {{ array.name }}[{{ array.size }}];
{% endfor %}

#endif // RTE_TYPE_H