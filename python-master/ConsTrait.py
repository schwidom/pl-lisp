from tools import ensure, IsNotInstance
from symbols import Symbol, nil, ar_list, typeSymbol
from tools import IsAbstract
from symbols import ensureConsType
from tools import parameterReducer
from tools import Wrapper

class ConsEqState:
 
 def __init__( self):
  self.eq_lhs= False
  self.eq_rhs= False

 def mirrors( self, consEqState2):

  ensure( consEqState2, [ConsEqState])
  
  return self.eq_lhs == consEqState2.eq_rhs and self.eq_rhs == consEqState2.eq_lhs

 def isFalse( self):
  return not self.eq_lhs and not self.eq_rhs


class Cons:
 pass

class ConsSimple( Cons):
  
 def __init__( self, ar, dr):
  self.ar= ar
  self.dr=dr

 def car( self, value= None): # baustelle ist diese konvention gut? entweder setzen oder holen, nie beides
  if None == value:
   return self.ar
  else:
   self.ar= value
  
 def cdr( self, value= None): # baustelle ist diese konvention gut? entweder setzen oder holen, nie beides
  if None == value:
   return self.dr
  else:
   self.dr= value

def makeConsTrait( consWrapped, ht_wrappedId2Wrapper= None):
 if None == ht_wrappedId2Wrapper:
  ht_wrappedId2Wrapper= dict()
  return ConsTrait( consWrapped, ht_wrappedId2Wrapper)
 elif ht_wrappedId2Wrapper.has_key( id( consWrapped)):
  return ht_wrappedId2Wrapper[ id( consWrapped)]
 else:
  return ConsTrait( consWrapped, ht_wrappedId2Wrapper)

