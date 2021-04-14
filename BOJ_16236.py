import sys
import collections

input = sys.stdin.readline
dx = [-1,0,1,0] # 상 좌 하 우 
dy = [0,-1,0,1]


# BFS
def BFS(x, y):
    q = collections.deque()
    visited = set()
    weight = 2
    time = 0
    count = 0
    flag = False

    q.append((x,y))
    visited.add((x,y))

    while q:
       cur_x, cur_y = q.popleft()
       for i in range(4):
           nx = cur_x + dx[i]
           ny = cur_y + dy[i]
           if 0<= nx < N and 0<= ny < N and 0 < area[nx][ny] <= weight:
               if area[nx][ny] < weight:
                   area[nx][ny] = 0
                   count += 1
                   if count == weight:
                       count = 0
                       weight += 1
                q.append((nx,ny))






N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            x, y = i, j
            area[i][j] = 0
            break

BFS(x, y)