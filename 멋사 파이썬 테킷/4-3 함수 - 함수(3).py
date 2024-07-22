# 8-3 함수 - 함수(3)
# 이 부분 이해안감. 다시 한 번 볼 것

def get_id(email):
    if email.endswith('@test.com'):
        # removesuffix : 뒷 부분을 잘라내는 함수
        email_id = email.removesuffix('@test.com')
        print(email_id)
        # return : 변수의 데이터를 활용 할 수 있도록 해주는 것
        return email_id
    else:
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@test.com')
# 이 부분은 return을 통해 반환하고자 하는 데이터의 타겟을 지정하여 출력가능한 것
print(user_id)