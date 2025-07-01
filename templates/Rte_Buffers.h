#ifndef RTE_BUFFERS_H
#define RTE_BUFFERS_H

/**
 * [SWS_Rte_80001]
Upstream requirements: SRS_Rte_00306
dThe RTE Generator shall create the RTE Global Buffer Declaration File
when the RTE Implementation Plug-In mode is enabled.
 */
#include "Rte_DataHandleType.h"
#include "Rte_Rips_myPlugin1_Buffers.h"
#include "Rte_Rips_myPlugin2_Buffers.h"

extern uint32 Rte_someInternalNameForData;

#define Rte_Rips_GlobalCopy_myMappedData Rte_someInternalNameForData

#endif /* RTE_BUFFERS_H */