N = 8

def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            line += "Q " if cell else ". "
        print(line)
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0
    return False

def main():
    board = [[0] * N for _ in range(N)]
    if not solve(board, 0):
        print("No solution exists.")

if __name__ == "__main__":
    main()
