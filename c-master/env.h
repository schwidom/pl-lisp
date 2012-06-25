
struct envList
{
 struct envList * prev;
 char * name;
 char * type;
 void * value;
};

extern struct envList * envListCurrent;

extern char * envListTypeRet;

