from testEnvSimple import test, te
from ConsTrait import ConsTrait, ConsSimple, ConsRepr
from ConsTrait import CpctRepr
from symbols import nil
from tools import uNames, usRename
from ConsTrait import ar_assoc, ar_assocElem, assocMake, assocAdd, assocGet, assocDel, listLen, listNth0, not_found
from symbols import Symbol
from ConsTrait import CpctReprListGeneral, CpctReprAssocGeneral, CpctReprAssocElemGeneral, CpctReprAssocInternGeneral, CpctReprConses
from ConsTrait import consesMake, ar_list, listMake, assocMakeIntern, assocElemMake
from ConsTrait import consesDistanceSeek
from ConsTrait import consesMakeRest
from ConsTrait import CpctReprHTselfID2NameCreate # testConsTrait6
from ConsTrait import CpctReprConsesRest

def testConsTrait1():

 te.checkComplainAndAdjustExpected( 0)

 cs1= ConsSimple( 1, 2)

 cs2= ConsSimple( cs1, ConsSimple( cs1, cs1))

 ctcs2= ConsTrait( cs2)
 ctcs2parameters= ctcs2.find_repetitions_parameter_template()
 ctcs2.find_repetitions( ctcs2parameters)

 test( id( cs2.ar), id( cs2.dr.ar))
 test( id( cs2.ar), id( cs2.dr.dr))

 test( id( ctcs2.ar), id( ctcs2.dr.ar))
 test( id( ctcs2.ar), id( ctcs2.dr.dr))

 test( "ConsSimple( ConsSimple( 1, 2), ConsSimple( ConsSimple( 1, 2), ConsSimple( 1, 2)))",
  ctcs2.repr_wrapped())

 test( "ConsSimple( repr_1, ConsSimple( repr_1, repr_1))",
  ctcs2.repr_wrapped( ctcs2parameters[ 'ht_selfid2Name']))

 # problem P001 dabei: ht_selfid2Name kann nicht von Hand bereitgestellt werden, 
 # da hier an ConsSimple gebunden

 test( 'repr_1', ctcs2parameters[ 'ht_selfid2Name'][ id( ctcs2.ar)])

 crcs2parameters= ConsRepr( cs2).find_repetitions_parameter_template()
 ConsRepr( cs2).find_repetitions( crcs2parameters)

 test( "ConsSimple( ConsSimple( 1, 2), ConsSimple( ConsSimple( 1, 2), ConsSimple( 1, 2)))",
  ConsRepr( cs2).repr_wrapped())

 test( "ConsSimple( repr_1, ConsSimple( repr_1, repr_1))",
  ConsRepr( cs2).repr_wrapped( crcs2parameters[ 'ht_selfid2Name']))

 # problem P001 geloest

 test( "ConsSimple( ox1, ConsSimple( ox1, ox1))",
  ConsRepr( cs2).repr_wrapped( dict( { id( cs1): 'ox1'})))

 test( 'repr_1', crcs2parameters[ 'ht_selfid2Name'][ id( cs2.ar)])

 te.checkComplainAndAdjustExpected( 11)

def testConsTrait2():

 te.checkComplainAndAdjustExpected( 0)

 def f( a, b, c):
  return ConsSimple( 'f', ConsSimple( a, ConsSimple( b, c)))

 class crsF( CpctRepr):

  def test( self):
   try:
    return 'f' == self.consWrapped.car()
   except:
    return False

  def paramList( self):
   assert( 0==len( self.lParams))
   self.lParams.append( self.consWrapped.cdr().car())
   self.lParams.append( self.consWrapped.cdr().cdr().car())
   self.lParams.append( self.consWrapped.cdr().cdr().cdr())
   return self.lParams

  def repr_wrapped( self, ht_selfid2Name, lCpctRepr):
   assert( 3==len( self.lParams))
   return 'f( %s, %s, %s)' % tuple( self.lParams)

 uNames.next( usRename( ConsSimple, 'cs'))

 cs= ConsSimple

 cs1= cs( 'q', cs( 'f', cs( cs( 3, 4), cs( cs( 5, 6), cs( 7, 8)))))
 cs2= cs( 'q', f( cs( 3, 4), cs( 5, 6), cs( 7, 8)))

 rep1= "cs( 'q', cs( 'f', cs( cs( 3, 4), cs( cs( 5, 6), cs( 7, 8)))))"
 rep2= "cs( 'q', f( cs( 3, 4), cs( 5, 6), cs( 7, 8)))"

 test( rep1, ConsRepr( cs1).repr_wrapped())
 test( rep2, ConsRepr( cs1).repr_wrapped( None, [crsF]))
 test( rep2, ConsRepr( cs2).repr_wrapped( None, [crsF]))
 test( rep1, ConsRepr( cs2).repr_wrapped())

 uNames.undo()

 te.checkComplainAndAdjustExpected( 4)

