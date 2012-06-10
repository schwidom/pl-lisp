
#include "api.h"

void * xMalloc( size_t size)
{
 return malloc( size);
}

void xFree( void * ptr)
{
 free( ptr);
}

void * xRealloc( void * ptr, size_t size)
{
 return realloc( ptr, size);
}


