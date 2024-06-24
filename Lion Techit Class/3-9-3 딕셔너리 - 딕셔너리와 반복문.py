# 7-12 딕셔너리 - 딕셔너리와 반복문

tech = {
    "HTML" : "Advanced",
    "JavaScript" : "Intermdiate",
    "Python" : "Expert",
    "Go" : "Novice"
}

# 키만 할당하게 됨
for i in tech:
    print(i)

# 키와 값 둘다 선언 가능. 둘다 출력함
for key, value in tech.items():
    print(f'{key} - {value}')

# 전체 키만 출력
for key in tech.keys():
    print(key)

# 전체 값만 출력
for value in tech.values():
    print(value)