def testConsTrait3():
 
 def testCrCr( ex, ou, htEnvLocals= None):
  if None==htEnvLocals:
   htEnvLocals= dict()
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))

 s= Symbol
 cs= ConsSimple

 te.checkComplainAndAdjustExpected( 0)
 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 as1= assocMake()

 test( "cs( s( 'ar_assoc'), s( 'nil'))", ConsRepr( as1).repr_wrapped())
 testCrCr( cs( ar_assoc, nil), as1)
 test( 0, listLen( as1))

 asGot= assocGet( as1, (lambda elem: False))
 testCrCr( cs( ar_assoc, nil), asGot)

 asGot= assocGet( as1, (lambda elem: True))
 testCrCr( cs( ar_assoc, nil), asGot)

 del asGot

 assocAdd( as1, cs( '1', nil))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '1', nil)), nil)), as1)
 test( 1, listLen( as1))

 assocAdd( as1, cs( '2', nil))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '1', nil)), cs( cs( ar_assocElem, cs( '2', nil)), nil))), as1)
 test( "listGeneral( listGeneral( '1'), listGeneral( '2'))", ConsRepr( as1).repr_wrapped( None, [ CpctReprListGeneral]))
 test( "assocInternGeneral( assocElemGeneral( '1'), assocElemGeneral( '2'))", ConsRepr( as1).repr_wrapped( None, [ CpctReprAssocInternGeneral, CpctReprAssocElemGeneral]))
 test( "consesMake( s( 'ar_assoc'), consesMake( s( 'ar_assocElem'), '1'), consesMake( s( 'ar_assocElem'), '2'))", ConsRepr( as1).repr_wrapped( None, [ CpctReprConses])) 
 test( "assocGeneral( consesMake( '1'), consesMake( '2'))", ConsRepr( as1).repr_wrapped( None, [ CpctReprAssocGeneral, CpctReprConses])) # klar: konflikt, geloest per f5fbafd44f9a4a3c9f65860301b2c1c5
 test( 2, listLen( as1)) 

 testCrCr( cs( ar_assocElem, cs( '1', nil)), listNth0( as1, 0))
 testCrCr( cs( ar_assocElem, cs( '2', nil)), listNth0( as1, 1))

 test( not_found, listNth0( as1, -1))
 test( not_found, listNth0( as1, 2))

 as2= assocGet( as1, (lambda elem: '1'==elem.car()))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '1', nil)), nil)), as2)

 as3= assocGet( as1, (lambda elem: '2'==elem.car()))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '2', nil)), nil)), as3)

 as4= assocDel( as1, (lambda elem: '1'==elem.car()))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '1', nil)), nil)), as4)
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '2', nil)), nil)), as1)
 test( 1, listLen( as1))

 as5= assocDel( as1, (lambda elem: '2'==elem.car()))
 testCrCr( cs( ar_assoc, cs( cs( ar_assocElem, cs( '2', nil)), nil)), as5)
 testCrCr( cs( ar_assoc, nil), as1)
 test( 0, listLen( as1))

 uNames.undo()
 uNames.undo()
 te.checkComplainAndAdjustExpected( 25)

def testConsTrait4():
 
 def testCrCr( ex, ou, htEnvLocals= None):
  if None==htEnvLocals:
   htEnvLocals= dict()
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))

 s= Symbol
 cs= ConsSimple

 te.checkComplainAndAdjustExpected( 0)
 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 test( nil, consesMake())

 testCrCr( cs( 1, nil), consesMake( 1))
 testCrCr( cs( 1, cs( 2, nil)), consesMake( 1, 2))

 testCrCr( cs( ar_list, nil), listMake())

 testCrCr( cs( ar_assoc, nil), assocMake())

 testCrCr( cs( ar_assoc, nil), assocMakeIntern())

 as1= assocMake( consesMake( '1'), consesMake( '2'))
 as2= assocMakeIntern( assocElemMake( '1'), assocElemMake( '2'))

 exp1= "assocInternGeneral( assocElemGeneral( '1'), assocElemGeneral( '2'))"
 exp2= "assocGeneral( consesMake( '1'), consesMake( '2'))"
 exp3= "consesMake( s( 'ar_assoc'), consesMake( s( 'ar_assocElem'), '1'), consesMake( s( 'ar_assocElem'), '2'))"

 test( exp1, ConsRepr( as1).repr_wrapped( None, [ CpctReprAssocInternGeneral, CpctReprAssocElemGeneral]))
 test( exp1, ConsRepr( as2).repr_wrapped( None, [ CpctReprAssocInternGeneral, CpctReprAssocElemGeneral]))

 test( exp2, ConsRepr( as1).repr_wrapped( None, [ CpctReprAssocGeneral, CpctReprConses]))
 test( exp2, ConsRepr( as2).repr_wrapped( None, [ CpctReprAssocGeneral, CpctReprConses]))

 test( exp3, ConsRepr( as1).repr_wrapped( None, [ CpctReprConses]))
 test( exp3, ConsRepr( as2).repr_wrapped( None, [ CpctReprConses]))

 testCrCr( as1, as2)

 uNames.undo()
 uNames.undo()
 te.checkComplainAndAdjustExpected( 13)

