# 5-4 변수와 자료형 - 문자열(2)

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