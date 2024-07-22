# 7-5 리스트 - 리스트와 흐름 제어

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