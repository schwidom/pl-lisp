#!/bin/bash

set -x
exuberant-ctags $(cat cfiles.txt) builtin_functions/*/*.c tests/*.c


