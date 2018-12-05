#!/bin/bash
#
# CISC/CMPE 327 Assignment 6 weekly testing script
#
# will call dailyScript.sh 5 times. 

for i in 1 2 3 4 5
do 

    ./dailyScript.sh ${i}

done