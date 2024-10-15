with open("/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/CSV/datetime.csv", "r") as inFp :
    with open("/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/CSV/datetime.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            # replace 함수로 .을 /로 변경한다는 뜻
            row_list[-1] = row_list[-1].replace('.', '/')
            height_str = "{0:.2f}".format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')

print('Save. OK~')