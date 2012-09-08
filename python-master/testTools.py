from testEnvSimple import test, te
from tools import FunctionalUndo, Undo, UndoStep

def testTools1():
 
 te.checkComplainAndAdjustExpected( 0)

 fu= FunctionalUndo()

 try:
  fu.getIdx()
  te.test( False)
 except:
  te.test( True)
 
 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)
 
 try:
  te.redo()
  te.test( False)
 except:
  te.test( True)
 
 undoAble= [0]

 def f( i):
  def fret():
   undoAble[0]= i
  return fret
 

 fu.next( f( 1))
 idx1= fu.getIdx()

 test( 1, undoAble[ 0])

 fu.next( f( 2))
 test( 2, undoAble[ 0])

 fu.next( f( 3))
 test( 3, undoAble[ 0])

 fu.next( f( 4))
 test( 4, undoAble[ 0])
 idx4= fu.getIdx()

 try:
  fu.redo()
  te.test( False)
 except:
  te.test( True)
 
 test( 4, undoAble[ 0])
 fu.undo()
 test( 3, undoAble[ 0])
 fu.redo()
 test( 4, undoAble[ 0])

 fu.undo( idx1)
 test( 1, undoAble[ 0])

 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)

 fu.redo()
 test( 2, undoAble[ 0])

 fu.undo()
 test( 1, undoAble[ 0])

 fu.redo( idx4)
 test( 4, undoAble[ 0])

 try:
  fu.redo()
  te.test( False)
 except:
  te.test( True)

 fu.undo()
 test( 3, undoAble[ 0])

 fu.undo()
 test( 2, undoAble[ 0])

 fu.undo()
 test( 1, undoAble[ 0])

 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)

 te.checkComplainAndAdjustExpected( 21)

def testTools2():
 
 te.checkComplainAndAdjustExpected( 0)

 fu= Undo()

 try:
  fu.getIdx()
  te.test( True)
 except:
  te.test( False)
 
 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)
 
 try:
  te.redo()
  te.test( False)
 except:
  te.test( True)
 
 undoAble= [0]

 def f( i):

  undoAbleInF= undoAble[ 0]

  class fret( UndoStep):

   def undo( self):
    undoAble[ 0]= undoAbleInF

   def redo( self):
    undoAble[0]= i
  return fret()
 
 fu.next( f( 1))
 idx1= fu.getIdx()

 test( 1, undoAble[ 0])

 fu.undo()
 test( 0, undoAble[ 0])

 fu.redo()
 test( 1, undoAble[ 0])

 fu.next( f( 2))
 test( 2, undoAble[ 0])

 fu.next( f( 3))
 test( 3, undoAble[ 0])

 fu.next( f( 4))
 test( 4, undoAble[ 0])
 idx4= fu.getIdx()

 try:
  fu.redo()
  te.test( False)
 except:
  te.test( True)
 
 test( 4, undoAble[ 0])
 fu.undo()
 test( 3, undoAble[ 0])
 fu.redo()
 test( 4, undoAble[ 0])

 fu.undo( idx1)
 test( 1, undoAble[ 0])

 try:
  fu.undo()
  te.test( True)
 except:
  te.test( False)

 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)

 test( 0, undoAble[ 0])

 fu.redo()
 test( 1, undoAble[ 0])

 fu.redo()
 test( 2, undoAble[ 0])

 fu.undo()
 test( 1, undoAble[ 0])

 fu.redo( idx4)
 test( 4, undoAble[ 0])

 try:
  fu.redo()
  te.test( False)
 except:
  te.test( True)

 fu.undo()
 test( 3, undoAble[ 0])

 fu.undo()
 test( 2, undoAble[ 0])

 fu.undo()
 test( 1, undoAble[ 0])

 try:
  fu.undo()
  te.test( True)
 except:
  te.test( False)

 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)

 test( 0, undoAble[ 0])

 try:
  fu.undo()
  te.test( False)
 except:
  te.test( True)

 te.checkComplainAndAdjustExpected( 29)


def testToolsAll():
 testTools1()
 testTools2()

