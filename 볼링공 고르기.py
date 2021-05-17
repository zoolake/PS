import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
temp = list(map(int, input().split()))
balls = [0] * 11

for i in temp:
    balls[i] += 1

result = 0
for i in range(1,10):
    result += balls[i] * sum(balls[i+1:])

print(result)


