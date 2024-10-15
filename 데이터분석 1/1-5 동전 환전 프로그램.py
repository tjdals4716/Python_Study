money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환 할 돈을 작성하시오 : "))

c500 = money
money %= 100

c50 = money
money %= 50

c10 = money
money %= 10

print("500원 : %d개 " % c500)
print("100원 : %d" % c100)
print("50원 : %d" % c50)
print("10원 : %d" % c10)
print("바꾸지 못한 잔돈 : %s" % money)
