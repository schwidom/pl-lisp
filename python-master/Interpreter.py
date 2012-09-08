#from Cons import Cons
from tools import ensure
from ConsTrait import ConsTrait, Cons, ConsSimple, makeConsTrait, ConsAbstractClassFunctions, makeConsAbstractSwap, makeConsAbstractCarHistory, consHistory, makeConsAbstractCarAutoHistory
from symbols import Symbol, nil, ar_list, noo, typeSymbol, typeSymbolNot, typeSymbolChk 
from ConsTrait import ConsRepr
from tools import uNames, usRename
from ConsTrait import ar_assoc, assocMake, consesMake
from symbols import doSubConsType
from ConsTrait import CpctRepr
from ConsTrait import listLen, assocGet, listNth0, assocNth0, consesNth0
from symbols import ensureConsType
from ConsTrait import assocAdd
from ConsTrait import CpctReprListGeneral, assocClone, CpctReprConses
from symbols import true
from EssentialsContainer import EssentialsContainer
from ExecuteObject import ExecuteObject
from executeObjects.Function import Function
from executeObjects.Quotation import Quotation
from executeObjects.Macro import Macro
from CpctReprCodeListConfigMake import CpctReprCodeListConfigMake
from InterpreterSymbols import ar_codeList, ar_codeListConfig
from InterpreterSymbols import s_environment, s_macroLevel, s_environment_quotationMode
from InterpreterStructures import codeListConfigGet, codeListConfigSet, codeListConfigClone
from Environment import Environment
from InterpreterSymbols import ar_codeListParameters
from InterpreterStructures import codeListCheck, codeListEnsure, codeListConfigMake
from InterpreterStructures import codeListMake, codeListParametersMake
from InterpreterStructures import codeListGetParameterValuesCdrContainer
from InterpreterStructures import codeListGetParameterValuesCdrContainer2
from InterpreterStructures import codeListGetParameterValues
from InterpreterStructures import codeListParametersEnsure, codeListParametersGetParameterValues
from InterpreterSymbols import ar_retList, ar_retValue
from symbols import ar_value
from InterpreterSymbols import ar_retValueFromMacro
from ConsTrait import consesDistanceSeek
from InterpreterSymbolTable import InterpreterSymbolTable # htInterpreterSymbolTable, htInterpreterSymbolTableNames
from InterpreterStructures import codeListGetParameters
from symbols import whitespace

from debugVariables import uNooProblem, nooProblem

class ExceptionQuit( Exception):

 def __init__( self, msg):
  Exception.__init__( self, msg)

class Essentials: # siehe 8c231655685648cc99e5b0bf3b0b8687

 def ess_print( self, *l):
  print reduce( (lambda x, y: x + ' '+ y), map( str, l), '')

ConsAbstractCarAutoHistoryCSCS= makeConsAbstractCarAutoHistory( ConsSimple, ConsSimple)

