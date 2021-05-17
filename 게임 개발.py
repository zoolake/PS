import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
row, col, direction = map(int, input().split()) #  북 동 남 서
board = [list(map(int, input().split())) for _ in range(N)]
print(board)
result = 0
flag = 0
while True:
    # 갈 곳 탐색 (반시계방향)
    for _ in range(4):
        if direction - 1 < 0:
            direction = 3
        else:
            direction -= 1

        nrow, ncol = row + dx[direction], col + dy[direction]
        if 0<=nrow<N and 0<=ncol<M and board[nrow][ncol] == 0:
            board[row][col] == -1
            result += 1
            row, col = nrow, ncol     
            flag = 0     
            break

        flag += 1
    
    if flag == 4:
        back = abs(direction-2)
        nrow, ncol = row + dx[back], col + dy[back]
        if 0<=nrow<N and 0<=ncol<M and board[nrow][ncol] <= 0:
            row, col = nrow, ncol
            continue
        else:
            break

print(result)
