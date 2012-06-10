#include "api.h"

struct parseTree * evalParseTree( struct parseTree * ptp)
{

 // der struct parseTree * ptp Pointer repraesentiert den aktuellen Abarbeitungszustand
 // (vgl. befehls-pointer). Der gesamte parseTree verbleibt unveraendert. Es kann passieren, dass
 // der ptp in einen Parsetree gelangt, der vom Haupt-Parsetree abgekoppelt ist
 // (Returnwert der Macro-Funktion, Funktions/Macroaufruf oder aehnliches).
 // Ein derartiger Parsetree ist dann ueber envListCurrent zu erreichen.

 // Die Macrofunktion laeuft im Context eines eigenen Environments,
 // der Expandierte Code jedoch im Context des Macroaufrufs

 // Der parseTree-Knoten muss bei betreten des Macros / der Funktion in den envListCurrent
 // eingepflegt sein. Da die Funktion auch hier wie ein Thread behandelt wird, muss
 // ermittelt werden koennen ob der jeweilige Vorgang bereits geschehen ist:
 // einfaches Indiz: Kann der naechste parseTree-Knoten nicht bearbeitet werden,
 // erfolgt auch keine Operation und der returnwert bleibt derselbe.

 // die erkannten zu expandierenden / evaluierenden Symbole sind entweder system-symbole
 // oder im envListCurrent zu finden. wenn der ptp einem befehlspointer entspricht, muesse
 // er auf den dortigen entsprechenden Code gesetzt werden. Ist der Code-Typ kein parseTree
 // sondern eine bufList, muss entsprechend der blp gesetzt werden und der ptp entsprechend daraus
 // generiert werden (wie jetzt in der mainloop)
 // der return von dem nicht-Haupt-parseTree muss durch eine rueckkehradresse definiert
 // sein, die sich im envListCurrent befindet. weiterhin wird fuer die rueckkehr ein Indiz
 // gebraucht, welches das ende von bufList und parseTree anzeigt. Im Falle des parseTree 
 // koennte es sich um ein token vom tokenType tokenTypeEnd (ggs von tokenTypeBeginning) handeln.

 // WEITERBEI

 struct parseTree * ptpNext= NULL;

 while( 1)
 {
  ptpNext= parseTreeNext( ptp);

  if( NULL == ptpNext) break;

  // behandlung

  printf( "evalParseTree %s\n", ptpNext -> tokenType);
  printf( "evalParseTree %s\n", bufListPtr2Str2( ptp -> blp, ptpNext -> blp));

  ptp = ptpNext;
 }


 return ptp;
}

