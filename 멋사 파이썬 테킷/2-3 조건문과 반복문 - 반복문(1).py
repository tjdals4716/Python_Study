# 6-3 조건문과 반복문 - 반복문(1)

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