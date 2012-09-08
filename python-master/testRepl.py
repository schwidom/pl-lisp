from testEnvSimple import test, te
from Interpreter import Interpreter
from ConsTrait import ConsSimple, ConsRepr
from symbols import nil, Symbol
from tools import uNames, usRename
from symbols import true
from InterpreterSymbols import ar_codeList, ar_codeListConfig
from CpctReprCodeListConfigMake import CpctReprCodeListConfigMake
from InterpreterStructures import codeListMake, codeListCheck, codeListEnsure
from InterpreterStructures import codeListConfigMake, codeListParametersMake, codeListParametersEnsure
from InterpreterStructures import codeListParametersCheck, codeListGetConfig, codeListGetParameters
from InterpreterStructures import codeListConfigCheck, codeListGetParameterValues
import InterpreterStructures
from InterpreterStructures import codeListGetParameterValuesCdrContainer
from InterpreterStructures import codeListParametersGetParameterValues
from InterpreterStructures import codeListGetParameterValuesCdrContainer2
from ConsTrait import CpctReprConses
from InterpreterSymbols import ar_codeListParameters
from executeObjects.NativeFunctionSet2 import NativeFunctionSet2
from ConsTrait import CpctReprHTselfID2NameCreate
from ConsTrait import consesMake, consesConcatSymbols
from InterpreterOverridings import InterpreterOverridings
from InterpreterStructures import stackClone4Try1, stackMakeFromInterpreter
from InterpreterStructures import CpctReprStack, CpctReprStack2
from ConsTrait import CpctReprConsesRest

from debugVariables import uNooProblem, problemSet, nooProblem

cs= ConsSimple
s= Symbol

def makeOverridenInterpreter():

 ios= InterpreterOverridings()
 i= Interpreter()

 i.readTokenRawInput= ios.readTokenRawInput
 i.essentials_macro_function.ess_print= ios.ess_ess_print # 8c231655685648cc99e5b0bf3b0b8687
 i.s_print= ios.s_print

 return ( ios, i)

