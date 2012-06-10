
#include "api.h"

// geparst werden hier ausschliesslich PL-Lisp-Klammern
// fremdcode muesste mit einem anderen Parser geparst werden
// ein Token gilt als vorhanden, wenn auf dieses eines
// der Zeichen " ()" folgt 
// es muss eine Art Parsetree aufgebaut werden, der dann
// schrittweise evaluiert wird
// d.h. ein Parse-Schritt erfolgt solange, bis ein auswertbarer Ausdruck dasteht
// der Parse-Schritt kann aber auch abgebrochen und spaeter weitergefuehrt werden, 
// sobald neue Daten vorliegen (der buffer blp -> bl weiter aufgefuellt wurde)
// auch sollte es moeglich sein, im buffer zurueckzuspringen (try/catch); nur
// ist im Moment noch unklar, ob dabei auch der parseTree zurueckgesetzt werden muss.

char * const tokenTypeBeginning= "tokenTypeBeginning";
char * const tokenTypeWhite= "tokenTypeWhite";
char * const tokenTypeNonWhite= "tokenTypeNonWhite";
char * const tokenTypeBraceOpen= "tokenTypeBraceOpen";
char * const tokenTypeBraceClose= "tokenTypeBraceClose";

struct parseTree * parseTreeMake( struct bufListPtr * blp)
{

 struct parseTree * ret= (struct parseTree *) xMalloc( sizeof( struct parseTree));

 if( NULL!=ret)
 {
  ret -> blp= blp;
  ret -> len= -1;
  ret -> ptPrevToken= NULL;
  ret -> ptNextToken= NULL;
  ret -> ptSubToken= NULL;
  ret -> ptParentToken= NULL;
  ret -> tokenType= tokenTypeBeginning;
 }
 
 return ret;
}

int isSymbol( char c)
{
 return ! isspace( c) && '(' != c && ')' != c;
}

struct parseTree * parseTreeReadToken( struct parseTree * pt, int * blocked) // ret -> blp zeigt zurueck, damit pt -> blp nicht modifiziert werden muss
{
 // umgang mit spaces? : erhalte ich einen pt -> blp, der gerade mit
 // spaces weitergeht, wie wird verfahren? wird der pt -> blp darauf angepasst? oder wird eine Kopie angelegt?
 // ausprobieren! am besten per Config-Struktur, die man dann durchprobieren kann fuer verschiedene Tests

 // Entscheidung: es wird nichts veraendert, stattdessen wird ein Token 'white' eingefuehrt
 // welches dann spaeter bei der Evaluation ignoriert wird
 // es wird zeichenweise gelesen

 // baustelle: es wird grundsaetzlich davon ausgegangen, dass wir immer bei diesem Funktionsaufruf am
 // Anfang eines Tokens stehen, so dass wir nicht zurueckschauen muessen, womit wir zu tun haben.
 // gelingt das Auslesen des Tokens nicht, wird der als Parameter uebergebene pt zurueckgeliefert,
 // wir sind dann stehengeblieben (ggf. codieren)

 // erst, wenn ich weiss, was das aktuelle Zeichen zu bedeuten hat, kann ich einen schritt weitergehen, oder auch nicht.
 // da ich aber mit bufListPtrReadChar automatisch einen Schritt vor gehe, gehe ich bei einem Tokenwechsel zu weit
 // somit muss ich einen Schritt zueueck gehen koennen. Das macht dann bufListPtrReadCharBack

 // andererseits scheint mir, dass ess besser ist, wenn statt auf den Beginn eines Tokens das jeweils erreichte Ende
 // eines Tokens gezeigt wird - das wuerde verhindern, dass der als Parameter uebergebene parseTree geaendert werden muss
 // allerdings muss dann der parseTree doppelt verlinkt werden

 int debug= 1;

 struct parseTree * ret= pt;

 char rodBefore= 0;
 char rod= 0;
 int breakState= 0;

 struct bufListPtr * blp= ( struct bufListPtr *) xMalloc( sizeof( struct bufListPtr));
 
 memcpy( blp, pt -> blp, sizeof( struct bufListPtr));

 *blocked= 1;

 if( debug) printf( "blp: %ld, %ld, %d, %d\n", (long int) blp -> bl -> next, blp -> contentIdx, blp -> bl -> content_len_current, bufListPtrAvailable( blp));

