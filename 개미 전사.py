import sys

input = sys.stdin.readline
N = int(input())
warehouse = list(map(int, input().rstrip('\n').rsplit()))
dp = [0] * N
dp[0] = warehouse[0]
dp[1] = max(warehouse[0],warehouse[1])

for i in range(2,len(warehouse)):
    dp[i] = max(warehouse[i] + dp[i-2], dp[i-1])

print(dp[-1])