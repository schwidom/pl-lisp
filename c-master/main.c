#include "api.h"

struct envList * envListMake( struct envList * prev, char * name, char * type, void * value)
{

 struct envList * ret= (struct envList *) xMalloc( sizeof( struct envList));

 ret -> prev= prev;
 ret -> name= name;
 ret -> type= type;
 ret -> value= value;

 return ret;
}

char * dash= "-";

int main( int argc, char** argv)
{
 
 if( 0)
  bufListAppendTest();

 set( "set", c_builtin_macro, (void *)set);
 // hier fehlen zusatzinformationen, wie die aufgerufen werden kann
 // wenn c-function: wieviel Parameter, welche typen
 // ggf. ueber pl-lisp calling convention loesen oder mixen

 char* nil= "nil"; // Hack
 set( nil, builtin_symbol_macro, nil); // Hack

 if( 1)
 {

  FILE * fInputFile= NULL;

  char * fnameInputFile= NULL;

  // printf( "argc %d\n", argc);
  // printf( "argv[ 0] %s\n", argv[ 0]); // a.out

  if( 1==argc) // wenn keine parameter uebergeben worden sind
  {
   // fnameInputFile= "-";
   fnameInputFile= dash;
   fInputFile= stdin;
  }
  else
  {
   fnameInputFile= argv[ 1];
   fInputFile= fopen( fnameInputFile, "r");
  }

  {
   struct bufInfo * bi= NULL;
   bi= (struct bufInfo *) xMalloc( sizeof( struct bufInfo));
   struct bufList * bl=  bufListMake( bi, NULL, NULL);
   struct bufList * blStart= bl;
   struct bufListPtr * blp= bufListPtrMake( blStart, 0);
   struct parseTree * pt= parseTreeMake( blp);
   struct parseTree * ptBegin= pt;
   //struct parseTreePointer ptp= parseTreePointerMake( ptBegin);
   struct parseTree * ptp= ptBegin; // mehr wird als parseTreePointer nicht benoetigt anfangs
   //struct parseTreeContainer * ptpc= (struct parseTreeContainer *) xDup( &( (struct parseTreeContainer) { ptp: ptp}), sizeof( struct parseTreeContainer));
   struct parseTreeContainer * ptpc= XDUP( struct parseTreeContainer, { ptp: ptp});

   while( ! bl -> eof)
   {

    bl= readerLoop( fInputFile, bl);
    printf( "bufListLength %d\n", bufListLength( bl));
    printf( "bufList2Str bl\n%s\n", bufList2Str( bl));

    pt= parseCode( pt);
    // printf( "pt -> tokenType: %s\n", pt -> tokenType);
    // printf( "pt -> blp: %c\n", bufListPtrReadCharBack( pt -> blp));
    bufListPtrReadChar( pt -> blp);

    prettyPrintParseTree( ptBegin, 0);

    ptpc= evalParseTree( ptpc);

   }
   printf( "bufList2Str blStart\n%s\n", bufList2Str( blStart));
  }

 }

 return 0;
}

