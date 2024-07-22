# 8-2 함수 - 함수(2)

def order_coffee(qty, option = 'hot'):
    print(f'{qty}잔, {option}')

order_coffee(3, 'iced')
# 이렇게 값을 지정하지 않으면 위에서 입력한 기본 값이 입력됨
order_coffee(3)
# 매개변수를 가져와서 값을 직접 넣어주는 방법도 있음
# 그리고 여기서는 매개변수의 순서를 안지켜줘도 알아서 값이 잘 들어감
order_coffee(option = 'iced', qty = 3)