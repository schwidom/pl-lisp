from symbols import Symbol, typeSymbol, ar_list, doSubConsType
from ConsTrait import ar_assoc, assocMake, assocAdd, consesMake
from symbols import ensureConsType
from ConsTrait import assocGet, listLen, consesNth0, assocNth0, assocClone
from ConsTrait import Cons, ConsRepr
from CpctReprCodeListConfigMake import CpctReprCodeListConfigMake
from InterpreterSymbols import ar_codeList, ar_codeListConfig, ar_codeListParameters
from InterpreterSymbols import s_environment, s_macroLevel, s_environment_quotationMode
from ConsTrait import CpctReprConses, consesMakeRest, ConsSimple
from symbols import nil
from InterpreterSymbols import ar_stack
from symbols import true
from ConsTrait import CpctRepr
from CpctReprCodeListConfigMake import CpctReprCodeListConfigMake
from ConsTrait import CpctReprConsesRest
from ConsTrait import CpctReprHTselfID2NameCreate
from ConsTrait import consesDistanceSeek
from ConsTrait import Conses

alteVariante= False # alteVariante= True : ohne ar_codeListParameters

def codeListParametersMake( codeListParametersValues):
 if alteVariante:
  return codeListParametersValues
 else:
  return ConsSimple( ar_codeListParameters, codeListParametersValues)

def codeListParametersCheck( codeListParameters):
 if alteVariante:
  if id( nil) == id( codeListParameters): return True
  if isinstance( codeListParameters, Cons): return True 
 else:
  if not isinstance( codeListParameters, Cons): return False
  if not id( ar_codeListParameters) == id( codeListParameters.car()): return False

 return True

def codeListParametersGetParameterValues( codeListParameters):
 if alteVariante:
  return codeListParameters
 else:
  return codeListParameters.cdr()


def codeListParametersEnsure( codeListParameters):
 if not codeListParametersCheck( codeListParameters):
  print 'codeListParametersEnsure', ConsRepr( codeListParameters).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
  raise Exception()

def codeListMake( codeListConfig, codeListParameters= nil):
 ret= consesMakeRest( ar_codeList, codeListConfig, codeListParameters)
 codeListEnsure( ret) # baustelle kann wieder raus
 return ret
 
def codeListGetConfig( codeList):
 return codeList.cdr().car()

def codeListGetParameters( codeList):
 return codeList.cdr().cdr()

def codeListGetParameterValues( codeList):
 if alteVariante:
  return codeListGetParameters( codeList)
 else:
  return codeListGetParameters( codeList).cdr()

def codeListGetParameterValuesCdrContainer( codeList): # fuer ar_codeListParameters umstellung notwendig
 if alteVariante:
  return codeList.cdr()
 else:
  return codeList.cdr().cdr()

def codeListGetParameterValuesCdrContainer2( codeList): # fuer ar_codeListParameters umstellung notwendig
 if alteVariante:
  return codeList
 else:
  return codeList.cdr()

def codeListCheck( codeList):

 if not isinstance( codeList, Cons): return False
 if not id( ar_codeList) == id( codeList.car()): return False

 codeListConfigAtAr= codeList.cdr()

 if not isinstance( codeListConfigAtAr, Cons): return False
 
 codeListConfig= codeListConfigAtAr.car()

 if not isinstance( codeListConfig, Cons): return False
 if not id( ar_codeListConfig) == id( codeListConfig.car()): return False

 codeListParameters= codeListConfigAtAr.cdr()

 if not codeListParametersCheck( codeListParameters): return False

 return True

def codeListEnsure( codeList): # baustelle: wenn eine Exception geworfen wird, ist der genaue Grund unklar
 
 if not codeListCheck( codeList):
  print 'codeListEnsure', ConsRepr( codeList).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
  raise Exception()

def codeListConfigMake( environment= None, quotationMode= None, environment_quotationMode= None): # 27f019a4b85c45ec9dbab2a59306eccc
 #ret= assocMake( consesMake( s_environment, environment))
 ret= assocMake()
 if not None== environment:
  assocAdd( ret, consesMake( s_environment, environment))
 if not None== quotationMode:
  assocAdd( ret, consesMake( s_macroLevel, quotationMode))
 if not None== environment_quotationMode:
  assocAdd( ret, consesMake( s_environment_quotationMode, environment_quotationMode))
 doSubConsType( ret, ar_codeListConfig)
 return ret

def codeListConfigGet( codeListConfig, key):
 ensureConsType( codeListConfig, ar_codeListConfig)
 codeListConfigEnvironment= assocGet( codeListConfig, (lambda x: x.car()==key))
 if 0==listLen( codeListConfigEnvironment):
  assert( False) # test-hook
  codeListConfigSet( codeListConfigSet, key, None) # baustelle: ungetestet
  codeListConfigEnvironment= assocGet( codeListConfig, (lambda x: x.car()==key))
 assert( 1==listLen( codeListConfigEnvironment))
 return consesNth0( assocNth0( codeListConfigEnvironment, 0), 1)

