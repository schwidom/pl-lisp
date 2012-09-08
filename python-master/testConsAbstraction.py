from testEnvSimple import test, te
from Interpreter import ConsTrait, ConsSimple, nil, makeConsAbstractSwap # testConsAbstraction1
from ConsTrait import ConsRepr
from ConsTrait import consHistory, makeConsAbstractCarHistory # testConsAbstraction2
from ConsTrait import makeConsAbstractCarAutoHistory # testConsAbstraction3
from symbols import Symbol

def testCrCr( ex, ou, d= None):
 htEnvLocals= {}
 if not None == d:
  htEnvLocals.update( d)
 test( ConsRepr( ex ).repr_wrapped( htEnvLocals),
  ConsRepr( ou ).repr_wrapped( htEnvLocals))

s= Symbol
cs= ConsSimple

def testConsAbstraction1(): # Referenzbeispiel fuer Cons-Abstraktion

 te.checkComplainAndAdjustExpected( 0)
 
 CAS1= makeConsAbstractSwap( ConsSimple)
 CAS1.__name__= 'CAS1'
 CAS2= makeConsAbstractSwap( CAS1)
 CAS2.__name__= 'CAS2'
 CAS3= makeConsAbstractSwap( CAS2)
 CAS3.__name__= 'CAS3'
 CAS4= makeConsAbstractSwap( CAS3)
 CAS4.__name__= 'CAS4'

 cs4= CAS4( 1, CAS4( 2, CAS4( 3, nil)))

 #print ConsTrait( ConsSimple( 1, ConsSimple( 2, ConsSimple( 3, nil)))).repr_wrapped()

 testCrCr( CAS4( 1, CAS4( 2, CAS4( 3, nil))), cs4)
 testCrCr( CAS3( CAS3( CAS3( nil, 3), 2), 1), cs4.consWrapped)
 testCrCr( CAS2( 1, CAS2( 2, CAS2( 3, nil))), cs4.consWrapped.consWrapped)
 testCrCr( CAS1( CAS1( CAS1( nil, 3), 2), 1), cs4.consWrapped.consWrapped.consWrapped)
 testCrCr( cs( 1, cs( 2, cs( 3, nil))), cs4.consWrapped.consWrapped.consWrapped.consWrapped)

 cs4.cdr( CAS4( 4, nil))

 test( "CAS4( 1, CAS4( 4, Symbol( 'nil')))", ConsTrait( cs4).repr_wrapped())
 testCrCr( CAS4( 1, CAS4( 4, nil)), cs4)
 testCrCr( cs( 1, cs( 4, nil)), cs4.consWrapped.consWrapped.consWrapped.consWrapped)

 cs4_2= CAS4.cf.packDeep( ConsSimple( 5, 6))

 test( "CAS4( 5, 6)", ConsTrait( cs4_2).repr_wrapped())
 test( "CAS3( 6, 5)", ConsTrait( cs4_2.consWrapped).repr_wrapped())
 test( "CAS2( 5, 6)", ConsTrait( cs4_2.consWrapped.consWrapped).repr_wrapped())
 test( "CAS1( 6, 5)", ConsTrait( cs4_2.consWrapped.consWrapped.consWrapped).repr_wrapped())
 test( "ConsSimple( 5, 6)", ConsTrait( cs4_2.consWrapped.consWrapped.consWrapped.consWrapped).repr_wrapped())

 test( id( cs4_2.consWrapped), id( cs4_2.cf.unpack( cs4_2)))
 test( id( cs4_2.consWrapped), id( cs4_2.cf.unpackDeep( cs4_2, CAS3)))
 test( id( cs4_2.consWrapped.consWrapped), id( cs4_2.cf.unpackDeep( cs4_2, CAS2)))
 test( id( cs4_2.consWrapped.consWrapped.consWrapped), id( cs4_2.cf.unpackDeep( cs4_2, CAS1)))
 test( id( cs4_2.consWrapped.consWrapped.consWrapped.consWrapped), id( cs4_2.cf.unpackDeep( cs4_2, ConsSimple)))

 cs4.cdr().cdr( cs4_2)

 test( "CAS4( 1, CAS4( 4, CAS4( 5, 6)))", ConsTrait( cs4).repr_wrapped())
 test( "ConsSimple( 1, ConsSimple( 4, ConsSimple( 5, 6)))", ConsTrait( cs4.consWrapped.consWrapped.consWrapped.consWrapped).repr_wrapped())

 test( ConsTrait( cs4), ConsTrait( cs4.consWrapped.consWrapped.consWrapped.consWrapped))

 cs4_cloned= ConsTrait( cs4).cloneDeep()

 test( "ConsSimple( 1, ConsSimple( 4, ConsSimple( 5, 6)))", ConsTrait( cs4_cloned).repr_wrapped())

 test( ConsTrait( cs4), ConsTrait( cs4_cloned))

 test( id( cs4.cdr()), id( cs4.cdr()))

 cs5= ConsSimple( nil, nil)
 cs5.cdr( cs5)

 cs6= CAS1.cf.packDeep( cs5)
 cs7= CAS4.cf.packDeep( cs5)

 test( id( cs5), id( cs5.cdr()))
 test( id( cs6), id( cs6.car()))
 test( id( cs7), id( cs7.cdr()))

 test( id( cs6), id( CAS1.cf.pack( cs5)))
 test( id( cs6), id( CAS1.cf.packDeep( cs5)))
 test( id( cs7), id( CAS4.cf.packDeep( cs5)))

 test( id( CAS1.cf.packDeep( cs5)), id( CAS1.cf.packDeep( cs5)))
 test( id( CAS2.cf.pack( cs6)), id( CAS2.cf.pack( cs6)))
 test( id( CAS2.cf.packDeep( cs6)), id( CAS2.cf.packDeep( cs6)))

 test( id( CAS2.cf.packDeep( cs5)), id( CAS2.cf.packDeep( cs5)))

  # baustelle_geloest: nachteil der jetzigen loesung war, dass durch die dynamik immer neue Objekte in den oberen leveln entstehen 
  # Vorteil - der obere Aufbau ist immer ein korrektes Abbild des Unterbaus
  # Vorteil - die ids sind jetzt eindeutig, wegen nicht mehr immer neuer Objekte und das bedeutet fuer die registrierung in Hash-Tables keine Zuverlaessigkeit
  # Vorteil - zyklische Datenstrukturen sollten jetzt auch keine unendlichen Views abbilden

 cs8= CAS4( nil, nil)
 cs8.cdr( cs8)

 cs9= cs8.consWrapped.consWrapped.consWrapped.consWrapped

 test( id( cs9), id( cs9.cdr())) # sogar das geht, prima

 te.checkComplainAndAdjustExpected( 35)

