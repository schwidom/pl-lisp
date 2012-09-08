from tools import ensure
from ConsTrait import Cons

def removeIfContains( inAble, key):
 if key in inAble:
  if isinstance( inAble, dict):
   del inAble[ key]
  else:
   inAble.remove( key) # set, list

class ConsType( str): # zuweisung eines typs zu einer Cons-Datenstruktur (oder auch anderen) erfolgt unabhaengig von der erzeugung des Cons Objekts und fliesst nicht in gleichheits, hash, vergleichs Operationen ein
 
 pass

ht_cons_consid2consAndTypeSet= dict()
ht_cons_consType2ConsidSetAndFunctionSet= dict()

# das mit den Funktionen ist noch schwierig, da nochts ueber den parameter ausgesagt wird - nehmen wir erstmal nur den ersten ( self, this)

def cons_ensureConsDataStructure( cons):
 ensure( cons, [Cons])
 consid= id( cons)
 if False:
  pass
 elif not ht_cons_consid2consAndTypeSet.has_key( consid):
  ht_cons_consid2consAndTypeSet[ consid]= ( cons, set())
 
def cons_ensureConsTypeDataStructure( consType):
 ensure( consType, [ConsType])
 if False:
  pass
 elif not ht_cons_consType2ConsidSetAndFunctionSet.has_key( consType):
  ht_cons_consType2ConsidSetAndFunctionSet[ consType]= ( set(), set())
 
def cons_addType( cons, consType):
 cons_ensureConsDataStructure( cons)
 cons_ensureConsTypeDataStructure( consType)
 consid= id( cons)
 ht_cons_consid2consAndTypeSet[ consid][ 1].add( consType)
 ht_cons_consType2ConsidSetAndFunctionSet[ consType][ 0].add( consid)

def cons_delType( cons, consType):
 cons_ensureConsDataStructure( cons)
 cons_ensureConsTypeDataStructure( consType)
 consid= id( cons)
 removeIfContains( ht_cons_consid2consAndTypeSet[ consid][ 1], consType)
 removeIfContains( ht_cons_consType2ConsidSetAndFunctionSet[ consType][ 0], consid)

def cons_addFunction( consType, consFunction):
 cons_ensureConsTypeDataStructure( consType)
 ht_cons_consType2ConsidSetAndFunctionSet[ consType][ 1].add( consFunction)

def cons_delFunction( consType, consFunction):
 cons_ensureConsTypeDataStructure( consType)
 removeIfContains( ht_cons_consType2ConsidSetAndFunctionSet[ consType][ 1], consFunction)

ht_evalObjectid2previousObjectid= dict()
ht_objectid2Object= dict()
ht_objectid2Object[ id( None)]= None

def registerPreviousObjectID( o, oPrev):
 oId= id( o)
 oPrevId= id( oPrev)
 if not ht_objectid2Object.has_key( oPrevId):
  raise Exception( 'not ht_objectid2Object.has_key( oPrev {==%s})' % str( oPrev))
 if ht_objectid2Object.has_key( oId):
  raise Exception( 'ht_objectid2Object.has_key( o {==%s})' % str( o))
 ht_objectid2Object[ oId]= o
 ht_evalObjectid2previousObjectid[ oId]= oPrevId

ht_objectid2LineFromTo= dict()

def registerObjectLine( o, lineFrom= None, lineTo= None):
 oId= id( o)
 if ht_objectid2LineFromTo.has_key( oId):
  fromTo= ht_objectid2LineFromTo[ oId]
  if None==lineFrom:
   lineFrom= fromTo[ 0]
  if None==lineTo:
   lineTo= fromTo[ 1]

 ht_objectid2LineFromTo[ oId]=( lineFrom, lineTo)