class ConsTrait( Cons):

 def __init__( self, consWrapped, ht_wrappedId2Wrapper= None):
  if None == ht_wrappedId2Wrapper:
   ht_wrappedId2Wrapper= dict()
  elif ht_wrappedId2Wrapper.has_key( id( consWrapped)): 
   raise Exception( 'ht_wrappedId2Wrapper.has_key( id( consWrapped))')

  consWrapped.car
  consWrapped.cdr
  self.consWrapped= consWrapped # liefert car, cdr

  ht_wrappedId2Wrapper[ id( consWrapped)]= self

  self.hashState= False
  self.eqState= ConsEqState()
  self.cloneDeepState= None # erhaelt geklontes Element, damit der Klonvorgang auch zyklisch funktioniert

  if not isinstance( consWrapped.car(), Cons): # baustelle: vieleicht fuer anderen typ anderen wrapper
   self.ar= None
  elif ht_wrappedId2Wrapper.has_key( id( consWrapped.car())):
   self.ar= ht_wrappedId2Wrapper[ id( consWrapped.car())]
  else:
   self.ar= ConsTrait( consWrapped.car(), ht_wrappedId2Wrapper)

  if not isinstance( consWrapped.cdr(), Cons): # baustelle: vieleicht fuer anderen typ anderen wrapper
   self.dr= None
  elif ht_wrappedId2Wrapper.has_key( id( consWrapped.cdr())):
   self.dr= ht_wrappedId2Wrapper[ id( consWrapped.cdr())]
  else:
   self.dr= ConsTrait( consWrapped.cdr(), ht_wrappedId2Wrapper)

 def __hash__( self):
  ret= hash( self.__hash_calc())
  self.__hash_cleanup()
  return ret

 def __hash_calc( self):

  if self.hashState:
   return 1

  self.hashState= True

  try:
   hAr= self.ar.__hash_calc()
  except AttributeError:
   hAr= hash( self.consWrapped.ar)

  try:
   hDr= self.dr.__hash_calc()
  except AttributeError:
   hDr= hash( self.consWrapped.ar)

  return hAr + (hDr << 1)

 def __hash_cleanup( self):

  if self.hashState:
   self.hashState = False

   try:
    self.ar.__hash_cleanup()
   except AttributeError:
    pass

   try:
    self.dr.__hash_cleanup()
   except AttributeError:
    pass

 def car( self, value= None): # baustelle ist diese konvention gut? entweder setzen oder holen, nie beides
  if None == value:
   return self.ar
  else:
   self.ar= value
  
 def cdr( self, value= None): # baustelle ist diese konvention gut? entweder setzen oder holen, nie beides
  if None == value:
   return self.dr
  else:
   self.dr= value

 def __eq__( self, cons): # baustelle, ggf. oberklassifizierbar, wie hash-related, nicht threadsafe

  if not isinstance( cons, Cons): 
   return False

  if id( None) == id( cons): # baustelle es wird davon ausgegangen, das self belegt ist
   return False

  ret= self.__eq_calc( cons)
  self.__eq_cleanup()
  cons.__eq_cleanup()

  return ret

 def __eq_calc( self, cons): # baustelle, ggf. oberklassifizierbar, wie hash-related, nicht threadsafe

  # if id( self)==id( cons): # erstaunlich, dass das falsch ist - mirror schlaegt hier fehl
  #  return True # a43a47b2f46344feb8098bdd2268218d

  if not isinstance( cons, Cons): 
   return False

  if self.eqState.mirrors( cons.eqState):
   if not self.eqState.isFalse(): # and not cons.eqState.isFalse()
    return True
   else:
    pass
  else:
   return False

  if id( self)==id( cons): # shortcut, ist hier folglich richtig aber auch optional: baustelle: fuer tests soll dieser teil ausschaltbar sein (m4?)
   # print 'id( self)==id( cons)'
   return True # a43a47b2f46344feb8098bdd2268218d

  self.eqState.eq_lhs= True
  cons.eqState.eq_rhs= True

  try:
   condAr= self.ar.__eq_calc( cons.ar)
  except AttributeError:
   condAr= self.consWrapped.car() == cons.consWrapped.car()

  try:
   condDr= self.dr.__eq_calc( cons.dr)
  except AttributeError:
   condDr= self.consWrapped.cdr() == cons.consWrapped.cdr()

  return condAr and condDr

 def __eq_cleanup( self):

  if not self.eqState.isFalse():
   self.eqState.__init__()

   try:
    self.ar.__eq_cleanup()
   except AttributeError:
    pass

   try:
    self.dr.__eq_cleanup()
   except AttributeError:
    pass

 def cloneDeep( self): # erzeugt nur den direkten klon des consWrapped als ConsSimple, egal, was dahintersteht # baustelle: muss auch wrapper der Cons-Abstraktion klonen koennen, also weitere cloneDeep-Funktionen - erstmal reicht aber das
  ret= self.cloneDeep_calc()
  self.cloneDeep_cleanup()
  return ret

 def cloneDeep_calc( self):

  if not None == self.cloneDeepState:
   return self.cloneDeepState

  self.cloneDeepState= ConsSimple( nil, nil) # baustelle: muss auch wrapper der Cons-Abstraktion klonen koennen

  try: # baustelle : ggf. clone() beachten
   clonedAr= self.ar.cloneDeep_calc()
  except AttributeError:
   clonedAr= self.consWrapped.car()

  try: # baustelle : ggf. clone() beachten
   clonedDr= self.dr.cloneDeep_calc()
  except AttributeError:
   clonedDr= self.consWrapped.cdr()

  self.cloneDeepState.car( clonedAr)
  self.cloneDeepState.cdr( clonedDr)

  return self.cloneDeepState

 def cloneDeep_cleanup( self):
  
  if not None == self.cloneDeepState:
   self.cloneDeepState= None

   try:
    self.cloneDeep_cleanup()
   except AttributeError:
    pass
  
 def __repr__( self): # baustelle: funktioniert nicht zyklisch
  return 'ConsTrait( %s, %s)' % ( repr( self.ar), repr( self.dr))

 def find_repetitions_parameter_template( self):
  ret= dict()
  ret[ 'ht_selfid2Name1st']= dict()
  ret[ 'ht_selfid2Name']= dict()
  ret[ 'var_prefix']= 'repr_'
  ret[ 'var_idx']= 0

  return ret

 def find_repetitions( self, parameters): # wiederholungen schliessen zyklen ein
  
  ht_selfid2Name1st= parameters[ 'ht_selfid2Name1st']
  ht_selfid2Name= parameters[ 'ht_selfid2Name']
  var_prefix= parameters[ 'var_prefix']
  var_idx= parameters[ 'var_idx']

  if ht_selfid2Name1st.has_key( id( self)):
   ht_selfid2Name[ id( self)]= ht_selfid2Name1st[ id( self)] # repetition
   return None
  else:
   ht_selfid2Name1st[ id( self)]= var_prefix + str( var_idx)
   #ht_selfid2Name[ id( self)]= ht_selfid2Name1st[ id( self)] # test
   del var_idx
   parameters[ 'var_idx']+= 1

  try:
   self.ar.find_repetitions( parameters)
  except AttributeError:
   pass

  try:
   self.dr.find_repetitions( parameters)
  except AttributeError:
   pass


 def repr_wrapped( self, ht_selfid2Name= None): 

  repr_wrapped_class_name= self.consWrapped.__class__.__name__

  registered_to_ht_selfid2Name= False

  if None == ht_selfid2Name:
   ht_selfid2Name= dict()
  elif ht_selfid2Name.has_key( id( self)):
   #return '<cycle>'
   return ht_selfid2Name[ id( self)]
  else:
   #ht_selfid2Name[ id( self)]= self
   ht_selfid2Name[ id( self)]= '<cycle>'
   registered_to_ht_selfid2Name= True


  try:
   repr_wrapped_ar= self.ar.repr_wrapped( ht_selfid2Name)
  except AttributeError:
   repr_wrapped_ar= repr( self.consWrapped.car())

  try:
   repr_wrapped_dr= self.dr.repr_wrapped( ht_selfid2Name)
  except AttributeError:
   repr_wrapped_dr= repr( self.consWrapped.cdr())

  if registered_to_ht_selfid2Name:
   del ht_selfid2Name[ id( self)]

  return '%s( %s, %s)' % ( repr_wrapped_class_name, repr_wrapped_ar, repr_wrapped_dr)

