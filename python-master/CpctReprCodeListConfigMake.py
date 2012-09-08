from ConsTrait import CpctRepr
from InterpreterSymbols import ar_codeListConfig

class CpctReprCodeListConfigMake( CpctRepr):

 def test( self):
  assert( 0==len( self.lParams))
  try:
   #print ':', ConsRepr( self.consWrapped).repr_wrapped()
   return id( ar_codeListConfig) == id( self.consWrapped.car())
  except NameError:
   raise
  except:
   return False

 def paramList( self):
  assert( 0==len( self.lParams))
  #self.lParams.append( self.consWrapped.cdr().car())
  return self.lParams

 def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
  assert( 0==len( self.lParams))
  return "'codeListConfigMake( ...)'" % tuple( self.lParams)
  
