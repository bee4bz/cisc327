import sys,os

#RUN AS python3 main_backend.py validServiceFile.txt transactionSummaryFile.txt centralFile.txt

#Function that adds the zeros on to a line item
def zeroRemaster(incoming):
    if incoming<10:
        final="000"+str(incoming)
    if incoming<100 and incoming>9:
        final="00"+str(incoming)
    if incoming<1000 and incoming>99:
        final="0"+str(incoming)
    if incoming<10000 and incoming>9999:
        final=str(incoming)
    else:
    	final=str(incoming)
    return final

cancelledTickets = 0
changedTickets = 0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

files = sys.argv[1:]
validServiceListFile = files[0]
transactionSummaryFile = files[1]
centralFile = files[2]

#Import old Valid Services List
fileName= os.path.join(__location__,validServiceListFile)
fileName2= os.path.join(__location__,transactionSummaryFile)
fileName3= os.path.join(__location__,centralFile)
summaryArray=[]
transactArray=[]
i=0

#Get the summary (Has all the services that are valid)
summary=[]
with open(fileName) as my_file:
    summary = my_file.read().splitlines()

# Get the central Services (has all the service number, tickets... )
central=[]
with open(fileName3) as my_file:
    central = my_file.read().splitlines()


# Get the transaction (grab the stuff just made. )
transact=[]
with open(fileName2) as my_file:
    transact = my_file.read().splitlines()

#Keep track of lines that have been taken out. Used to recreate the file later
linesTracker=[None]*len(central)


# loop statement
for f in range(0,(len(transact))):
#moves the transaction line to a temp list
    tempTrans=transact[f].split()
    #print (tempTrans)
    #SELL ----------------------
    #----------------------
    if (tempTrans[0]=='SEL'):
        #check if in summary file
        if not any(tempTrans[1] in s for s in summary):
            print('INVALID')
        #check in central services
        CServicesLine=[]
        #Keep track of lines that have been taken out. 
        lineTrack=0
        
        #Scan the central file for the transaction service ID
        for item in central:                    
            if tempTrans[1] in item:
                #print (item.split())
                CServicesLine= item.split() #if found, split it into this variable
                break;
                lineTrack=lineTrack+1
        
        #add the number of tickets in CServices
        CServicesLine[2]=zeroRemaster(int(CServicesLine[2])+int(tempTrans[2]))
        
        #keep line track and add it to the linetracker array with the new written line
        linesTracker[lineTrack-1]=str(CServicesLine[0]) +" "+ str(CServicesLine[1])+" "+str(CServicesLine[2]) +" "+ str(CServicesLine[3])
    #CANCEL ----------------------
    #----------------------
    if (tempTrans[0]=='CAN'):
        #check if in summary file
        if any(tempTrans[1] in s for s in summary):                    
            #check in central services
            CServicesLine=[]
            #Keep track of lines that have been taken out. 
            lineTrack=0
            flag = true
            #Scan the central file for the transaction service ID
            for item in central:				
                if tempTrans[1] in item:
                    ##print (item.split())
                    CServicesLine= item.split() #if found, split it into this variable
                    flag = false #THE PROPER SERVICE NUMBER HAS BEEN FOUND. NO NEED FOR ERROR
                    break;
                lineTrack=lineTrack+1

            if (flag):
                print('INVALID')
                sys.exit()

            #sub the number of tickets in CServices
            CServicesLine[2]=zeroRemaster(int(CServicesLine[2])-int(tempTrans[2]))
            
            #keep line track and add it to the linetracker array with the new written line
            linesTracker[lineTrack]=str(CServicesLine[0]) +" "+ str(CServicesLine[1])+" "+str(CServicesLine[2]) +" "+ str(CServicesLine[3])
        else:
            print ('INVALID')
            sys.exit()
    #CHANGE TICKET ----------------------
    #----------------------
    if (tempTrans[0]=='CHG'):
        #check if service number is in summary file
        #print("----------------------")
        #print("----------------------")
        if not any(tempTrans[1] in s for s in summary):
            print ('INVALID')
        #check if other service number is in summary file
        if not any(tempTrans[3] in s for s in summary):
            print ('INVALID')


        #check in central services
        CServicesLine=[]
        #Keep track of lines that have been taken out. 
        lineTrack=0

        #Scan the central file for the transaction service ID
        for item in central:                
            if tempTrans[1] in item:
                ##print (item.split())
                CServicesLine= item.split() #if found, split it into this variable
                break;
            lineTrack=lineTrack+1

        #sub the number of tickets in CServices
        CServicesLine[2]=zeroRemaster(int(CServicesLine[2])-int(tempTrans[2]))        

        #keep line track and add it to the linetracker array with the new written line
        linesTracker[lineTrack]=str(CServicesLine[0]) +" "+ str(CServicesLine[1])+" "+str(CServicesLine[2]) +" "+ str(CServicesLine[3])

        lineTrack=0
        #Scan the central file for the second transaction service ID
        for item in central:                
            if tempTrans[3] in item:
                #print (item.split())
                CServicesLine= item.split() #if found, split it into this variable
                break;
            lineTrack=lineTrack+1

        #add the number of tickets in CServices
        CServicesLine[2]=zeroRemaster(int(CServicesLine[2])+int(tempTrans[2]))
        ##print(CServicesLine[2])
        #print(linesTracker[2])
        #keep line track and add it to the linetracker array with the new written line
        linesTracker[lineTrack]=str(CServicesLine[0]) +" "+ str(CServicesLine[1])+" "+str(CServicesLine[2]) +" "+ str(CServicesLine[3])
    #Create service ----------------------
    #----------------------
    if (tempTrans[0]=='CRE'):
        #check number of tickets
        if (int(tempTrans[2])<1000 and int(tempTrans[2])>=0):
            #Add to summary
            if ((('DEL '+tempTrans[1]) not in open(fileName2).read()) and (('SEL '+tempTrans[1]) not in open(fileName2).read()) and (('CAN '+tempTrans[1]) not in open(fileName2).read()) and (('CHG '+tempTrans[1]) not in open(fileName2).read())):								
                #First check if the service already excists
                if tempTrans[1] in open(fileName).read():
                    print("INVALID")
                    sys.exit()
                else:			
                    tempList=[]
                    tempList=tempTrans[1].split() #seperate the temptrans variable by character
                if (len(tempList)==5) and (tempList[0]!= '0'): #Then check If list length is equal to five																	#check if first element not zero. 
                    with open(fileName, 'a') as file:
                        file.write(str(tempTrans[1])+'\n')
                    with open(fileName3, 'a') as file:
                        file.write(str(tempTrans[1])+' '+str(tempTrans[2])+' 0000'+str(tempTrans[4]))
                else:
                    print("INVALID")
                    sys.exit()							
            else:
                print("INVALID")
                sys.exit()
        else:
            print("INVALID")
            sys.exit()
                            

#Delete service ----------------------
    #----------------------
    if (tempTrans[0]=='DEL'):
        #Delete line from summary file
        f = open(fileName,"r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != tempTrans[1]:
                f.write(i)
        f.truncate()
        f.close()
		
#---------------------------------------
#Writing new Central Services File
#We take all the lines made by linestracker and add them to a new file, if they are not found, we take the 
#ones from the old central services file

for i in range(0,(len(central)-1)):
    if (linesTracker[i])==None: #if nothing is found in the element
        linesTracker[i]=central[i] #fill with the excisting line in the old central services file

#overwrite everything to a the central file!
with open(fileName3, "w+") as output:
    for item in linesTracker:
        output.write("%s\n" % item)