def codeListConfigSet( codeListConfig, key, value):
 ensureConsType( codeListConfig, ar_codeListConfig)
 codeListConfigEnvironment= assocGet( codeListConfig, (lambda x: x.car()==key))
 assert( 1==listLen( codeListConfigEnvironment))
 assocNth0( codeListConfigEnvironment, 0).cdr().car( value)

def codeListConfigClone( codeListConfig):
 return assocClone( codeListConfig)

def codeListConfigCheck( codeListConfig):
 if not isinstance( codeListConfig, Cons): return False
 if not id( ar_codeListConfig) == id( codeListConfig.car()): return False

 return True

def stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, codeCurrentLeafList, macroBuf, readbuf, codeLevel, codeList):
 return consesMake( ar_stack, codeListCurrentEvalTokenList, codeListParent2EvalToken, codeCurrentLeafList, macroBuf, readbuf, codeLevel, codeList)

def stackMakeFromInterpreter( interpreter):
 i= interpreter
 return stackMake( i.codeListCurrentEvalTokenList, i.codeListParent2EvalToken, i.codeCurrentLeafList, i.macroBuf, i.readbuf, i.codeLevel, i.codeList)
 
def stackApply2( interpreter, stack):

 # ensureConsType( stack, ar_stack)

 if not ( isinstance( stack, Cons) and id( ar_stack) == id( stack.car())): # baustelle0: besser typeSymbolChk
  return stack

 i= interpreter
 walker= stack.cdr()
 i.codeListCurrentEvalTokenList= walker.car(); walker= walker.cdr()
 i.codeListParent2EvalToken= walker.car(); walker= walker.cdr()
 i.codeCurrentLeafList= walker.car(); walker= walker.cdr()
 i.macroBuf= walker.car(); walker= walker.cdr()
 i.readbuf= walker.car(); walker= walker.cdr()
 i.codeLevel= walker.car(); walker= walker.cdr()
 i.codeList= walker.car(); walker= walker.cdr()


 assert( id(nil)==id(walker))
 del walker
 

def stackClone4Try1( stack):

 # ensureConsType( stack, ar_stack)

 if not ( isinstance( stack, Cons) and id( ar_stack) == id( stack.car())): # baustelle0: besser typeSymbolChk
  return stack

 walker= stack.cdr()
 codeListCurrentEvalTokenList= walker.car(); walker= walker.cdr()
 codeListParent2EvalToken= walker.car(); walker= walker.cdr()
 codeCurrentLeafList= walker.car(); walker= walker.cdr()
 macroBuf= walker.car(); walker= walker.cdr()
 readbuf= walker.car(); walker= walker.cdr()
 codeLevel= walker.car(); walker= walker.cdr()
 codeList= walker.car(); walker= walker.cdr()

 assert( id(nil)==id(walker))
 del walker

 codeListParent2EvalTokenComplete= ConsSimple( stackGetCodeListCurrentEvalTokenList( stack), # e584963f104a4fb19b326b4ddd2721d6
  stackGetCodeListParent2EvalToken( stack))

 conses= Conses()

 conses.crossPointInit( codeList) # muesste eigentlich in codeCurrentLeafList enthalten sein

 walkerLeafList= codeCurrentLeafList
 walkerCurrentToken= codeListParent2EvalTokenComplete

 while not id( nil) == id( walkerLeafList):
  conses.crossPointInit( walkerLeafList.car())
  walkerLeafList= walkerLeafList.cdr()

 while not id( nil) == id( walkerCurrentToken):
  walkerCurrentToken_car= walkerCurrentToken.car()
  conses.crossPointInit( walkerCurrentToken_car)
  walkerCurrentToken= walkerCurrentToken.cdr()


 codeListParent2EvalTokenComplete2= conses.clone( codeListParent2EvalTokenComplete)
 codeCurrentLeafList2= conses.clone( codeCurrentLeafList)
 codeList2= conses.clone( codeList) # baustelle ungetestet

 codeListCurrentEvalTokenList2= codeListParent2EvalTokenComplete2.car()
 codeListParent2EvalToken2= codeListParent2EvalTokenComplete2.cdr()

 return stackMake( codeListCurrentEvalTokenList2, codeListParent2EvalToken2, codeCurrentLeafList2, macroBuf, readbuf, codeLevel, codeList2)
 

def stackGetCodeListCurrentEvalTokenList( stack):
 ensureConsType( stack, ar_stack)
 return stack.cdr().car()

def stackGetCodeListParent2EvalToken( stack):
 ensureConsType( stack, ar_stack)
 return stack.cdr().cdr().car()

def stackGetCodeCurrentLeafList( stack):
 ensureConsType( stack, ar_stack)
 return stack.cdr().cdr().cdr().car()

