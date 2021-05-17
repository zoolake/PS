import sys

line = sys.stdin.readline
N, M = map(int, line().split())

nums = [0]
nums.extend(list(map(int, line().split())))
for i in range(1,len(nums)):
    nums[i] += nums[i-1]

for _ in range(M):
    start, end = map(int, line().split())
    print(nums[end] - nums[start-1])