class ReprWrapped: # 3983c6dc25884e128afd14473a844527

 def repr_wrapped( self, ht_selfid2Name= None, lCpctRepr= None):
  raise IsAbstract()

class CpctReprParamListWrapper( Wrapper):
 pass

class ReprWrapper( Wrapper):
 pass

# wird es zusaetzlich erlauben, Datenstrukturen darzustellen, die keine Conses sind
class CpctRepr( ReprWrapped): # 3983c6dc25884e128afd14473a844527
 
 def __init__( self, consWrapped):
  self.consWrapped= consWrapped
  self.lParams= []

 def test( self):
  raise IsAbstract()
 
 def paramList( self): # liefert weitere darzustellende Parameter, die von ihrer Darstellung ueberschrieben werden, welche danach in self.repr_wrapped verwendet werden
  raise IsAbstract()

 def repr_wrapped( self, ht_selfid2Name= None, lCpctRepr= None):
  raise IsAbstract()

class ConsRepr( ReprWrapped):

 def __init__( self, consWrapped):
  self.consWrapped= consWrapped
 
 def find_repetitions_parameter_template( self):
  ret= dict()
  ret[ 'ht_selfid2Name1st']= dict()
  ret[ 'ht_selfid2Name']= dict()
  ret[ 'var_prefix']= 'repr_'
  ret[ 'var_idx']= 0

  return ret

 def find_repetitions( self, parameters): # wiederholungen schliessen zyklen ein
  
  ht_selfid2Name1st= parameters[ 'ht_selfid2Name1st']
  ht_selfid2Name= parameters[ 'ht_selfid2Name']
  var_prefix= parameters[ 'var_prefix']
  var_idx= parameters[ 'var_idx']

  id_self= id( self.consWrapped)

  if ht_selfid2Name1st.has_key( id_self):
   ht_selfid2Name[ id_self]= ht_selfid2Name1st[ id_self] # repetition
   return None
  else:
   ht_selfid2Name1st[ id_self]= var_prefix + str( var_idx)
   del var_idx
   parameters[ 'var_idx']+= 1

  if isinstance( self.consWrapped.car(), Cons):
   ConsRepr( self.consWrapped.car()).find_repetitions( parameters)
  else:
   pass

  if isinstance( self.consWrapped.cdr(), Cons):
   ConsRepr( self.consWrapped.cdr()).find_repetitions( parameters)
  else:
   pass

 class RecursionScheme: # baustelle: pruefen, ob ggf. als allgemeine Klasse nutzbar

  def __init__( self, consRepr, ht_selfid2Name= None, lCpctRepr= None):
   self.consRepr= consRepr
   self.ht_selfid2Name= ht_selfid2Name
   self.lCpctRepr= lCpctRepr

  def calculate( self, consWrapped= None): # parameter von ConsRepr fuer rekursion notwendig

   if None == consWrapped:
    consWrapped= self.consRepr.consWrapped

   if isinstance( consWrapped, CpctReprParamListWrapper):
    lCpctReprIdxStart= 1+ consWrapped.lCpctReprIdx # baustelle0 : ungetestet
    consWrapped= consWrapped.wrapped
   else:
    lCpctReprIdxStart= 0

   ht_selfid2Name= self.ht_selfid2Name
   lCpctRepr= self.lCpctRepr

   repr_wrapped_class_name= consWrapped.__class__.__name__
 
   registered_to_ht_selfid2Name= False
 
   id_self= id( consWrapped)
 
   if None == ht_selfid2Name:
    ht_selfid2Name= dict() # baustelle0: ggf. ineffizient 
   elif ht_selfid2Name.has_key( id_self):
    #return '<cycle>'
    return self.ht_selfid2NameRepr( ht_selfid2Name[ id_self])
   else:
    ht_selfid2Name[ id_self]= '<cycle>'
    registered_to_ht_selfid2Name= True
 
   foundIn_lCpctRepr= []
   if not None == lCpctRepr:
    i= idx= None
    #for i in lCpctRepr:
    for idx in range( lCpctReprIdxStart, len( lCpctRepr)):
     i= lCpctRepr[ idx]
     i= i( consWrapped)
     ensure( i, [CpctRepr])
     if i.test():
      foundIn_lCpctRepr.append( i)
      break # f5fbafd44f9a4a3c9f65860301b2c1c5
    lCpctReprIdx= idx
    del idx, i
 
   # if 2==len( foundIn_lCpctRepr): # f5fbafd44f9a4a3c9f65860301b2c1c5
   #  raise Exception( '2==len( foundIn_lCpctRepr)')
 
   if 1==len( foundIn_lCpctRepr):
    paramList= foundIn_lCpctRepr[ 0].paramList()
    for n in range( 0, len( paramList)):

     if isinstance( paramList[ n], CpctReprParamListWrapper):
      paramList[ n].lCpctReprIdx= lCpctReprIdx

     # 991ade2498184498ab8cdce0867ceae5
     #paramList[ n]= ConsRepr( paramList[ n]).repr_wrapped( ht_selfid2Name, lCpctRepr)
     paramList[ n]= self.calculate( paramList[ n]) 
     # /991ade2498184498ab8cdce0867ceae5

    ret= foundIn_lCpctRepr[ 0].repr_wrapped( ht_selfid2Name, lCpctRepr)
   elif not isinstance( consWrapped, Cons):
     #ret= repr( consWrapped)
     ret= self.whenUnknown( consWrapped)
   else:
 
    # 991ade2498184498ab8cdce0867ceae5
    #repr_wrapped_ar= ConsRepr( consWrapped.car()).repr_wrapped( ht_selfid2Name, lCpctRepr)
    #repr_wrapped_dr= ConsRepr( consWrapped.cdr()).repr_wrapped( ht_selfid2Name, lCpctRepr)
    repr_wrapped_ar= self.calculate( consWrapped.car())
    repr_wrapped_dr= self.calculate( consWrapped.cdr()) 
    # /991ade2498184498ab8cdce0867ceae5

    #ret= '%s( %s, %s)' % ( repr_wrapped_class_name, repr_wrapped_ar, repr_wrapped_dr)
    ret= self.returnFunction( repr_wrapped_class_name, repr_wrapped_ar, repr_wrapped_dr)
 
   if registered_to_ht_selfid2Name:
    del ht_selfid2Name[ id_self]
 
   return ret

  def returnFunction( self, *l):
   raise IsAbstract()

  def setReturnFunction( self, returnFunction):
   self.returnFunction= returnFunction

  def whenUnknown( self, *l):
   raise IsAbstract()

  def setWhenUnknown( self, whenUnknown):
   self.whenUnknown= whenUnknown

  def ht_selfid2NameRepr( self, *l):
   return IsAbstract()

  def setHT_selfid2NameRepr( self, ht_selfid2NameRepr):
   self.ht_selfid2NameRepr= ht_selfid2NameRepr

 def repr_wrapped( self, ht_selfid2Name= None, lCpctRepr= None): 

  rs= self.RecursionScheme( self, ht_selfid2Name, lCpctRepr)
  rs.setReturnFunction( (lambda consName, ar, dr: '%s( %s, %s)' % ( consName, ar, dr)))
  def tmpRepr( x):
   if isinstance( x, ReprWrapper):
    return x.wrapped
   else:
    return repr( x)
  rs.setWhenUnknown( tmpRepr)
  rs.setHT_selfid2NameRepr( (lambda x: x))
  return rs.calculate()

 def cloneDeep2( self, ht_selfid2Name= None, lCpctRepr= None): 

  # baustelle: Umgang mit Zyklen hier noch ungeklaert, da in RecursionScheme eine Ersetzung mit '<cycle>' erfolgt
  # sinnvoll erscheint hier, einen ruckgabewert anzubieten, der die cycles und repetitions enthaelt

  rs= self.RecursionScheme( self, ht_selfid2Name, lCpctRepr)
  rs.setReturnFunction( (lambda consName, ar, dr: ConsSimple( ar, dr))) # baustelle: ggf. Cons-Typ
  rs.setWhenUnknown( (lambda x: x))
  rs.setHT_selfid2NameRepr( (lambda x: ReprWrapper( x)))
  return rs.calculate()


 def cloneDeep( self, ht_selfid2Name= None, lCpctRepr= None): 

  # baustelle: Umgang mit Zyklen hier noch ungeklaert, da in RecursionScheme eine Ersetzung mit '<cycle>' erfolgt
  # sinnvoll erscheint hier, einen ruckgabewert anzubieten, der die cycles und repetitions enthaelt

  rs= self.RecursionScheme( self, ht_selfid2Name, lCpctRepr)
  rs.setReturnFunction( (lambda consName, ar, dr: ConsSimple( ar, dr))) # baustelle: ggf. Cons-Typ
  rs.setWhenUnknown( (lambda x: x))
  rs.setHT_selfid2NameRepr( (lambda x: x))
  return rs.calculate()


