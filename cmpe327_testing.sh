#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#

cd inputs

for fileName in *.txt
do
    echo "running test $fileName"

    inputFile=$(sed '1d' ./input/"$fileName.txt") #remove first descripter line of every txt file.

    ./main.py ../activeaccts.txt ../transsummary.txt  < $inputFile \ > ../outputs/$fileName.log

done
