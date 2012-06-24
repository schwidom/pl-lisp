#include <stdio.h>
#include <stdlib.h> // malloc, size_t, free, realloc
#include <string.h> // strlen, strcmp, strncat
#include <assert.h> // assert
#include <ctype.h> // isspace

#include "buf.h"
#include "env.h"
#include "mem.h"
#include "externals.h"

// tests/bufListAppendTest.c

void bufListAppendTest();

// builtin_functions/set/code.c

void set( char* name, char* type, void* value);

#include "builtinTypes.h"

// readerLoop.c

struct bufList * readerLoop( FILE * fInputFile, struct bufList * bl);

// parseCode.c

#include "parseCode.h"

// eval.c

struct parseTree * evalParseTree( struct parseTree * ptp);