class ConsAbstractClassFunctions: 

 def __init__( self, ConsAbstract, ConsWrapped):
  self.ht_consWrappedId2ConsAbstract= dict()
  self.ConsAbstract= ConsAbstract
  self.ConsWrapped= ConsWrapped

 def unpack( self, obj):
  if isinstance( obj, self.ConsAbstract):
   if self.ht_consWrappedId2ConsAbstract.has_key( id( obj.consWrapped)): # 891fa253ef4846c980548ffd8710a605
    if obj != self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]:
     raise Exception( 'obj != self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]')
   else:
    self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]= obj
   return obj.consWrapped
  return obj

 def unpackDeep( self, obj, ConsWrappedType):
  if isinstance( obj, self.ConsAbstract):
   if self.ht_consWrappedId2ConsAbstract.has_key( id( obj.consWrapped)): # 891fa253ef4846c980548ffd8710a605
    if obj != self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]:
     raise Exception( 'obj != self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]')
   else:
    self.ht_consWrappedId2ConsAbstract[ id( obj.consWrapped)]= obj
   if isinstance( obj.consWrapped, ConsWrappedType):
    return obj.consWrapped
   else:
    return obj.consWrapped.cf.unpackDeep( obj.consWrapped, ConsWrappedType) # AttributeError, wenn Parameter Fehlerhaft war
  return obj

 def pack( self, obj):
  if isinstance( obj, self.ConsWrapped):
   if self.ht_consWrappedId2ConsAbstract.has_key( id( obj)): # 891fa253ef4846c980548ffd8710a605
    return self.ht_consWrappedId2ConsAbstract[ id( obj)]
   consWrapped= obj
   consAbstract= self.ConsAbstract( nil, nil, consWrapped)
   self.ht_consWrappedId2ConsAbstract[ id( consWrapped)]= consAbstract
   return consAbstract
  return obj

 def packDeep( self, obj):
  if isinstance( obj, self.ConsWrapped):
   if self.ht_consWrappedId2ConsAbstract.has_key( id( obj)): # 891fa253ef4846c980548ffd8710a605
    return self.ht_consWrappedId2ConsAbstract[ id( obj)]
   consWrapped= obj
   consAbstract= self.ConsAbstract( nil, nil, consWrapped)
   self.ht_consWrappedId2ConsAbstract[ id( consWrapped)]= consAbstract
   return consAbstract
  consWrapped= self.ConsWrapped.cf.packDeep( obj) # AttributeError, wenn Parameter Fehlerhaft war
  if self.ht_consWrappedId2ConsAbstract.has_key( id( consWrapped)): # 891fa253ef4846c980548ffd8710a605
   return self.ht_consWrappedId2ConsAbstract[ id( consWrapped)]
  consAbstract= self.ConsAbstract( nil, nil, consWrapped)
  self.ht_consWrappedId2ConsAbstract[ id( consWrapped)]= consAbstract
  return consAbstract

