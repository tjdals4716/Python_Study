numbers = [42, 15, 23, 34, 21]
print("원본 리스트 : ", numbers)

# sort 함수는 작은 것부터 정렬
numbers.sort()
print("1. 정렬된 리스트 : ", numbers)

# append는 추가
numbers.append(50)
print("2. 추가 후 : ", numbers)

# pop은 맨 뒤의 하나를 뺌, 그리고 뺀 것을 새로운 값에 리턴
pop_number = numbers.pop()
print("3-1. 제거된 숫자 : ", pop_number)
print("3-2. 제거 후 : ", numbers)

# pop에 매개변수 값이 들어가면 매개변수 특정 위치 원소를 꺼냄 (0부터 시작)
numbers.pop(3)
print("4. 특정 원소만 뺌 : ", numbers)

# 3번째 바로 뒤에 (0부터 시작) 두 번째 인자값 삽입
numbers.insert(3, 5)
print("5. 추가된 리스트 : ", numbers)

# 특정 원소 삭제
numbers.remove(42)
print("6. 삭제된 후 : ", numbers)

# 원소를 뒤집음
numbers.reverse() # 참고로 괄호 빼고 reverse만 쓰면 맨 앞, 맨 뒤만 위치 바낌
print("7. 뒤집은 결과 : ", numbers)

# 슬라이싱 참고
slice_number = numbers[1:4]
print("8. 슬라이싱 된 숫자 : ", slice_number)