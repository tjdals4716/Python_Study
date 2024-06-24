def plus(v1, v2):
    result = 0
    result = v1 + v2
    # 위로 리턴시킨다는 의미, 그래서 플러스 함수가 쓰이는 것
    return result

sum = 0

# 이 부분이 먼저 작동 후 위 함수가 작동
sum = plus(100, 200)
print("100과 200dml plus() 함수 결과 : ", sum)