def testRepl1():

 def testCrCr( ex, ou, d= None):
  #htEnvLocals= { id( env_locals1) : "env_locals1"}
  htEnvLocals= {}
  if not None == d:
   htEnvLocals.update( d)
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))


 ( ios, i)= makeOverridenInterpreter()

 env_locals1= i.getEnvLocals()

 ios.__init__()
 ios.setInputString( '(pyprint (q1 1))')

 test( nil, i.readbuf.cdr())
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())

 i.replStep()

 test( 'pyprint (q1 1))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())

 i.replStep()

 test( ' (q1 1))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( i.currentEvalTokenIsInExecutePosition())

 i.replStep()

 test( 'q1 1))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())

 i.replStep()

 test( ' 1))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( i.currentEvalTokenIsInExecutePosition())


 i.replStep()


 test( '))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())


 i.replStep()

 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())
 test( [], ios.ess_ess_pront)


 i.replStep()

 test( nil, i.readbuf.cdr())
 test( nil, i.macroBuf)
 te.test( not i.currentEvalTokenIsInExecutePosition())
 #test( [('1',)], ios.ess_ess_pront)
 test( [( ConsRepr( cs( s( '1'), nil)).repr_wrapped(),)], ios.ess_ess_pront)

 ios.__init__()
 ios.setInputString( '(pyprint (eval1 (ql q1 1)))')

 test( nil, i.readbuf.cdr())
 test( nil, i.macroBuf)

 i.replStep()

 test( 'pyprint (eval1 (ql q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( ' (eval1 (ql q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( 'eval1 (ql q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( ' (ql q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( 'ql q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( ' q1 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( ' 1)))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( ')))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 test( '))', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)

 i.replStep()

 macroBufCdr= i.macroBuf.cdr()
 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 testCrCr( cs( cs( True, s( '(')), macroBufCdr), i.macroBuf)
 te.test( not i.quotationModeIsActivated())

 i.replStep()

 macroBufCdr= macroBufCdr.cdr()
 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 testCrCr( cs( cs( False, s( 'q1')), macroBufCdr), i.macroBuf)
 te.test( not i.quotationModeIsActivated())

 #print ConsRepr( i.macroBuf).repr_wrapped( None, [ CpctReprCodeListConfigMake, CpctReprConses])
 #exit()

 i.replStep()

 macroBufCdr= macroBufCdr.cdr()
 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 testCrCr( cs( cs( False, s( '1')), macroBufCdr), i.macroBuf)
 te.test( i.quotationModeIsActivated())

 i.replStep()

 macroBufCdr= macroBufCdr.cdr()
 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 testCrCr( cs( cs( False, s( ')')), macroBufCdr), i.macroBuf)
 test( nil, macroBufCdr)
 te.test( i.quotationModeIsActivated())

 i.replStep()

 test( ')', consesConcatSymbols( i.readbuf.cdr()))
 test( nil, i.macroBuf)
 te.test( not i.quotationModeIsActivated())
 test( [], ios.ess_ess_pront)

 i.replStep()

 test( nil, i.readbuf.cdr())
 test( nil, i.macroBuf)
 te.test( not i.quotationModeIsActivated())
 #test( [('1',)], ios.ess_ess_pront)
 test( [( ConsRepr( cs( s( '1'), nil)).repr_wrapped(),)], ios.ess_ess_pront)

 #ios.setInputString( '(pyprint (eval (q1 1)))') # ist semantisch falsch (enspricht: (eval '1)), Test auf korrekte Fehlerausgabe waere hier sinvoll # das war das falsche, liefert raise IsNotInstance
 #ios.setInputString( '(pyprint (eval (ql q1 (q1 1))))')
 ios.setEOF()

 try:
  i.repl()
  te.test( False)
 except EOFError:
  te.test( True)

 te.checkComplainAndAdjustExpected( 68)


def testRepl2(): # auf zu neuen Tests

 def testCrCr( ex, ou, d= None):
  htEnvLocals= { id( env_locals1) : "env_locals1"}
  if not None == d:
   htEnvLocals.update( d)
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))

 te.checkComplainAndAdjustExpected( 0)
 
 def loop1( ios, i):
  while [] == ios.ess_ess_pront:
   i.replStep()

 def loopEmptyString( ios, i):
  while not None == ios.input_string:
   i.replStep()

 def loop2( ios, i):
  while [] == ios.ess_ess_pront:
   #print 'ios.ess_ess_pront ', ios.ess_ess_pront
   print 'i.codeLevel ', i.codeLevel
   print 'i.readbuf ', i.readbuf
   print 'i.macroBufRepr() ', i.macroBufRepr()
   print 'i.quotationModeIsActivated() ', i.quotationModeIsActivated()
   i.replStep()

 subtestCount= [0]

 def subtest( query, results, loop= loop1):

  subtestCount[0]+= 1

  ( ios, i)= makeOverridenInterpreter()

  env_locals1= i.getEnvLocals()

  ios.__init__()
  ios.setInputString( query)

  loop( ios, i)

  test( results, ios.ess_ess_pront)

  ios.setEOF()

  try:
   i.repl()
   te.test( False)
  except EOFError:
   te.test( True)

 cmpStatementsCount= [0]

 def cmpStatements( stmt1, stmt2, loop= loop1):

  cmpStatementsCount[0]+= 1

  ( ios1, i1)= makeOverridenInterpreter()

  env_locals1= i1.getEnvLocals()

  ios1.__init__()
  ios1.setInputString( stmt1)

  loop( ios1, i1)

  ( ios2, i2)= makeOverridenInterpreter()

  env_locals1= i2.getEnvLocals()

  ios2.__init__()
  ios2.setInputString( stmt2)

  loop( ios2, i2)

  ios1.setEOF()
  ios2.setEOF()

  try:
   i1.repl()
   te.test( False)
  except EOFError:
   te.test( True)

  try:
   i2.repl()
   te.test( False)
  except EOFError:
   te.test( True)

  #test( results, ios.ess_ess_pront)
  test( ios1.ess_ess_pront, ios2.ess_ess_pront)

 interpretCount= [0]

 def interpret( query, loop= loop1):

  interpretCount[0]+= 1

  ( ios, i)= makeOverridenInterpreter()

  env_locals1= i.getEnvLocals()

  ios.__init__()
  ios.setInputString( query)

  loop( ios, i)

  ret= ios.ess_ess_pront

  ios.setEOF()

  try:
   i.repl()
   te.test( False)
  except EOFError:
   te.test( True)

  return ret

 codeListConfigMake= 'codeListConfigMake( ...)'

 result_pyprint_1= ConsRepr( cs( s( '1'), nil)).repr_wrapped()
 result_pyprint_1_2= ConsRepr( cs( s( '1'), cs( s( '2'), nil))).repr_wrapped()
 if InterpreterStructures.alteVariante:
  result_pyprint_ql_1= ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( s( '1'), nil))), nil)).repr_wrapped()
  result_pyprint_ql_1_2= ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( s( '1'), cs( s( '2'), nil)))), nil)).repr_wrapped()
 else:
  result_pyprint_ql_1= ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( ar_codeListParameters, cs( s( '1'), nil)))), nil)).repr_wrapped()
  result_pyprint_ql_1_2= ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( ar_codeListParameters, cs( s( '1'), cs( s( '2'), nil))))), nil)).repr_wrapped()

 subtest( '(pyprint (q1 1))', [(result_pyprint_1,)])
 subtest( '(pyprint (ql 1))', [(result_pyprint_ql_1,)])
 subtest( '(pyprint (q1 1) (q1 2))', [(result_pyprint_1_2,)]) # geloest, ging bislang nicht
 subtest( '(pyprint (ql 1 2))', [(result_pyprint_ql_1_2,)]) # geloest, ging bislang nicht

 subtest( '(pyprint (eval1 (q1 (q1 1))))', [(result_pyprint_1,)]) # 0fa6e6b10e2643d981504f9fa67adc82


 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 if InterpreterStructures.alteVariante:
  subtest( '(pyprint (ql q1 1))', [( ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( s( 'q1'), cs( s( '1'), nil)))), nil)).repr_wrapped( None, []), )])
  subtest( '(pyprint (q1 (q1 1)))', [( ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( s( 'q1'), cs( s( '1'), nil)))), nil)).repr_wrapped( None, [ CpctReprCodeListConfigMake]), )])
 else:
  subtest( '(pyprint (ql q1 1))', [( ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( ar_codeListParameters, cs( s( 'q1'), cs( s( '1'), nil))))), nil)).repr_wrapped( None, []), )])
  subtest( '(pyprint (q1 (q1 1)))', [( ConsRepr( cs( cs( ar_codeList, cs( codeListConfigMake, cs( ar_codeListParameters, cs( s( 'q1'), cs( s( '1'), nil))))), nil)).repr_wrapped( None, [ CpctReprCodeListConfigMake]), )])
  

 uNames.undo()
 uNames.undo()

 cmpStatements( '(pyprint (ql q1 1))', '(pyprint (q1 (q1 1)))') 

 subtest( '(pyprint (eval1 (ql q1 1)))', [(result_pyprint_1,)])

 subtest( '(pyprint (eval (q1 q1) (q1 1)))', [(result_pyprint_1,)])

 subtest( '(pyprint (eval1 (eval1 (ql q1 (q1 1)))))', [(result_pyprint_1,)]) 
 # subtest( '(pyprint (eval (eval (q1 q1) (q1 (ql q1 1)))))', [(result_pyprint_1,)]) # baustelle: fehler

 cmpStatements( '(pyprint (q1 (ql q1 1)))', '(pyprint (eval (q1 q1) (q1 (ql q1 1))))', loop1) 
 cmpStatements( '(pyprint (q1 (ql q1 1)))', '(pyprint (q1 (ql q1 1)))', loop1)

 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 if InterpreterStructures.alteVariante:
  test( [("cs( cs( s( 'ar_codeList'), cs( 'codeListConfigMake( ...)', cs( s( 'ql'), cs( s( 'q1'), cs( s( '1'), s( 'nil')))))), s( 'nil'))",)], interpret( '(pyprint (q1 (ql q1 1)))')) 
 else:
  test( [("cs( cs( s( 'ar_codeList'), cs( 'codeListConfigMake( ...)', cs( s( 'ar_codeListParameters'), cs( s( 'ql'), cs( s( 'q1'), cs( s( '1'), s( 'nil'))))))), s( 'nil'))",)], interpret( '(pyprint (q1 (ql q1 1)))')) 

 uNames.undo()
 uNames.undo()

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (q1 (q1 1))))') # 0fa6e6b10e2643d981504f9fa67adc82, 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval (q1 q1) (q1 (q1 1)))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval (q1 eval) (q1 (q1 q1)) (q1 (q1 (q1 1))))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (q1 (q1 (q1 1))))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (eval1 (q1 (q1 (q1 (q1 1))))))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (ql q1 1)))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (ql q1 (q1 1)))))') # 64005373aae94f3a9314d303d5f4016e
 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (ql ql q1 1))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (eval (q1 ql) (q1 ql) (q1 q1) (q1 1)))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (eval (q1 eval) (q1 (q1 ql)) (q1 (q1 ql)) (q1 (q1 q1)) (q1 (q1 1))))))') # 64005373aae94f3a9314d303d5f4016e

 cmpStatements( '(pyprint (q1 1))', '(eval1 (q1 (pyprint (q1 1))))') # das fehlte noch

 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (pyprint a)') # NativeFunctionSet2

 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 b) (set2 (q1 a) (q1 1))) (pyprint b)') 

 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (env-push-new0) (pyprint a)') 

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 1)) (env-push-new0) (set2 (q1 a) (q1 2)) (pyprint a)')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 1)) (env-push-new0) (set2 (q1 a) (q1 2)) (pyprint a) (env-pop0)')

 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (env-push-new0) (set2 (q1 a) (q1 2)) (env-pop0) (pyprint a)')

 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(pyprint (q1 1)) (pyprint (q1 2))')

 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 1)) (pyprint (q1 2)) (pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (pyprint a) (env-push-new0) (pyprint a) (set2 (q1 a) (q1 2)) (pyprint a) (env-pop0) (pyprint a)')

 cmpStatements( '(pyprint (q1 1))', '(eval1 (q1 (pyprint (q1 1))))')
 cmpStatements( '(pyprint (q1 1))', '(eval1 (q1 (prog (pyprint (q1 1)))))')
 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(eval1 (q1 (prog (pyprint (q1 1)) (pyprint (q1 2)))))')
 cmpStatements( '(pyprint (prog))', '(pyprint (prog (ql liefert nil)))')

 cmpStatements( '(pyprint (prog))', '(pyprint (prog (ql liefert nil)))')

 cmpStatements( '(set2 (q1 1) (q1 1)) (set2 (q1 2) (q1 2)) (pyprintconses (conses 1 2) )', '(set2 (q1 1) (q1 1)) (set2 (q1 2) (q1 2)) (pyprintconses (cons 1 (cons 2 nil)))')


 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(eval1 (ql prog (pyprint (q1 1)) (pyprint (q1 2))))') 

 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(prog (pyprint (q1 1)) (pyprint (q1 2)))') #interessanterweise funktioniert das

 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(eval1 (qswap2 (pyprint (q1 2)) (pyprint (q1 1))))')

 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2)) (pyprintconses (conses (conses (q1 1)) (conses (q1 2))))' , '(pyprintconses (eval1 (qswap2 (pyprint (q1 2)) (pyprint (q1 1)))))')

 cmpStatements( '(pyprint (q1 1) (q1 2)) (pyprintconses (conses (q1 1) (q1 2)))' , '(pyprintconses (pyprint (q1 1) (q1 2)))')

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (q1 2) (q1 3))')

 ### noo begin 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) noo (q1 2) (q1 3))') 
 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(eval1 (q1 (pyprint (q1 1) noo (q1 2) (q1 3))))') 

 cmpStatements( '(pyprint (q1 1) nil (q1 2) (q1 3))', '(pyprint (q1 1) (eval1 nil) (q1 2) (q1 3))') 

 cmpStatements( '(pyprint (q1 1) (q1 noo) (q1 2) (q1 3))', '(pyprint (q1 1) (q1 noo) (q1 2) (q1 3))') 

 cmpStatements( '(pyprintconses (q1 1) (q1 2) (q1 3))', '(pyprintconses (q1 1) (eval1 (q1 noo)) (q1 2) (q1 3))') 
 cmpStatements( '(pyprintconses (q1 1) (q1 2) (q1 3))', '(pyprintconses (q1 1) (eval1 (q1 (eval1 (q1 noo)))) (q1 2) (q1 3))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) ((macro p (q1 noo))) (q1 2) (q1 3))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) noo noo (q1 2) noo (q1 3))') 

 cmpStatements( '(pyprint)', '(pyprint)') 
 cmpStatements( '(pyprintconses)', '(pyprintconses)') 

 cmpStatements( '(pyprint (q1 1) (q1 noo) (q1 2) (q1 3))', '(pyprint (q1 1) (q2 nil noo) (q1 2) (q1 3))') 

 cmpStatements( '(pyprint (q1 2))', '(pyprint noo (q1 2))') 

 cmpStatements( '(pyprint noo)', '(pyprint noo noo noo)') # bugs heben sich auf

 cmpStatements( '(pyprint (q1 1))', '(pyprint (q1 1) noo)') # beabbbda7ec24dd0ab93e9314546cad0
 cmpStatements( '(pyprint)', '(pyprint noo)') # beabbbda7ec24dd0ab93e9314546cad0

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (unconses (conses (q1 2) (q1 3))))') 
 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (unconses (conses (q1 2))) (unconses (conses (q1 3))))')
 
 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (unconses (conses (q1 2))) noo (unconses (conses (q1 3))))')
 
 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (unconses (conses noo (q1 2))) (unconses (conses (q1 3))))')

 ### noo end

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (q1 1) (unconses (conses (q1 2) (q1 3) (q1 4))))')

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (q1 1) (unconses (conses (q1 2) (q1 3) (q1 4))))')

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (unconses (conses (q1 1) (q1 2))) (q1 3) (q1 4))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (q1 1) (unconses (conses (q1 2) (q1 3))) (q1 4))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (q1 1) (q1 2) (unconses (conses (q1 3) (q1 4))))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (unconses (conses (q1 1) (q1 2))) (unconses (conses (q1 3) (q1 4))))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (unconses (conses (unconses (conses (q1 1) (q1 2) (q1 3) (q1 4))))))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (unconses (eval1 (qswap2 (q1 2) (q1 1)))) (unconses (conses (q1 3) (q1 4))))))') 

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (conses (unconses (eval1 (qswap2 (q1 2) (q1 1)))) (unconses (eval1 (qswap2 (q1 4) (q1 3)))))))') 

 cmpStatements( '(pyprint (ql conses 1 2 3 4))', '(pyprint (q1 (conses 1 2 3 4)))')

 cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3) (q1 4))', '(pyprint (unconses (qconses 1 2 3 4)))')

 # cmpStatements( '(pyprint (q1 1) (q1 2) (q1 3))', '(pyprint (q1 1) (unconses (q1 3)))') # wegen 36268f550bcf4fb88d25868f8ea663bf hack nicht realisierbar, comment soll drin bleiben

 cmpStatements( '(pyprint (unconses (qconses 1 2 3 4)))', '(eval1 (q1 (pyprint (unconses (qconses 1 2 3 4)))))')

 cmpStatements( '(pyprint (unconses (qconses 1 2 3 4)))', '(eval (q1 pyprint) (q1 (unconses (qconses 1 2 3 4))))')

 cmpStatements( '(pyprint (unconses (qconses 1 2 3 4)))', '(eval (unconses (qconses pyprint (q1 1) (q1 2) (q1 3) (q1 4))))')

 cmpStatements( '(pyprint (unconses (qconses 1 2 3 4)))', '(eval (unconses (qconses pyprint (unconses (qconses 1 2 3 4)))))')

 cmpStatements( '(pyprint (q1 2))', '(pyprint (fif true (q1 2) (q1 3)))')

 cmpStatements( '(pyprint true)', '(pyprint true)')
 cmpStatements( '(pyprint true)', '(set2 (q1 t) true) (pyprint t)')

 cmpStatements( '(pyprint (q1 3))', '(pyprint (fif nil (q1 2) (q1 3)))')

 cmpStatements( '(pyprint (q1 2))', '(eval1 (fif true (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')
 cmpStatements( '(pyprint (q1 3))', '(eval1 (fif nil (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 t) true) (set2 (q1 f) nil) (eval1 (fif t (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')
 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 t) true) (set2 (q1 f) nil) (eval1 (fif f (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')

 cmpStatements( '(pyprint (q1 2))', '(eval1 (fif true (unconses (qconses (pyprint (q1 2)) (pyprint (q1 3))))))')
 cmpStatements( '(pyprint (q1 3))', '(eval1 (fif nil (unconses (qconses (pyprint (q1 2)) (pyprint (q1 3))))))')

 cmpStatements( '(pyprint nil)', '(pyprint (conses))')

 cmpStatements( '(pyprint (q1 a) (q1 b))', '(pyprint (q1 a) (unconses (conses)) (q1 b))') # neuheit zu unconses - das ging vor der eliminierung von 

 # cmpStatements( '(pyprint (q1 a) (q1 b))', '(pyprint (q1 a) (unconses) (q1 b))') # baustelle: das geht noch nicht, ist aber auch nicht soo eilig

 cmpStatements( '(pyprint (q1 a) (q1 b))', '(pyprint (q1 a) ((macro p (q1 (unconses (conses))))) (q1 b))')

 # cmpStatements( '(pyprint (q1 a) (q1 b))', '(pyprint (q1 a) ((macro2 p (unconses (conses)))) (q1 b))') # das geht noch nicht, vermutlich, da macro2 ar_retValue liefert statt ar_retList


 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (q1 (q1 1))))') 
 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 t) (q1 1)) (pyprint (eval1 (q1 t)))') 
 cmpStatements( '(pyprint true)', '(set2 (q1 t) true) (pyprint (eval1 (q1 t)))') 

 cmpStatements( '(pyprint (q1 2))', '(pyprint (fif (eval1 (q1 true)) (q1 2) (q1 3)))')
 cmpStatements( '(pyprint (q1 3))', '(pyprint (fif (eval1 (q1 nil)) (q1 2) (q1 3)))')

 cmpStatements( '(pyprint (q1 2))', '(eval1 (fif (eval1 (q1 true)) (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')
 cmpStatements( '(pyprint (q1 3))', '(eval1 (fif (eval1 (q1 nil)) (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))')


 cmpStatements( '(pyprint true)', '(pyprint true)')
 cmpStatements( '(pyprint true)', '(pyprint (eval1 true))')
 cmpStatements( '(pyprint true)', '(pyprint (eval1 (eval1 true)))')

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (set2 (q1 b) (q1 c)) (set2 (q1 c) (q1 a)) (pyprint (q1 a))')

 cmpStatements( '(pyprint (q1 b))', 
  '(set2 (q1 a) (q1 b)) (set2 (q1 b) (q1 c)) (set2 (q1 c) (q1 a)) (pyprint a)')

 cmpStatements( '(pyprint (q1 c))', 
  '(set2 (q1 a) (q1 b)) (set2 (q1 b) (q1 c)) (set2 (q1 c) (q1 a)) (pyprint (eval1 a))')

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (set2 (q1 b) (q1 c)) (set2 (q1 c) (q1 a)) (pyprint (eval1 (eval1 a)))')

 cmpStatements( '(pyprint (q1 b))', '(set2 (q1 a) (q1 (pyprint (q1 b)))) (eval1 a)')

 cmpStatements( ' ', ' ', loopEmptyString) # 59cc177458e34abcb943fd4351d93149
 cmpStatements( '', '', loopEmptyString) # 59cc177458e34abcb943fd4351d93149
 cmpStatements( '', ' ', loopEmptyString) # 59cc177458e34abcb943fd4351d93149

 cmpStatements( '(pyprint (q1 2))', '(eval1 (q1 (pyprint (q1 2))))')
 cmpStatements( '(pyprint (q1 2))', '(eval1 (thru1 (q1 (pyprint (q1 2)))))')


 cmpStatements( '(pyprint (q1 (fif true (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3))))))',
  '(pyprint (ifpre true (pyprint (q1 2)) (pyprint (q1 3))))')

 cmpStatements( '(pyprint (q1 (fif (eval1 (q1 true)) (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3))))))',
  '(pyprint (ifpre (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 3))))')

 cmpStatements( '(pyprint (q1 2))', '(eval1 (eval1 (ifpre (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 3)))))')
 cmpStatements( '(pyprint (q1 2))', '(eval1 (eval1 (q1 (fif (eval1 (q1 true)) (q1 (pyprint (q1 2))) (q1 (pyprint (q1 3)))))))')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 f) pyprint) (f (q1 2))')
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 f) pyprint) ((eval1 (q1 f)) (q1 2))')

 cmpStatements( '(pyprint (q1 2))', '(if (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 3)))')
 cmpStatements( '(pyprint (q1 3))', '(if (eval1 (q1 nil)) (pyprint (q1 2)) (pyprint (q1 3)))')

 cmpStatements( '(pyprint (q1 2))', '(if (eval1 (q1 true)) (if (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 true)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 2))', '(if (eval1 (q1 true)) (if (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 nil)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 4))', '(if (eval1 (q1 true)) (if (eval1 (q1 nil)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 true)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 4))', '(if (eval1 (q1 true)) (if (eval1 (q1 nil)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 nil)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 3))', '(if (eval1 (q1 nil)) (if (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 true)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 5))', '(if (eval1 (q1 nil)) (if (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 nil)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 3))', '(if (eval1 (q1 nil)) (if (eval1 (q1 nil)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 true)) (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 5))', '(if (eval1 (q1 nil)) (if (eval1 (q1 nil)) (pyprint (q1 2)) (pyprint (q1 4))) (if (eval1 (q1 nil)) (pyprint (q1 3)) (pyprint (q1 5))))')

 cmpStatements( '(pyprint (q1 2))', '(if true (if true (pyprint (q1 2)) (pyprint (q1 4))) (if true (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 2))', '(if true (if true (pyprint (q1 2)) (pyprint (q1 4))) (if nil (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 4))', '(if true (if nil (pyprint (q1 2)) (pyprint (q1 4))) (if true (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 4))', '(if true (if nil (pyprint (q1 2)) (pyprint (q1 4))) (if nil (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 3))', '(if nil (if true (pyprint (q1 2)) (pyprint (q1 4))) (if true (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 5))', '(if nil (if true (pyprint (q1 2)) (pyprint (q1 4))) (if nil (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 3))', '(if nil (if nil (pyprint (q1 2)) (pyprint (q1 4))) (if true (pyprint (q1 3)) (pyprint (q1 5))))')
 cmpStatements( '(pyprint (q1 5))', '(if nil (if nil (pyprint (q1 2)) (pyprint (q1 4))) (if nil (pyprint (q1 3)) (pyprint (q1 5))))')

 cmpStatements( '(pyprint (q1 2))', '(pyprint (car (cons (q1 2) (q1 3))))')
 cmpStatements( '(pyprint (q1 3))', '(pyprint (cdr (cons (q1 2) (q1 3))))')

 #cmpStatements( '(pyprint (q1 1)) (pyprint (q1 1)) (pyprint (q1 2)) (pyprint (q1 1))', 
 # '(set2 (q1 a) (q1 1)) (pyprint a) (env-push-new0) (pyprint a) (set2 (q1 a) (q1 2)) (pyprint a) (env-pop0) (pyprint a)')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 1)) (prog (env-push-new0) (set2 (q1 a) (q1 2)) (pyprint a))')

 # a86d44b091204dfda45448c187bfd720:
 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (prog (env-push-new0) (set2 (q1 a) (q1 2))) (pyprint a)')
 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 a) (q1 1)) (prog (env-push-new0) (set2 (q1 a) (q1 2)) (prog (env-push-new0) (set2 (q1 a) (q1 3)))) (pyprint a)')
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 1)) (prog (env-push-new0) (set2 (q1 a) (q1 2)) (prog (env-push-new0) (set2 (q1 a) (q1 3))) (pyprint a))')
 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 a) (q1 1)) (prog (env-push-new0) (set2 (q1 a) (q1 2)) (prog (env-push-new0) (set2 (q1 a) (q1 3)) (pyprint a)))')
 # fazit: schliessen der prog klammer entspricht sinngemaess einem (env-pop0) :a86d44b091204dfda45448c187bfd720

 cmpStatements( '(pyprint (q1 a))', '(pyprint (prog2 nil (q1 a)))')

 #cmpStatements( '(pyprint (q1 b))', 
 # '(set2 (q1 a) (q1 b)) (set2 (q1 i) (q1 u)) (uqset1 (q1 o)) (pyprint (q1 o a))') # noo hack a1306aa2c580467ca5b6440fc664d354, wieder entfernt

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (set2 (q1 i) (q1 u)) (uqset1 (q1 o)) (pyprint (q1 a))')

 cmpStatements( '(pyprint (q1 b))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q2 o a))')
 
 cmpStatements( '(pyprint (q1 b))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q1 (o a)))')
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (pyprint (q1 a))))')
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q2 o (q1 (pyprint (q1 a)))))')
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (o (q1 (pyprint (q1 a))))))')
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (eval1 (q1 (prog (uqset1 (q1 o)) (pyprint (q2 o (q1 a))))))') # korrekt 
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (eval1 (q1 (prog (uqset1 (q1 o)) (pyprint (q1 (o (q1 a)))))))') # korrekt 
 
 cmpStatements( '(pyprint (q1 (q1 a)))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (pyprint (q2 o (q1 (q1 a))))))') # korrekt ddfdc08cdef344b7bcd44d4e093d12ab

 cmpStatements( '(pyprint (q1 (q1 a)))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (pyprint (q1 (o (q1 (q1 a)))))))') # korrekt ddfdc08cdef344b7bcd44d4e093d12ab

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (pyprint (q2 o (q1 a)))))') # korrekt ddfdc08cdef344b7bcd44d4e093d12ab
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (eval1 (q1 (pyprint (q1 (o (q1 a))))))') # korrekt ddfdc08cdef344b7bcd44d4e093d12ab
 
 cmpStatements( '(pyprint (q1 b))',
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q2 o a))')

 cmpStatements( '(pyprint (q1 b))',
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q1 (o a)))')

 cmpStatements( '(pyprint (q1 b))',
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (eval1 (q1 (q2 o a))))') # korrekt ddfdc08cdef344b7bcd44d4e093d12ab

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (q2 o (pyprint (q2 o (q1 a))))') # korrekt

 cmpStatements( '(pyprint (pyprint (q1 a)))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q2 o (pyprint (q2 o (q1 a)))))') # korrekt

 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (q2 o (q1 a)))') # korrekt
 
 cmpStatements( '(pyprint (q1 a))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o)) (pyprint (eval1 (q1 (q1 a))))') # korrekt
 
 cmpStatements( '(pyprint (q1 b))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o1)) (env-push-new0) (set2 (q1 a) (q1 c)) (uqset1 (q1 o2)) (pyprint (eval1 (q1 (q2 o1 a))))') 
 
 cmpStatements( '(pyprint (q1 c))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o1)) (env-push-new0) (set2 (q1 a) (q1 c)) (uqset1 (q1 o2)) (pyprint (eval1 (q1 (q2 o2 a))))') 
 
 cmpStatements( '(pyprint (q1 b))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o1)) (env-push-new0) (set2 (q1 a) (q1 c)) (uqset1 (q1 o2)) (pyprint (q2 o1 a))') 
 
 cmpStatements( '(pyprint (q1 c))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o1)) (env-push-new0) (set2 (q1 a) (q1 c)) (uqset1 (q1 o2)) (pyprint (q2 o2 a))') 
 
 cmpStatements( '(pyprint (q1 c))', 
  '(set2 (q1 a) (q1 b)) (uqset1 (q1 o1)) (env-push-new0) (set2 (q1 a) (q1 c)) (uqset1 (q1 o2)) (pyprint (q1 (o2 a)))') 
 

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 (if true (pyprint (q1 2)) (pyprint (q1 3))))) (eval1 a)') # vorlage fuer macros / funktionen

 # cmpStatements( '(pyprint (q1 2))', '(macro p (pyprint (q1 2)))') # falsch

 cmpStatements( '(pyprint (q1 2))', '(pyprint (progn nil nil nil (q1 2)))')
 cmpStatements( '(pyprint (q1 2))', '(pyprint (progn-1 nil nil nil (q1 2) nil))')
 cmpStatements( '(pyprint nil)', '(pyprint (progn))')
 cmpStatements( '(pyprint nil)', '(pyprint (progn-1))')
 cmpStatements( '(pyprint (q1 2))', '(eval (unconses (qconses pyprint (q1 2))))')
 cmpStatements( '(pyprint (q1 2))', '(eval1 (ql pyprint (q1 2)))')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 f) (function p (pyprint (car p)))) (eval1 (f (q1 2)))')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 q) (quotation p (pyprint (car p)))) (eval1 (q 2))')

