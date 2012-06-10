#!/bin/bash

set -x
gcc $(cat cfiles.txt) builtin_functions/*/*.c tests/*.c

