import sys
import bisect

input = sys.stdin.readline
N = int(input())
items = list(map(int, input().rstrip('\n').split()))
M = int(input())
asked = list(map(int, input().rstrip('\n').split()))

# 이진탐색을 위한 items 정렬
items.sort()
# asked 순회하면서 items 이진탐색
for i in range(len(asked)):
    index = bisect.bisect_left(items, asked[i])
    if index < len(items) and items[index] == asked[i]:
        print('yes', end=' ')
    else:
        print('no', end=' ')
 

