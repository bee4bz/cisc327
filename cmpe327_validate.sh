#!/bin/bash
#
# CISC/CMPE 327 Assignment 3 testing script
#
#

for i in outputs/*
do

  echo "checking outputs of test"
  stuff=sudo diff "outputs/${i:8}" "expected/${i:8}"
  #cmp "outputs/${i:8}" "expected/${i:8}"

echo $stuff

    if [ -z "$stuff" ];
    then

      echo "no"

    else


      echo "$stuff"
      echo "$stuff"
      echo "$stuff"
      echo "$stuff"
      echo "$stuff"
      echo "$stuff"
      

      echo "!="

      echo "outputs/${i:8}"
      echo "         "
      echo "expected/${i:8}"
      echo "Not a Match"

      echo "       "
    #cat outputs/${i:8}
    #cat expected/${i:8}
      echo "-----------" >>"results/result${i:8}.txt"
      echo "outputs/${i:8}">>"results/result${i:8}.txt"
      echo "!="
      echo "!=" >>"results/result${i:8}.txt"
      echo "expected/${i:8}">>"results/result${i:8}.txt"
      echo "         " >>"results/result${i:8}.txt"


  fi

#echo "      "
#echo "outputs/${i:8}"
#echo "      "
#echo "expected/${i:8}"

done
