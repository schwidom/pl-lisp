from testEnvSimple import test, te
from Interpreter import ConsTrait, ConsSimple, Interpreter, ConsAbstractCarAutoHistoryCSCS, consHistory # test3
from ConsTrait import ConsRepr
from symbols import ar_list, nil, Symbol
from tools import uNames, usRename
from Interpreter import CpctReprCodeListConfigMake
from InterpreterSymbols import ar_codeList, ar_codeListConfig
import InterpreterStructures
from InterpreterSymbols import ar_codeListParameters
from InterpreterStructures import codeListGetParameterValues
from InterpreterSymbols import ar_value

# if InterpreterStructures.alteVariante

cs= ConsSimple
s= Symbol

def testInterpreterGeneral1( ConsClass):

 def testCrCr( ex, ou, d= None):
  htEnvLocals= { id( env_locals1) : "env_locals1"}
  if not None == d:
   htEnvLocals.update( d)
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals, [ CpctReprCodeListConfigMake]),
   ConsRepr( ou ).repr_wrapped( htEnvLocals, [ CpctReprCodeListConfigMake]))

 def codeListFake( rest):
  if InterpreterStructures.alteVariante:
   return cs( ar_codeList, cs( codeListConfigMakeRepr, rest))
  else:
   return cs( ar_codeList, cs( codeListConfigMakeRepr, cs( ar_codeListParameters, rest)))

 def codeListFakeRoot( rest):
  if InterpreterStructures.alteVariante:
   return cs( ar_codeList, cs( codeListConfigMakeRepr, rest))
  else:
   return cs( ar_codeList, cs( codeListConfigMakeRepr, cs( ar_codeListParameters, cs( s( 'progn-root'), rest))))


 te.checkComplainAndAdjustExpected( 0)

 i= Interpreter()
 env_locals1= i.getEnvLocals()
 codeListConfigMakeRepr= 'codeListConfigMake( ...)'

 uNames.next( usRename( ConsAbstractCarAutoHistoryCSCS, 'ConsSimple'))
 testCrCr( codeListFakeRoot( nil), i.codeList)
 test( nil , i.codeListParent2EvalToken )

 if InterpreterStructures.alteVariante:
  testCrCr( cs( cs( ar_codeList, i.codeListCurrentEvalTokenList.cdr()), nil), i.codeCurrentLeafList,
   { id( i.codeListCurrentEvalTokenList.cdr()): 'codeListCurrentEvalTokenList.cdr()'})
 else:
  testCrCr( cs( cs( ar_codeList, cs( codeListConfigMakeRepr, i.codeListCurrentEvalTokenList)), nil), i.codeCurrentLeafList,
   { id( i.codeListCurrentEvalTokenList.cdr()): 'codeListCurrentEvalTokenList.cdr()'})

 uNames.undo()

 codeLeaf= i.codeLeafBackTree.car()
 testCrCr( cs( codeLeaf, nil), i.codeLeafBackTree, { id( codeLeaf): 'codeLeaf'})

 te.checkComplainAndAdjustExpected( 4)

 if False:
  pass
 elif id( ConsClass) == id( ConsAbstractCarAutoHistoryCSCS): # b4dfedc64bf1440b82f109a25c7f8421

  #ConsAbstractCarAutoHistoryCSCS.__name__= 'cs'
  #ConsSimple.__name__= 'cs'

  uNames.next( usRename( ConsAbstractCarAutoHistoryCSCS, 'cs'))
  uNames.next( usRename( ConsSimple, 'cs'))

  i.evalToken( s( 'aa'))

  ht_selfid2Name= { id( env_locals1): 'env_locals1'}
  testCrCr( cs( ar_codeList, cs( env_locals1, cs( s( 'aa'), nil))), i.codeList)

  testCrCr( cs( s( 'aa'), nil), i.codeListCurrentEvalTokenList.cdr())
  currentLeaf= i.codeCurrentLeafList.car()
  testCrCr( cs( ar_codeList, cs( env_locals1, i.codeListCurrentEvalTokenList.cdr())), currentLeaf)
  testCrCr( cs( currentLeaf, nil), i.codeCurrentLeafList)
  codeLeaf= i.codeLeafBackTree.car()
  testCrCr( cs( codeLeaf, nil), i.codeLeafBackTree)
  
  test( 'aa', i.codeList.cdr().cdr().car())

  test( id( consHistory), id( i.codeList.cdr().consWrapped.car().car()))
  testCrCr( cs( consHistory, cs( s( 'aa'), nil)), i.codeList.cdr().cdr().consWrapped.car())

  i.evalToken( s( '('), True)

  testCrCr( cs( env_locals1, nil), i.codeListCurrentEvalTokenList.cdr())
  currentLeaf= i.codeCurrentLeafList.car()
  testCrCr( cs( ar_codeList, i.codeListCurrentEvalTokenList.cdr()), currentLeaf)
  testCrCr( cs( currentLeaf, cs( cs( ar_codeList, cs( env_locals1, cs( currentLeaf, nil))), nil)), i.codeCurrentLeafList)
  codeLeaf= i.codeLeafBackTree.car()
  testCrCr( cs( codeLeaf, nil), i.codeLeafBackTree)

  i.evalToken( s( 'bb'))

  testCrCr( cs( s( 'bb'), nil), i.codeListCurrentEvalTokenList.cdr())
  currentLeaf= i.codeCurrentLeafList.car()
  testCrCr( cs( ar_codeList, cs( env_locals1, i.codeListCurrentEvalTokenList.cdr())), currentLeaf)
  testCrCr( cs( currentLeaf, cs( cs( ar_codeList, cs( env_locals1, cs( currentLeaf, nil))), nil)), i.codeCurrentLeafList)
  codeLeaf= i.codeLeafBackTree.car()
  testCrCr( cs( codeLeaf, nil), i.codeLeafBackTree)

  i.evalToken( s( ')'))

  testCrCr( cs( cs( ar_codeList, cs( env_locals1, cs( s( 'bb'), nil))), nil), i.codeListCurrentEvalTokenList.cdr())
  currentLeaf= i.codeCurrentLeafList.car()
  testCrCr( cs( ar_codeList, cs( env_locals1, i.codeListCurrentEvalTokenList.cdr())), currentLeaf)
  testCrCr( cs( currentLeaf, nil), i.codeCurrentLeafList)
  codeLeafBefore= codeLeaf
  codeLeaf= i.codeLeafBackTree.car()
  testCrCr( cs( codeLeaf, cs( codeLeafBefore, nil)), i.codeLeafBackTree)

  testCrCr( cs( ar_codeList, cs( env_locals1, cs( s( 'bb'), nil))), i.codeList.cdr().cdr().car())

  testCrCr( cs( consHistory, cs( cs( cs( consHistory, cs( ar_codeList, nil)), cs( cs( consHistory, cs( env_locals1, nil)), cs( cs( consHistory, cs( s( 'bb'), nil)), nil))), cs( s( 'aa'), nil))), i.codeList.cdr().cdr().consWrapped.car())

  i.evalToken( s( 'a'), True) # aa => a
  test( 'a', i.codeList.cdr().cdr().car())

  testCrCr( cs( consHistory, cs( s( 'a'), cs( cs( cs( consHistory, cs( ar_codeList, nil)), cs( cs( consHistory, cs( env_locals1, nil)), cs( cs( consHistory, cs( s( 'bb'), nil)), nil))), cs( s( 'aa'), nil)))), i.codeList.cdr().cdr().consWrapped.car())

  test( id( consHistory), id( i.codeList.cdr().consWrapped.car().car()))
  testCrCr( cs( cs( consHistory, cs( ar_codeList, nil)), cs( cs( consHistory, cs( env_locals1, nil)), cs( cs( consHistory, cs( s( 'a'), cs( cs( cs( consHistory, cs( ar_codeList, nil)), cs( cs( consHistory, cs( env_locals1, nil)), cs( cs( consHistory, cs( s( 'bb'), nil)), nil))), cs( s( 'aa'), nil)))), nil))), i.codeList.consWrapped)
  testCrCr( cs( ar_codeList, cs( env_locals1, cs( s( 'a'), nil))), i.codeList)

  uNames.undo()
  uNames.undo()

  te.checkComplainAndAdjustExpected( 27)

 elif id( ConsClass) == id( ConsSimple): # b4dfedc64bf1440b82f109a25c7f8421
  
  i.evalToken( cs( ar_value, s( 'a')))

  test( ar_codeListConfig, i.codeList.cdr().car().car())
  #test( s( 'a'), i.codeList.cdr().cdr().car())
  test( s( 'a'), codeListGetParameterValues( i.codeList).cdr().car())

  te.checkComplainAndAdjustExpected( 2)

 else:
  assert( False)

 test( nil , i.codeListParent2EvalToken )
 i.evalToken( cs( ar_value, s( '(')))
 elem= codeListFake( nil)
 tail= cs( elem, nil)

 uNames.next( usRename( ConsAbstractCarAutoHistoryCSCS, 'ConsSimple'))
 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 testCrCr( codeListFakeRoot( cs( s( 'a'), tail)), i.codeList)

 test( ConsTrait( cs( cs( s( 'a'), tail), nil)).repr_wrapped()
 , ConsRepr( i.codeListParent2EvalToken).repr_wrapped( None, [ CpctReprCodeListConfigMake]))
 i.evalToken( cs( ar_value, s( 'b')))
 elem= codeListFake( cs( s( 'b'), nil))
 tail= cs( elem, nil)

 testCrCr( codeListFakeRoot( cs( s( 'a'), tail)), i.codeList)
 testCrCr( cs( cs( s( 'a'), tail), nil), i.codeListParent2EvalToken)

 i.evalToken( cs( ar_value, s( 'c')))
 elem= codeListFake( cs( s( 'b'), cs( s( 'c'), nil)))
 tail= cs( elem, nil)

 testCrCr( codeListFakeRoot( cs( s( 'a'), tail)), i.codeList)
 testCrCr( cs( cs( s( 'a'), tail), nil), i.codeListParent2EvalToken)

 i.evalToken( cs( ar_value, s( ')')))

 testCrCr( codeListFakeRoot( cs( s( 'a'), cs( elem, nil))), i.codeList)
 test( nil , i.codeListParent2EvalToken )

 i.evalToken( cs( ar_value, s( 'd')))

 testCrCr( codeListFakeRoot( cs( s( 'a'), cs( elem, cs( s( 'd'), nil)))), i.codeList)
 test( nil , i.codeListParent2EvalToken )

 uNames.undo()
 uNames.undo()
 uNames.undo()

 te.checkComplainAndAdjustExpected( 11)

