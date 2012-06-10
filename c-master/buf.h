struct bufInfo
{
 int row; // init 1
 int col; // init 1
 int chr; // init 1
 char* filename; // ggf. URL
};

struct bufList
{
 struct bufInfo * bi;
 struct bufList * prev;
 struct bufList * next;
 char * content; // immer mit maximaler allokation von bufMaxLen bzw content_len_allocated
 int content_len_allocated; // aktuelle Laenge, anfangs 0
 int content_len_current; // aktuelle Laenge, anfangs 0
 int eof;
};

struct bufListPtr
{
 struct bufList * bl;
 long contentIdx;
};

struct envList
{
 struct envList * prev;
 char * name;
 char * type;
 void * value;
};

struct bufList * bufListMake( struct bufInfo * bi, struct bufList * prev, struct bufList * next);
struct envList * envListMake( struct envList * prev, char * name, char * type, void * value);

struct bufInfo * bufInfoMake( int row, int col, int chr, char* filename);
struct bufInfo * bufInfoMakeInit( char* filename);
struct bufList * bufListAppend( struct bufList * bl, char * c2append, int bufMaxLenOverride);
struct bufList * bufListAppendChar( struct bufList * bl, char c2append, int bufMaxLenOverride);
int bufListLength( struct bufList * bl);
char * bufList2Str( struct bufList * bl);
struct bufListPtr * bufListPtrMake( struct bufList * bl, long contentIdx);
int bufListPtrEof( struct bufListPtr *blp);
char bufListPtrReadChar( struct bufListPtr *blp); // Achtung: blp wird modifiziert!
char bufListPtrReadCharBack( struct bufListPtr *blp); // Achtung: blp wird modifiziert!
int bufListPtrAvailable( struct bufListPtr *blp);
int bufListPtrLength2( struct bufListPtr * blpFrom, struct bufListPtr * blpTo); // baustelle: assertions, umwandeln: nichtrekursiv
char * bufListPtr2Str2( struct bufListPtr * blpFrom, struct bufListPtr * blpTo); // baustelle: spaeter auch per bufListPtr


