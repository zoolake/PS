import sys

input = sys.stdin.readline
N, M = map(int, input().split())
cash = [0] * N
for i in range(N):
    cash[i] = int(input())

# init
dp = [float('inf')] * 10001
for i in cash:
    dp[i] = 1

for i in range(1,M+1):
    if dp[i] == 1:
        continue
    else:
        for c in cash:
            if i-c >= 1 and dp[i-c] >= 1:
                dp[i] = min(dp[i-c] + 1, dp[i])

if dp[M] == float('inf'):
    print(-1)
else:
    print(dp[M])