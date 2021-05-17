import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
array = sorted(list(map(int, input().split())),reverse=True)
first, second = array[0], array[1]
count = result = 0

while M > 0:
    if count == K:
        result += second
        count = 0
    else:
        result += first
        count += 1
    M -= 1

print(result)
        