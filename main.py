import sys

def main(validServiceListFile):
    #files = sys.argv[1:]

    #validServiceListFile = files[0]
    #transactionSummaryFile = files[1]


    #Start Code: Login Agent
    while True:
        start = input("Please login and specify login type (agent/planner):")
        if (start != "login agent" and start != "login planner"):
            print("Incorrect login format. Enter login agent or login planner.")
        else:
            transac,loginType = start.split(" ")
            break
        
    #init Services file
    validServices = []

    #opens the service list file and copies each line to "line"
    with open(validServiceListFile) as serviceListFile:
        for line in serviceListFile:
            line = line.rstrip()
            validServices.append(line)

    #print the line
    print(validServices)

    print("Logged in as " + loginType + ".")

    tempServices = []

    #Get transaction
    while True:
        transaction = input("Enter your transaction:")

        if (transaction == "logout"):
            print("Logging out. Transaction summary file generated.")
            #GENERATE TRANSACTION SUMMARY. probably seperate method.
            break

        result = transaction.split(" ")
        if (result[0] == "createservice" and loginType == "planner"):
            print("creating service")
            createservice(result[1],result[2],result[3])
            
def createservice(serviceNum,date,serviceName):
    
        

    

    #fileObject = open(transactionSummaryFile, "w")

    #start = raw_input()
    #start = start.split(" ")

    #if start[0] == login:
      #  startLogin(start[1])

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
    with open(fileName,"r+") as f:
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
    else
        bufferLine[0]= str(serviceNumNew) + changedResult [1] + str(ticketNum) + changedResult [3] + changedResult [4]





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
    
    
main("validServiceList.txt")