def testConsAbstraction2():

 te.checkComplainAndAdjustExpected( 0)

 CACH= makeConsAbstractCarHistory( ConsSimple, ConsSimple)
 CACH.__name__= 'CACH'

 cach1= CACH( 1, 2)
 test( 'CACH( 1, 2)', ConsTrait( cach1).repr_wrapped())
 testCrCr( cs( cs( consHistory, cs( 1, nil)), 2), cach1.consWrapped)

 test( 1, cach1.car())
 test( 2, cach1.cdr())

 cach1.car( 3)
 cach1.cdr( 4)

 testCrCr( cs( cs( consHistory, cs( 3, nil)), 4), cach1.consWrapped)

 test( 3, cach1.car())
 test( 4, cach1.cdr())

 te.checkComplainAndAdjustExpected( 7)
 
def testConsAbstraction3():

 te.checkComplainAndAdjustExpected( 0)

 CACH= makeConsAbstractCarAutoHistory( ConsSimple, ConsSimple)
 CACH.__name__= 'CACH'

 cach1= CACH( 1, 2)
 test( 'CACH( 1, 2)', ConsTrait( cach1).repr_wrapped())

 cach1HistoryAr= cach1.consWrapped.car()

 testCrCr( cs( consHistory, cs( 1, nil)), cach1HistoryAr)
 testCrCr( cs( cach1HistoryAr, 2), cach1.consWrapped, { id( cach1HistoryAr) : 'cach1HistoryAr'})

 test( 1, cach1.car())
 test( 2, cach1.cdr())

 cach1.car( 3)
 cach1.cdr( 4)

 testCrCr( cs( consHistory, cs( 3, cs( 1, nil))), cach1HistoryAr)
 testCrCr( cs( cach1HistoryAr, 4), cach1.consWrapped, { id( cach1HistoryAr) : 'cach1HistoryAr'})

 test( 3, cach1.car())
 test( 4, cach1.cdr())

 cach1.cdr( CACH( 5, 6))

 cach1HistoryDrAr= cach1.cdr().consWrapped.car()

 test( 'CACH( 3, CACH( 5, 6))', ConsTrait( cach1).repr_wrapped())

 testCrCr( cs( consHistory, cs( 5, nil)), cach1HistoryDrAr)
 testCrCr( cs( cach1HistoryAr, cs( cach1HistoryDrAr, 6)), cach1.consWrapped, { id( cach1HistoryAr) : 'cach1HistoryAr', id( cach1HistoryDrAr) : 'cach1HistoryDrAr'})

 
 cach1HistoryArListOld= cach1.consWrapped.car().cdr()
 cach1.car( CACH( 7, 8))
 test( 'CACH( CACH( 7, 8), CACH( 5, 6))', ConsTrait( cach1).repr_wrapped())

 cach1HistoryArAr= cach1.car().consWrapped.car()

 testCrCr( cs( consHistory, cs( 7, nil)), cach1HistoryArAr)
 testCrCr( cs( consHistory, cs( cs( cach1HistoryArAr, 8), cach1HistoryArListOld)), cach1HistoryAr, { id( cach1HistoryArListOld): 'cach1HistoryArListOld', id( cach1HistoryArAr): 'cach1HistoryArAr'})
 test( "ConsSimple( cach1HistoryAr, ConsSimple( cach1HistoryDrAr, 6))", ConsRepr( cach1.consWrapped).repr_wrapped( { id( cach1HistoryAr) : 'cach1HistoryAr', id( cach1HistoryDrAr) : 'cach1HistoryDrAr'}))

 test( 7, cach1.car().car())

 cach2= CACH( CACH( 7, 8), CACH( 5, 6))
 test( 'CACH( CACH( 7, 8), CACH( 5, 6))', ConsTrait( cach2).repr_wrapped())

 cach2HistoryArAr= cach2.car().consWrapped.car()
 cach2HistoryDrAr= cach2.cdr().consWrapped.car()
 testCrCr( cs( consHistory, cs( 7, nil)), cach2HistoryArAr)
 testCrCr( cs( consHistory, cs( 5, nil)), cach2HistoryDrAr)

 testCrCr( cs( cs( consHistory, cs( cs( cach2HistoryArAr, 8), nil)), cs( cach2HistoryDrAr, 6)), cach2.consWrapped, { id( cach2HistoryArAr): 'cach2HistoryArAr', id( cach2HistoryDrAr): 'cach2HistoryDrAr'})

 test( 7, cach2.car().car())

 te.checkComplainAndAdjustExpected( 22)
 
