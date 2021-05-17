import sys
import bisect

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lines = sorted(list(map(int, input().rstrip().split())))
left = 0
right = lines[-1]
# find H
while left < right:
    mid = (right-left)//2 + left
    index = bisect.bisect_right(lines, mid)
    right_part_sum = sum(list(map(lambda x: x-mid, lines[index:])))

    if right_part_sum >= M:
        left = mid + 1
        H = mid
    else:
        right = mid - 1
    
print(H)