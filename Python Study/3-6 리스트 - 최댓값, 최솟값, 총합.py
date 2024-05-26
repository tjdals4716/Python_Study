# 7-6 리스트 - 최댓값, 최솟값, 총합

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