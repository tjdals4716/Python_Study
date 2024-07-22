# 5-1. 변수와 자료형 - 변수 선언

print("안녕하세요")

# greeting 이라고 하는 변수를 선언
# 이 변수에 문자열 값을 할당 
greeting = "안녕하세요:)"
print(greeting)

# 변수의 특징은 데이터를 변경해서 할당할 수 있는 공간
greeting = "반갑습니다"
print(greeting)


# 5-2 변수와 자료형 - 변수 선언 시 주의 사항
'''
# Naming Convention(명명 규칙)

# 1. 변수 사이의 공백은 허용되지 않는다.
# greet ing, my greeting 등 띄어쓰기나 공백 등을 포함한 이런건 안된다는 것
greeting = "안녕하세요"

# 2. 1.을 해결하기 위해 단어 사이는 _(언더스코어)를 사용하여 연결
my_greet = "안녕하세요"
myString = "hi"

# 3. 변수를 선언하기 위한 문자열은 숫자, 특수문자로 시작이 불가하다.
# 1_greeting, !_greeting 이런건 안된다는 것.
# 앞에 시작하는 문자는 반드시 영문자로 해줘야함. 그 뒤는 상관 X
greeting_1 = "안녕"

# 4. 예약어는 변수로 선언이 불가하다.
# print = "안녕" 이런것이 안된다는 것

# 5. 변수는 가급적 소문자를 사용하는 것이 좋음.

# 6. 오타를 주의해야하는 것이 가장 중요!
# Ctrl-F를 통해 직접 검색을 해서 찾을 수도 있음.
'''

# 5-3 변수와 자료형 - 문자열(1)
'''
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
'''

# 5-4 변수와 자료형 - 문자열(2)
'''
score = "점수 : 90"
# removeprefix() : 없애고 싶은 부분의 문자열을 입력해서 없애주는 함수
print(score.removeprefix("점수 : "))

score_2 = "75점"
# removesuffix() : 없애고 싶은 부분의 문자열을 입력해서 없애주는 함수
print(score_2.removesuffix("점"))

# 문자열을 가지고 치환을 하는 방법
city = "서울 중구"
# 처음엔 바꿀 문자열을 선택, 다음에 어떤 문자열로 바꾸고싶은지 선택
print(city.replace("서울", "서울시"))
'''

# 5-5 변수와 자료형 - 문자열(3)
'''
# 문자열과 변수를 한꺼번에 다루는 방법
si_1 = "대구"
gu_1 = "달서"
# f string을 활용한 함수 선언. f string이 아니라면 +를 사용해서 일일히 모두 선언해줘야함
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

# 대구시 달서구
# 서울시 종로구
# (시의 이름)시 (구의 이름)구 이렇게 출력되게 하고싶음
# f string을 사용. {}를 사용해서 표현하면 됨
print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구")
'''

# 5-6 변수와 자료형 - 숫자(1)
'''
# 정수에 대해서

# a에 2를 선언, b에 3을 선언
a = 2
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 이 외에도 파이썬에서는 더 많은 연산이 있음

# 제곱수를 구하는 식. 밑에 식은 a의 b승의 계산 결과를 알려줌
print(a ** b)

# 더하기 연산을 먼저한다고 명령. 괄호를 하지않는다면 곱하기를 우선으로 처리함
print((a + b) * b)

# 나누기의 결과로 몫을 얻는 방법
print(a // b)

# 나누기의 결과로 나머지를 얻는 방법
print(a % b)

# 실수에 대해서 - 십진 부동 소수점

x = 10.0
y = 0.3
z = 1

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x + z)
print(x - z)
print(x * z)
print(x / z)

# 실수와 연산하는 수는 그 결과가 모두 실수이다
'''

# 5-7 변수와 자료형 - 숫자(2)
# 이 부분 마지막 상수 부분 다시 보기
'''
# 세자리마다 _(언더스코어)를 넣어주면 됨
# 두 정수는 동일한 값을 나타냄
price_1 = 12_349_000_000_000
price_2 = 12349000000000
print(price_1)
print(price_2)

# 상수(contants)
# 파이썬은 최초에 할당된 값을 고정시킴. 소문자는 변수 대문자는 상수
PI = 3.141592

# 이렇게 재할당이 되어선 안됨
PI = 1.23

print(PI)
'''

