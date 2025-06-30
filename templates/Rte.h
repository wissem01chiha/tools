#ifndef RTE_H
#define RTE_H

// Generated function prototypes
{% for func in functions %}
void {{ func.name }}({{ func.args }});
{% endfor %}

// Global variables
{% for var in variables %}
extern {{ var.ctype }} {{ var.name }};
{% endfor %}

#endif // RTE_H
