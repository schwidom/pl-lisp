
#include "api.h"

struct bufList * bufListMake( struct bufInfo * bi, struct bufList * prev, struct bufList * next)
{

 struct bufList * ret= (struct bufList *) xMalloc( sizeof( struct bufList));

 if( NULL != ret)
 {
  ret -> bi= bi;
  ret -> prev= prev;
  ret -> next= next;
  ret -> content= (void *) xMalloc( 0); // zulaessig
  ret -> content_len_allocated= 0;
  ret -> content_len_current= 0;
  ret -> eof= 0;
 }

 return ret;
}

struct bufListPtr * bufListPtrMake( struct bufList * bl, long contentIdx)
{

 struct bufListPtr * ret= (struct bufListPtr *) xMalloc( sizeof( struct bufListPtr));

 if( NULL != ret)
 {
  ret -> bl= bl;
  ret -> contentIdx= contentIdx;
 }

 return ret;
}

int bufListLength( struct bufList * bl)
{
 if( NULL==bl) return 0;
 return bl -> content_len_current + bufListLength( bl -> next);
}

int bufListPtrLength2( struct bufListPtr * blpFrom, struct bufListPtr * blpTo) // baustelle: assertions, umwandeln: nichtrekursiv
{

 struct bufListPtr sblpTmp;

 if( blpFrom -> bl == blpTo -> bl)
  return blpTo -> contentIdx - blpFrom -> contentIdx;
 else
 {
  sblpTmp.bl = blpFrom -> bl -> next;
  sblpTmp.contentIdx= 0;
  return blpFrom -> bl -> content_len_current - blpFrom -> contentIdx + bufListPtrLength2( &sblpTmp, blpTo);
 }
}

char * bufList2Str( struct bufList * bl) // baustelle: spaeter auch per bufListPtr
{
 int len= bufListLength( bl);

 char * ret= (char *) xMalloc( len + 1);
 ret[ 0]= 0;

 while( bl)
 {
  strncat( ret, bl -> content, bl -> content_len_current); // baustelle: sollte immer langsamer werten => optimierung
  bl= bl -> next;
 }

 return ret;
}

char * bufListPtr2Str2( struct bufListPtr * blpFrom, struct bufListPtr * blpTo) // baustelle: spaeter auch per bufListPtr
{
 int len=  bufListPtrLength2( blpFrom, blpTo);

 char * ret= (char *) xMalloc( len + 1);
 ret[ 0]= 0;

 if( blpFrom -> bl == blpTo -> bl)
 {
  strncat( ret, blpFrom -> bl -> content + blpFrom -> contentIdx, len); // len == blpTo -> contentIdx - blpFrom -> contentIdx
 }
 else
 {

  struct bufList * bl= blpFrom -> bl;

  strncat( ret, blpFrom -> bl -> content + blpFrom -> contentIdx, bl -> content_len_current - blpFrom -> contentIdx);


  while( bl -> next != blpTo -> bl)
  {
   bl= bl -> next;
   strncat( ret, bl -> content, bl -> content_len_current); // baustelle: sollte immer langsamer werten => optimierung
  }
 
  bl= bl -> next;

  strncat( ret, bl -> content, blpTo -> contentIdx);

 }

 return ret;
}

struct bufList * bufListSeekToEnd( struct bufList * bl)
{
 while( NULL != bl -> next) bl= bl-> next; // seek
 return bl;
}

struct bufInfo * bufInfoMake( int row, int col, int chr, char* filename)
{
 struct bufInfo * ret= (struct bufInfo *) xMalloc( sizeof( struct bufInfo));
 ret -> row= row;
 ret -> col= col;
 ret -> chr= chr;
 ret -> filename= filename;
 return ret;
}

struct bufInfo * bufInfoMakeInit( char* filename)
{
 return bufInfoMake( 1, 1, 1, filename);
}

struct bufList * bufListAppendChar( struct bufList * bl, char c2append, int bufMaxLenOverride)
{
 //char * c2appendContainer= " ";
 //c2appendContainer[0]= c2append; // hier krachts
 //c2appendContainer[1]= 0; // hier auch
 char * c2appendContainer= NULL;
 c2appendContainer= (char *)xMalloc( 2);
 c2appendContainer[0]= c2append;
 c2appendContainer[1]= 0;

 //printf( "%d\n", c2appendContainer[1] == 0);

 {
  struct bufList* ret= bufListAppend( bl, c2appendContainer, bufMaxLenOverride);
  xFree( c2appendContainer);
  return ret;
 }
}

struct bufList * bufListAppend( struct bufList * bl, char * c2append, int bufMaxLenOverride)
{

 if( 0 == bufMaxLenOverride) bufMaxLenOverride = bufMaxLen;

 //assert( 0 <= bufMaxLenOverride); // erfolgt implizit
 assert( bl -> content_len_current <= bufMaxLenOverride); // baustelle: zu pruefen, ob bei bl -> content_len_allocated nachgeschraubt werden muss (realloc zum verkleinern ggf?)

