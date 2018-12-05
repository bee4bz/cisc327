#!/bin/bash
#
# CISC/CMPE 327 Assignment 6 daily testing script
#
#

#initiate  bash script with arguments
#ex.
#./dailyScript.sh 1
# first argument recieved as $1
#script expects 1, 2, 3, 4+ input numbers

#Front end stuff*********

echo "Day ${1} script starts now." # To indicate all three run.

#run session front end. 

loopNumber=0 #loop number will generate save, move trasnaction file into session number

for fileName in session${1}Inputs/*.txt;
do
    echo "running session${1}: $fileName"

    inputFile=$(sed '1d' "$fileName") #remove first descripter line of every txt file.

    echo "$inputFile"

    python3 main.py validServiceList.txt transactionSummaryFile.txt <<< "$inputFile"  > session${1}Outputs/${fileName:14}.log

    #echo "$inputFile"
    
    mv transactionSummaryFile.txt sessions/session${1}transactionSummaryFile${loopNumber}.txt
    
    #iterate up loopNumber
    loopNumber=$((var + 1))
    
done

#combine transaction summary files at the end of the 'day'
loopNumber=0

#mv transactionSummaryFile.txt transactionSummaryFile.old.txt
touch transactionSummaryFile.txt

for fileName in sessions/*.txt;
do
    cat sessions/session${1}transactionSummaryFile${loopNumber}.txt >> transactionSummaryFile.txt
    echo "copying transactionSummaryFile${loopNumber}.txt into main trans file."
    loopNumber=$((var + 1))
done

#end of session code at the end of the concatenated validTransactionFile
echo "EOS" >> transactionSummaryFile.txt

# Begin backend stuff*******

#commented out right now becasue backend script won't work

python3 main_backend.py validServiceList.txt transactionSummaryFile.txt centralFile.txt

echo "Day ${1} end"


