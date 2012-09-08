from testEnvSimple import test, te
from Interpreter import ConsSimple, ConsTrait, makeConsTrait # test1

def testConses1():

 te.checkComplainAndAdjustExpected( 0)

 c1= ConsSimple( 1, 1)
 c1.cdr( c1)
 c2= ConsSimple( 1, 1)
 c2.cdr( c2)
 c3= ConsSimple( 1, 1)
 c3.cdr( c1)
 c4= ConsSimple( 1, 1)
 c4.cdr( c3)
 c5= ConsSimple( 1, 1)
 c5.cdr( c2)
 
 test( True , ConsTrait( c1)==ConsTrait( c2) )
 test( False , ConsTrait( c1)==ConsTrait( c3) )
 test( False , ConsTrait( c3)==ConsTrait( c1) )
 test( True , ConsTrait( c3)==ConsTrait( c3) )
 test( False , ConsTrait( c4)==ConsTrait( c3) )
 test( True , ConsTrait( c5)==ConsTrait( c3) )
 test( False , ConsTrait( c5)==ConsTrait( c4) )
 
 
 c6_1= ConsSimple( 1, 1)
 c6_2= ConsSimple( 1, 1)
 c6_1.cdr( c6_2)
 c6_2.cdr( c6_1)
 
 test( True , ConsTrait( c6_1)==ConsTrait( c6_1) )
 test( True , ConsTrait( c6_1)==ConsTrait( c6_2) )
 test( True , ConsTrait( c6_2)==ConsTrait( c6_1) )
 
 c7_1= ConsSimple( 1, 1)
 c7_2= ConsSimple( 1, 1)
 c7_3= ConsSimple( 1, 1)
 c7_1.cdr( c7_2)
 c7_2.cdr( c7_3)
 c7_3.cdr( c7_1)
 
 test( True , ConsTrait( c7_1)==ConsTrait( c7_1) )

 ct7_1= ConsTrait( c7_1)
 ct7_2= ct7_1.cdr()
 test( True , ct7_2.consWrapped==c7_2 )

 test( False , ct7_1==ct7_2 )
 
 test( True , ConsTrait( c7_1)==ConsTrait( c7_2) )
 
 d= dict()
 test( False , ConsTrait( c7_1, d)==makeConsTrait( c7_2, d) )
 del d
 
 c8_1= ConsSimple( 1, 1)
 c8_2= ConsSimple( 1, 1)
 c8_3= ConsSimple( 1, 1)
 c8_4= ConsSimple( 1, 1)
 c8_1.cdr( c8_2)
 c8_2.cdr( c8_3)
 c8_3.cdr( c8_4)
 c8_4.cdr( c8_1)
 
 test( True , ConsTrait( c8_1)==ConsTrait( c8_1) )

 test( True , ConsTrait( c8_1)==makeConsTrait( c8_2) )

 d= dict()
 test( False , ConsTrait( c8_1, d)==makeConsTrait( c8_2, d) )
 del d

 test( True , ConsTrait( c8_1)==ConsTrait( c8_3) )
 test( True , ConsTrait( c8_2)==ConsTrait( c8_4) )
 
 c8_2_clonedDeep= ConsTrait( c8_2).cloneDeep()
 
 test( True , ConsTrait( c8_1)==ConsTrait( c8_2_clonedDeep) )
 
 test( True, hash( ConsTrait( c8_1)) == hash( ConsTrait( c8_2_clonedDeep)))
 
 # ok, es werden also die symmetrien beachtet, das soll mir recht sein
 
 test( True, hash( ConsTrait( c1)) == hash( ConsTrait( c2)))
 test( False, hash( ConsTrait( c1)) == hash( ConsTrait( c3)))

 test( True, hash( ConsTrait( c7_1)) == hash( ConsTrait( c7_2)))
 test( True, hash( ConsTrait( c7_1)) == hash( ConsTrait( c7_3)))

 test( True, hash( ConsTrait( c8_1)) == hash( ConsTrait( c8_2)))
 test( True, hash( ConsTrait( c8_1)) == hash( ConsTrait( c8_3)))
 test( True, hash( ConsTrait( c8_1)) == hash( ConsTrait( c8_4)))

 te.checkComplainAndAdjustExpected( 29)

