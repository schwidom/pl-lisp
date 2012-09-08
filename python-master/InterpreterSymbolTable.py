from symbols import nil, noo, true, Symbol
from executeObjects.BuiltinFunctionPyPrint import BuiltinFunctionPyPrint
from executeObjects.BuiltinFunctionPyPrintConses import BuiltinFunctionPyPrintConses
from executeObjects.BuiltinFunctionProg import BuiltinFunctionProg
from executeObjects.BuiltinFunctionProg2 import BuiltinFunctionProg2
from executeObjects.BuiltinFunctionProgN import BuiltinFunctionProgN
from executeObjects.BuiltinFunctionProgNMinus1 import BuiltinFunctionProgNMinus1
from executeObjects.BuiltinFunctionConses import BuiltinFunctionConses
from executeObjects.BuiltinFunctionThru1 import BuiltinFunctionThru1
from executeObjects.BuiltinFunctionCons import BuiltinFunctionCons
from executeObjects.BuiltinFunctionCar import BuiltinFunctionCar
from executeObjects.BuiltinFunctionCdr import BuiltinFunctionCdr
from executeObjects.NativeMacroIf import NativeMacroIf
from executeObjects.NativeQuotationMacro import NativeQuotationMacro
from executeObjects.NativeQuotationIfPre import NativeQuotationIfPre
from executeObjects.NativeQuotationQ1 import NativeQuotationQ1
from executeObjects.NativeQuotationQ2 import NativeQuotationQ2
from executeObjects.NativeQuotationQL import NativeQuotationQL
from executeObjects.NativeQuotationQConses import NativeQuotationQConses
from executeObjects.NativeFunctionUQSet1 import NativeFunctionUQSet1
from executeObjects.NativeQuotationQSwap2  import NativeQuotationQSwap2 
from executeObjects.NativeFunctionSet2 import NativeFunctionSet2
from executeObjects.NativeFunctionFif import NativeFunctionFif
from executeObjects.NativeFunctionUnConses import NativeFunctionUnConses
from executeObjects.NativeFunctionEnvPushNew0 import NativeFunctionEnvPushNew0
from executeObjects.NativeFunctionEnvPop0 import NativeFunctionEnvPop0
from executeObjects.NativeFunctionEval1 import NativeFunctionEval1
from executeObjects.NativeFunctionEval import NativeFunctionEval
from executeObjects.NativeQuotationFunction import NativeQuotationFunction
from executeObjects.NativeQuotationQuotation import NativeQuotationQuotation
from executeObjects.NativeQuotationMacro2 import NativeQuotationMacro2
from executeObjects.NativeFunctionEnvExists1 import NativeFunctionEnvExists1
from executeObjects.NativeFunctionEnvQuotationModePushNew0 import NativeFunctionEnvQuotationModePushNew0
from executeObjects.BuiltinFunctionConsesRest import BuiltinFunctionConsesRest
from executeObjects.BuiltinFunctionPyPrintConsesRest import BuiltinFunctionPyPrintConsesRest
from executeObjects.BuiltinMacroQN1 import BuiltinMacroQN1
from executeObjects.NativeFunctionStackGet import NativeFunctionStackGet
from executeObjects.BuiltinFunctionPyPrintStack import BuiltinFunctionPyPrintStack
from InterpreterNative import InterpreterNative
from tools import ensure
import Interpreter 
from ExecuteObject import ExecuteObject
from executeObjects.BuiltinFunctionNameOfSymbol import BuiltinFunctionNameOfSymbol
from executeObjects.BuiltinFunctionPyPrintStack2 import BuiltinFunctionPyPrintStack2
from executeObjects.BuiltinFunctionPyPrintStackShort import BuiltinFunctionPyPrintStackShort
from executeObjects.NativeFunctionStackClone import NativeFunctionStackClone
from executeObjects.NativeFunctionStackApply import NativeFunctionStackApply

