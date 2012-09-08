#!/usr/bin/python -i

import os
import sys
import rlcompleter
import readline
historyfile=sys.argv[0] + '.history'
readline.parse_and_bind("tab: complete")
readline.set_history_length( -1)
if os.path.exists( historyfile):
 if not os.path.isfile( historyfile):
  raise Exception
 readline.read_history_file( historyfile)

import atexit
atexit.register(readline.write_history_file, historyfile)

from testInterpreter import testInterpreter1, testInterpreter2, testInterpreter3, testInterpreter4, testInterpreter5
from testConsAbstraction import testConsAbstraction1, testConsAbstraction2, testConsAbstraction3
from tests import testConses1, testHashes1, testInterpreterAll, testConsAbstractionAll, testEnvironment1, testConsTraitAll
from tests import testAll
from ConsTrait import ConsTrait
from Interpreter import Interpreter
from ConsTrait import makeConsAbstractCarAutoHistory, ConsSimple
from Interpreter import ConsAbstractCarAutoHistoryCSCS
from testEnvSimple import testReset, testResult
from ConsTrait import ConsRepr
from symbols import Symbol, nil
from Interpreter import EssentialsContainer, Essentials
from symbols import typeSymbol, typeSymbolNot, typeSymbolChk
from testSymbols import testSymbolsAll, testSymbols1
from tools import FunctionalUndo
from testTools import testToolsAll, testTools1
from testRepl import testReplAll, testRepl1, testRepl2, testRepl3, testRepl4
from Interpreter import CpctReprCodeListConfigMake
from ConsTrait import CpctReprConses
from InterpreterStructures import codeListMake, codeListConfigMake, codeListParametersMake
from ConsTrait import consesMakeRest
from ConsTrait import CpctReprConsesRest
from ConsTrait import CpctReprHTselfID2NameCreate

from InterpreterStructures import stackMake, stackClone4Try1, stackMakeFromInterpreter
from InterpreterOverridings import InterpreterOverridings
from InterpreterStructures import CpctReprStack, CpctReprStack2

 
### fuer tests: ###

from Interpreter import Environment


