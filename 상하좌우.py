import sys

input = sys.stdin.readline
N = int(input())
plans = list(input().split())
x = y = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L','R','U','D']

for plan in plans:
    for i in range(4):
        if plan == move[i]:
            nx = x + dx[i] 
            ny = y + dy[i]
    
    if 1<= nx<= N and 1<= ny<= N:
        x, y = nx, ny

print(x, y)