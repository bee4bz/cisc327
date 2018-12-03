#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#


for fileName in inputs/*.txt;
do
    echo "running test: $fileName"

    inputFile=$(sed '1d' "$fileName") #remove first descripter line of every txt file.

    echo "$inputFile"

    python3 main.py validServiceList.txt transactionSummaryFile.txt <<< "$inputFile"  > outputs/${fileName:7}.log

    #echo "$inputFile"
done
echo "I'm done"
