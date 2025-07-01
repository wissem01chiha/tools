// RTE life cycle API gen

#include "Rte.h"

Std_ReturnType Rte_Start(void){
    return RTE_E_OK;
    // RTE_E_LIMIT
};

Std_ReturnType Rte_Stop(void);

void Rte_PartitionTerminated_<PID>(void);
void Rte_PartitionRestarting_<PID>(void);
Std_ReturnType Rte_RestartPartition_<PID>(void);