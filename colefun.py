import sys,os

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

def changeticket(serviceNum,serviceNumNew,ticketNum,validServiceListFile):
    #Flag to determine if the Service Number is Found. One if YES
    flag =0
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    fileName= os.path.join(__location__,validServiceListFile)
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
    print(changedResult)
    #if the flag was raised
    if (flag ==1):
        #Write the new lines. 
        bufferLine=[]
        print(changedResult[2])
        if (int(changedResult[2]) > ticketNum):
            bufferLine= str(serviceNumNew) +" "+ zeroRemaster(int(changedResult[2])-ticketNum) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CHG "+str(bufferLine)+"\n")
        if (int(changedResult[2]) == ticketNum):
            bufferLine= str(serviceNumNew) +" "+ zeroRemaster(int(changedResult[2])) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CHG "+str(bufferLine)+"\n")




def cancelticket(serviceNum,ticketNum,validServiceListFile):

    flag =0
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    fileName= os.path.join(__location__,validServiceListFile)
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
    print(changedResult)
    #if the flag was raised
    if (flag ==1):
        #Write the new lines. 
        bufferLine=[]
        print(changedResult[2])
        if (int(changedResult[2]) > ticketNum):
            bufferLine= changedResult[1] +" "+ zeroRemaster(int(changedResult[2])-ticketNum) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CHG "+str(bufferLine)+"\n")
        if (int(changedResult[2]) == ticketNum):
            bufferLine= changedResult[1] +" "+ zeroRemaster(int(changedResult[2])) +" "+changedResult [3] +" "+ changedResult [4]+" "+changedResult [5]
            print (bufferLine)
            with open(fileName, 'a') as file:
                file.write("CAN "+str(bufferLine)+"\n")



cancelticket(1,1,"transactionSummaryFile.txt")

