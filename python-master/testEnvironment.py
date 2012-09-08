from testEnvSimple import test, te
from Interpreter import Environment

def testEnvironment1():

 te.checkComplainAndAdjustExpected( 0)

 e1= Environment()

 try:
  e1.get( 'a')
 except KeyError:
  test( True, True)

 e1.set( 'a', 1)

 test( 1, e1.get( 'a'))

 e2= e1.newChild() # | Environment( e1)

 test( 1, e2.get( 'a'))

 try:
  e2.get( 'b')
 except KeyError:
  test( True, True)

 te.test( e2.has_key( 'a'))
 te.test( not e2.has_key( 'b'))

 te.checkComplainAndAdjustExpected( 6)

