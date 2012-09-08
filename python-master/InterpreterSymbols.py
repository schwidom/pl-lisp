from symbols import Symbol, typeSymbol, ar_list, doSubConsType
from ConsTrait import ar_assoc, assocMake, assocAdd, consesMake
from symbols import ensureConsType
from ConsTrait import assocGet, listLen, consesNth0, assocNth0, assocClone
from ConsTrait import Cons, ConsRepr
from symbols import ar_value

ar_codeList= Symbol( 'ar_codeList')
typeSymbol.symAdd( ar_codeList, [ar_list])

ar_codeListConfig= Symbol( 'ar_codeListConfig')
typeSymbol.symAdd( ar_codeListConfig, [ar_assoc])

ar_codeListParameters= Symbol( 'ar_codeListParameters')
typeSymbol.symAdd( ar_codeListParameters, [ar_list])

ar_retList= Symbol( 'ar_retList')
typeSymbol.symAdd( ar_retList, [ar_list])

ar_retValue= Symbol( 'ar_retValue')
typeSymbol.symAdd( ar_retValue, [ar_value])

ar_retValueFromMacro= Symbol( 'ar_retValueFromMacro')
typeSymbol.symAdd( ar_retValueFromMacro, [ar_value])

ar_stack= Symbol( 'ar_stack')
typeSymbol.symAdd( ar_stack, [ar_list])

s_environment= Symbol( 's_environment')
s_macroLevel= Symbol( 's_macroLevel')
s_environment_quotationMode= Symbol( 's_environment_quotationMode')


