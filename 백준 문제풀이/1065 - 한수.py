def is_han_number(n):
    str_n = str(n)
    if len(str_n) <= 2:
        return True
    diff = int(str_n[1]) - int(str_n[0])
    for i in range(1, len(str_n) - 1):
        if int(str_n[i + 1]) - int(str_n[i]) != diff:
            return False
    return True

def count_han_numbers(N):
    count = 0
    for i in range(1, N + 1):
        if is_han_number(i):
            count += 1
    return count

N = int(input())
print(count_han_numbers(N))
