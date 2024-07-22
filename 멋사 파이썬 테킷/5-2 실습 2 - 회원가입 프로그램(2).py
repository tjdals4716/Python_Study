# 9-2 실습 2 - 회원가입 프로그램(2)

print("=============================")
print("회원가입")
print("=============================")

register = False

while not register:
    print("회원가입을 진행하시겠습니까?\ny : 진행      n : 취소")
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print("=============================")
        print("회원가입이 진행됩니다.")
        print("=============================")
    elif register_input == 'n':
        register = False
        print("=============================")
        print("회원가입이 취소됩니다.")
        print("=============================")
        exit()
    else:
        print("입력 값을 확인해주세요.\n")

user = []

while True:

    user = {}

    username = input("ID : ")
    while True:
        password = input("PW : ")
        password_confirm = input("PW 확인 : ")
        if password == password_confirm:
            break
        else:
            print("비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.")
    
    name = input("이름 : ")
    while True:
        birth_date = input("생년월일(6자리) : ")
        if len(birth_date) == 6:
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다. 다시 확인해주세요.")

    email = input("이메일 : ")