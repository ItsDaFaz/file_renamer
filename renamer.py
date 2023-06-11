import os,csv
import natsort

#Read and store each row of personnel from the Key Resource Personnel List
listDict=[]
with open('list.csv') as f:
   for line in csv.DictReader(f, fieldnames=('serial','name','designation')):
      listDict.append(line)

#Returns new name following our standard format
def findName(name):
    for i in listDict:
        if i['name'] in name:
            #print(i['name'],name)
            return str(i['serial']+'. '+i['name']+' - '+i['designation']+'.docx')

# Get the list of all files and directories
inList = natsort.natsorted(os.listdir())
print(inList)

#main file renaming process
for i in inList:
    try:
        extCheck=i[-5:]
        #print(i[-5:])
        print(i[0:-5])
        newName=findName(i[0:-5])
        if extCheck ==".docx":
            #print("Rename\n"+i+"\nto\n"+newName)
            
            os.rename(i,newName)
    except Exception as e:
        print(e)
        print("Failed to rename ",i)