 if( bufListPtrAvailable( blp))
 {
  rodBefore= bufListPtrReadChar( blp);

  if( debug) printf( "rodBefore %c\n", rodBefore);

  if( '('==rodBefore) breakState++;
  if( ')'==rodBefore) breakState++;
  if( breakState)
  {
   *blocked= 0;
   ret= parseTreeMake( blp);
   if( '('==rodBefore) ret -> tokenType= tokenTypeBraceOpen;
   if( ')'==rodBefore) ret -> tokenType= tokenTypeBraceClose;
  }
  else
  {
   while( bufListPtrAvailable( blp))
   {
    rod= bufListPtrReadChar( blp);

    if( debug) printf( "rod %c\n", rod);

    //if( isspace( rodBefore) != isspace( rod)) breakState++; // achtung: optimierung (war zu ungenau)
    if( 0);
    else if( isspace( rodBefore) && ! isspace( rod)) breakState ++;
    else if( isSymbol( rodBefore) && ! isSymbol( rod)) breakState ++;
    else assert( 1);
  
    printf( "breakState %d\n", breakState);

    if( breakState)
    {
     *blocked= 0;
     ret= parseTreeMake( blp);
     bufListPtrReadCharBack( blp);
  
     if( isspace( rodBefore)) ret -> tokenType= tokenTypeWhite;
     else ret -> tokenType= tokenTypeNonWhite;

     //ps -> ptNextToken
     break;
    }
   }
  }
 }

 if( debug) printf( "*blocked %d\n", *blocked);

 if( breakState) // Verkettung
 {
  // Verkettung erfolgt anhand aktuellem und vorangegangenem TokenType
  
  if( debug) printf( "braceconfig: %d %d\n", tokenTypeBraceOpen == pt -> tokenType, tokenTypeBraceClose == ret -> tokenType);

  if( 0);

  else if( tokenTypeBraceOpen == pt -> tokenType  && tokenTypeBraceClose == ret -> tokenType)
  {
   pt -> ptNextToken = ret;
   ret -> ptPrevToken = pt;
   ret -> ptParentToken= pt -> ptParentToken;
  }

  else if( tokenTypeBraceOpen == pt -> tokenType  && tokenTypeBraceClose != ret -> tokenType)
  {
   pt -> ptSubToken= ret;
   ret -> ptParentToken= pt;
  }

  else if( tokenTypeBraceOpen != pt -> tokenType  && tokenTypeBraceClose != ret -> tokenType)
  {
   pt -> ptNextToken = ret;
   ret -> ptPrevToken = pt;
   ret -> ptParentToken= pt -> ptParentToken;
  }

  else if( tokenTypeBraceOpen != pt -> tokenType  && tokenTypeBraceClose == ret -> tokenType) // baustelle: redundant, aber lassen!
  {
   // baustelle: es knallt hier, wenn eine Klammer zuviel geschlossen wurde

   assert( NULL != pt -> ptParentToken);

   struct parseTree * ptPrev= pt -> ptParentToken;

   ptPrev -> ptNextToken= ret;
   ret -> ptPrevToken= ptPrev;
   ret -> ptParentToken= ptPrev -> ptParentToken;
  }

 }

 return ret;
}

struct parseTree * parseCode( struct parseTree * pt)
{
 
 int blocked= 0;
 struct parseTree * ret= pt;

 while( ! blocked) 
  ret= parseTreeReadToken( ret, &blocked);

 return ret;
}

void prettyPrintParseTree( struct parseTree * pt, int rekDepth)
{

 printf( "%d %s\n", rekDepth, pt -> tokenType);
 if( pt -> ptSubToken) prettyPrintParseTree( pt -> ptSubToken, 1+ rekDepth);
 if( pt -> ptNextToken) prettyPrintParseTree( pt -> ptNextToken, 0+ rekDepth);
}

struct parseTree * parseTreeNext( struct parseTree * pt)
{
 if( NULL != pt -> ptSubToken) return pt -> ptSubToken; // fehlte
 if( NULL != pt -> ptNextToken) return pt -> ptNextToken;
 if( NULL != pt -> ptParentToken && NULL != pt -> ptParentToken -> ptNextToken) return pt -> ptParentToken -> ptNextToken;
 return NULL;
}

struct parseTree * parseTreePrev( struct parseTree * pt)
{
 if( NULL != pt -> ptPrevToken && NULL != pt -> ptPrevToken -> ptSubToken)
 { // baustelle: ungetestet
  struct parseTree * ret= pt -> ptPrevToken -> ptSubToken;
  while( ret -> ptNextToken) ret= ret -> ptNextToken; // baustelle: dieser Umstand liesse sich durch eine bessere Verkettung des Trees vermeiden
  return ret;
 }
 if( NULL != pt -> ptPrevToken) return pt -> ptPrevToken;
 if( NULL != pt -> ptParentToken) return pt -> ptParentToken;
 return NULL;
}