# 5-8 변수와 자료형 - 숫자(3)
'''
# 문자열 - 숫자 간 형 변환

a = 100
b = "100"
c = "0.453"

# str = string의 약자
a = str(a)
# 정수를 선언하고 싶다면 int를 사용하면 됨
b = int(b)
# 실수를 선언하고 싶다면 float를 사용
c = float(c)
'''

# 5-9 변수와 자료형 - 논리형(부울)
'''
# 논리형(Bool, Boolean)
# 대문자로 시작하는 키워드
True
False

# 이렇게 출력하면 해당 값에 대해서 참이라는 결과가 출력됨
print(3 > 2)
# 이렇게 출력하면 해당 값에 대해서 거짓이라는 결과가 출력됨
print(3 == 2)
# 형이 다른데 왜 참인가? 파이썬에서는 값을 비교하는 연산자가 == 외에도 하나 더 있음
print(3 == 3.0)
# == 외에도 하나 더 있다는 것이 바로 is. ==는 같은 값을 가진다고 추정. 하지만 is는 타입을 확인함. 그러므로 False를 출력
print(3 is 3.0)
'''

# 5-10 변수와 자료형 - 명령 프롬프트
'''
# input()은 사용자가 어떠한 데이터를 입력해주기를 기다리고있는 것
# input()은 콘솔창에서 값을 입력하기 전까지 실행을 종료하지 않음

# input() 예시
# input("설치를 계속 진행하시겠습니까? : ")

# text = 를 하면 text라고 선언한 함수로 input으로 받은 값을 저장하는 것
text = input("출력할 텍스트를 입력해 주세요 : ")
print(text)
'''

# 5-11 변수와 자료형 - 주석
'''
# # : 한 줄 주석
# '''''', """"""" : 여러 줄 주석
'''

# 6-1 조건문과 반복문 - 조건문(1)
'''
# 조건문으로는 if, switch가 있음
# 앞에서도 말했듯이 True와 False는 앞에 무조건 대문자로 써야함
# 들여쓰기(tap 한 번)를 제대로 해야 if 하나의 식으로 인식됨
# if False 라면 if 쪽을 실행, 아니라면 else 쪽을 실행
if False:
    print("True")
else:
    print("False")

if 4 > 4:
    print("참")
else:
    print("거짓")

# input으로 부터 입력한 값을 value라는 변수에 담음
# 입력 값을 모두 string 으로 출력함
value = input("값을 입력해주세요 : ")

"""
# int로 감싸줘야 실수나 정수로 입력됨 (C#의 Parse와 비슷해보임)
if int(value) > 10:
    print("10보다 큰 수 입니다")
else:
    print("10보다 작은 수 입니다")
"""

# input으로 부터 입력한 값을 모두 대문자로 처리
value = value.upper()

if value == "ENFP":
    print("ENPF")
else:
    print("NULL")
'''

# 6-2 조건문과 반복문 - 조건문(2)
'''
# 다중 조건에 대해서
# 다중 조건은 elif를 사용
day = input("요일을 입력해주세요(0~6) : ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축 영업")
elif day == "1":
    print("연장 영업")
else:
    print("정상영업")
'''

# 6-3 조건문과 반복문 - 반복문(1)
'''
i = 0
sum = 0
# 이 text와 같은 문자열은 항상 빈칸으로 처리해주면 좋음 (지금은 안쓰임)
text = ""

# 파이썬에서는 다른 언어들과 다르게 in을 사용하고 range로 범위를 설정
# range에 다음과 같이 설정하면 1 이상 101 미만으로 반복을 수행하라고 설정된 것
for i in range(1, 101):
    print(i)

# 1부터 100까지의 합을 구하는 식
for i in range(1, 101):
    sum = sum + i
# 이렇게 for문에서 들려쓰기 하지 않아야 for문에 포함이 되지않고 합을 구하게 됨
print(sum)
'''

# 6-4 조건문과 반복문 - 반복문(2)
'''
# while 반복문
# 콘솔에서 Ctrl + C 를 하면 콘솔에서 실행 중인 실행을 강제로 종료
"""
# 아래를 실행하면 무한히 반복하게 됨
while True:
    print("while loop")
"""

# progress = 0 에서 설정한 초깃값 0부터 1이 더해지면서 100까지 설정한대로 출력
progress = 0

while progress < 100:
    
    progress = progress + 1
    print(f"{progress}% 완료됨")
'''

