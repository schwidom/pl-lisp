from testEnvSimple import test, te
from Interpreter import ConsSimple # test2
from unbenutztesTypkonzept import cons_addType, ConsType, cons_delType, ht_cons_consid2consAndTypeSet, ht_cons_consType2ConsidSetAndFunctionSet # test2

def testHashes1():

 te.checkComplainAndAdjustExpected( 0)

 c1= ConsSimple( 1, 2)
 c2= ConsSimple( 1, 2)
 
 cons_addType( c1, ConsType( 'test1'))
 cons_addType( c1, ConsType( 'test2'))

 cons_delType( c2, ConsType( 'test1'))
 
 test( 2 , len( ht_cons_consid2consAndTypeSet[ id( c1)][1]) )
 test( True , ConsType( 'test1') in ht_cons_consid2consAndTypeSet[ id( c1)][1] )
 test( True , ConsType( 'test2') in ht_cons_consid2consAndTypeSet[ id( c1)][1] )
 test( 0 , len( ht_cons_consid2consAndTypeSet[ id( c2)][1]) )
 test( True , set( [id( c1)]) == ( ht_cons_consType2ConsidSetAndFunctionSet[ ConsType( 'test1')][0]) )

 cons_delType( c1, ConsType( 'test1'))

 test( 1 , len( ht_cons_consid2consAndTypeSet[ id( c1)][1]) )
 test( False , ConsType( 'test1') in ht_cons_consid2consAndTypeSet[ id( c1)][1] )
 test( True , ConsType( 'test2') in ht_cons_consid2consAndTypeSet[ id( c1)][1] )
 test( 0 , len( ht_cons_consid2consAndTypeSet[ id( c2)][1]) )
 test( False , set( [id( c1)]) == ( ht_cons_consType2ConsidSetAndFunctionSet[ ConsType( 'test1')][0]) )

 te.checkComplainAndAdjustExpected( 10)


