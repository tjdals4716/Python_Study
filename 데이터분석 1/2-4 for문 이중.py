for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %2d" % (i, j, i * j))
    # 구구단 별로 띄어서 출력
    print("")



for i in range(1, 10):
    for j in range(1, 10):
        a = i * j
        print(f"{i} * {j} = {a}")
    # 구구단 별로 띄어서 출력
    print("") 