class InterpreterSymbolTable:

 def __init__( self, interpreter):

  ensure( interpreter, [Interpreter.Interpreter])

  self.htInterpreterSymbolTableNames= dict()
  ht= self.htInterpreterSymbolTableNames
  
  ht[ 'macro']= NativeQuotationMacro()
  ht[ 'macro2']= NativeQuotationMacro2()
  ht[ 'function']= NativeQuotationFunction()
  ht[ 'quotation']= NativeQuotationQuotation()
  
  ht[ 'if']= NativeMacroIf()
  ht[ 'ifpre']= NativeQuotationIfPre()
  ht[ 'fif']= NativeFunctionFif()
  
  ht[ 'q1']= NativeQuotationQ1()
  ht[ 'q2']= NativeQuotationQ2() # parameter1 wird ignoriert, fuer uq2pre
  ht[ 'ql']= NativeQuotationQL()
  ht[ 'qn1']= BuiltinMacroQN1()
  ht[ 'qconses']= NativeQuotationQConses()
  ht[ 'qswap2']= NativeQuotationQSwap2()
  
  ht[ 'pyprint']= BuiltinFunctionPyPrint()
  ht[ 'pyprintconses']= BuiltinFunctionPyPrintConses()
  ht[ 'pyprintconsesRest']= BuiltinFunctionPyPrintConsesRest()
  ht[ 'pyprintStack']= BuiltinFunctionPyPrintStack()
  ht[ 'pyprintStack2']= BuiltinFunctionPyPrintStack2()
  ht[ 'pyprintStackShort']= BuiltinFunctionPyPrintStackShort()
  
  ht[ 'prog']= BuiltinFunctionProg()
  ht[ 'prog2']= BuiltinFunctionProg2()
  ht[ 'progn']= BuiltinFunctionProgN()
  ht[ 'progn-1']= BuiltinFunctionProgNMinus1()
  
  ht[ 'conses']= BuiltinFunctionConses()
  ht[ 'consesRest']= BuiltinFunctionConsesRest()
  
  ht[ 'unconses']= NativeFunctionUnConses()
  
  ht[ 'thru1']= BuiltinFunctionThru1()
  ht[ 'nameOfSymbol']= BuiltinFunctionNameOfSymbol()
  
  ht[ 'cons']= BuiltinFunctionCons()
  ht[ 'car']= BuiltinFunctionCar()
  ht[ 'cdr']= BuiltinFunctionCdr()
  
  ht[ 'eval1']= NativeFunctionEval1()
  ht[ 'eval']= NativeFunctionEval()
  
  ht[ 'set2']= NativeFunctionSet2()
  
  ht[ 'env-push-new0']= NativeFunctionEnvPushNew0()
  ht[ 'env-quotationMode-push-new0']= NativeFunctionEnvQuotationModePushNew0()
  ht[ 'env-pop0']= NativeFunctionEnvPop0()
  ht[ 'env-exists1']= NativeFunctionEnvExists1()
  
  ht[ 'uqset1']= NativeFunctionUQSet1()
  
  ht[ 'stack-get0']= NativeFunctionStackGet()
  ht[ 'stack-clone1']= NativeFunctionStackClone()
  ht[ 'stack-apply2']= NativeFunctionStackApply()
  
  del ht 
  
  self.htInterpreterSymbolTable= dict()
  
  for k in self.htInterpreterSymbolTableNames:
   v= self.htInterpreterSymbolTableNames[ k]
   self.htInterpreterSymbolTable[ Symbol( k)]= v
  del k, v
  
  self.htInterpreterSymbolTableNames[ 'nil']= nil
  self.htInterpreterSymbolTableNames[ 'noo']= noo
  self.htInterpreterSymbolTableNames[ 'true']= true
  
  self.htInterpreterSymbolTable[ nil]= nil
  self.htInterpreterSymbolTable[ noo]= noo
  self.htInterpreterSymbolTable[ true]= true

  for k in self.htInterpreterSymbolTable:
   v= self.htInterpreterSymbolTable[ k]
   if isinstance( v, InterpreterNative):
    v.setInterpreter( interpreter)
  del k, v

  def tmpSetRepr( v, repr_name):
   v.__repr__= (lambda : repr( repr_name))
   

  for k in self.htInterpreterSymbolTableNames:

   v= self.htInterpreterSymbolTable[ k]
   repr_name= 'sys:'+ k

   if isinstance( v, ExecuteObject):
    tmpSetRepr( v, repr_name)


