# 7-2 리스트 - 리스트 데이터 접근 및 조작

colors = ['red', 'blue', 'green']

# 리스트 2자리(green)를 black으로 수정하는 방법
colors[2] = 'black'
print(colors)

# 리스트 추가하는 방법(append 사용, 안에 추가를 원하는 데이터를 입력하면 됨)
# append 함수는 가장 마지막 순서에 purple을 배치에서 출력함
colors.append('purple')
print(colors)

# 순서를 중점으로 리스트 추가하는 방법 (insert 함수 사용)
# 괄호에 어떤 데이터의 인덱스를 넣을 것인지를 정해줘야함
# 1번 인덱스에 yellow를 넣는다는 뜻(인덱스 순서는 0, 1, 2, 3 ... )
colors.insert(1, 'yellow')
print(colors)

# 리스트를 제거하는 방법 1 (del 사용)
del colors[0]
print(colors)

# 리스트를 제거하는 방법 2 (pop 사용)
# 인자로 인덱스를 취해서 사용함
# 데이터를 삭제하면서 참초하려면 del보단 pop을 사용해야함
color = colors.pop(0)
print(colors)
print(color)

# 리스트를 제거하는 방법 3 (remove 사용)
# 리스트에 값을 알고있어야 사용이 가능
colors.remove('blue')
print(colors)