def makeConsAbstractSwap( ConsWrapped): # baustelle: sollte kreiert werden koennen durch:  (makeConsAbstract (cons A B) => (cons B A))

 class ConsAbstractSwap( Cons):

  def __init__( self, ar, dr, internal_pack= None):

   if None == internal_pack:
    self.consWrapped= ConsWrapped( self.cf.unpack( dr), self.cf.unpack( ar))
   else:
    self.consWrapped= internal_pack

  def car( self, value= None): 
   return self.cf.pack( self.consWrapped.cdr( self.cf.unpack( value)))
   
  def cdr( self, value= None): 
   return self.cf.pack( self.consWrapped.car( self.cf.unpack( value)))
 
 ConsAbstractSwap.cf= ConsAbstractClassFunctions( ConsAbstractSwap, ConsWrapped) # 1 mal pro Klasse ist Korrekt, auch mit der neuen hashtable, die das Vorhandensein der jeweiligen ConsAbstract (im moment noch ConsAbstractSwap ) prueft

 ConsAbstractSwap.__name__+= ' '+ str( id( ConsAbstractSwap))
 return ConsAbstractSwap

consHistory= Symbol( 'consHistory')

def makeConsAbstractCarHistory( ConsWrapped, ConsHistory): # baustelle: sollte kreiert werden koennen durch:  (makeConsAbstract (cons A B) => (cons (cons consHistory (cons A nil)) B))

 class ConsAbstractCarHistory( Cons):

  def __init__( self, ar, dr, internal_pack= None):

   if None == internal_pack:
    self.consWrapped= ConsWrapped( ConsHistory( consHistory, ConsHistory( self.cf.unpack( ar), nil)), self.cf.unpack( dr))
   else:
    self.consWrapped= internal_pack

  def car( self, value= None): 
   return self.cf.pack( self.consWrapped.car().cdr().car( self.cf.unpack( value)))
   
  def cdr( self, value= None): 
   return self.cf.pack( self.consWrapped.cdr( self.cf.unpack( value)))
 
 ConsAbstractCarHistory.cf= ConsAbstractClassFunctions( ConsAbstractCarHistory, ConsWrapped) # 1 mal pro Klasse ist Korrekt, auch mit der neuen hashtable, die das Vorhandensein der jeweiligen ConsAbstract (im moment noch ConsAbstractCarHistory ) prueft

 ConsAbstractCarHistory.__name__+= ' '+ str( id( ConsAbstractCarHistory))
 return ConsAbstractCarHistory

  
