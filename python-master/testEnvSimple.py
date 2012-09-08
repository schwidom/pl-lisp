from TestEnv import TestEnv

te= TestEnv()

def testReset():
 #globals()[ 'te']= TestEnv()
 te.reset()
 
def testResult():
 print te.result()

def test( exp, out):
 if exp == out:
  te.test( True)
 else:
  print " Exp:", exp
  print " Out:", out
  te.test( False)


