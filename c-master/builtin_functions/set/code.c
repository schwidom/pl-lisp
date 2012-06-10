
#include "../../api.h"

void set( char* name, char* type, void* value)
{
 envListCurrent= envListMake( envListCurrent, name, type, value);
}

