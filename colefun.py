changeticket(serviceNum,serviceNumNew,ticketNum):

def changeticket(serviceNum,serviceNumNew,ticketNum):
    #Flag to determine if the Service Number is Found. One if YES
    flag =0
    fileName="transactionSummaryFile.txt"
    #open transactionSummaryFile
    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNum) in part: #If the serviceNUM is found in the file
                    flag=1 
                    updatedLine=line #store the old line in UpdatedLine

    #Parse and change the ticket
    changedResult=[]
    changedResult = updatedLine.split(" ")
    #if the flag was raised
    if (flag ==1):
        #Remove the line
        with open(fileName,'r+') as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if str(serviceNum) not in line:
                    f.write(line)
            f.truncate()

    #Write the new lines. 
    bufferLine=[]
    if (int(changedResult[2]) > ticketNum):
        bufferLine[0]= str(serviceNumNew) + changedResult [1] + str((int(changedResult[2])-ticketNum)) + changedResult [3] + changedResult [4]
        bufferLine[1]= str(serviceNumNew) + changedResult [1] + str(ticketNum) + changedResult [3] + changedResult [4]
    else:
        bufferLine[0]= str(serviceNumNew) + changedResult [1] + str(ticketNum) + changedResult [3] + changedResult [4]
    print (bufferLine)




def cancelticket(serviceNum,ticketNum):

#Flag to determine if the Service Number + ticket num is Found. One if YES
    flag =0
    fileName="transactionSummaryFile.txt"
    #open transactionSummaryFile
    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNum) in part: #If the serviceNUM is found in the file
                    if str(ticketNum) in part: #If the serviceNUM is found in the file
                        flag=1 
                        updatedLine=line #store the old line in UpdatedLine

    #if the flag was raised
    if (flag ==1):
        #Remove the line
        with open(fileName,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if updatedLine not in line:
                    f.write(line)
                    f.truncate()
                if (result[0] == "deleteservice" and loginType == "planner"):
                    print("Deleting service...")
                    deleteservice(result[1],result[2], validServices)

                if (result[0] == "sellticket"):
                    print("Selling ticket...")
                    sellticket(result[1], result[2], validServices)
