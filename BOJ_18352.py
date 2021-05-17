import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
dist[x] = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

q = deque([x])
while q:
    start = q.popleft()
    for end in graph[start]:
        if dist[end] == INF:
            dist[end] = dist[start] + 1
            q.append(end)

for city in range(1,n+1):
    if dist[city] == k:
        print(city)
if k not in dist:
    print(-1)