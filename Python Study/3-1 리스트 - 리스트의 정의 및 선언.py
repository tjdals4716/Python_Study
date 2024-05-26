# 7-1 리스트 - 리스트의 정의 및 선언

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