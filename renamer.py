import os,csv
import natsort
from thefuzz import fuzz
#Read and store each row of personnel from the Key Resource Personnel List
listDict=[]
with open('./project_team.csv') as f:
   for line in csv.DictReader(f, fieldnames=('serial','name','designation')):
      listDict.append(line)

def similar(a, b):
    return fuzz.ratio(a, b)


print(listDict)

#Returns new name following our standard format
def findName(name):
    max_similar_score=0
    max_score_item=[None]*3
    for i in listDict:
        similar_score=similar(i['name'],name)
        if similar_score>max_similar_score:
            max_similar_score=similar_score
            max_score_item[0]=i['serial']
            max_score_item[1]=i['name']
            max_score_item[2]=i['designation']
    print(f"Max score is {max_similar_score}%")
    print("Max "+str(str(max_score_item[0])+'. '+max_score_item[1]+' - '+max_score_item[2]+'.docx\n'))

    return str(str(max_score_item[0])+'. '+max_score_item[1]+' - '+max_score_item[2]+'.docx')
    

# Get the list of all files and directories
inList = natsort.natsorted(os.listdir())
#print(inList)

# main file renaming process
count=0
fail_count=0
for i in inList:

    try:
        extCheck=i[-5:]
        #print(i[-5:])
        print("for "+i[0:-5])
        newName=findName(i[0:-5])
        if extCheck ==".docx":
            os.rename(i,newName)
    except Exception as e:
        print("Failed to rename ",i)
        fail_count+=1
    count+=1

print(f"There are {count} files checked")
print(f"{fail_count} files have failed")



