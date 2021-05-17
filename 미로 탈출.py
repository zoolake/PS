import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque([(0,0)])

while q:
    front = q.popleft()
    if front[0] == N-1 and front[1] == M-1:
        continue
    for i in range(4):
        x, y = front[0], front[1]
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.append((nx,ny))

print(maze[N-1][M-1])
