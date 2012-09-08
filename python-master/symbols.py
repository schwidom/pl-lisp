from tools import ensure

class Symbol( str):

 pass # baustelle: __init__: wenn vom typ Symbol (also Symbol( Symbol( X)), dann darstellung immer noch als Symbol( X), das kann aber auch richtig sein

 def __init__( self, s):
  assert( isinstance( s, str)) # trotzdem landet s in der basisklasse
  assert( not isinstance( s, Symbol))

 def __repr__( self):
  return '%s( %s)' % ( self.__class__.__name__, str.__repr__( self))

ar_value= Symbol( 'ar_value')
ar_list= Symbol( 'ar_list') # spezielles listen symbol fuer (cons AR-LIST ?)= (list (uncons ?)), ar_ steht fuer das erscheinen im car des conses
ar_eval_chain= Symbol( 'ar_eval_chain') # haelt die vorangegangenen schritte und das letzte ergebnis
ar_eval = Symbol( 'ar_eval') # container fuer ht_evalObjectid2previousObjectid und andere anwendungen


class ISRelation: # 010407a6a37b49bfb9836e84236e5586

 def __init__( self):
  self.ht= dict()

 def symAdd( self, symbol, lParents):
 
  ensure( symbol, [Symbol])
 
  if None==lParents:
   lParents= []
  
  ensure( lParents, [list])
 
  if self.ht.has_key( symbol):
   raise Exception( 'already registered %s' % symbol)
  
  self.ht[ symbol]= lParents
 
 def symDel( self, symbol):
 
  ensure( symbol, [Symbol])
 
  del self.ht[ symbol]
 
typeSymbol= ISRelation() # 010407a6a37b49bfb9836e84236e5586
typeSymbolNot= ISRelation() # 010407a6a37b49bfb9836e84236e5586

def private_typeSymbolNotChk( symbol2Chk, symbol): # 010407a6a37b49bfb9836e84236e5586
 
 if not typeSymbolNot.ht.has_key( symbol2Chk):
  return False

 for i in typeSymbolNot.ht[ symbol2Chk]: # baustelle: sequentieller zugriff u.u. zu langsam
  if id( symbol) == id( i):
   return True

 for i in typeSymbolNot.ht[ symbol2Chk]:
  if typeSymbolChk( i, symbol):
   return True
 
 return False

def typeSymbolChk( symbol2Chk, symbol): # 010407a6a37b49bfb9836e84236e5586
 
 if id( symbol2Chk)== id( symbol):
  return True

 if not typeSymbol.ht.has_key( symbol2Chk):
  return False

 if private_typeSymbolNotChk( symbol2Chk, symbol):
  return False

 for i in typeSymbol.ht[ symbol2Chk]: # baustelle: sequentieller zugriff u.u. zu langsam
  if id( symbol) == id( i):
   return True

 for i in typeSymbol.ht[ symbol2Chk]:
  if typeSymbolChk( i, symbol):
   return True
 
 return False

nil=Symbol( 'nil')
true=Symbol( 'true') # glueck gehabt, kein konflikt mit python
noo=Symbol( 'noo')

class IsNotTypeSymbolInstance( Exception):

 def __init__( self, msg):
  Exception.__init__( self, msg)

def ensureConsType( cons, symbolType): # baustelle: unleserlich
 if not typeSymbolChk( cons.car(), symbolType):
  raise IsNotTypeSymbolInstance( 'symbolType: %s' % symbolType)
 
class IsNotTypeSymbol( Exception):

 def __init__( self, msg):
  Exception.__init__( self, msg)

def doSubConsType( cons, symbolTypeSub): 
 if not typeSymbolChk( symbolTypeSub, cons.car()):
  raise IsNotTypeSymbol( 'symbolType: %s' % symbolType)
 cons.car( symbolTypeSub)

whitespace= map( Symbol, [ ' ', '\n'])


