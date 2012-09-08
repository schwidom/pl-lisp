from tools import Undo, UndoStep

class NooProblem:
 pass

nooProblem= NooProblem()
nooProblem.debug1= False

uNooProblem= Undo()

def problemSet( obj, field, value):
 
 newValue= value
 oldValue= obj.__dict__[ field]

 class ret( UndoStep):
  
  def redo( self):
   obj.__dict__[ field]= newValue

  def undo( self):
   obj.__dict__[ field]= oldValue

 return ret()



