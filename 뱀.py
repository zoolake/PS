import sys
from collections import deque

# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def simulation() -> int:
    time = 1
    row, col = 0, 0
    direction = 0
    q = deque([(row,col)])
    board[row][col] = 2
    while True:
        # 여기서 새로운 변수 nrow, ncol을 선언해서 했었는데
        # 그렇게 하면 방향을 계속 갱신하는게 아니게 된다.
        row, col = row+dx[direction], col+dy[direction]
        # 범위 내 + 몸과 충돌 여부
        if 0<=row<n and 0<=col<n and board[row][col] != 2:
            # 사과 없다면
            if board[row][col] != 1:
                tail_row, tail_col = q.popleft()
                board[tail_row][tail_col] = 0
            # 사과 여부와 관계없이 공통연산
            board[row][col] = 2
            q.append((row,col))
            # 방향 전환해야 하는지
            if time in time_table:
                if time_table[time] == 'L':
                    direction = (direction - 1) % 4
                else:
                    direction = (direction + 1) % 4
            time += 1
        else:
            return time

# 입력
input = sys.stdin.readline
# 보드 크기 설정 및 초기화
n = int(input())
board = [[0]*n for _ in range(n)]
# 사과 위치 초기화
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
# 타임테이블 초기화 (특정 시간에 방향 전환)
l = int(input())
time_table = {}
for _ in range(l):
    x, c = input().split()
    time_table[int(x)] = c

print(simulation())