 if( NULL != bl -> next)
 {
  printf( "warning: bufListAppend needs to seek\n");
  bl= bufListSeekToEnd( bl); // seek if needed
 }

 {

  int c2appendLen= strlen( c2append);
  int c2appendLen2Use= c2appendLen;

  int lenNeeded= bl -> content_len_current + c2appendLen;

  int len2Use= lenNeeded;

  int performNextOperation= 0; // bool
 
  if( len2Use > bufMaxLenOverride)
  {
   len2Use= bufMaxLenOverride;
   performNextOperation= 1;
   c2appendLen2Use= c2appendLen- ( lenNeeded - bufMaxLenOverride);
  }

  if( len2Use > bl -> content_len_allocated)
  {
   bl -> content = (char *) xRealloc( (void *)bl -> content, len2Use);
   bl -> content_len_allocated= len2Use;
  }
  
  if( len2Use > bl -> content_len_current)
  {
   memcpy( bl-> content + bl -> content_len_current, c2append, c2appendLen2Use);
   bl -> content_len_current += c2appendLen2Use; // == len2Use
  }

  {
   struct bufList * ret= bl;
 

   if( performNextOperation)
   {

    int row = bl -> bi -> row;
    int col = bl -> bi -> col;
    int chr = bl -> bi -> chr;
 
    {
     int i= 0;
     for( i= 0; i < bl -> content_len_current; i++)
     {
      if( '\n' == bl -> content[ i]) col= 1, row++;
      else col++;
      chr++;
     }
    } 

    {
     struct bufInfo * bi= bufInfoMake( row, col, chr, bl -> bi -> filename);
 
     ret= bufListMake( bi, bl, NULL);
     bl -> next= ret;

     {
      //struct bufList * tmp= bufListAppend( bl, c2append+ c2appendLen2Use, bufMaxLenOverride); // warning: bufListAppend needs to seek
      // printf( "rest %s\n", c2append+ c2appendLen2Use);
      struct bufList * tmp= bufListAppend( ret, c2append+ c2appendLen2Use, bufMaxLenOverride);
      if(  lenNeeded - len2Use < bufMaxLenOverride) assert( tmp == ret);
      ret= tmp;
     }
    }
   }

#ifdef FALSE
  axiome: bl -> content_len_current <= bl -> content_len_allocated <= bufMaxLenOverride
#endif

   return ret;
  }
 }
}

int bufListPtrEof( struct bufListPtr *blp)
{
 
 struct bufList * bl= blp -> bl;

 assert( NULL != bl);
 assert( blp -> contentIdx <= bl -> content_len_current);


 if( blp -> contentIdx == bl -> content_len_current && bl -> eof)
  return 1;
 
 return 0;
}

int bufListPtrAvailable( struct bufListPtr *blp)
{
 
 struct bufList * bl= blp -> bl;

 assert( NULL != bl);
 assert( blp -> contentIdx <= bl -> content_len_current);


 if( blp -> contentIdx < bl -> content_len_current)
  return 1;
 else if( bl -> next)
 { // erlaubt ueberspringen leerer bl-s
  struct bufListPtr sbl={ bl: bl -> next, contentIdx: 0};
  return bufListPtrAvailable( &sbl);
 }

 return 0;
}

char bufListPtrReadChar( struct bufListPtr *blp) // Achtung: blp wird modifiziert!, vorher auf EOF testen
{

 struct bufList *bl = blp -> bl;

 assert( NULL != bl);
 assert( blp -> contentIdx <= bl -> content_len_current);


 char ret;

 if( blp -> contentIdx == bl -> content_len_current)
 { 
  //printf( "passiert\n"); // tatsache
  assert( NULL != bl -> next);
  blp -> bl = bl -> next;
  blp -> contentIdx = 0;
  ret= bufListPtrReadChar( blp); // wuerde leere bufList Elemente erlauben
 }
 else
 { // genau hier tritt obiger Fall an der Grenze auf
  assert( NULL != bl -> content);
  ret= bl -> content[ blp -> contentIdx];
  blp -> contentIdx++;
 }

 return ret;
}

char bufListPtrReadCharBack( struct bufListPtr *blp) // Achtung: blp wird modifiziert!, vorher auf EOF testen
{

 struct bufList *bl = blp -> bl;

 assert( NULL != bl);
 assert( blp -> contentIdx >= 0);


 char ret;

 if( blp -> contentIdx == 0)
 { 
  //printf( "passiert\n"); // tatsache
  assert( NULL != bl -> prev);
  blp -> bl = bl -> prev;
  blp -> contentIdx = blp -> bl -> content_len_current;
  ret= bufListPtrReadCharBack( blp); // wuerde leere bufList Elemente erlauben
 }
 else
 { // genau hier tritt obiger Fall an der Grenze auf
  assert( NULL != bl -> content);
  blp -> contentIdx--;
  ret= bl -> content[ blp -> contentIdx];
 }

 return ret;
}

