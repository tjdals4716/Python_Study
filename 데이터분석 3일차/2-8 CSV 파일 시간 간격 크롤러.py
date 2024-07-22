# CSV 파일은 텍스트로 이뤄진 파일을 말함
# 시간 간격은 변화하는 시간에 대한 데이터를 저장하는 것을 말함. 여기서는 CSV 파일을 사용하여 저장하였으니 CSV 파일에 변화하는 시간 데이터를 저장함. 엑셀에서도 활용가능하다함
import csv
import time
import datetime

csvName =  '/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/CSV/datetime.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초'])

count = 10
while count > 0 :
    count -= 1

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss]
    print(time_list)

    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    # 3초마다 동작을 시킴
    time.sleep(5)
