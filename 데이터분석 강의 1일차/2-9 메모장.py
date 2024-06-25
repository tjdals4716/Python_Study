inFp = None
inStr = "" 

inFp = open("파일 경로 설정")

inList = inFp.readlines()
print(inList)

inFp.close()