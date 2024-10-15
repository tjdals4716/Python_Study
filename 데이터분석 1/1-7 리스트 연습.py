list = ['a', 'b', 'c', 'd']
print(list)

# 리스트를 추가할 땐 append 함수를 사용
list.append("나도 추가")
print(list)

a = input("값을 입력하세요 : ")

if a in list:
    print("리스트에 존재하는 값입니다")
else:
    print("리스트에 값이 존재하지 않습니다")