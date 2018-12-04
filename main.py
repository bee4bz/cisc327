import sys,os

cancelledTickets = 0
changedTickets = 0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():

    
    global __location__
    global cancelledTickets
    global changedTickets

    while True:
        files = sys.argv[1:]
        validServiceListFile = files[0]
        transactionSummaryFile = files[1]

        #Start Code: Login Agent
        while True:
            start = input("Please login and specify login type (agent/planner):")

            if (start == "exit"):
                sys.exit()
            elif (start != "login agent" and start != "login planner"):
                print("Incorrect login format. Enter login agent or login planner.")
            else:
                transac,loginType = start.split(" ")
                break

        #init Services file
        validServices = []

        #opens the service list file and copies each line to "line"
        with open(os.path.join(__location__,validServiceListFile)) as serviceListFile:
            for line in serviceListFile:
                line = line.rstrip()
                validServices.append(line)

        #print the line
        #print(validServices)

        print("Logged in as " + loginType + ".")

        tempServices = []

        #Get transaction
        while True:
            transaction = input("Enter your transaction:")

            if (transaction == "logout"):
                print("Logging out. Transaction summary file generated.")
                cancelledTickets = 0
                changedTickets = 0
                validServices.append(tempServices)
                break
            result = transaction.split(" ")
            if (result[0] == "createservice" and loginType == "agent"):
                print("Must be a planner to create a service.")

            if (result[0] == "createservice" and loginType == "planner"):
                print("Creating service...")
                try:
                    temp = createservice(result[1],result[2],result[3], transactionSummaryFile,validServiceListFile)
                    tempServices.append(temp)
                except Exception as err:
                    print("Invalid Response")
    

            if (result[0] == "deleteservice" and loginType == "agent"):
                print("Must be a planner to delete a service.")

            if (result[0] == "deleteservice" and loginType == "planner"):
                print("Deleting service...")
                deleteservice(result[1],result[2], transactionSummaryFile,validServiceListFile)

            if (result[0] == "sellticket"):
                print("Selling ticket...")
                sellticket(result[1], result[2], transactionSummaryFile,validServiceListFile)

            if (result[0] == "changeticket"):
                print("Changing ticket...")
                changeticket(result[1], result[2], result[3], transactionSummaryFile,validServiceListFile, loginType)

            if (result[0] == "cancelticket"):
                print("Cancelling ticket...")
                cancelticket(result[1], result[2],transactionSummaryFile, loginType)
            

def createservice(serviceNum,date,serviceName, validTransaction,validServices):
    try:
        serviceNumber = int(serviceNum)
        #print (serviceNumber)
    except ValueError:
        print("Illegal service number. Not a number.")
        return 

    if (len(serviceNum) != 5 or serviceNum[0] == 0):
        print("Illegal service number. Must be 5 numbers and not start with 0")
        return 

    if (serviceNum in validServices):
        print("Service with that service number already exists")
        return 

    try:
        dateNum = int(date)
    except ValueError:
        print("Illegal date. Not a number.")
        return 

    if (len(date) != 8):
        print("Illegal date.")
        return 

    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    if (year < 1980 or year > 2999 or month < 1 or month > 12 or day < 1 or day > 31):
        print("Illegal date. Date format incorrect.")
        return 

    if (len(serviceName) < 3 or len(serviceName) > 39):
        print("Illegal service name. Must be between 3 and 39 characters")
        return 


    global __location__
    fileName= os.path.join(__location__,validTransaction)
    fileName2= os.path.join(__location__,validServices)
    bufferLine=[]
    bufferLine= str(serviceNum) +" 0000 0000 "+serviceName+" "+date
    ##print (bufferLine)
    with open(fileName, 'a') as file:
         file.write("CRE "+str(bufferLine)+"\n")
    with open(fileName2, 'a') as file:
         file.write(str(serviceNum)+"\n")

    return serviceNum

