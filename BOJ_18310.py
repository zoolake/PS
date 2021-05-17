import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
table = Counter(map(int,input().split()))

min_dist = float('inf')
result = float('inf')
for antenna in table.keys():
    dist = 0
    for house, value in table.items():
        dist += abs(antenna-house)

    if min_dist > dist:
        min_dist = dist
        result = antenna   

print(result)