# 리스트와 합을 0으로 초기화
list = [0, 0, 0, 0]
sum = 0

list[0] = int(input("첫 번째 숫자 : "))
list[1] = int(input("두 번째 숫자 : "))
list[2] = int(input("세 번째 숫자 : "))
list[3] = int(input("네 번째 숫자 : "))

sum = list[0] + list[1] + list[2] + list[3]

print("리스트에 있는 숫자의 합 : ", sum)