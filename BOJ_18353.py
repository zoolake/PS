import sys
# 현재 병사보다 앞에 위치하면서 가장 큰 DP값을 갖는 병사를 찾는다.
input = sys.stdin.readline
n = int(input())
soldiers = list(map(int, input().split()))
dp = [1]*n
for i in range(1,n):
    for idx, val in enumerate(soldiers[0:i]):
        if val > soldiers[i]:
            dp[i] = max(dp[i], dp[idx]+1)

print(n-max(dp))


