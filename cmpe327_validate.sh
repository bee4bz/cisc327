#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#

cd inputs

for i in *.txt do
  echo "checking outputs of test $i"
  diff ../outputs/$i.txt ../expected/$i.txt
  diff ../outputs/$i.log ../expected/$i.log
done
