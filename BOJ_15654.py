import sys
import itertools

input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(list(itertools.permutations(list(map(int, input().split())), M)))
for num in nums:
    for index in range(M):
        print(num[index], end=" ")
    print()