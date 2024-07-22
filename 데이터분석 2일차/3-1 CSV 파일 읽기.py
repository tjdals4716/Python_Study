# CSV 파일은 텍스트로 이뤄진 파일을 말함
inFp = open("/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/CSV/datetime.csv", "r", )

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()