# 7-1 리스트 - 리스트의 정의 및 선언
'''
# 리스트 - 파이썬의 자료구조, 여러개를 모아놓은 컬렉션
# mbti라는 변수에 리스트가 저장됨
mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']

print(mbti)
print(mbti[0])

# 이렇게 하면 정의한 리스트가 밑과 같이 설정한대로 변경되어서 출력됨
mbti[0] = 'INFJ'

print(mbti)
print(mbti[0])

# 파이썬에서는 같은 리스트에서 숫자든 문자열이든 상관없음
my_list = [123, 'apple']
print(my_list)
'''

# 7-2 리스트 - 리스트 데이터 접근 및 조작
'''
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
'''

# 7-3 리스트 - 리스트 정렬
'''
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
'''

# 7-4 리스트 - 리스트 슬라이싱 및 복사
'''
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
'''

# 7-5 리스트 - 리스트와 흐름 제어
'''
scores = [88, 100, 96, 43, 65, 78]
# 큰 숫자 부터 배열이 되게 하는 것
scores.sort(reverse=True)
print(scores)

# for 변수 in 이런식으로 작성
for score in scores:
    if score >= 80:
        print(score)
# 아니라면 리스트에 존재하는 인덱스 값이 아닌 Fail로 출력하라는 뜻
    else:
        print("Fail")
'''

# 7-6 리스트 - 최댓값, 최솟값, 총합
'''
scores = [88, 100, 96, 43, 65, 78]

# 최댓값 구하기
max_val = max(scores)

# 최솟값 구하기
min_val = min(scores)

# 합 구하기
sum_val = sum(scores)
print(sum_val)

# 평균 구하기 (전체 합의 len 즉 수를 나눈 값)
avg_val = sum(scores) / len(scores)
print(avg_val)

# 위의 합 구하기의 프린트 결과랑 동일 (동일한 방법, 결과가 같음)
sum_values = 0
for score in scores:
    sum_values = sum_values + score
print(sum_values)
'''

# 7-7 튜플 - 튜플의 정의 및 특징

# 튜플은 각각의 요소의 값을 변경할 수 없다는 것이 특징
'''
tup = (1, 20, 40)
print(tup[0])

# tup[0] = 100 이런 식으로 출력을 할 시 최초에 정의된 값은 변경이 불가하며 오류가 발생함
# 하지만 아래와 같이 튜플을 자체를 다시 생성해 할당하는 것은 가능함
tup = (100, 30, 4)
print(tup)
'''

# 7-8 튜플 - 튜플, 리스트 변환
'''
tup = (1, 20, 40)

# for 뒤에는 새로 선언한 함수를, in 뒤에는 순회할 자료구조를 넣어주면 됨
for x in tup:
    print(x)


tup = (1, 20, 40)

# 튜플을 리스트로 변환하는 방법 1 (튜플을 list로 감싸는 방법)
list_1 = list(tup)
print(list_1)

# 튜플을 리스트로 변환하는 방법 2
list_2 = [x for x in tup]
print(list_2)

# 튜플을 리스트로 변환하는 방법 3 (for문을 사용)
# for문을 이용하여 하나하나 값을 추가하는 방법
list_3 = []

for x in tup:
    list_3.append(x)
print(list_3)
'''

# 7-9 딕셔너리 - 딕셔너리 정의 및 선언
'''
# 딕셔너리는 중괄호로 선언
student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 대괄호에 키값을 넣어서 출력함 (여기서 키는 student_no, major, grade)
print(student["student_no"])

# 학번 데이터를 변경 후 출력
student["student_no"] = "202301235"

print(student)
print(student["student_no"])
'''

# 7-10 딕셔너리 - 딕셔너리 데이터 조작
'''
student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 딕셔너리 추가 (원하는 값을 추가적으로 작성하면 됨)
student["gpa"] = 4.5
print(student)

# 딕셔너리 수정 (기존의 값을 설정 후 값을 입력하면 됨)
student["gpa"] = 4.3
print(student)

# 딕셔너리 삭제 (del 방법은 앞서 배웠지만 삭제되는 값이 반환이 안됨. 할거면 pop 같은 것을 사용)
del student["grade"]
print(student)
'''

# 7-11 딕셔너리 - 딕셔너리 함수
'''
student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 데이터에 접근할때 사용하는 함수 : get (캡스톤때 했던 CRUD의 조회같음)
print(student.get("gpa", "해당 키-값 쌍이 없습니다"))

# 딕셔너리의 키를 반환하는 함수 : keys
# list로 감싸면 형변환이 됨(앞에 dict_keys 이게 없어짐)
print(list(student.keys()))

# 딕셔너리의 값을 반환하는 함수 : values
# list로 감싸면 형변환이 됨(앞에 dict_values 이게 없어짐)
print(list(student.values()))
'''

