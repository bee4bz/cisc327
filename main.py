import sys

def main(validServiceListFile):

    while True:
        #files = sys.argv[1:]
    
        #validServiceListFile = files[0]
        #transactionSummaryFile = files[1]
        #fileObject = open(transactionSummaryFile, "w")

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
            if (result[0] == "createservice" and loginType == "agent"):
                print("Must be a planner to create a service.")

            if (result[0] == "createservice" and loginType == "planner"):
                print("Creating service...")
                do = createservice(result[1],result[2],result[3], validServices)

            if (result[0] == "deleteservice" and loginType == "agent"):
                print("Must be a planner to delete a service.")

            if (result[0] == "deleteservice" and loginType == "planner"):
                print("Deleting service...")
                deleteservice(result[1],result[2], validServices)

            if (result[0] == "sellticket"):
                print("Selling ticket...")
                sellticket(result[1], result[2], validServices)
            
def createservice(serviceNum,date,serviceName, validServices):
    try:
        serviceNumber = int(serviceNum)
    except ValueError:
        print("Illegal service number. Not a number.")
        return false
    
    if (len(serviceNum) != 5 or serviceNum[0] == 0):
        print("Illegal service number. Must be 4 numbers and not start with 0")
        return false

    if (serviceNum in validServices):
        print("Service with that service number already exists")
        return false

    try:
        dateNum = int(date)
    except ValueError:
        print("Illegal date. Not a number.")
        return false

    if (len(date) != 8):
        print("Illegal date.")
        return false
    
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    if (year < 1980 or year > 2999 or month < 1 or month > 12 or day < 1 or day > 31):
        print("Illegal date. Date format incorrect.")
        return false

    if (len(serviceName) < 3 or len(serviceName) > 39):
        print("Illegal service name. Must be between 3 and 39 characters")
        return false

    #PASSED ALL TESTS, STORE IN TRANS SUMMARY FILE + add to tempservices

def deleteservice(serviceNum, serviceName, validServices):
    try:
        serviceNumber = int(serviceNum)
    except ValueError:
        print("Illegal service number. Not a number.")
        return false
    
    if (len(serviceNum) != 5 or serviceNum[0] == 0):
        print("Illegal service number. Must be 5 numbers and not start with 0")
        return false

    if (not serviceNum in validServices):
        print("Service with that service number does not exist.")
        return false

    #store in trans summary file and remove from validservices

def sellticket(serviceNum, numTickets, validServices):    
    if (not serviceNum in validServices):
        print("Service with that service number does not exist.")
        return false

    try:
        serviceNumber = int(serviceNum)
    except ValueError:
        print("Illegal service number. Not a number.")
        return false

    try:
        numberTickets = int(numTickets)
    except ValueError:
        print("Illegal service number. Not a number.")
        return false

    if (numberTickets < 1 or numberTickets > 1000):
        print("Illegal number of tickets. Must be between 1 and 1000")
        return false
    
    #subtract ticket number from total ticket count, store in trans summary file

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
    else:
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
                if (result[0] == "deleteservice" and loginType == "planner"):
                    print("Deleting service...")
                    deleteservice(result[1],result[2], validServices)

                if (result[0] == "sellticket"):
                    print("Selling ticket...")
                    sellticket(result[1], result[2], validServices)

    
main("validServiceList.txt")
