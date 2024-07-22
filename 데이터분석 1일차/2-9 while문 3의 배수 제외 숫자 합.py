sum = 0
a = 0

for a in range(1, 101):
    if a % 3 == 0:
        continue
    sum += a

print("1 ~ 100의 합계 (3의 배수 제외) : ", sum)