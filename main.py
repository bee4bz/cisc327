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


    
    
main("validServiceList.txt")