def makeConsAbstractCarAutoHistory( ConsWrapped, ConsHistory): # baustelle: sollte kreiert werden koennen durch:  (makeConsAbstract (cons A B) => (cons (cons consHistory (cons A nil)) B)) (wird schwierig wegen auto)

 class ConsAbstractCarAutoHistory( Cons):

  def __init__( self, ar, dr, internal_pack= None):

   if None == internal_pack:
    self.consWrapped= ConsWrapped( ConsHistory( consHistory, ConsHistory( self.cf.unpack( ar), nil)), self.cf.unpack( dr))
   else:
    self.consWrapped= internal_pack

  def car( self, value= None): 
   if None == value:
    #return self.cf.pack( self.consWrapped.car().cdr().car( self.cf.unpack( value)))
    return self.cf.pack( self.consWrapped.car().cdr().car())
   else:
    consWrappedCar= self.consWrapped.car()
    assert( id( consHistory) == id( consWrappedCar.car()))
    consWrappedCar.cdr( ConsHistory( self.cf.unpack( value), consWrappedCar.cdr()))
    
  def cdr( self, value= None): 
   return self.cf.pack( self.consWrapped.cdr( self.cf.unpack( value)))
 
 ConsAbstractCarAutoHistory.cf= ConsAbstractClassFunctions( ConsAbstractCarAutoHistory, ConsWrapped) # 1 mal pro Klasse ist Korrekt, auch mit der neuen hashtable, die das Vorhandensein der jeweiligen ConsAbstract (im moment noch ConsAbstractCarAutoHistory ) prueft

 ConsAbstractCarAutoHistory.__name__+= ' '+ str( id( ConsAbstractCarAutoHistory))
 return ConsAbstractCarAutoHistory

ar_assoc= Symbol( 'ar_assoc')
typeSymbol.symAdd( ar_assoc, [ar_list])

ar_assocElem= Symbol( 'ar_assocElem')
typeSymbol.symAdd( ar_assocElem, [ar_list])

not_found= Symbol( 'not_found')

def consesMake( *l):
 if 0==len( l):
  return nil
 else:
  ret= ConsSimple( l[ 0], nil)
  current= ret
  for i in l[1:]:
   current.cdr( ConsSimple( nil, nil))
   current= current.cdr()
   current.car( i)
  return ret

# baustelle, es fehlt noch CpctReprConses-Rest bzw CpctReprConsesRest
# baustelle, ungetestet, nur Handtest
def consesMakeRest( *l): 
 if 0==len( l):
  return nil
 if 1==len( l):
  return l[ 0]
 else:
  ret= ConsSimple( l[ 0], nil)
  current= ret
  for i in l[ 1: -1]:
   current.cdr( ConsSimple( nil, nil))
   current= current.cdr()
   current.car( i)
  current.cdr( l[ -1])
  return ret

def consesAdd( csConses, cs2Add): # baustelle ineffizient
 if None == csConses:
  raise Exception()
 if id( nil) == id( csConses):
  raise Exception()
 walker= csConses
 while not nil == walker.cdr(): # e81b14fbc95d425b90b9849b493c7ac9
  walker= walker.cdr()
 walker.cdr( ConsSimple( cs2Add, nil))

def listAdd( csList, cs2Add): # baustelle ineffizient
 ensureConsType( csList, ar_list) # baustelle vieleicht zu viele tests (da durch interne verwendung abgesichert)
 walker= csList
 while not nil == walker.cdr(): # e81b14fbc95d425b90b9849b493c7ac9
  walker= walker.cdr()
 walker.cdr( ConsSimple( cs2Add, nil))

def listMake( *l): # baustelle: eigentlich auslagern, zusammen mit ar_list symbol
 return ConsSimple( ar_list, consesMake( *l))

