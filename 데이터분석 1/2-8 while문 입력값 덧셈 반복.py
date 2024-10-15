a = 0
sum = 0

while True:
    a = int(input("더할 첫 번째 수를 입력하세요 (종료하려면 0을 입력) : "))
    if a == 0:
        break
    b = int(input("더할 두 번째 수를 입력하세요 (종료하려면 0을 입력) : "))
    sum = a + b
    print(a + b)

print("0을 입력하여 프로그램이 종료됩니다")