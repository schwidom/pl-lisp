#include "../api.h"

void bufListAppendTest()
{

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 0);

  printf( "%d\n", 3== bufListLength( blStart));

  bl= bufListAppend( bl, "def", 0);

  printf( "%d\n", 6==bufListLength( blStart));

  int res= memcmp( "abcdef", bl -> content, 6);
  printf( "%d\n", 0==res);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 1== bl -> bi -> col);
  printf( "%d\n", 1== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart)); 

  bl= bufListAppend( bl, "ab", 1);

  printf( "%d\n", 2== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "ab", bufList2Str( blStart)));

  int res= memcmp( "b", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 2== bl -> bi -> col);
  printf( "%d\n", 2== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 1);

  printf( "%d\n", 3== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "abc", bufList2Str( blStart)));

  int res= memcmp( "c", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 3== bl -> bi -> col);
  printf( "%d\n", 3== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 0);
  bl= bufListAppend( bl, "defg", 6); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 7== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "abcdefg", bufList2Str( blStart)));

  int res= memcmp( "g", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 7== bl -> bi -> col);
  printf( "%d\n", 7== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 0);
  bl= bufListAppend( bl, "d", 3); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 4== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "abcd", bufList2Str( blStart)));

  int res= memcmp( "d", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 4== bl -> bi -> col);
  printf( "%d\n", 4== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 0);
  bl= bufListAppend( bl, "defg", 3); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 0== strcmp( "abcdefg", bufList2Str( blStart)));

  printf( "%d\n", 7== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  int res= memcmp( "g", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 7== bl -> bi -> col);
  printf( "%d\n", 7== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "a\nc", 0);
  bl= bufListAppend( bl, "d\nfg", 3); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 7== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "a\ncd\nfg", bufList2Str( blStart)));

  int res= memcmp( "g", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 3== bl -> bi -> row);
  printf( "%d\n", 2== bl -> bi -> col);
  printf( "%d\n", 7== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "a\nc", 2);
  bl= bufListAppend( bl, "d\nfg", 2); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 7== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "a\ncd\nfg", bufList2Str( blStart)));

  int res= memcmp( "g", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 3== bl -> bi -> row);
  printf( "%d\n", 2== bl -> bi -> col);
  printf( "%d\n", 7== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "a\nc", 2);
  bl= bufListAppend( bl, "d\n", 2); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 5== bufListLength( blStart));
  printf( "%d\n", 1== bufListLength( bl));

  bl -> eof= 1;

  // printf( "--\n");
  {
   struct bufListPtr * blp= bufListPtrMake( bl, 0); // baustelle, wird vorerst nicht wieder freigegeben
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", '\n' == bufListPtrReadChar( blp));
   printf( "%d\n", 1 == bufListPtrEof( blp));
   printf( "%d\n", '\n' == bufListPtrReadCharBack( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", bl == blp -> bl);
   printf( "%d\n", 'd' == bufListPtrReadCharBack( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", bl -> prev == blp -> bl);
   printf( "%d\n", 'c' == bufListPtrReadCharBack( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", bl -> prev == blp -> bl);
  }

  {
   struct bufListPtr * blp= bufListPtrMake( blStart, 0); // baustelle, wird vorerst nicht wieder freigegeben
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", 'a' == bufListPtrReadChar( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", '\n' == bufListPtrReadChar( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", 'c' == bufListPtrReadChar( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", 'd' == bufListPtrReadChar( blp));
   printf( "%d\n", 0 == bufListPtrEof( blp));
   printf( "%d\n", '\n' == bufListPtrReadChar( blp));
   printf( "%d\n", 1 == bufListPtrEof( blp));
  }

  printf( "%d\n", 0== strcmp( "a\ncd\n", bufList2Str( blStart)));

  int res= memcmp( "\n", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 2== bl -> bi -> row);
  printf( "%d\n", 3== bl -> bi -> col);
  printf( "%d\n", 5== bl -> bi -> chr);
 }

 if( 1)
 {

  struct bufInfo * bi= bufInfoMakeInit( "fakefile");
  struct bufList * bl= bufListMake( bi, NULL, NULL);
  struct bufList * blStart= bl;

  printf( "%d\n", 0== bufListLength( blStart));

  bl= bufListAppend( bl, "abc", 0);
  bl= bufListAppend( bl, "", 3); // bei 3 gab es einen assert Fehler

  printf( "%d\n", 3== bufListLength( blStart));
  printf( "%d\n", 3== bufListLength( bl));

  printf( "%d\n", 0== strcmp( "abc", bufList2Str( blStart)));

  int res= memcmp( "abc", bl -> content, 1);
  printf( "%d\n", res==0);

  printf( "%d\n", 1== bl -> bi -> row);
  printf( "%d\n", 1== bl -> bi -> col);
  printf( "%d\n", 1== bl -> bi -> chr);
 }
 
}

