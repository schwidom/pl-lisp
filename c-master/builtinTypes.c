#include "api.h"

int isType( char* t1, char* t2)
{
 return t1==t2 || 0==strcmp( t1, t2);
}

int isTypeDefault( char* t1, char* t2)
{
 return t1==t2;
}

char* function= "function";
char* macro= "macro";
char* builtin_macro= "builtin_macro";
char* c_builtin_macro= "builtin_macro";
char* builtin_symbol_macro= "builtin_symbol_macro";