# 7-12 딕셔너리 - 딕셔너리와 반복문
'''
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

'''

# 7-13 딕셔너리 - 중첩
# 이 부분 강의 한 번 더 보기
'''
student_1 = {
    "student_no" : "1",
    "gpa" : "4.3"
}

student_2 = {
    "student_no" : "2",
    "gpa" : "3.8"
}

# students 함수를 선언 후 리스트 형식으로 배열하면 됨
students = [student_1, student_2]

# 입력한 키에 대한 값을 출력
for student in students:
    print(student['student_no'])

# 키에 graduted를 추가
for student in students:
    student['graduted'] = False
    print(student)

# 새롭게 선언해줌 (위랑 관련 X)
student = {
    "subjects" : ["운영체제", "데이터베이스", "컴퓨터네트워크"]
}

print(student["subjects"])

subject_list = student["subjects"]

for subject in subject_list:
    print(subject)

# 새롭게 선언해줌 (위랑 관련 X)
student_3 = {
    "scholarship" : {
        "name" : "국가장학금",
        "amount" : "100000"
    }
}

print(student_3)

# 키에 대한 데이터를 확인
for key in student_3.keys():
    print(key)

# 값에 대한 데이터를 확인
for value in student_3.values():
    print(value)

# 값에 대한 이중 for문으로 데이터를 확인
for value in student_3.values():
    for value_2 in value.values():
        print(value_2)
'''

# 8-1 함수 - 함수(1)
'''
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
'''

# 8-2 함수 - 함수(2)
'''
def order_coffee(qty, option = 'hot'):
    print(f'{qty}잔, {option}')

order_coffee(3, 'iced')
# 이렇게 값을 지정하지 않으면 위에서 입력한 기본 값이 입력됨
order_coffee(3)
# 매개변수를 가져와서 값을 직접 넣어주는 방법도 있음
# 그리고 여기서는 매개변수의 순서를 안지켜줘도 알아서 값이 잘 들어감
order_coffee(option = 'iced', qty = 3)
'''

# 8-3 함수 - 함수(3)
# 이 부분 이해안감. 다시 한 번 볼 것
'''
def get_id(email):
    if email.endswith('@test.com'):
        # removesuffix : 뒷 부분을 잘라내는 함수
        email_id = email.removesuffix('@test.com')
        print(email_id)
        # return : 변수의 데이터를 활용 할 수 있도록 해주는 것
        return email_id
    else:
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@test.com')
# 이 부분은 return을 통해 반환하고자 하는 데이터의 타겟을 지정하여 출력가능한 것
print(user_id)
'''

# 8-4 함수 - 모듈
# 환경 설정 후 강의 다시 보기

# 9-1 실습 1 - 회원가입 프로그램(1)
'''
print("=============================")
print("회원가입")
print("=============================")

register = False

while not register:
    print("회원가입을 진행하시겠습니까?\ny : 진행      n : 취소")
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print("=============================")
        print("회원가입이 진행됩니다.")
        print("=============================")
    elif register_input == 'n':
        register = False
        print("=============================")
        print("회원가입이 취소됩니다.")
        print("=============================")
        exit()
    else:
        print("입력 값을 확인해주세요.\n")
'''

# 9-2 실습 2 - 회원가입 프로그램(2)
'''
print("=============================")
print("회원가입")
print("=============================")

register = False

while not register:
    print("회원가입을 진행하시겠습니까?\ny : 진행      n : 취소")
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print("=============================")
        print("회원가입이 진행됩니다.")
        print("=============================")
    elif register_input == 'n':
        register = False
        print("=============================")
        print("회원가입이 취소됩니다.")
        print("=============================")
        exit()
    else:
        print("입력 값을 확인해주세요.\n")

user = []

while True:

    user = {}

    username = input("ID : ")
    while True:
        password = input("PW : ")
        password_confirm = input("PW 확인 : ")
        if password == password_confirm:
            break
        else:
            print("비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.")
    
    name = input("이름 : ")
    while True:
        birth_date = input("생년월일(6자리) : ")
        if len(birth_date) == 6:
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다. 다시 확인해주세요.")

    email = input("이메일 : ")
'''

