#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#

cd inputs
for i in *txt

do
    echo "running test $i"
    ./main.py activeaccts.txt transsummary.txt 


done
