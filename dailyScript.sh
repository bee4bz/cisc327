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

    python3 main.py validServiceList.txt transactionSummaryFile.txt <<< "$inputFile"  > session${1}Outputs/${fileName:15}.log

    #echo "$inputFile"
    
    echo "moving transfile"
    
    mv transactionSummaryFile.txt sessions/session${1}transactionSummaryFile${fileName:15}
    
    #iterate up loopNumber
    loopNumber=$((var + 1))
    
done

#combine transaction summary files at the end of the 'day'
loopyNumber=0

#mv transactionSummaryFile.txt transactionSummaryFile.old.txt
touch transactionSummaryFile.txt

for fileName in session${1}Inputs/*.txt;
do
    cat sessions/session${1}transactionSummaryFile${fileName:15} >> transactionSummaryFile.txt
    echo "copying sessions/session${1}transactionSummaryFile${fileName:15} into main trans file."
    loopyNumber=$((var + 1))
    
done

#end of session code at the end of the concatenated validTransactionFile
echo "EOS" >> transactionSummaryFile.txt

# Begin backend stuff*******

#commented out right now becasue backend script won't work

echo "running backend"

python3 main_backend.py validServiceList.txt transactionSummaryFile.txt centralFile.txt

echo "backend done"

#making central file output Day

cp centralFile.txt centralFilesDailyBackup/centralFileSession1.txt

echo "Day ${1} end"