class CpctReprStack(CpctRepr): 

  def test( self):
   assert( 0==len( self.lParams))
   return isinstance( self.consWrapped, Cons) and id( ar_stack) == id( self.consWrapped.car())

  def paramList( self):
   assert( 0==len( self.lParams))
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( 0==len( self.lParams))

   stack= self.consWrapped
   ht= dict()

   walker= ConsSimple( stackGetCodeListCurrentEvalTokenList( stack), # e584963f104a4fb19b326b4ddd2721d6
    stackGetCodeListParent2EvalToken( stack))

   xNr= 0
   while not id( nil) == id( walker):
    walker_car= walker.car()
    ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'sclp2et_'+ str( xNr- 1))).repr_wrapped() # baustelle: hack 53de4cb72e4647409c28cab4b29a5f92
    #ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'consesNth0( stackGetCodeListParent2EvalToken, '+ str( xNr- 1)+ ')')).repr_wrapped() # baustelle: hack
    walker= walker.cdr()
    xNr += 1

   ht[ id( stack)] = 'stack'

   codeCurrentLeafListRepr= ConsRepr( stackGetCodeCurrentLeafList( self.consWrapped)).repr_wrapped( None, [CpctReprCodeListConfigMake, CpctReprHTselfID2NameCreate( ht), CpctReprConsesRest]) # 28ddde667ab3463080f3b16faa5a48b3 baustelle 

   return 'stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, ' + codeCurrentLeafListRepr + ')'
 
 
class CpctReprStack2(CpctRepr): # aus CpctReprStack

  def test( self):
   assert( 0==len( self.lParams))
   return isinstance( self.consWrapped, Cons) and id( ar_stack) == id( self.consWrapped.car())

  def paramList( self):
   assert( 0==len( self.lParams))
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( 0==len( self.lParams))

   stack= self.consWrapped
   ht= dict()

   ht[ id( stack)] = 'stack'

   walker= ConsSimple( stackGetCodeListCurrentEvalTokenList( stack), # e584963f104a4fb19b326b4ddd2721d6
    stackGetCodeListParent2EvalToken( stack))

   xNr= 0
   while not id( nil) == id( walker): # e584963f104a4fb19b326b4ddd2721d6
    walker_car= walker.car()
    ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'sclp2et_'+ str( xNr- 1))).repr_wrapped() # baustelle: hack 53de4cb72e4647409c28cab4b29a5f92
    #ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'consesNth0( stackGetCodeListParent2EvalToken, '+ str( xNr- 1)+ ')')).repr_wrapped() # baustelle: hack
    walker= walker.cdr()
    xNr += 1

   codeCurrentLeafList= stackGetCodeCurrentLeafList( self.consWrapped)
   
   ht[ id( consesDistanceSeek( codeCurrentLeafList))] = 'codeList' # sollte i.codeList entsprechen

   codeCurrentLeafListRepr= ConsRepr( codeCurrentLeafList).repr_wrapped( None, [CpctReprCodeListConfigMake, CpctReprHTselfID2NameCreate( ht), CpctReprConsesRest]) # 28ddde667ab3463080f3b16faa5a48b3 baustelle 

   return 'stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, ' + codeCurrentLeafListRepr + ')'
 
class CpctReprCodeListShort4Stack( CpctRepr): 

 def test( self):
  assert( 0==len( self.lParams))
  try:
   return id( ar_codeList) == id( self.consWrapped.car())
  except NameError:
   raise
  except:
   return False

 def paramList( self):
  assert( 0==len( self.lParams))
  #self.lParams.append( self.consWrapped.cdr().car())
  self.lParams.append( codeListParametersGetParameterValues( codeListGetParameters( self.consWrapped)))
  return self.lParams

 def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
  assert( 1==len( self.lParams))
  return '%s' % tuple( self.lParams)
  
class CpctReprStackShort(CpctRepr): # aus CpctReprStack

  def test( self):
   assert( 0==len( self.lParams))
   return isinstance( self.consWrapped, Cons) and id( ar_stack) == id( self.consWrapped.car())

  def paramList( self):
   assert( 0==len( self.lParams))
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( 0==len( self.lParams))

   stack= self.consWrapped
   ht= dict()

   ht[ id( stack)] = 'stack'

   walker= ConsSimple( stackGetCodeListCurrentEvalTokenList( stack),
    stackGetCodeListParent2EvalToken( stack))

   xNr= 0
   while not id( nil) == id( walker):
    walker_car= walker.car()
    ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'sclp2et_'+ str( xNr- 1))).repr_wrapped() # baustelle: hack
    #ht[ id( walker_car)]= ConsRepr( ConsSimple( walker_car.car(), 'consesNth0( stackGetCodeListParent2EvalToken, '+ str( xNr- 1)+ ')')).repr_wrapped() # baustelle: hack
    walker= walker.cdr()
    xNr += 1

   codeCurrentLeafList= stackGetCodeCurrentLeafList( self.consWrapped)
   
   ht[ id( consesDistanceSeek( codeCurrentLeafList))] = 'codeList' # sollte i.codeList entsprechen

   codeCurrentLeafListRepr= ConsRepr( codeCurrentLeafList).repr_wrapped( None, [CpctReprCodeListShort4Stack, CpctReprHTselfID2NameCreate( ht), CpctReprConsesRest]) # 28ddde667ab3463080f3b16faa5a48b3 baustelle 

   return 'stackShort( ' + codeCurrentLeafListRepr + ')'
 
 

