import sys, copy
from itertools import combinations
from collections import deque

def calculation(lab) -> int:
    area = 0
    for row in lab:
        area += row.count(0)
    return area
    
def bfs(lab, n, m, q: deque):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow, ncol = row+drow[i], col+dcol[i]
            if 0<=nrow<n and 0<=ncol<m and lab[nrow][ncol] == 0:
                lab[nrow][ncol] = 2
                q.append((nrow,ncol))

    return calculation(lab)


input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = float('-inf')

# 벽을 세울 수 있는 빈 공간을 담은 리스트 초기화
spaces = []
q = deque()
for row in range(n):
    for col in range(m):
        if board[row][col] == 0:
            spaces.append((row,col))
        elif board[row][col] == 2:
            q.append((row,col))

# 3개의 벽을 세우는 모든 조합
for walls in combinations(spaces,3):
    copy_board = copy.deepcopy(board)
    copy_q = copy.deepcopy(q)
    for wall in walls:
        wall_row, wall_col = wall[0], wall[1]
        copy_board[wall_row][wall_col] = 1
    result = max(result, bfs(copy_board, n, m, copy_q))

print(result)