def assocMakeIntern( *l):
 return ConsSimple( ar_assoc, consesMake( *l))

def assocMake( *l):
 ret= assocMakeIntern()
 for i in l:
  assocAdd( ret, i)
 return ret

def assocElemMake( *l):
 return ConsSimple( ar_assocElem, consesMake( *l))

def assocAddIntern( csAssoc, cs2Add):
 ensureConsType( cs2Add, ar_assocElem) # baustelle vieleicht zu viele tests (da durch interne verwendung abgesichert)
 walker= csAssoc
 while not nil == walker.cdr():
  walker= walker.cdr()
  ensureConsType( walker.car(), ar_assocElem) # baustelle vieleicht zu viele tests
 walker.cdr( ConsSimple( cs2Add, nil))

def assocAdd( csAssoc, cs2Add):
 ensureConsType( csAssoc, ar_assoc)
 return assocAddIntern( csAssoc, ConsSimple( ar_assocElem, cs2Add))

def assocGet( csAssoc, fSelector):
 ensureConsType( csAssoc, ar_assoc)
 ret= assocMake()
 walker= csAssoc.cdr()
 while not nil == walker:
  ensureConsType( walker.car(), ar_assocElem) # baustelle vieleicht zu viele tests
  if fSelector( walker.car().cdr()):
   #assocAdd( ret, walker.car().cdr()) # baustelle1 : ineffizient
   assocAddIntern( ret, walker.car()) # baustelle1 : ineffizient
  walker= walker.cdr()
 return ret

def assocElemClone( csAssocElem):
 ensureConsType( csAssocElem, ar_assocElem)
 ret= ConsSimple( csAssocElem.car(), nil)
 walker= csAssocElem.cdr()
 while not nil == walker:
  listAdd( ret, walker.car()) # baustelle1 : ineffizient
  walker= walker.cdr()
 return ret

def assocClone( csAssoc):
 ensureConsType( csAssoc, ar_assoc)
 ret= ConsSimple( csAssoc.car(), nil)
 walker= csAssoc.cdr()
 while not nil == walker:
  ensureConsType( walker.car(), ar_assocElem) # baustelle vieleicht zu viele tests
  assocAddIntern( ret, assocElemClone( walker.car())) # baustelle1 : ineffizient
  walker= walker.cdr()
 return ret


def assocDel( csAssoc, fSelector):
 ensureConsType( csAssoc, ar_assoc)
 ret= assocMake()
 walker= csAssoc
 while not id( nil) == id( walker.cdr()):
  ensureConsType( walker.cdr().car(), ar_assocElem) # baustelle vieleicht zu viele tests
  if fSelector( walker.cdr().car().cdr()):
   #assocAdd( ret, walker.car().cdr()) # baustelle1 : ineffizient
   assocAddIntern( ret, walker.cdr().car()) # baustelle1 : ineffizient
   walker.cdr( walker.cdr().cdr())
   continue
  walker= walker.cdr()

 return ret

def listLen( csList):
 ensureConsType( csList, ar_list)
 ret= 0
 walker= csList
 while not nil == walker.cdr():
  ret+=1
  walker= walker.cdr()
 return ret
 
def listNth0( csList, i):
 
 ensureConsType( csList, ar_list)

 if i < 0:
  return not_found

 ensureConsType( csList, ar_list)
 
 walker= csList
 while not nil == walker.cdr():
  walker= walker.cdr()
  if 0==i:
   return walker.car()
  i-=1

 return not_found

def assocNth0( csAssoc, i):

 ret1= listNth0( csAssoc, i)
 ensureConsType( ret1, ar_assocElem)
 return ret1.cdr()

def consesNth0( csConses, i):
 
 if i < 0:
  return not_found

 walker= csConses
 while not nil == walker:
  if 0==i:
   return walker.car()
  i-=1
  walker= walker.cdr()

 return not_found

def consesConcatSymbols( csConses):
 
 ret= ''

 walker= csConses
 while not nil == walker:
  ret += walker.car()
  walker= walker.cdr()

 return Symbol( ret)

def consesDistanceSeek( csConses, distance= 0, fRest= None): # baustelle: negative zahlen fuer Distanz zum Anfang

 walker= csConses
 ret= walker

 def cndEndCdr( walkerCdr):
  return not id( nil) == id( walkerCdr)

 if None == fRest:
  fRest= cndEndCdr

 while fRest( walker.cdr()):
  walker= walker.cdr()
  if 0==distance:
   ret= ret.cdr()
  else:
   distance -= 1

 return ret

