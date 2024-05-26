# 5-3 변수와 자료형 - 문자열(1)

# 문자열(Strings) = 문자의 나열

city = "seoul"
print(city)

city.upper()
print(city.upper())

city = city.upper()
print(city)

# 이렇게 하면 아직은 변환이 안됨
city.lower()
print(city)

city.lower()
print(city.lower())

city = city.lower()
print(city)

# 공백 처리

occupation = "   developer   "
print(occupation)

# rstrip()은 우측 공백을 지워주는 함수
occupation.rstrip()
print(occupation.rstrip())

# lstrip()은 좌측 공백을 지워주는 함수
occupation.lstrip()
print(occupation.lstrip())

# strip()은 좌우측 모두 공백을 지워주는 함수
occupation.strip()
print(occupation.strip())

# \n은 한줄씩 엔터로 띄어서 출력하라는 뜻
print("INFP\nENFP\nISTJ\nESTJ")
# \t는 tap씩 띄어서 출력하라는 뜻
print("INFP\tENFP\tISTJ\tESTJ")