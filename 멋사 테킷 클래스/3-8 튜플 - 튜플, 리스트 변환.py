# 7-8 튜플 - 튜플, 리스트 변환

tup = (1, 20, 40)

# for 뒤에는 새로 선언한 함수를, in 뒤에는 순회할 자료구조를 넣어주면 됨
for x in tup:
    print(x)


tup = (1, 20, 40)

# 튜플을 리스트로 변환하는 방법 1 (튜플을 list로 감싸는 방법)
list_1 = list(tup)
print(list_1)

# 튜플을 리스트로 변환하는 방법 2
list_2 = [x for x in tup]
print(list_2)

# 튜플을 리스트로 변환하는 방법 3 (for문을 사용)
# for문을 이용하여 하나하나 값을 추가하는 방법
list_3 = []

for x in tup:
    list_3.append(x)
print(list_3)