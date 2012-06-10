struct parseTree 
{
 struct bufListPtr * blp;
 long len; // -1 == unknown
 struct parseTree * ptPrevToken;
 struct parseTree * ptNextToken;
 struct parseTree * ptSubToken; // zeigt auf den Beginn der Liste
 struct parseTree * ptParentToken;
 char * tokenType;
};

struct parseTree * parseTreeMake( struct bufListPtr * blp);
struct parseTree * parseCode( struct parseTree * pt);
void prettyPrintParseTree( struct parseTree * pt, int rekDepth);

struct parseTree * parseTreeNext( struct parseTree * pt);
struct parseTree * parseTreePrev( struct parseTree * pt);

