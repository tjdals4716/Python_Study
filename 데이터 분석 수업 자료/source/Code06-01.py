inFp = open("/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/CSV/singerA.csv", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()