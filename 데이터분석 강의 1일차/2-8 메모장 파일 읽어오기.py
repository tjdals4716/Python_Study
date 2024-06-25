# 입력 파일
inFp = None
# 읽어온 문자열
inStr = "" 

inFp = open("파일 경로 설정")

# 첫 번째 라인
inStr = inFp.readline()
print(inStr, end = "")

# 두 번째 라인
inStr = inFp.readline()
print(inStr, end = "")

# 세 번째 라인
inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
