import sys

input = sys.stdin.readline
N, M = map(int, input().split())
result = float('-inf')
for _ in range(N):
    result = max(result, min(list(map(int, input().split()))))
print(result)
    