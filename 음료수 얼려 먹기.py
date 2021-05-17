import sys

input = sys.stdin.readline
result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(row, col):
    for i in range(4):
        nrow, ncol = row + dx[i], col + dy[i]
        if 0<=nrow<N and 0<=ncol<M and board[nrow][ncol] == 0:
            board[nrow][ncol] = 1
            dfs(nrow,ncol)
        else:
            continue
    else:
        return

N, M = map(int, input().split())
board = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            board[row][col] = 1
            dfs(row, col)
            result += 1

print(result)