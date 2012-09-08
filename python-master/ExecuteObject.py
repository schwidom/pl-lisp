from EssentialsContainer import EssentialsContainer
from symbols import nil
from tools import ensure
from ConsTrait import Cons
from InterpreterStructures import codeListParametersEnsure, codeListParametersGetParameterValues
from InterpreterStructures import codeListMake, codeListConfigMake, codeListParametersMake

class ExecuteObject( EssentialsContainer):
 
 def setEnvironment( self, env): # 0bea40a420ca4ffa9140051cf20b778f
  self.env= env # 

 def setParameters( self, cons):

  codeListParametersEnsure( cons)

  self.parameters_o= cons

  cons= codeListParametersGetParameterValues( cons)

  # 80d1ab47171e42ba9bac8c8409b87bee

  self.parameters= cons

 def execute( self):
  raise Exception( "execute not implemented")

 def tmp0( self, rest): # c3ee5239baaf4484a61bd525f589ef76
  return codeListMake( codeListConfigMake( self.env), codeListParametersMake( rest))

