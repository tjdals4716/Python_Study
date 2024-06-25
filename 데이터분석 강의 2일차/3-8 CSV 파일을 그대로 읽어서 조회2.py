def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

with open("/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/CSV/datetime.csv", "r") as inFp :
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)