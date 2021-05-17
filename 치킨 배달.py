import sys
import itertools

input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
for row in range(n):
    for col in range(n):
        if board[row][col] == 1:
            houses.append((row,col))
        elif board[row][col] == 2:
            chickens.append((row,col))

result = float('inf')
for chicken in itertools.combinations(chickens, m):
    dist_sum = 0
    for house in houses:
        dist_sum += min([abs(house[0]-store[0]) + abs(house[1]-store[1]) for store in chicken])
    result = min(result, dist_sum)

print(result)