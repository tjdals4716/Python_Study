list = [30, 10, 20]
print("현재 리스트 : ", list)

list.append(40)
print("추가 후 리스트 : ", list)

print("pop 함수로 추출한 값 : ", list.pop())
print("pop 함수 사용 후 리스트 : ", list)

list.sort()
print("sort 함수 사용 후 리스트", list)

print("20값의 위치 : ", list.index(20))

list.insert(2, 222)
print("insert 함수 사용 후 리스트 : ", list)

list.remove(222)
print("remove 함수 사용 후 리스트 : ", list)

list.extend([77, 88, 77])
print("extend 함수 사용 후 리스트 : ", list)

# print("77 값의 개수  : ", list[77])