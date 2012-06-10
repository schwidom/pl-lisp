#!/bin/bash

set -x
vim $(cat cfiles.txt) builtin_functions/*/*.c tests/*.c

