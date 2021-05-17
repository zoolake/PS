import sys
from collections import deque

# 입력
input = sys.stdin.readline
n, k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

# 바이러스 위치 저장
virus = []
for i in range(n):
    for j in range(n):
        virus_type = board[i][j]
        if virus_type:
            virus.append((virus_type,i,j,0))

virus.sort()
virus = deque(virus)

# BFS
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
count = 0
prev_type = 0
while virus:
    virus_type, row, col, time = virus.popleft()
    if time == s:
        break

    for i in range(4):
        nrow, ncol = row+drow[i], col+dcol[i]
        if 0<=nrow<n and 0<=ncol<n and board[nrow][ncol] == 0:
            board[nrow][ncol] = virus_type
            virus.append((virus_type, nrow, ncol, time+1))

print(board[x-1][y-1])
