# 8-1 함수 - 함수(1)

# 함수명, 매개변수, 함수 구현도 이렇게 나눌 수가 있음
# 매개변수(파라미터), 인자(인수) (이 개념에 대해서 강의 다시 한 번 보기)

# 프로그래밍에서의 함수는 코드의 집합
# name이라는 매개변수(파라미터)를 넣어서 활용 (이 부분 강의 다시 한 번 보기)
def print_name(name):
    print(f'이름은 {name}입니다')

# 여러개를 사용해도 누적되어 사용되지 않고 반복적으로 사용가능
# 여기서 홍길동, 김길동은 인자(인수) 
print_name("홍길동")
print_name("김길동")

# 아래는 위와 다르게 매개변수 없이 선언
# 그러므로 밑에 print_string() 부분도 매개변수 없이 해줘야함
def print_string():
    print('예시 문자열 입니다.')

print_string()

# 이름과 나이를 한꺼번에 이용한 예시
def print_name_age(name, age):
    print(f'이름은 {name}이고 나이는 {age}살 입니다.')

print_name_age("홍길동", "25")