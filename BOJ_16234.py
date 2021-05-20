import sys
from collections import deque

input = sys.stdin.readline

n,l,r = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

result = 0
while True:
    visited = [[False]*n]*n
    # 국경선 조회
    for i in range(n):
        for j in range(n):
            q = deque()
            total = 0
            union = []
            if not visited[i][j]:
                visited[i][j] = True
                total += board[i][j]
                q.append((i,j))
                while q:
                    row, col = q.popleft()
                    union.append((row,col))
                    for i in range(4):
                        nrow = row + drow[i]
                        ncol = col + dcol[i]
                        if 0<=nrow<n and 0<=ncol<n and l<=abs(board[nrow][ncol]-board[row][col])<=r:
                            visited[nrow][ncol] = True
                            total += board[nrow][ncol]
                            q.append((nrow,ncol))
            # 연합국가 인구 재분배
            population = total // len(union)
            for row, col in union:
                board[row][col] = population
                if len(union) == 1:
                    visited[row][col] = False

    check = True
    for row in range(n):
        for col in range(n):
            if visited[row][col]:
                check = False
                break
    
    if check:
        break

print(result)

