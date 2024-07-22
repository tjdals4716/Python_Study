def solution(_str):
    stack = []
    for a in _str:
        stack.append(a)

    reversed_str = ''

    while stack:
        reversed_str = reversed_str + stack.pop()
    return reversed_str

while True:
    _str = input("앵무새에게 말을 걸어보세요 : ")
    print("앵무새 대답 : ", solution(_str))