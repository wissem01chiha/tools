
#ifdef RTE_APPLICATION_HEADER_FILE
2 #error Multiple application header files included.
3 #endif /* RTE_APPLICATION_HEADER_FILE */
4 #define RTE_APPLICATION_HEADER_FILE
#endif
#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */


// this is an example of a swc rte generation 


// The following declaration in the input XML:
// 1 <APPLICATION-SOFTWARE-COMPONENT-TYPE>
// 2 <SHORT-NAME>Source</SHORT-NAME>
// 3 </APPLICATION-SOFTWARE-COMPONENT-TYPE>
// should result in the application header file Rte_Source.h being generated.

#define Rte_InitValue_<Port>_<DEPType> <initValue><suffix>

#ifdef __cplusplus
}; /* extern "C" */
#endif /* __cplusplus */

