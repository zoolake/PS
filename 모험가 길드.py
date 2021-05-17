import sys

n = int(input())
people = sorted(list(map(int, input().split())))
result = 0
count = 0
for fear in people:
    count += 1
    if count >= fear:
        result += 1
        count = 0

print(result)
    