from tools import ensure

class InterpreterNative:

 def setInterpreter( self, interpreter):
  assert( 'Interpreter'==interpreter.__class__.__name__)
  self.interpreter= interpreter
