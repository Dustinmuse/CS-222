def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
def solve_nqueens_util(board, row, N):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_nqueens_util(board, row + 1, N):
                return True
            board[row][col] = 0

    return False
def is_safe(board, row, col, N):
    #checks same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    #upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    #upper-right diagonal
    for i, j, in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return

    print_board(board)

if __name__ == '__main__':
    N = 8  # You can change this to the desired size of the chessboard
    solve_nqueens(N)