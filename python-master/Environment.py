class Environment: # Cons-Liste sollte ggf. ueber Cons-Abstraktion erfolgen

 def __init__( self, pl_symbols_prev= None):

  self.pl_symbols_prev= pl_symbols_prev
  self.pl_symbols= dict()

 def private_getAllSymbols( self):

  if None == self.pl_symbols_prev:
   ret= dict()
  else:
   ret= self.pl_symbols_prev.private_getAllSymbols()

  ret.update( self.pl_symbols)

  return ret

  
 
 def newChild( self):
  return Environment( self)

 def get( self, key):
  if self.pl_symbols.has_key( key):
   return self.pl_symbols[ key]
  elif None == self.pl_symbols_prev:
   return self.pl_symbols[ key] # liefert Exception
  else:
   return self.pl_symbols_prev.get( key)

 def set( self, key, value):
  self.pl_symbols[ key]= value
  
 def has_key( self, key):
  if self.pl_symbols.has_key( key):
   return True
  if None == self.pl_symbols_prev:
   return False
  return self.pl_symbols_prev.has_key( key)
   