def testInterpreter1():

 testInterpreterGeneral1( ConsSimple)

def testInterpreter2():

 testInterpreterGeneral1( ConsAbstractCarAutoHistoryCSCS)

def testInterpreter3():

 te.checkComplainAndAdjustExpected( 0)

 i= Interpreter()
 i.evalToken( s( '(')) # baustelle: testbarkeit der repl
 
 te.checkComplainAndAdjustExpected( 0)

def testInterpreterGeneral4( ConsClass): # pruefung des execute-symbols (erstes symbol einer Liste)

 te.checkComplainAndAdjustExpected( 0)

 i= Interpreter()

 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( '(')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( 'a')))
 test( True, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( 'a')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( ')')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i= Interpreter()

 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( '(')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( '(')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( 'a')))
 test( True, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( 'a')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( ')')))
 test( True, i.currentEvalTokenIsInExecutePosition())

 i.evalToken( cs( ar_value, s( ')')))
 test( False, i.currentEvalTokenIsInExecutePosition())

 te.checkComplainAndAdjustExpected( 12)

def testInterpreter4():

 testInterpreterGeneral4( ConsSimple)

def testInterpreter5():

 testInterpreterGeneral4( ConsAbstractCarAutoHistoryCSCS)


def testInterpreterAll():
 testInterpreter1()
 #testInterpreter2() # baustelle0: vermutlich ein Fehler in der Cons-Abstraktion
 #testInterpreter3()
 testInterpreter4()
 #testInterpreter5()

