def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2

    return result

res = 0
var1, var2, oper = 0, 0, ""

oper = input("연산자를 입력하세요 : ")
var1 = int(input("첫 번째 수 입력 : "))
var2 = int (input("두 번째 수 입력 : "))

res = calc(var1, var2, oper)

print("계산 결과 : ", res)