class CpctReprListGeneral(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   try:
    ensureConsType( self.consWrapped, ar_list)
    return True
   except:
    return False

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped.cdr()
   while not id( nil) == id( walker):
    self.lParams.append( walker.car())
    walker= walker.cdr()
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( not 0==len( self.lParams))
   return 'listGeneral( ' + parameterReducer( self.lParams) + ')'
 
class CpctReprAssocGeneral(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   try:
    ensureConsType( self.consWrapped, ar_assoc)
    return True
   except:
    return False

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped.cdr()
   while not id( nil) == id( walker):
    self.lParams.append( walker.car().cdr())
    walker= walker.cdr()
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( not 0==len( self.lParams))
   return 'assocGeneral( ' + parameterReducer( self.lParams) + ')'
 
class CpctReprAssocInternGeneral(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   try:
    ensureConsType( self.consWrapped, ar_assoc)
    return True
   except:
    return False

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped.cdr()
   while not id( nil) == id( walker):
    self.lParams.append( walker.car())
    walker= walker.cdr()
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( not 0==len( self.lParams))
   return 'assocInternGeneral( ' + parameterReducer( self.lParams) + ')'
 
class CpctReprAssocElemGeneral(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   try:
    ensureConsType( self.consWrapped, ar_assocElem)
    return True
   except:
    return False

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped.cdr()
   while not id( nil) == id( walker):
    self.lParams.append( walker.car())
    walker= walker.cdr()
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( not 0==len( self.lParams))
   return 'assocElemGeneral( ' + parameterReducer( self.lParams) + ')'
 
class CpctReprConses(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   try:
    ensure( self.consWrapped, [Cons])
   except:
    return False
   walker= self.consWrapped
   while isinstance( walker.cdr(), Cons): # baustelle: loopt ggf. unendlich
    walker= walker.cdr()
   return id( nil) == id( walker.cdr())

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped
   while not id( nil) == id( walker):
    self.lParams.append( walker.car())
    walker= walker.cdr()
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( not 0==len( self.lParams))
   return 'consesMake( ' + parameterReducer( self.lParams) + ')'
 
 
class CpctReprConsesRest(CpctRepr): # baustelle1 noch mehr verallgemeinerbar 8d15e25bfbc3430f83e553979868b0ec

  def test( self):
   assert( 0==len( self.lParams))
   return isinstance( self.consWrapped, Cons)

  def paramList( self):
   assert( 0==len( self.lParams))

   walker= self.consWrapped
   while isinstance( walker, Cons):
    self.lParams.append( walker.car())
    walker= walker.cdr()
   self.lParams.append( walker)
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   #assert( not 0==len( self.lParams))
   return 'consesMakeRest( ' + parameterReducer( self.lParams) + ')'

def CpctReprHTselfID2NameCreate( p_ht_selfid2Name= None, p_lCpctRepr= None): # baustelle: nicht Fehlerfrei bei zyklen / '<cycle>'

 class CpctReprHTselfID2Name(CpctRepr):
  
   def test( self):
    assert( 0==len( self.lParams))
    return True
   
   def paramList( self):
    assert( 0==len( self.lParams))
    self.lParams.append( CpctReprParamListWrapper( ConsRepr( self.consWrapped).cloneDeep2( p_ht_selfid2Name, p_lCpctRepr))) # Klonen bis an unbekannte Datenstrukturen, Aufbau, wie repr_wrapped, mit Ersetzung der Inhalte
    # print ConsRepr( self.lParams[ 0].wrapped).repr_wrapped()
    return self.lParams

   def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
    assert( 1==len( self.lParams))
    return self.lParams[ 0]
 
 return CpctReprHTselfID2Name

class Conses: # baustelle: keine zyklen

 def __init__( self):
  self.crossPointCloneHT= dict()

 def crossPointInit( self, value):
  if id( nil) == id( value):
   self.crossPointCloneHT[ id( value)]= nil
  else:
   self.crossPointCloneHT[ id( value)]= None
   

 def clone( self, conses):

  conses_id= id( conses)

  if id( nil) == conses_id:
   return nil
  
  if self.crossPointCloneHT.has_key( conses_id):
   if not id( None) == id( self.crossPointCloneHT[ conses_id]):
    return self.crossPointCloneHT[ conses_id]

  conses_car= conses.car()
  conses_car_id= id( conses_car)

  if not self.crossPointCloneHT.has_key( conses_car_id):
   conses_car_cloned= conses_car
  elif id( None) == id( self.crossPointCloneHT[ conses_car_id]):
   conses_car_cloned= self.clone( conses_car)
   self.crossPointCloneHT[ conses_car_id]= conses_car_cloned
  else:
   conses_car_cloned= self.crossPointCloneHT[ conses_car_id]

  ret= ConsSimple( conses_car_cloned, self.clone( conses.cdr()))

  if self.crossPointCloneHT.has_key( conses_id):
   self.crossPointCloneHT[ conses_id]= ret

  return ret
  
  

