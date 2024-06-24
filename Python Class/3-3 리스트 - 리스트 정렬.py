# 7-3 리스트 - 리스트 정렬

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬(sort)이라는 메서드를 이용하여 정렬하는 방법
colors.sort()
print(colors)

# 정렬을 통해 역순으로 정렬하는 방법
colors.sort(reverse=True)
print(colors)

# 정렬을 통한 정렬
# 원본데이터를 유지하느냐, 변경하느냐에 따라서 알맞게 위 아래 방법을 사용하면 됨
print(sorted(colors))

# 리스트의 길이 - 요소의 갯수(len 사용)
# 리스트의 갯수를 출력 (총 6개)
print(len(colors))

# 데이터가 존재하지않는 인덱스를 출력하려할땐 오류가 발생함
# ex) print(colors[7])

# 강의 확인
print(colors[-1])