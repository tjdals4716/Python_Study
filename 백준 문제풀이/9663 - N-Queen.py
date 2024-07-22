def is_safe(board, row, col, n):
    # 위쪽 열을 검사
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 왼쪽 대각선을 검사
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 오른쪽 대각선을 검사
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n, result):
    if row >= n:
        result[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, result)
            board[row][col] = 0  # 백트래킹

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    result = [0]
    solve_n_queens(board, 0, n, result)
    return result[0]

n = int(input())
print(n_queens(n))
