#!/usr/bin/env bash
cd 5_lab_testing/calcSkeleton
tox -e $TOX_ENV

## Test lab 1

cd .. && cd ..
cd 1_lab
python -m pytest
