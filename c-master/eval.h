
struct parseTreeContainer
{
 struct parseTreeContainer * prev;
 struct parseTree * ptp;

 // baustelle: weitere Felder
};

struct parseTreeContainer * evalParseTree( struct parseTreeContainer * ptpc);

