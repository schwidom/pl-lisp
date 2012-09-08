
class InterpreterOverridings:
 
 def __init__( self):
  self.ess_ess_pront= []

 def ess_ess_print( self, *l): # baustelle : ueberschreiben auf PL-Lisp Basis waere hier sauberer 8c231655685648cc99e5b0bf3b0b8687
  self.ess_ess_pront.append( l)

 def setInputString( self, input_string): # Leerstring funktioniert

  self.input_string= input_string
  self.eof= False

 def setEOF( self):
  self.eof= True

 def readTokenRawInput( self):
  if None==self.input_string and self.eof:
   raise EOFError()
  ret= self.input_string;
  self.input_string= None
  return ret

 def s_print( self, *l):
  pass

