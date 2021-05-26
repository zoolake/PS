# 반례
# 6 13
# 2 3 5 7 11 13
# 해결하기 위해서 수열 마지막에 0을 넣어줘서 마지막까지 탐색할 수 있게끔 변경.
n, m = map(int, input().split())
nums = list(map(int, input().split()))
start, end, partial_sum, result = 0, 0, 0, 0
nums.append(0)
while end<=n:
    if partial_sum >= m:
        partial_sum -= nums[start]
        start += 1
    elif partial_sum < m:
        partial_sum += nums[end]   
        end += 1
    if partial_sum == m:
        result += 1

print(result)
