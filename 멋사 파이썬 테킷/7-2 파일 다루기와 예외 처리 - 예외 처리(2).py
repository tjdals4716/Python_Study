# 11-2 파일 다루기와 예외 처리 - 예외 처리(2)

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