#####

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 m) (macro p (q1 (pyprint (q1 2))))) (m)')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 m) (macro p (ql pyprint (q1 2)))) (m)') # neu
 cmpStatements( '(pyprint (q1 2)) (pyprint (q1 3))', '((macro p (progn (pyprint (q1 2)) (q1 (pyprint (q1 3))))))') # neu

 cmpStatements( '(pyprint (q1 2))', '((macro2 p (pyprint (q1 2))))')
 cmpStatements( '(pyprint (q1 2))', '((macro p (q1 (pyprint (q1 2)))))')
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 m) (macro p (q1 (pyprint (q1 2))))) (m nil)')
 cmpStatements( '(pyprint (q1 2))', '((macro p (q1 (pyprint (q1 2)))))')
 cmpStatements( '(pyprint (q1 2))', '((macro p (prog (pyprint (q1 2)))))')


 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 m) (macro p (progn (uqset1 (q1 o)) (q1 (pyprint (q2 o (car p))))))) (m 2)')
 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 m) (macro p (progn (uqset1 (q1 o)) (q1 (pyprint (q2 o (car p))))))) (m 3)')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o)) (q1 (pyprint (prog2 o (car p))))))) (m a)')

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o)) (q1 (pyprint (o (car p))))))) (m a)') # neues uqset1 handling erlaubt vereinfachungen 96c8d565e4f946c38838d30756ce5c0d

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o2)) (q1 (pyprint (q2 o2 (car (cdr p)))))))) (m o a)') # baustelle: geht zwar, ist aber nicht zufriedenstellend, da aenderung im macro notwendig, wird mit 96c8d565e4f946c38838d30756ce5c0d geloest
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o2)) (q1 (pyprint (q1 (o2 (car p)))))))) (m (o a))') # 96c8d565e4f946c38838d30756ce5c0d problem geloest
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro2 p (pyprint (car p)))) (eval (q1 m) a)') # schon besser, o eigentlich hier nicht benoetigt
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o2)) (q1 (pyprint (q2 o2 (car p))))))) (eval (q1 m) a)') # schon besser, o eigentlich hier nicht benoetigt
 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (progn (uqset1 (q1 o2)) (q1 (pyprint (q2 o a)))))) (m)') # schon besser, o eigentlich hier nicht benoetigt

 #cmpStatements( '(pyprintconses (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (pyprintconses (car p)))) (m (progn o a))') # baustelle : (q2 o X) => (q1 (progn o X)) geht nicht immer 8c3a5910f8784e98b20aa35d0aacfc4b
 #cmpStatements( '(pyprintconses (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (pyprintconses (eval1 (car p))))) (m (progn o a))') # baustelle : (q2 o X) => (q1 (progn o X)) geht nicht immer 8c3a5910f8784e98b20aa35d0aacfc4b
 #cmpStatements( '(pyprintconses (q1 2))', '(set2 (q1 a) (q1 2)) (uqset1 (q1 o)) (set2 (q1 m) (macro p (pyprintconses (car p)))) (m (o a))') # baustelle: diese Notation koennte die loesung sein, wenn (o a) zu dem Inhalt von a wird # WEITERBEI

 cmpStatements( '(pyprint (q1 2))', '((macro2 p ((car p) (car (cdr p)))) pyprint (q1 2))') # vorbereitung zur endlosloop
 cmpStatements( '(pyprint (q1 2))', '((macro p (progn (uqset1 (q1 o)) (q2 o (prog ((car p) (car (cdr p))))))) pyprint (q1 2))') # vorbereitung zur endlosloop
 cmpStatements( '(pyprint (q1 2))', '((macro p (progn (uqset1 (q1 o)) (q1 ((q2 o (car p)) (q2 o (car (cdr p))))))) pyprint (q1 2))') # vorbereitung zur endlosloop

 #cmpStatements( '(pyprint (q1 2))', '(pyprint (q1 2)) ((macro2 p ((car p) (car p))) (macro p ((car p) (car p))))') # endlosloop
 # emdet wie folgt:
 # File "/home/fschwidom/dev-git/tags/1/tagdb/mainCode.py", line 265, in has_key
 #   return self.pl_symbols_prev.has_key( key)
 # ...
 # File "/home/fschwidom/dev-git/tags/1/tagdb/mainCode.py", line 263, in has_key
 #   if None == self.pl_symbols_prev:


 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 if2) (macro p (prog2 (uqset1 (q1 o)) (fif (eval1 (car p)) (q2 o (car (cdr p))) (q2 o (car (cdr (cdr p)))))))) (if2 true (pyprint (q1 2)) (pyprint (q1 3)))') # 

 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 if2) (macro p (prog2 (uqset1 (q1 o)) (fif (eval1 (car p)) (q2 o (car (cdr p))) (q2 o (car (cdr (cdr p)))))))) (if2 nil (pyprint (q1 2)) (pyprint (q1 3)))') # 

 # problem hierbei: da das Symbol true in NativeFunctionFif / fif per id verglichen wird 
 # id( true) == id( ret.car())
 # ist hier (eval1 (car p)) notwendig

 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 if2) (macro p (prog2 (uqset1 (q1 o)) (fif (eval1 (car p)) (q2 o (car (cdr p))) (q2 o (car (cdr (cdr p)))))))) (if2 (eval1 (q1 true)) (pyprint (q1 2)) (pyprint (q1 3)))') # 


 cmpStatements( '(pyprint (q1 2))', '(set2 (q1 if2) (macro p (progn (uqset1 (q1 o)) (fif (eval1 (car p)) (q1 (progn o (car (cdr p)))) (q1 (progn o (car (cdr (cdr p))))))))) (if2 true (pyprint (q1 2)) (pyprint (q1 3)))') # (q2 o X) => (q1 (progn o X))
 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 if2) (macro p (progn (uqset1 (q1 o)) (fif (eval1 (car p)) (q1 (progn o (car (cdr p)))) (q1 (progn o (car (cdr (cdr p))))))))) (if2 nil (pyprint (q1 2)) (pyprint (q1 3)))') # (q2 o X) => (q1 (progn o X))


 # cmpStatements( '(pyprint (q1 2))', '(pyprint (q1 2)) (nil)') # typ nicht erwartet: nil

 # betrachtung der environmentgueltigkeiten:

 cmpStatements( '(pyprint (q1 3))', '(set2 (q1 m) (macro p (q1 (set2 (q1 a) (q1 3))))) (m) (pyprint a)') # das geht zb mit macro2 nicht (noch nicht)
 cmpStatements( '(pyprint nil) (pyprint (q1 3)) (pyprint true)', '(set2 (q1 m) (macro p (q1 (set2 (q1 a) (q1 3))))) (pyprint (env-exists1 (q1 a))) (m) (pyprint a) (pyprint (env-exists1 (q1 a)))') 
 cmpStatements( '(pyprint nil (q1 3) (q1 3) true)', '(set2 (q1 m) (macro p (q1 (set2 (q1 a) (q1 3))))) (pyprint (env-exists1 (q1 a)) (m) a (env-exists1 (q1 a)))') # und das kann noch keine sprache (a entsteht durch (m) 
 # geht auch in Lisp: (defmacro m () '(setf a 'q)) (list (m) a)
 cmpStatements( '(pyprint nil (q1 4) (q1 3) true)', '(set2 (q1 m) (macro p (q1 (progn (set2 (q1 a) (q1 3)) (q1 4))))) (pyprint (env-exists1 (q1 a)) (m) a (env-exists1 (q1 a)))') # noo ist auch hier wieder brauchbar (als rueckgabewert von m)

 cmpStatements( '(pyprintconses (q1 1))', '(pyprintconses (consesRest (q1 1)))')
 cmpStatements( '(pyprintconses (cons (q1 1) (q1 2)))', '(pyprintconses (consesRest (q1 1) (q1 2)))')
 cmpStatements( '(pyprintconses (cons (q1 1) (cons (q1 2) (q1 3))))', '(pyprintconses (consesRest (q1 1) (q1 2) (q1 3)))')

 cmpStatements( '(pyprint (consesRest (q1 1) (q1 2)))', '(pyprint (conses (unconses (consesRest (q1 1) (q1 2)))))')
 cmpStatements( '(pyprint (consesRest (q1 1) (q1 2)))', '(pyprint (consesRest (unconses (conses (q1 1) (q1 2)))))')

 cmpStatements( '(pyprint (consesRest (q1 1)))', '(pyprint (conses (unconses (consesRest (q1 1)))))') # 80d1ab47171e42ba9bac8c8409b87bee
 cmpStatements( '(pyprint (consesRest (q1 1)))', '(pyprint (consesRest (unconses (conses (q1 1)))))') # 80d1ab47171e42ba9bac8c8409b87bee

 cmpStatements( '(pyprint (q1 1))', '(pyprint (qn1 1 1))') 
 cmpStatements( '(pyprint (q1 1))', '(pyprint (qn1 0 (q1 1)))') 
 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (qn1 1 (q1 1))))') 
 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (qn1 2 (q1 1)))))') 
 cmpStatements( '(pyprint (q1 1))', '(pyprint (eval1 (eval1 (eval1 (qn1 3 (q1 1))))))') 

 cmpStatements( '(pyprint set2)', '(set2 (q1 s) (stack-get0)) (pyprint (car (cdr (cdr (cdr (car (car (cdr (cdr (cdr s))))))))))')

 cmpStatements( '(pyprint (q1 s))', '(set2 (q1 s) (stack-get0)) (pyprint (car (cdr (cdr (cdr (cdr (car (car (cdr (cdr (cdr s)))))))))))')
 cmpStatements( '(pyprint (q1 ar_stack))', '(set2 (q1 s) (stack-get0)) (pyprint (car (car (cdr (cdr (cdr (cdr (cdr (car (car (cdr (cdr (cdr s)))))))))))))')


 cmpStatements( '(set2 (q1 s) (stack-get0)) (pyprintStack s)', '(set2 (q1 s) (stack-get0)) (set2 (q1 a) (q1 1)) (pyprintStack s)')

 #cmpStatements( '(set2 (q1 s) (stack-get0)) (pyprintconses s)', '(set2 (q1 s) (stack-get0)) (set2 (q1 a) (q1 1)) (pyprintconses s)') # zum Vergleich: diese Ausgabe ist nicht gleich (derzeit gibt es keine cmpStatementsFail - Funktion)

 # fuere weitere Stack Tests waere gut: 
 #  eine Copy - Funktion 
 #  eine Darstellung der ExecuteObject-e
 #  weitere Stack Zugriffsfunktionen
 #   que

 #uNames.undo()

 cmpStatements( '(pyprint (nameOfSymbol (q1 sys:set2)))', '(pyprint set2)')

 sExp= "consesMake( stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, consesMakeRest( consesMakeRest( Symbol( 'ar_codeList'), 'codeListConfigMake( ...)', Symbol( 'ar_codeListParameters'), 'sys:set2', ConsSimple( Symbol( 's'), 'sclp2et_-1')), consesMakeRest( Symbol( 'ar_codeList'), 'codeListConfigMake( ...)', Symbol( 'ar_codeListParameters'), ConsSimple( Symbol( 'progn-root'), 'sclp2et_0')), Symbol( 'nil'))))"

 test( [(sExp,),], interpret( "(set2 (q1 s) (stack-get0)) (pyprintStack s)"))
 test( [(sExp,), (sExp,)], interpret( "(set2 (q1 s) (stack-get0)) (pyprintStack s) (pyprintStack s)"))

 del sExp

 sExp= "consesMake( stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, consesMakeRest( consesMakeRest( Symbol( 'ar_codeList'), 'codeListConfigMake( ...)', Symbol( 'ar_codeListParameters'), 'sys:set2', ConsSimple( Symbol( 's'), 'sclp2et_-1')), consesMakeRest( Symbol( 'ar_codeList'), 'codeListConfigMake( ...)', Symbol( 'ar_codeListParameters'), Symbol( 'progn-root'), ConsSimple( Symbol( '1'), 'sclp2et_0')), Symbol( 'nil'))))"

 test( [(sExp,),], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStack s)"))
 test( [(sExp,), (sExp,)], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStack s) (pyprintStack s)"))

 del sExp

 sExp= "consesMake( stackMake( codeListCurrentEvalTokenList, codeListParent2EvalToken, consesMakeRest( consesMakeRest( Symbol( 'ar_codeList'), 'codeListConfigMake( ...)', Symbol( 'ar_codeListParameters'), 'sys:set2', ConsSimple( Symbol( 's'), 'sclp2et_-1')), codeList)))"

 test( [(sExp,),], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStack2 s)"))
 test( [(sExp,), (sExp,)], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStack2 s) (pyprintStack2 s)"))
 test( [(sExp,), (sExp,)], interpret( "               (set2 (q1 s) (stack-get0)) (pyprintStack2 s) (pyprintStack2 s)"))

 test( [(sExp,), (sExp,)], interpret( "               (set2 (q1 s) (stack-get0)) (pyprintStack2 (stack-clone1 s)) (pyprintStack2 (stack-clone1 s))"))

 del sExp

 sExp= "consesMake( stackShort( consesMakeRest( consesMakeRest( 'sys:set2', ConsSimple( Symbol( 's'), 'sclp2et_-1')), codeList)))"

 test( [(sExp,),], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStackShort s)"))
 test( [(sExp,), (sExp,)], interpret( "(progn (q1 1)) (set2 (q1 s) (stack-get0)) (pyprintStackShort s) (pyprintStackShort s)"))
 test( [(sExp,), (sExp,)], interpret( "               (set2 (q1 s) (stack-get0)) (pyprintStackShort s) (pyprintStackShort s)"))

 del sExp


 # baustelle0: pyprintStack noch nicht fertig (x0, x1)


 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 m1) (macro2 p (progn (pyprint (q1 1))))) (m1)')

 def f1( mvar, code):
  return 'nil (set2 (q1 '+ mvar+ ') (macro p (prog nil '+ code+ ' nil))) nil ( '+ mvar +') nil'

 def f2( mvar, code):
  return 'nil (set2 (q1 '+ mvar+ ') (macro p (q1 (prog nil '+ code+ ' nil)))) nil ( '+ mvar +') nil'

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', '(pyprint (q1 1))'))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', '(pyprint (q1 1))'))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f1( 'm2', '(pyprint (q1 1))')))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f2( 'm2', '(pyprint (q1 1))')))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f1( 'm2', '(pyprint (q1 1))')))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f2( 'm2', '(pyprint (q1 1))')))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f1( 'm2', f1( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f1( 'm2', f2( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f2( 'm2', f1( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f1( 'm1', f2( 'm2', f2( 'm3', '(pyprint (q1 1))'))))
 
 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f1( 'm2', f1( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f1( 'm2', f2( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f2( 'm2', f1( 'm3', '(pyprint (q1 1))'))))

 cmpStatements( '(pyprint (q1 1))', f2( 'm1', f2( 'm2', f2( 'm3', '(pyprint (q1 1))'))))


 def f1a( mvar, code):
  return 'nil (set2 (q1 '+ mvar+ ') (macro p (prog nil '+ code+ ' nil))) nil'

 def f2a( mvar, code):
  return 'nil (set2 (q1 '+ mvar+ ') (macro p (q1 (prog nil '+ code+ ' nil)))) nil'

 cmpStatements( '(pyprint (q1 1))', f1a( 'm1', '(pyprint (q1 1))')+ ' '+ f1( 'm2', '(m1)'))
 cmpStatements( '(pyprint (q1 1))', f1a( 'm1', '(pyprint (q1 1))')+ ' '+ f2( 'm2', '(m1)'))
 cmpStatements( '(pyprint (q1 1))', f2a( 'm1', '(pyprint (q1 1))')+ ' '+ f1( 'm2', '(m1)'))
 cmpStatements( '(pyprint (q1 1))', f2a( 'm1', '(pyprint (q1 1))')+ ' '+ f2( 'm2', '(m1)'))

 del f1, f2, f1a, f2a

 #cmpStatements( '(pyprint (q1 2)) (pyprint (q1 3))', '((macro p (progn (pyprint (q1 2)) (q1 (pyprint (q1 3))))))') # neu

 # Exceptions:

 cmpStatements( '(pyprint (q1 1))', '(set2 (q1 st) (stack-clone1 (stack-get0))) (pyprint (q1 1))') 
 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', '(set2 (q1 st) (stack-clone1 (stack-get0))) (stack-apply2 st (q1 2)) (pyprint (q1 1)) (pyprint st)') 
 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', """
   (set2 (q1 st) (stack-clone1 (stack-get0)))
   (set2 (q1 m) (macro p (q1 (progn (stack-apply2 st (q1 2))))))
   (m)
   (pyprint (q1 1))
   (pyprint st)
  """) 
 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', """
   (set2 (q1 st) (stack-clone1 (stack-get0)))
   (set2 (q1 m) (macro2 p (progn (stack-apply2 st (q1 2)))))
   (m)
   (pyprint (q1 1))
   (pyprint st)
  """) 
 # baustelle0: (pyprint (q1 3)) darf nicht ausgegeben werden
 cmpStatements( '(pyprint (q1 1)) (pyprint (q1 2))', """ 
   (set2 (q1 st) (stack-clone1 (stack-get0)))
   (set2 (q1 m) (macro2 p (progn (stack-apply2 st (q1 2)) (pyprint (q1 3)))))
   (m)
   (pyprint (q1 1))
   (pyprint st)
  """) 


 te.checkComplainAndAdjustExpected( 2* subtestCount[0] + 3* cmpStatementsCount[0] + 2* interpretCount[0])

def testRepl3Sub(): # test zur ueberleitung auf ar_codeListParameters
 
 te.checkComplainAndAdjustExpected( 0)
 
 codeList= codeListMake( codeListConfigMake(), codeListParametersMake( nil))

 te.test( codeListCheck( codeList))

 te.test( codeListConfigCheck( codeListGetConfig( codeList)))

 te.test( codeListParametersCheck( codeListGetParameters( codeList)))
 

 codeList= codeListMake( codeListConfigMake(), codeListParametersMake( ConsSimple( true, nil)))

 te.test( codeListCheck( codeList))

 te.test( codeListConfigCheck( codeListGetConfig( codeList)))

 codeListParameters= codeListGetParameters( codeList)

 te.test( codeListParametersCheck( codeListParameters))
 
 te.test( id( true) == id( codeListGetParameterValues( codeList).car()))

 te.test( id( true) == id( codeListGetParameterValuesCdrContainer( codeList).cdr().car()))

 te.test( id( true) == id( codeListParametersGetParameterValues( codeListParameters).car()))

 te.test( id( true) == id( codeListGetParameterValuesCdrContainer2( codeList).cdr().cdr().car()))

 te.checkComplainAndAdjustExpected( 10)

def testRepl3(): # test zur ueberleitung auf ar_codeListParameters
 tmp= InterpreterStructures.alteVariante
 try:
  InterpreterStructures.alteVariante= True
  testRepl3Sub()
  InterpreterStructures.alteVariante= False
  testRepl3Sub()
 finally:
  InterpreterStructures.alteVariante= tmp

def testRepl4():

 te.checkComplainAndAdjustExpected( 0)

 # ios= InterpreterOverridings()
 # i= Interpreter()
 # i.readTokenRawInput= ios.readTokenRawInput
 # i.essentials_macro_function.ess_print= ios.ess_ess_print
 # i.s_print= ios.s_print
 ( ios, i)= makeOverridenInterpreter()
 
 ios.setInputString( '(pyprint (pyprint (q1 (q1') # ))))
 #ios.setInputString( '(pyprint') # )
 ios.setEOF()
 
 i.replStep()
 while not id( nil) == id( i.readbuf.cdr()):
  # print i.readbuf.cdr().car()
  i.replStep()
 
 stack= stackMakeFromInterpreter( i)
 stack_cloned= stackClone4Try1( stack)
 stack_cloned2= stackClone4Try1( stack_cloned)
 
 def stack_repr_wrapped( stack):
  return ConsRepr( stack).repr_wrapped( None, [ CpctReprStack, CpctReprCodeListConfigMake, CpctReprConses, CpctReprConsesRest])

 stack_repr= stack_repr_wrapped( stack)
 stack_cloned_repr= stack_repr_wrapped( stack_cloned)
 stack_cloned2_repr= stack_repr_wrapped( stack_cloned2)
 
 # CpctReprStack / CpctReprStack2 zeigt bei falscher Verknuepfung die Fehler, die anderen CpctRepr* nicht

 test( stack_repr, stack_cloned_repr)
 test( stack_repr, stack_cloned2_repr)

 te.checkComplainAndAdjustExpected( 2)

def testReplAll():
 testRepl1() 
 testRepl2()
 testRepl3()
 testRepl4() # stackClone4Try1: Vorbereitung fuer Exceptions
 