# 9-3 실습 2 - 회원가입 프로그램(3)
'''
print("=============================")
print("회원가입")
print("=============================")

register = False

while not register:
    print("회원가입을 진행하시겠습니까?\ny : 진행      n : 취소")
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print("=============================")
        print("회원가입이 진행됩니다.")
        print("=============================")
    elif register_input == 'n':
        register = False
        print("=============================")
        print("회원가입이 취소됩니다.")
        print("=============================")
        exit()
    else:
        print("입력 값을 확인해주세요.\n")

users = []

while True:

    user = {}

    username = input("ID : ")
    while True:
        password = input("PW : ")
        password_confirm = input("PW 확인 : ")
        if password == password_confirm:
            break
        else:
            print("비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.")
    
    name = input("이름 : ")
    while True:
        birth_date = input("생년월일(6자리) : ")
        if len(birth_date) == 6:
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다. 다시 확인해주세요.")

    email = input("이메일 : ")

    user["username"] = username
    user["password"] = password
    user["name"] = name
    user["birth_date"] = birth_date
    user["email"] = email

    users.append(user)
    print(users)

    print("=============================")
    print(f"{user['name']}님 회원가입이 완료되었습니다!")
    print("=============================")

    print("회원가입을 추가로 진행 하시겠습니까?\ny : 진행      n : 취소")
    register_another_input = input('>> ')
    register_another_input.lower()

    if register_another_input == 'y':
        pass
    elif register_another_input == 'n':
        exit()
'''

# 10-1 객체지향 - 클래스(1)
'''
class Student:
    
    def __init__(self, name, major, is_graduated):
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")
'''

# 10-2 객체지향 - 클래스(2)
'''
class Student:
    
    def __init__(self, name, major, is_graduated):
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

# 인스턴스 - 실체와된 사물
        
student_1 = Student("홍길동", "컴퓨터공학과", False)

# student_1_name = student_1.name
# print(student_1_name)

student_1.study()
'''

# 10-3 객체지향 - 클래스(3)
'''
class Student:
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f"{student_1.major}로 전공이 변경되었습니다.")

# 인스턴스 - 실체와된 사물

student_1 = Student("홍길동", "컴퓨터공학과")

# 학과데이터를 기계공학과로 새롭게 덮어씀(수정) 
# student_1.major = "기계공학과"

# 함수를 통해서 학과를 변경하는 방법
student_1.edit_major("기계공학과")
print(student_1.major)

student_1_name = student_1.name
print(student_1_name)

student_1_graduated = student_1.is_graduated
print(student_1_graduated)

student_1.study()
'''

# 10-4 객체지향 - 상속(1)
'''
class Student:
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        #Student 클래스에는 없는 개체를 생성
        self.country = country

foreign_student_1 = ForeignStudent("외길동", "러시아어학과", "미국")
print(foreign_student_1.name)
print(foreign_student_1.major)
print(foreign_student_1.country)
print(foreign_student_1.is_graduated)
'''

# 10-5 객체지향 - 상속(2)
'''
class Student:
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        #Student 클래스에는 없는 개체를 생성
        self.country = country

    # 오버라이딩 : 부모클래스에 있는 것을 자식클래스에서 덮어씌운것
    def study(self):
        print(f"{self.name} is studying now.")

foreign_student_1 = ForeignStudent("외길동", "러시아어학과", "미국")
foreign_student_1.study()
# print(foreign_student_1.name)
# print(foreign_student_1.major)
# print(foreign_student_1.country)
# print(foreign_student_1.is_graduated)
'''

# 10-6 객체지향 - 클래스 활용
# 강의 천천히 보면서 다시 해보기

# 11-1 파일 다루기와 예외 처리 - 예외 처리(1)
'''
a = 10
b = 0
a / b

fruits = ['apply', 'banana', 'strawberry']
fruits[3]
'''

# 11-2 파일 다루기와 예외 처리 - 예외 처리(2)
'''
fruits = ['apply', 'banana', 'strawberry']

try:
    fruits[3]
except:
    print("인덱스를 참조할 수 없습니다.")
else:
    print("정상 수행")

try:
    fruits[3]
except:
    print("인덱스를 참조할 수 없습니다.")
finally:
    print("명령 수행")

print(fruits)
'''

# 11-3 파일 다루기와 예외 처리 - 파일 읽기 
# 강의 천천히 다시보고 해보기
'''
# 절대경로, 상대경로

f = open('', 'r', encoding='UTF-8')

print(f)
'''

# 11-4 파일 다루기와 예외 처리 - 파일 쓰기
# 강의 천천히 다시보고 해보기
'''
f = open('literature\poem.txt', 'a', encoding='UTF-8')

f.write("\n새로운 글이 작성되었습니다.")

f.close()
'''