def testConsAbstraction4(): # pruefung von mehrfach-referenzierung und zyklen

 te.checkComplainAndAdjustExpected( 0)

 CACH= makeConsAbstractCarAutoHistory( ConsSimple, ConsSimple)
 CACH.__name__= 'CACH'

 c1= CACH( 1, 2)

 c2= CACH( c1, c1)

 test( "CACH( CACH( 1, 2), CACH( 1, 2))", ConsTrait( c2).repr_wrapped())
 
 c1Wrapped= c1.consWrapped

 testCrCr( cs( cs( consHistory, cs( 1, nil)), 2), c1Wrapped)
 testCrCr( cs( cs( consHistory, cs( c1Wrapped, nil)), c1Wrapped), c2.consWrapped, { id( c1Wrapped): 'c1Wrapped'})

 c2.car( c1)
 c2.cdr( c1)
 
 test( "CACH( CACH( 1, 2), CACH( 1, 2))", ConsTrait( c2).repr_wrapped())

 testCrCr( cs( cs( consHistory, cs( 1, nil)), 2), c1Wrapped)
 testCrCr( cs( cs( consHistory, cs( c1Wrapped, cs( c1Wrapped, nil))), c1Wrapped)
  , c2.consWrapped, { id( c1Wrapped): 'c1Wrapped'})

 c1.cdr( c2)

 # die zyklen sind noch nicht zufriedenstellend
 test( "CACH( 1, CACH( CACH( 1, <cycle>), CACH( 1, <cycle>)))", ConsTrait( c1).repr_wrapped())
 test( "CACH( CACH( 1, CACH( <cycle>, <cycle>)), CACH( 1, CACH( <cycle>, <cycle>)))", ConsTrait( c2).repr_wrapped())

 # aber jetzt

 test( "CACH( 1, c2)", ConsRepr( c1).repr_wrapped( { id( c2): 'c2'}))
 test( "CACH( c1, c1)", ConsRepr( c2).repr_wrapped( { id( c1): 'c1'}))

 te.checkComplainAndAdjustExpected( 10)

def testConsAbstractionAll():
 testConsAbstraction1()
 testConsAbstraction2()
 testConsAbstraction3()
 testConsAbstraction4()
