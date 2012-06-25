void * xMalloc( size_t size);
void * xRealloc( void * ptr, size_t size);
void xFree( void * ptr);
void * xDup( void * src, size_t size);
#define XDUP(T,I...) ( (T *) xDup( &( (T) I), sizeof( T)) )
// example: struct parseTreeContainer * ptpc= XDUP(struct parseTreeContainer, { ptp: ptp});
// instead: struct parseTreeContainer * ptpc= (struct parseTreeContainer *) xDup( &( (struct parseTreeContainer) { ptp: ptp}), sizeof( struct parseTreeContainer));
// I... => I is an gnu macro extension, ISO C is: ... => __VA_ARGS__

