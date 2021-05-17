import sys

input = sys.stdin.readline
s = list(map(int, input().rstrip('\n')))
result = 0
for num in s:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)