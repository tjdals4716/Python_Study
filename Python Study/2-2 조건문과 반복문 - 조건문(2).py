# 6-2 조건문과 반복문 - 조건문(2)

# 다중 조건에 대해서
# 다중 조건은 elif를 사용
day = input("요일을 입력해주세요(0~6) : ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축 영업")
elif day == "1":
    print("연장 영업")
else:
    print("정상영업")