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
 // oder im envListCurrent zu finden. wenn der ptp einem befehlspointer entspricht, muesste
 // er auf den dortigen entsprechenden Code gesetzt werden. Ist der Code-Typ kein parseTree
 // sondern eine bufList, muss entsprechend der blp gesetzt werden und der ptp entsprechend daraus
 // generiert werden (wie jetzt in der mainloop)
 // der return von dem nicht-Haupt-parseTree muss durch eine rueckkehradresse definiert
 // sein, die sich im envListCurrent befindet. weiterhin wird fuer die rueckkehr ein Indiz
 // gebraucht, welches das ende von bufList und parseTree anzeigt. Im Falle des parseTree 
 // koennte es sich um ein token vom tokenType tokenTypeEnd (ggs von tokenTypeBeginning) handeln.

 // das Environment der Funktion sollte das Environment zum Definitionszeitpunkt sein (normal),
 // koennte aber auch jenes zum Zeitpunkt des Aufrufs sein (ungewoehnlich). Das hiesse dann
 // dass die gerufene Funktion Variablen der rufenden Funktion sehen und ggf. modifizieren kann.
 // Die Entscheidung sollte dem Entwickler (PL-Lisp Anwender) ueberlassen werden zb durch
 // Definition des Funktionstyps (vgl. Macro).
 
 // da envListCurrent sowohl eine Art Stack, als auch das Environment darstellt, ist zu
 // hinterfragen, ob es sich dabei um eine sinvolle semantische Doppelbelegung handelt.
 // Es wuerde bedeuten, dass eine definierte Funktion nur auf Symbole zugreifen kann, die
 // vor ihr definiert wurden. Dies koennte der Programmierer (PL-Lisp Anwender) 
 // temporaer oder dauernd aendern, indem er das Environment der Funktion nach belieben neu setzt.

 // Es haette auch den Vorteil, dass die Funktion bei bedarf zum Definitionszeitpunkt 
 // pruefen koennte, ob all ihre enthaltenen symbole auch tatsaechlich bereits existieren.
 // (auch bei inneren Funktionen, passiert dann bei definition der inneren 
 // in der aeusseren beim Aufruf der aeusseren zur Laufzeit)

 // Aufgrund dessen, dass die aktuell gerufene Funktion auf den Stack zur Rueckkehr 
 // und zur Rueckgabe von Werten zugreifen muss, existieren zum Zeitpunkt des Funktionsaufrufs
 // 2 relevante envList - Datenstrukturen: envListCurrent (pro Thread) und die der Funktion
 // zugeordnete envList. Kommt der envListPtr  bei der Suche nach einem Symbol an einer Markierung
 // vorbei, die die Funktion bezeichnet, in der wir uns gerade befinden (ptp), muss er 
 // (ausser in ausnahmefaellen) dort weitersuchen. Funktioniert auch mit inneren Funktionen.
 //
 // def f1
 //  def f2
 //  ret f2
 // call f1 -> fx
 // call fx

 // die Expansion / Auswertung eines Klammerausdrucks erfolgt mit schliessen der Klammer

 // als naechstes: Auswertung von Symbol und Symbol-Macro (liefert Voraussetzung fuer 
 // Macros)
 //
 // als naechstes: Calling-Convention

 // da Symbole schrittweise ersetzt werden, sind diese vergleichbar mit einem Ausdruck, der einen
 // returncode hat. folglich werden diese aehnlich behandelt, wie spaeter funktionen: sie hinterlassen
 // auf dem envListCurrent einen returnwert. Da der envListCurrent aber nicht, wie ein Stack ein Array 
 // darstellt, sondern eine rueckwaertsverkettete Liste ist, muss genuegend von ihm aus dem aufrufenden 
 // Context her bekannt sein um den rueckkehrwert zu sehen

 // irgendwie noch unklar: Evaluation vs. Parameteruebergabe (naming)
 // die an eine Funktion uebergebenen parameter werden zunaechst auf envListCurrent gelegt 
 // und parameter_1 ... parameter_n benannt. (im falle eines macros ohne evaluation der parameter;
 // im falle einer funktion muessen die symbole der parameter evaluiert, also ihre rueckgabewerte
 // gesetzt werden.)
 // dann mussen fuer die gerufene Funktion vor ihrem eigentlichen Aufruf die positionalen Parameter
 // erneut gesetzt werden, aber mit dem von der Funktion vorgesehenen Namen
 // jedenfalls stehen die Parameter vor der Funktion im envListCurrent, was interessant ist, wenn man
 // die bereits vorhandene Parametrisierung auf eine andere Funktion mit dem selben oder einem kompatiblen
 // Parameterschema (Prototyp/Head) anwenden will.
 // Jedenfalls muss der Eintragstyp der Parameter in envListCurrent klar von variablen symbolen
 // abgegrenzt werden; dazu existiert in struct envList der Eintrag 'char * type' (buf.h)
 // es fehlen noch die vordefinierten typen

 // auch fuer den rueckkehrwert muss ein entsprechender envList.typ definiert sein, es koennen auf
 // diesem Wege sogar mehrere Parameter aus unterschiedlichen Stellen zurueckgegeben werden,
 // jedoch fuer suspend/yield wird noch mehr gebraucht (ggf. eine Art suspendNow, der fuer mehrere
 // vorangegangene returns die Funktion verlaesst) in jedem fall braechte man dann auch ein klares
 // keyword fuer das endgueltige Verlassen der Funktion

 // envListCurrent:
 // ( ... funktionskopf begin
 // a b c ... parameter # vorerst anonym
 // ) ... funktionskopf end # pruefung der uebergebenen parameter (Anzahl), 
 //                         # uebersetzen der parameter auf die lokalen parameternamen der funktion
 // x y z                   # x=a, y=b, z=x, es erfolgt der eigentliche funktionsaufruf

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

