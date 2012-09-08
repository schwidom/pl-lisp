class IsNotInstance( Exception):

 def __init__( self, msg):
  Exception.__init__( self, msg)


def ensure( instance, lTypes):
 for iType in lTypes:
  if isinstance( instance, iType):
   return True
 raise IsNotInstance( ''+ repr( instance))

class IsAbstract( Exception): # /home/fschwidom/dev-git/dependency-graph-solution/1/dgs_v1/main.py

 def __init__( self, msg):
  Exception.__init__( self, msg)



class FunctionalUndo:

 def __init__( self):
  self.lastCallIdx= -1
  self.ubuf= []
 
 def getIdx( self):
  if -1==self.lastCallIdx:
   raise Exception()
  return self.lastCallIdx

 def redo( self, destIdx= None):
  if -1==destIdx:
   raise Exception( '-1==destIdx')
  if not None == destIdx:
   while not destIdx <= self.lastCallIdx:
    self.redo()
  else:
   if self.lastCallIdx + 1 > len( self.ubuf)- 1:
    raise Exception( 'self.lastCallIdx + 1 > len( self.ubuf)- 1')
   self.lastCallIdx += 1
   self.ubuf[ self.lastCallIdx]()
 
 def undo( self, destIdx= None):
  if -1==destIdx:
   raise Exception( -1==destIdx)
  if not None == destIdx:
   while destIdx < self.lastCallIdx:
    self.undo()
  else:
   if self.lastCallIdx -1 < 0:
    raise Exception( 'self.lastCallIdx -1 < 0') 
   self.lastCallIdx -= 1
   self.ubuf[ self.lastCallIdx]()

 def next( self, f):
  self.lastCallIdx += 1
  self.ubuf[ self.lastCallIdx: len( self.ubuf)]= [ f]
  f()

class UndoStep:
 
 def redo( self):
  raise IsAbstract( '')

 def undo( self):
  raise IsAbstract( '')

class Undo:

 def __init__( self):
  self.lastCallIdx= -1
  self.ubuf= []
 
 def getIdx( self):
  return self.lastCallIdx

 def redo( self, destIdx= None):
  if not None == destIdx:
   while not destIdx <= self.lastCallIdx:
    self.redo()
  else:
   if self.lastCallIdx + 1 > len( self.ubuf)- 1:
    raise Exception( 'self.lastCallIdx + 1 > len( self.ubuf)- 1')
   self.lastCallIdx += 1
   self.ubuf[ self.lastCallIdx].redo()
 
 def undo( self, destIdx= None):
  if not None == destIdx:
   while destIdx < self.lastCallIdx:
    self.undo()
  else:
   if self.lastCallIdx < 0:
    raise Exception( 'self.lastCallIdx -1 < 0') 
   self.ubuf[ self.lastCallIdx].undo()
   self.lastCallIdx -= 1

 def next( self, f):
  ensure( f, [UndoStep])
  self.lastCallIdx += 1
  self.ubuf[ self.lastCallIdx: len( self.ubuf)]= [ f]
  f.redo()

uNames= Undo()

def usRename( obj, newname):
 
 oldname= obj.__name__

 class ret( UndoStep):
  
  def redo( self):
   obj.__name__= newname

  def undo( self):
   obj.__name__= oldname

 return ret()

def parameterReducer( l):
 
 o= object()
 def catParameters( x, y):
  if id( o)== id( x):
   return ''+ y
  else:
   return ''+ x+ ', '+ y

 return reduce( catParameters, l, o)

class Wrapper:
 def __init__( self, wrapped):
  self.wrapped= wrapped


