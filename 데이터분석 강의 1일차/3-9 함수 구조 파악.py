# 함수 선언 부분
def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

# 변수 선언 (0으로 초기화)
sum = 0

# 메인 코드 부분
sum = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 : ", sum)
sum = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 : ", sum)