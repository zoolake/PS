# 중요!
# visited = [[False]*n]*n
# visited = [[False]*n for _ in range(n)]
# 위 두개는 다르다. 예를들어, visited[0][0] = True 연산을 하면 첫번째 문장은 [[True,False],[True,False]]가 되는 반면, 
# 두번째 문장은 [[True,False],[False,False]]가 된다.

# 실수한 점
# 1. 중첩 for 문 변수 겹치는 문제
# 2. BFS 내부 조건문 하나 빠져서(방문 여부) 무한루프 발생

import sys
from collections import deque

input = sys.stdin.readline

n,l,r = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

result = 0
while True:
    visited = [[False]*n for _ in range(n)]
    movable = False
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue  
            
            q = deque()
            total = 0
            union = []
            # BFS
            visited[i][j] = True
            total += board[i][j]
            q.append((i,j))
            union.append((i,j))
            while q:
                row, col = q.popleft()              
                for index in range(4):
                    nrow = row + drow[index]
                    ncol = col + dcol[index]
                    if 0<=nrow<n and 0<=ncol<n and l<=abs(board[nrow][ncol]-board[row][col])<=r and not visited[nrow][ncol]:
                        visited[nrow][ncol] = True
                        total += board[nrow][ncol]
                        q.append((nrow,ncol))
                        union.append((nrow,ncol))

            # 연합국가 인구 재분배
            population = total // len(union)
            if len(union) > 1:
                for row, col in union:
                    board[row][col] = population
                    movable = True
    
    if not movable:
        break
    result += 1

print(result)

