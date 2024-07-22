import random

# 빈 리스트에 랜덤으로 0 ~ 9까지 수를 10번 찍음
list = []
for num in range(0, 10):
    list.append(random.randrange(0, 10))
print("생성된 리스트 : ", list)

# 존재하지 않은 값만 출력하게 하는 코드
for num in range(0, 10):
    if num not in list:
        print("숫자 %d는 리스트에 존재하지 않습니다" %num)