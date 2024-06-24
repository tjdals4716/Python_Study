# 7-4 리스트 - 리스트 슬라이싱 및 복사

# 리스트 슬라이싱 : 원하는 범위에 리스트를 잘라 사용하는 것을 말함 ([:] 사용)

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 전체요소를 반환해서 새로운 변수에 할당한다는 뜻
colors_2 = colors[:]

colors_2.pop()

print(colors)
print(colors_2)

# 두 번째 인덱스에서 여섯 번째 인덱스를 잘라서 가져오고 싶다는 뜻
print(colors[1:5])
# 첫 번째 부터 네 번째 까지를 슬라이스해서 출력
print(colors[:4])
# 세 번째 인덱스 부터 끝까지 슬라이스해서 출력
print(colors[2:])
# 끝에서 첫 번째를 출력하고 싶으면 아래와 같이 음수를 사용하면 됨
print(colors[-1])
# -5까지 모든 값을 출력
print(colors[-5:])