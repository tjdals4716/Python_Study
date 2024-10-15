# 정수형 타입


# 문자형 타입
text = "hello, world!"
text2 = "HELLO, WORLD!"
text3 = "apple, banana, cherry"

# 첫 번째 문자만 대문자로 바꿔줌
a = text.capitalize()
print("1. capitalize 함수 결과 : ", a)

# 모든 문자를 대문자로 바꿔줌
b = text.upper()
print("2. upper 함수 결과 : ", b)

# 모든 문자를 소문자로 바꿔줌
c = text2.lower()
print("3. lower 함수 결과 : ", c)

# 앞 뒤 빈칸을 없애줌
d = text.strip()
print("4. strip 함수 결과 : ", d)

# 첫 번째 인자의 문자를 두 번째 인자의 문자로 바꿈
e = text.replace("world", "hi")
print("5. replace 함수 결과 : ", e)

# 특정 문자 기준으로 쪼개줌
f = text.split(",")
print("6. split 함수 결과 : ", f)

# join = split의 반대


# 시작하는 문자가 일치하면 true 아니면 false를 출력
print(text.startswith("hello"))
print(text.startswith("world"))

# 이외에도 대소문자를 서로 바꿔주는 swapcase, 맨 앞에만 대문자로 바꿔주는 title, 앞에 매개변수만큼 0을 채워주는 number.zfill, text.zfill 등이 있음