class Interpreter:

 def __init__( self):

  self.debug= False

  selfInterpreter= self

  self.readbuf= ConsSimple( nil, nil)
  self.macroBuf= nil
  self.env_globals= Environment()
  env_locals= self.env_globals.newChild()
  self.env_quotationMode_globals= Environment()
  env_quotationMode_locals= self.env_quotationMode_globals.newChild()

  codeListConfig= codeListConfigMake( env_locals, False, env_quotationMode_locals) # 27f019a4b85c45ec9dbab2a59306eccc
  self.codeList= codeListMake( codeListConfig, codeListParametersMake( nil)) # ehemals 76ff812ddb0f47f5be9ca34925a4a3b6
  del codeListConfig

  codeListGetParameters( self.codeList).cdr( ConsSimple( Symbol( 'progn-root'), nil))
  self.codeListCurrentEvalTokenList= codeListGetParameterValuesCdrContainer2( self.codeList).cdr()

  self.codeListParent2EvalToken= nil

  self.codeCurrentLeafList= ConsSimple( self.codeList, nil) # 2bb546ca3ffd48bc851d17494f5c286f

  codeListEnsure( self.codeList)

  assert( ar_codeListConfig==self.getCurrentCodeListConfig().car())
  self.codeLeafBackTree= ConsSimple( self.codeCurrentLeafList, nil) # 2bb546ca3ffd48bc851d17494f5c286f

  self.codeLevel= 0

  self.essentials_macro_function= Essentials()
  
  #for i in ( pl_q1, pl_q2, pl_ql, pl_pyprint, pl_pyprintconses, pl_pyprintconsesRest, pl_pyprintStack, pl_eval, pl_qswap2):
  # i.setEssentials( self.essentials_macro_function)

 
  self.interpreterSymbolTable= InterpreterSymbolTable( self)
  ist= self.interpreterSymbolTable

  for k in 'pyprint pyprintconses pyprintconsesRest pyprintStack pyprintStack2 pyprintStackShort'.split():
   ist.htInterpreterSymbolTableNames[ k].setEssentials( self.essentials_macro_function)
  del k

  for k in ist.htInterpreterSymbolTable:
   v= ist.htInterpreterSymbolTable[ k]
   self.env_globals.set( k, v)
  del k, v
  
  del ist

 def getCurrentLeaf( self):
  return self.codeCurrentLeafList.car()

 def getCurrentCodeListConfig( self, currentLeaf= None): # baustelle1 : name seit Parameter currentLeaf unpassend, 96c8d565e4f946c38838d30756ce5c0d
  if id( None) == id( currentLeaf):
   currentLeaf= self.getCurrentLeaf()
  assert( id( ar_codeList)== id( currentLeaf.car()))
  return currentLeaf.cdr().car()

 def getEnvLocals( self):
  return codeListConfigGet( self.getCurrentCodeListConfig(), s_environment)

 def getEnvQuotationModeLocals( self):
  return codeListConfigGet( self.getCurrentCodeListConfig(), s_environment_quotationMode)

 def quotationModeIsActivated( self):
  return codeListConfigGet( self.getCurrentCodeListConfig(), s_macroLevel) # b391d502688f40e38126ac0f8881e895, cf83b621ff51441298093b7e55dcfc1a

 def quotationModeActivate( self):
  codeListConfig= self.getCurrentCodeListConfig() # baustelle weiter optimierbar
  assert( False == codeListConfigGet( codeListConfig, s_macroLevel)) # cf83b621ff51441298093b7e55dcfc1a
  codeListConfigSet( codeListConfig, s_macroLevel, True) # cf83b621ff51441298093b7e55dcfc1a

 def quotationModeDeActivate( self, codeListConfig= None): # 96c8d565e4f946c38838d30756ce5c0d
  if id( None) == id( codeListConfig):
   codeListConfig= self.getCurrentCodeListConfig() # baustelle weiter optimierbar
  assert( True == codeListConfigGet( codeListConfig, s_macroLevel)) # cf83b621ff51441298093b7e55dcfc1a
  codeListConfigSet( codeListConfig, s_macroLevel, False) # cf83b621ff51441298093b7e55dcfc1a

 def currentEvalTokenIsInExecutePosition( self):
  if nil == self.codeListParent2EvalToken:
   return False
  codeList= self.codeListParent2EvalToken.car().cdr().car()
  codeListEnsure( codeList)
  return id( codeListGetParameterValues( codeList)) == id( self.codeListCurrentEvalTokenList.cdr()) # ehemals 76ff812ddb0f47f5be9ca34925a4a3b6

 def readTokenRawInput( self):
  return raw_input()

 readTokenNothingFound= Symbol( 'readTokenNothingFound')

 def readToken( self):

  ret= self.readTokenNothingFound

  if id( nil)==id( self.readbuf.cdr()):
   rodString= self.readTokenRawInput()
   
   walkerCdr= self.readbuf
   for i in range( 0, len( rodString)):
    walkerCdr.cdr( ConsSimple( Symbol( rodString[ i]), nil))
    walkerCdr= walkerCdr.cdr()

   del walkerCdr
   del rodString

  while not id( nil) == id( self.readbuf.cdr()) and self.readbuf.cdr().car() in whitespace: # cb0b78e10b2642518a4be06499144918 
   self.readbuf= self.readbuf.cdr()

  if not id( nil) == id( self.readbuf.cdr()):
   if self.readbuf.cdr().car() in [ Symbol( '('), Symbol( ')')]: # d5f0b2975f864ba1823b3e2774699cc8
    ret= self.readbuf.cdr().car()
    self.readbuf= self.readbuf.cdr()
   else:
    ret = self.readbuf.cdr().car()
    self.readbuf= self.readbuf.cdr() # 14be901c62904a49970db50824f11287 
    while not id( nil) == id( self.readbuf.cdr()) and not self.readbuf.cdr().car() in whitespace and not self.readbuf.cdr().car() in [ Symbol( '('), Symbol( ')')]: # cb0b78e10b2642518a4be06499144918, d5f0b2975f864ba1823b3e2774699cc8
     ret = Symbol( ret+ self.readbuf.cdr().car()) # baustelle: Hack, derzeit keine + ueberladung fuer Symbol
     self.readbuf= self.readbuf.cdr() # 14be901c62904a49970db50824f11287 

  #if not id( self.readTokenNothingFound) == id( ret):
   # ret= Symbol( ret) # 59cc177458e34abcb943fd4351d93149
  return ret

 def evalToken( self, rodTyped, evalMode= False): # evalMode=True wird bei '(' nur zu beginn gesetzt, ob evaluiert wird, wird von aussen festgelegt

  rodType= rodTyped.car()
  rod= rodTyped.cdr()

  if id( rodType) not in [ id( ar_value), id( ar_retValue), id( ar_retList)]:
   print ConsRepr( rodTyped).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
   raise Exception()

  if False: # 8337c49584d44686be0bc780cf310dfc
   pass
  elif '(' == rod:
   self.codeLevel+=1
   codeListConfigCloned= codeListConfigClone( self.getCurrentCodeListConfig())
   elem= codeListMake( codeListConfigCloned, codeListParametersMake( nil)) # ehemals 76ff812ddb0f47f5be9ca34925a4a3b6
   self.codeCurrentLeafList= ConsSimple( elem, self.codeCurrentLeafList) # 2bb546ca3ffd48bc851d17494f5c286f
   self.codeLeafBackTree.car( self.codeCurrentLeafList) # 2bb546ca3ffd48bc851d17494f5c286f

   del codeListConfigCloned

   if True == evalMode: # 672b8ecafdae4e218d2268543f27119a
    elemNew= self.codeListCurrentEvalTokenList.cdr()
    elemNew.car( elem)
    elemCurrent= self.codeListCurrentEvalTokenList
   else:
    elemNew= ConsSimple( elem, nil)
    elemCurrent= consesDistanceSeek( self.codeListCurrentEvalTokenList)
    assert( not id( nil) == id( elemCurrent))
    elemCurrent.cdr( elemNew)
   ( elemPrevious, elemCurrent, elemNew, elemParent) = ( elemCurrent, 
     codeListGetParameterValuesCdrContainer( elem) # ehemals 76ff812ddb0f47f5be9ca34925a4a3b6
    , None, elemNew)

   self.codeListParent2EvalToken= ConsSimple( elemPrevious, self.codeListParent2EvalToken)
   self.codeListCurrentEvalTokenList= codeListGetParameterValuesCdrContainer2( elem) # ist das wirklich notwendig? zumindest liefert der Check keinen Fehler (also ist es wenigstens korrekt)

  elif ')' == rod:
   self.codeLevel-=1
   if nil == self.codeListParent2EvalToken:
    raise Exception( 'kann keine klammer mehr schliessen')
   elemParent2= self.codeListParent2EvalToken.car()
   self.codeListParent2EvalToken= self.codeListParent2EvalToken.cdr()
   ( elemCurrent2, elemParent)= ( elemParent2, None)
   self.codeListCurrentEvalTokenList= elemCurrent2
   self.codeCurrentLeafList= self.codeCurrentLeafList.cdr() # 2bb546ca3ffd48bc851d17494f5c286f baustelle: die und die folgende Zeile sind ohne Testfehler austauschbar, pruefen
   self.codeLeafBackTree= ConsSimple( self.codeCurrentLeafList, self.codeLeafBackTree) # 2bb546ca3ffd48bc851d17494f5c286f
  else: # not rod in [ '(', ')']
   elem= rod # 59cc177458e34abcb943fd4351d93149
   if True == evalMode: # 672b8ecafdae4e218d2268543f27119a
    elemNew= self.codeListCurrentEvalTokenList # 7171a8bd3cd641babf4ebcca7394f4c6
    if id( ar_retList) == id( rodType): # 7978cb4bee364b3a8359e2a0f8b7f1f4
     # baustelle0: isinstance( elem, Cons) kann raus, sobald ar_retValue implementiert ist

     wrappedValues= elem

     elemNew.cdr( wrappedValues) # 7171a8bd3cd641babf4ebcca7394f4c6, ehemals 36268f550bcf4fb88d25868f8ea663bf hack

     self.codeListCurrentEvalTokenList= consesDistanceSeek( elemNew, 1, (lambda walker : isinstance( walker, Cons))) # 7171a8bd3cd641babf4ebcca7394f4c6, 80d1ab47171e42ba9bac8c8409b87bee
     #self.codeListCurrentEvalTokenList= consesDistanceSeek( elemNew, 1) # 7171a8bd3cd641babf4ebcca7394f4c6
    elif id( ar_retValue) == id( rodType): # 7978cb4bee364b3a8359e2a0f8b7f1f4
     # baustelle0: isinstance( elem, Cons) kann raus, sobald die restlichen ar_ Symbole implementiert sind
     elemNew.cdr().car( elem)
    elif id( ar_value) == id( rodType): # 7978cb4bee364b3a8359e2a0f8b7f1f4
     # baustelle0: isinstance( elem, Cons) kann raus, sobald die restlichen ar_ Symbole implementiert sind
     elemNew.cdr().car( elem)
    else:
     raise Exception( ConsRepr( rodTyped).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses]))
   else: # False == evalMode
    elemNew= ConsSimple( elem, nil)
    elemCurrent= consesDistanceSeek( self.codeListCurrentEvalTokenList)
    elemCurrent.cdr( elemNew)
    ( elemPrevious, elemCurrent, elemNew) = ( elemCurrent, elemNew, None)
    self.codeListCurrentEvalTokenList= elemPrevious # baustelle ggf. wieder rauswerfen

  return rod
 
 def s_print( self, evol):
  print "out: ", evol

 def macroBufAdd( self, isQuotation, symbol):
  assert( not id( ar_codeListParameters) == id( symbol))
  self.macroBuf= ConsSimple( ConsSimple( isQuotation, symbol), self.macroBuf)

 def macroBufFeed( self, l, outer= True): 

  ensure( l, [Cons])

  if outer:
   if isinstance( l.cdr(), Cons):
    if isinstance( l.cdr().car(), Cons):
     ensureConsType( l.cdr().car(), ar_codeList) # baustelle: ggf. uebertestet
     ensureConsType( l.cdr().car().cdr().car(), ar_codeListConfig) # baustelle: ggf. uebertestet
     pass

  uNames.next( usRename( ConsSimple, 'cs'))
  uNames.next( usRename( Symbol, 's'))

  c= l
  r= nil # reverse

  while not id( nil) == id( c):
   r= ConsSimple( c.car(), r)
   c= c.cdr()

  self.macroBufAdd( False, Symbol( ')'))

  while not id( nil) == id( r):
   value= r.car()
   if isinstance( value, Cons) and typeSymbolChk( value.car(), ar_codeList): # f69eef8ad76e459da16194dcdd0c73c6
    codeListEnsure( value) # b73fcfe5b4de4df6946ee586d8f79713
    self.macroBufFeed( codeListGetParameterValues( value), outer= False) # 2849da4969b146bc88315f20fd205e06 baustelle0: hier wird das Environment verworfen
   else: 
    self.macroBufAdd( False, value)
   r= r.cdr()

  self.macroBufAdd( outer, Symbol( '(')) # 64005373aae94f3a9314d303d5f4016e

  uNames.undo()
  uNames.undo()

 def macroBufFeed_v2( self, l): # macroBufFeed
  if isinstance( l, Cons) and typeSymbolChk( l.car(), ar_codeList): # f69eef8ad76e459da16194dcdd0c73c6
   codeListEnsure( l) # b73fcfe5b4de4df6946ee586d8f79713
   return self.macroBufFeed( codeListGetParameterValues( l)) # 2849da4969b146bc88315f20fd205e06 baustelle0: hier wird das Environment verworfen
  else:
   return self.macroBufAdd( True, l)

 def macroBufRepr( self):
  
  ret= ""

  c= self.macroBuf

  while not id( nil) == id( c):
   ret += ' '+ str( c.car().cdr())
   c= c.cdr()

  return ret

 def evalStep( self, rod):

  if False: # 8337c49584d44686be0bc780cf310dfc
   pass
  elif '(' == rod:
   evol= '('
  elif ')' == rod:
   codeList= self.codeListCurrentEvalTokenList.cdr().car()
   codeListEnsure( codeList)
   codeListTmp= codeListGetParameterValues( codeList)
   executeObject= codeListTmp.car()
   executeParameters= codeListParametersMake( codeListTmp.cdr())

   if id( ar_codeList)== id( executeObject): # baustelle1 : harte fehlerausgabe
    print "self.codeListCurrentEvalTokenList ", ConsRepr( self.codeListCurrentEvalTokenList).repr_wrapped()
    raise Exception( "")

   del codeListTmp

   evol= ')'

   if not self.quotationModeIsActivated():

    codeList= self.codeCurrentLeafList.car()
    assert( id( ar_codeList)== id( codeList.car()))
    codeListConfig= codeList.cdr().car()
    assert( id( ar_codeListConfig)== id( codeListConfig.car()))
    del codeListConfig
    del codeList

    env_locals= self.getEnvLocals()
    if False: # 34c428c5375b49df9b919c610a5a9ce6
     pass
    elif isinstance( executeObject, Macro):
     executeObject.setEnvironment( env_locals)
     executeObject.setParameters( executeParameters)
     execote= executeObject.execute()

     cs= ConsSimple
    
     def tmp0( rest): # c3ee5239baaf4484a61bd525f589ef76
      return codeListMake( codeListConfigMake( env_locals), codeListParametersMake( rest))

     assert( id( ar_retValueFromMacro) == id( execote.car())) # baustelle: ggf. auch ar_retListFromMacro, loesung von 8357c3268e594c2f92afaa3a3af12afb

     execote= execote.cdr()

     self.macroBufFeed_v2( tmp0( consesMake( Symbol( 'eval1'), execote)))

    elif isinstance( executeObject, Quotation):
     executeObject.setEnvironment( env_locals)
     executeObject.setParameters( executeParameters) # 0bea40a420ca4ffa9140051cf20b778f
     execote= executeObject.execute()
     self.evalToken( execote, True)
    elif isinstance( executeObject, Function):
     executeObject.setEnvironment( env_locals) # 0bea40a420ca4ffa9140051cf20b778f
     executeObject.setParameters( executeParameters)
     execote= executeObject.execute()
     #print ConsRepr( execote).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
     self.evalToken( execote, True)
    else:
     print "typ nicht erwartet %s " % executeObject
     raise Exception( "") # baustelle1 ersetzt erstmal richtige Fehlermeldung

   else: # self.quotationModeIsActivated() 8191d96c8d9c4e31b9726088c66c7d67
    pass
    # baustelle0: executeObject ist von der semantischen Bedeutung her doppelt belegt

  else: # not rod in [ '(', ')']

   if not self.quotationModeIsActivated():
    
    if noo == rod: # baustelle0 : so nicht - 

     if None==self.codeListCurrentEvalTokenList:
      raise Exception()
     self.codeListCurrentEvalTokenList.cdr( nil)

    else:
     env_locals= self.getEnvLocals()
     if env_locals.has_key( rod):
      got= env_locals.get( rod) # baustelle1: noch zu unterscheiden: Value oder Symbol-Macro / Quotation
      self.evalToken( ConsSimple( ar_value, got), True) # baustelle1: in Funktion X001 auslagern, auch fuer den Listen-Fall | rod kann im aktuellen fall sogar eine Liste enthalten, die nicht in Einzelteilen an evalToken gefuettert werden muss, 7978cb4bee364b3a8359e2a0f8b7f1f4
      if self.currentEvalTokenIsInExecutePosition():
       if isinstance( got, Quotation) or isinstance( got, Macro): # 34c428c5375b49df9b919c610a5a9ce6
        self.quotationModeActivate()
     else:
      print "not found %s" % ConsRepr( rod).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
      raise Exception()
       
   else: # self.quotationModeIsActivated() 8191d96c8d9c4e31b9726088c66c7d67

    """ behandlung bezueglich uqset1 """
    if self.getEnvQuotationModeLocals().has_key( rod): # baustelle0 executeObject fuer diesen Fall umbenennen
     self.quotationModeDeActivate()
     env_quotationMode_locals= self.getEnvQuotationModeLocals().get( rod)
     del rod
     if self.currentEvalTokenIsInExecutePosition():
      self.codeListCurrentEvalTokenList.cdr().car( self.getEnvLocals().get( Symbol( 'progn'))) # ddfdc08cdef344b7bcd44d4e093d12ab, erweiterbar, siehe ideen.txt, 96c8d565e4f946c38838d30756ce5c0d
      parentCodeListConfig= self.getCurrentCodeListConfig( self.codeCurrentLeafList.cdr().car())
      self.quotationModeDeActivate( parentCodeListConfig)
     else:
      self.codeListCurrentEvalTokenList.cdr().car( nil) # ddfdc08cdef344b7bcd44d4e093d12ab, erweiterbar, siehe ideen.txt
     codeListConfig= self.getCurrentCodeListConfig()
     codeListConfigSet( codeListConfig, s_environment, env_quotationMode_locals)
     del env_quotationMode_locals
     del codeListConfig

    pass

   #evol= self.codeListCurrentEvalTokenList.cdr().car()
   evol= None # momentan bedeutungslos

  return evol

 def replStep( self):
  
  if not nil == self.macroBuf:
   macroBufElem= self.macroBuf.car()
   isQuotation= macroBufElem.car()
   rod= macroBufElem.cdr()
   del macroBufElem
   self.macroBuf= self.macroBuf.cdr()
  else:
   rod=self.readToken() # 59cc177458e34abcb943fd4351d93149
   isQuotation= False # entspricht der Abarbeitung der Quotation ( True p1 False p2 False ... ) False

  if not id( self.readTokenNothingFound) == id( rod):
   self.evalToken( ConsSimple( ar_value, rod), isQuotation) # evol == rod (aktuell, wird auch bis auf weiteres so bleiben), 7978cb4bee364b3a8359e2a0f8b7f1f4

   evol= self.evalStep( rod)

   self.s_print( evol)

 def repl( self):

  try:
   while True:
    self.replStep()
  except ExceptionQuit:
   pass

