import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())

table = collections.defaultdict()
for _ in range(N):
    address, password = map(str, input().split())
    table[address] = password

for _ in range(M):
    print(table[input().rstrip('\n')])
