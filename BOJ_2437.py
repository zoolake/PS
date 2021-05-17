import sys
input = sys.stdin.readline
n = int(input())
nums = sorted(list(map(int,input().split())))
total = 0

for num in nums:
    if total + 1 < num:
        break
    total += num

print(total + 1)