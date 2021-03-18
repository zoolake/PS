import collections, sys

N = int(input())
coordinate_list = list(map(int, input().split()))
table = collections.defaultdict(int)
s = list(set(coordinate_list))
s.sort()

for i in range(len(s)):
    table[s[i]] = i

for i in coordinate_list:
    print(table[i],end=' ')
    