def deleteservice(serviceNum, serviceName, validServices,validTransListFile):
    flag=0
    try:
        serviceNumber = int(serviceNum)
    except ValueError:
        print("Illegal service number. Not a number.")
        return 

    if (len(serviceNum) != 5 or serviceNum[0] == 0):
        print("Illegal service number. Must be 5 numbers and not start with 0")
        return 
        
    global __location__
    fileName= os.path.join(__location__,validServices)
    fileName2= os.path.join(__location__,validTransListFile)
    #check new servicenumber in service list file!!!
    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNum) in part: #If the serviceNUM is found in the file
                    flag=1
    bufferLine=[]
    bufferLine= str(serviceNum) +" 0000 0000 "+serviceName+" 00000000"
   ## print (bufferLine)
    if flag ==1:
        with open(fileName, 'a') as file:
            file.write("DEL "+str(bufferLine)+"\n")

        with open(fileName2,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if str(serviceNum) not in line:
                    f.write(line)
            f.truncate()
    else:
        print("Service with that service number does not exist.")
        return 

    #store in trans summary file and remove from validservices

def sellticket(serviceNum, numTickets, validTransactionFile, validServices):
    global __location__
    fileName= os.path.join(__location__,validTransactionFile)

    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if (not str(serviceNum) in part): #If the serviceNUM is found in the file
                    print("Service with that service number does not exist.")
                    return  

    try:
        serviceNumber = int(serviceNum)
    except ValueError:
        print("Illegal service number. Not a number.")
        return 

    try:
        numberTickets = int(numTickets)
    except ValueError:
        print("Illegal service number. Not a number.")
        return 

    if (numberTickets < 1 or numberTickets > 1000):
        print("Illegal number of tickets. Must be between 1 and 1000")
        return 

    #subtract ticket number from total ticket count, store in trans summary file

    flag=0
    
    #___location___ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file___)))
    fileName= os.path.join(__location__,validTransactionFile)
    flag=1
    # #open transactionSummaryFile
    # with open(fileName) as summaryfile:
    #     for line in summaryfile:
    #         for part in line.split():
    #             if str(serviceNum) in part: #If the serviceNUM is found in the file
    #                 flag=1+flag
    #                 updatedLine=line #store the old line in UpdatedLine
    #                 print (flag)
    #             else: 
    #                 print("That service exists, but has no more tickets for sale")
    
    bufferLine=[]
    bufferLine= str(serviceNum) +" "+ numTickets+" 0000 000000 00000000"
    print (bufferLine)
    with open(fileName, 'a') as file:
        file.write("SEL "+str(bufferLine)+"\n")
   

#Function that adds the zeros on to a line item
def zeroRemaster(incoming):
    if incoming<10:
        final="000"+str(incoming)
    if incoming<100 and incoming>9:
        final="00"+str(incoming)
    if incoming<1000 and incoming>99:
        final="0"+str(incoming)
    if incoming<10000 and incoming>9999:
        final=+str(incoming)
    return final

def changeticket(serviceNum,serviceNumNew,ticketNum,validTransactionFile,validServiceListFile,loginType):
    global changedTickets

    if (loginType == "agent" and changedTickets >= 20):
        print("Error. You may not change more than 20 tickets per session as an agent.")
        return

    #Flag to determine if the Service Number is Found. One if YES
    flag =0
    global __location__
    fileName= os.path.join(__location__,validServiceListFile)
    fileNameTransaction= os.path.join(__location__,validTransactionFile)
    #open transactionSummaryFile
    with open(fileNameTransaction) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNum) in part: #If the serviceNUM is found in the file
                    flag=1+flag
                    updatedLine=line #store the old line in UpdatedLine
                    print ("line")
                    print (line)

                    #DOESN"T ENTER THIS!!
    #check new servicenumber in service list file!!!
    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNumNew) in part: #If the serviceNUM is found in the file
                    flag=1+flag
                    print (line)

    if (flag <= 1):
        print("Invalid service numbers. Both must be existing service numbers.")
        return
    #Parse and change the ticket
    changedResult=[]

    try:
        changedResult = updatedLine.split(" ")
    except Exception as err:
        print("Invalid")
    
    #if the flag was raised
    if (flag ==2):
        #Write the new lines.
        bufferLine=[]
        
        if (int(changedResult[1]) > int(ticketNum)):
            bufferLine= str(serviceNumNew) +" "+ zeroRemaster(int(changedResult[2])-int(ticketNum)) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileNameTransaction, 'a') as file:
                file.write("CHG "+str(bufferLine)+"\n")
        if (int(changedResult[1]) == int(ticketNum)):
            bufferLine= str(serviceNumNew) +" "+ zeroRemaster(int(changedResult[2])) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileNameTransaction, 'a') as file:
                file.write("CHG "+str(bufferLine)+"\n")

    if (loginType == "agent"):
        changedTickets += int(ticketNum)




def cancelticket(serviceNum,ticketNum,validServiceListFile,loginType):
    global cancelledTickets

    if (loginType == "agent" and cancelledTickets >= 20):
        print("Error. Too many tickets cancelled in one session as agent.")
        return

    flag =0
    global __location__
    fileName= os.path.join(__location__,validServiceListFile)
    #open transactionSummaryFile
    with open(fileName) as summaryfile:
        for line in summaryfile:
            for part in line.split():
                if str(serviceNum) in part: #If the serviceNUM is found in the file
                    flag=1
                    updatedLine=line #store the old line in UpdatedLine

    if (flag == 0):
        print("Invalid service number. That service does not exist.")
        return

    #Parse and change the ticket
    changedResult=[]
    changedResult = updatedLine.split(" ")
    print(changedResult)
    #if the flag was raised
    if (flag ==1):
        #Write the new lines.
        bufferLine=[]
        print(changedResult[2])
        if (int(changedResult[2]) > int(ticketNum)):
            bufferLine= changedResult[1] +" "+ zeroRemaster(int(changedResult[2])-ticketNum) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CAN "+str(bufferLine)+"\n")
        if (int(changedResult[2]) == int(ticketNum)):
            bufferLine= changedResult[1] +" "+ zeroRemaster(int(changedResult[2])) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CAN "+str(bufferLine)+"\n")

    if (loginType == "agent"):
        cancelledTickets += int(ticketNum)

main()
