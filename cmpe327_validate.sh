#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#

for i in outputs/*
do

  echo " "
  echo " "
  echo "checking outputs of test"
  #stuff=sudo diff "outputs/${i:8}" "expected/${i:8}"
  
  stuff=sudo diff "outputs/${i:8}" "expected/${i:8}" && stuff=1 || stuff=2
  
  
  #cmp "outputs/${i:8}" "expected/${i:8}"




echo "----------------"

    echo $stuff
    touch "results/result-${i:8}"

echo "----------------"

    if [[ 1 -eq "$stuff" ]]
    then
      
      echo "-----------" >>"results/result-${i:8}"
      echo "It's a match" >>"results/result-${i:8}"
      echo "outputs/${i:8}">>"results/result-${i:8}"
      echo "==" >>"results/result-${i:8}"
      echo "expected/${i:8}">>"results/result-${i:8}"
      echo "         " >>"results/result-${i:8}"

      
      echo "Matches"
      

    else

      echo "$stuff"


      echo "!="

      echo "outputs/${i:8}"
      echo "Does not Match"
      echo "         "
      echo "expected/${i:8}"

      echo "       "
    #cat outputs/${i:8}
    #cat expected/${i:8}
      echo "-----------" >>"results/result-${i:8}"
      echo "It's not a match" >>"results/result-${i:8}"
      echo "outputs/${i:8}">>"results/result-${i:8}"
      echo "!=" >>"results/result-${i:8}"
      echo "expected/${i:8}">>"results/result-${i:8}"
      echo "         " >>"results/result-${i:8}"


  fi

#echo "      "
#echo "outputs/${i:8}"
#echo "      "
#echo "expected/${i:8}"

done
