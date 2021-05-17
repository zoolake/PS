import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for row in range(N):
    for col in range(N):
        if col == 0:
            continue
        board[row][col] += board[row][col-1]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda n: int(n)-1, input().split())
    result = 0
    for row in range(x1, x2+1):
        if y1 > 0:
            result -= board[row][y1-1]
        result += board[row][y2]
    print(result)