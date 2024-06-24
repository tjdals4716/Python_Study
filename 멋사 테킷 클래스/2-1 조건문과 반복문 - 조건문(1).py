# 6-1 조건문과 반복문 - 조건문(1)

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