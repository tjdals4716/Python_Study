inFp = None 
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()