def testConsTrait5():
 
 def testCrCr( ex, ou, htEnvLocals= None):
  if None==htEnvLocals:
   htEnvLocals= dict()
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))

 s= Symbol
 cs= ConsSimple

 te.checkComplainAndAdjustExpected( 0)
 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 csTest5= consesMake( 1, 2, 3, 4, 5)
 csTest2= consesMake( 6, 7)
 csTest1= consesMake( 8)

 testCrCr( csTest5.cdr().cdr().cdr().cdr(), consesDistanceSeek( csTest5, 0))
 testCrCr( csTest5.cdr().cdr().cdr(), consesDistanceSeek( csTest5, 1))
 testCrCr( csTest5.cdr().cdr(), consesDistanceSeek( csTest5, 2))
 testCrCr( csTest5.cdr(), consesDistanceSeek( csTest5, 3))
 testCrCr( csTest5, consesDistanceSeek( csTest5, 4))

 testCrCr( csTest5, consesDistanceSeek( csTest5, 5))
 testCrCr( csTest5, consesDistanceSeek( csTest5, 6))

 testCrCr( csTest2, consesDistanceSeek( csTest2, 6))
 testCrCr( csTest1, consesDistanceSeek( csTest1, 6))
 

 uNames.undo()
 uNames.undo()
 te.checkComplainAndAdjustExpected( 9)

def testConsTrait6():
 
 def testCrCr( ex, ou, htEnvLocals= None):
  if None==htEnvLocals:
   htEnvLocals= dict()
  test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
   ConsRepr( ou ).repr_wrapped( htEnvLocals))

 s= Symbol
 cs= ConsSimple

 te.checkComplainAndAdjustExpected( 0)
 uNames.next( usRename( ConsSimple, 'cs'))
 uNames.next( usRename( Symbol, 's'))

 cs= consesMakeRest( 1, 2, 3, 4, 6)

 test( 'cs( 1, cs( 2, cs( 3, cs( 4, 6))))', ConsRepr( cs).repr_wrapped())
 test( 'consesMakeRest( 1, 2, 3, 4, 6)', ConsRepr( cs).repr_wrapped( None, [ CpctReprConsesRest ]))

 test( 'cs( 1, cs( 2, cs( drei, cs( 4, 6))))', ConsRepr( cs).repr_wrapped( { id( 3):'drei'} ))
 test( 'cs( 1, cs( 2, cs( drei, cs( 4, 6))))', ConsRepr( cs).repr_wrapped( None, [ CpctReprHTselfID2NameCreate( { id( 3):'drei'} ) ] ))
 test( 'drei', ConsRepr( 3).repr_wrapped( { id( 3):'drei'} ))
 test( 'drei', ConsRepr( 3).repr_wrapped( None, [ CpctReprHTselfID2NameCreate( { id( 3):'drei'} ) ] )) # 0b539c705e06404d83a6966c52cb08a5

 test( 'consesMakeRest( 1, 2, drei, 4, 6)', ConsRepr( cs).repr_wrapped( { id( 3):'drei'}, [ CpctReprConsesRest ] ))
 test( 'consesMakeRest( 1, 2, drei, 4, 6)', ConsRepr( cs).repr_wrapped( None, [ CpctReprHTselfID2NameCreate( { id( 3):'drei'}), CpctReprConsesRest ] ))
 test( 'consesMakeRest( 1, 2, drei, 4, 6)', ConsRepr( cs).repr_wrapped( None, [ CpctReprConsesRest, CpctReprHTselfID2NameCreate( { id( 3):'drei'})] )) # 0b539c705e06404d83a6966c52cb08a5

 cs2= cs.cdr().cdr()

 test( 'cs( 3, cs( 4, 6))', ConsRepr( cs2).repr_wrapped())

 test( 'cs( 1, cs( 2, cs2))', ConsRepr( cs).repr_wrapped( { id( cs2):'cs2'}))
 test( 'consesMakeRest( 1, 2, 3, 4, 6)', ConsRepr( cs).repr_wrapped( { id( cs2):'cs2'}, [CpctReprConsesRest])) # die schwaeche, weswegen CpctReprHTselfID2NameCreate eingefuehrt wurde
 test( 'consesMakeRest( 1, 2, cs2)', ConsRepr( cs).repr_wrapped( None, [ CpctReprHTselfID2NameCreate( { id( cs2):'cs2'}), CpctReprConsesRest])) # die Loesung

 uNames.undo()
 uNames.undo()
 te.checkComplainAndAdjustExpected( 13)

def testConsTraitAll():
 testConsTrait1()
 testConsTrait2()
 testConsTrait3()
 testConsTrait4()
 testConsTrait5()
 testConsTrait6()

