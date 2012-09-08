from testEnvSimple import test, te
from symbols import nil, Symbol, typeSymbol, typeSymbolNot, typeSymbolChk
from symbols import ar_list

def testSymbols1(): # 010407a6a37b49bfb9836e84236e5586
 
 te.checkComplainAndAdjustExpected( 0)

 s1= Symbol( 's1')
 s2= Symbol( 's2')
 s3= Symbol( 's3')
 s4= Symbol( 's4')

 te.test( not typeSymbolChk( s4, Symbol( 's4')))

 te.test( typeSymbolChk( s4, s4)) 
 te.test( typeSymbolChk( s1, s1))

 typeSymbol.symAdd( s2, [s1])
 typeSymbol.symAdd( s3, [s1])
 typeSymbol.symAdd( s4, [s2, s3])

 te.test( typeSymbolChk( s4, s3))
 te.test( typeSymbolChk( s4, s2))
 te.test( typeSymbolChk( s4, s1))
 te.test( typeSymbolChk( s3, s1))
 te.test( typeSymbolChk( s2, s1))

 typeSymbolNot.symAdd( s3, [s1])

 te.test( typeSymbolChk( s4, s3))
 te.test( typeSymbolChk( s4, s2))
 te.test( typeSymbolChk( s4, s1))
 te.test( not typeSymbolChk( s3, s1))
 te.test( typeSymbolChk( s2, s1))
 
 typeSymbolNot.symAdd( s2, [s1])

 te.test( typeSymbolChk( s4, s3))
 te.test( typeSymbolChk( s4, s2))
 te.test( not typeSymbolChk( s4, s1))
 te.test( not typeSymbolChk( s3, s1))
 te.test( not typeSymbolChk( s2, s1))
 
 typeSymbolNot.symAdd( s4, [s3,s2])

 te.test( not typeSymbolChk( s4, s3))
 te.test( not typeSymbolChk( s4, s2))
 te.test( not typeSymbolChk( s4, s1))
 te.test( not typeSymbolChk( s3, s1))
 te.test( not typeSymbolChk( s2, s1))

 typeSymbolNot.symDel( s3)

 te.test( not typeSymbolChk( s4, s3))
 te.test( not typeSymbolChk( s4, s2))
 te.test( not typeSymbolChk( s4, s1))
 te.test( typeSymbolChk( s3, s1))
 te.test( not typeSymbolChk( s2, s1))

 typeSymbolNot.symDel( s2)

 te.test( not typeSymbolChk( s4, s3))
 te.test( not typeSymbolChk( s4, s2))
 te.test( not typeSymbolChk( s4, s1))
 te.test( typeSymbolChk( s3, s1))
 te.test( typeSymbolChk( s2, s1))
 
 typeSymbolNot.symDel( s4)
 for i in ( s4, s3, s2):
  typeSymbol.symDel( i)


 te.checkComplainAndAdjustExpected( 33)

def testSymbols2():

 te.checkComplainAndAdjustExpected( 0)

 test( 'ar_list', ar_list)

 sy= Symbol( 'sy')
 sy2= Symbol( 'sy')

 te.test( not id( sy) == id( sy2))

 test( sy, sy2)
 test( "Symbol( 'sy')", repr( sy))
 test( "Symbol( 'sy')", repr( sy2))

 te.checkComplainAndAdjustExpected( 5)

def testSymbols3():

 te.checkComplainAndAdjustExpected( 0)

 s1= Symbol( 's1')
 s2= Symbol( 's2')
 s3= Symbol( 's3')
 s4= Symbol( 's4')
 s5= Symbol( 's5')

 typeSymbol.symAdd( s2, [s1])
 typeSymbol.symAdd( s3, [s2])
 typeSymbol.symAdd( s4, [s3])
 typeSymbol.symAdd( s5, [s4])

 te.test( typeSymbolChk( s5, s1))

 typeSymbolNot.symAdd( s4, [s2])

 te.test( not typeSymbolChk( s5, s1))
 te.test( not typeSymbolChk( s5, s2))
 te.test( typeSymbolChk( s5, s3))
 te.test( typeSymbolChk( s5, s4))

 te.test( not typeSymbolChk( s4, s1))
 te.test( not typeSymbolChk( s4, s2))
 te.test( typeSymbolChk( s4, s3))

 te.test( typeSymbolChk( s3, s1))
 te.test( typeSymbolChk( s3, s2))

 te.test( typeSymbolChk( s2, s1))

 typeSymbol.symDel( s5)
 typeSymbol.symDel( s4)
 typeSymbol.symDel( s3)
 typeSymbol.symDel( s2)

 typeSymbolNot.symDel( s4)

 te.checkComplainAndAdjustExpected( 11)

def testSymbolsAll():
 testSymbols1()
 testSymbols1() # wiederholbarkeit des tests muss gewaehrleistet werden (wegen neuer Symbole)
 testSymbols2()
 testSymbols3()
 testSymbols3() # wiederholbarkeit des tests muss gewaehrleistet werden (wegen neuer Symbole)
 
