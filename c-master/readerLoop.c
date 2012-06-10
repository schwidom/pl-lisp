
#include "api.h"

// erstmal nur einlesen in eine struct bufList

struct bufList * readerLoop( FILE * fInputFile, struct bufList * bl) 
{
  {
   int fgotc;
   char c;
   while( 1)
   {
    fgotc= fgetc( fInputFile);
    c= (char) fgotc;
    // printf( "%c", c);


    if( EOF == fgotc)
    {
     bl -> eof= 1; // 0f8b9318a3884bc7a1d14c31728cde13 wenn bereits vorher abgebrochen werden kann, muss ausserhalb eof festgestellt werden koennen
     break;
    }

    bl= bufListAppendChar( bl, c, 0);

    if( '\n' == fgotc) break; // baustelle: allgemeiner, 0f8b9318a3884bc7a1d14c31728cde13
   } 
  }
  return bl;
}

