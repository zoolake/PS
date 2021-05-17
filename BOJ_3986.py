import sys

input = sys.stdin.readline
N = int(input())
result = 0
for _ in range(N):
    word = input().rstrip('\n')
    stack = []
    for ch in word:
        if len(stack) == 0:
            stack.append(ch)
            continue
        if stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) == 0:
        result += 1

print(result)