'''
a = int(input("값을 입력하세요 : "))

if a > 50:
    if a < 100:
        print("a는 50 이상 100 이하이다")
    else:
        print("a는 100 이상이다")
else:
    print("a는 50 이하이다")
'''


a = int(input("점수를 입력하세요 : "))

if a >= 90:
    print("A 학점입니다")
elif a >= 80:
    print("B 학점입니다")
elif a >= 70:
    print("C 학점입니다")
elif a >= 60:
    print("D 학점입니다")
else:
    print("F 학점입니다")