import sys
from collections import deque

input = sys.stdin.readline
limit = 100001
N, K = map(int, input().split())
q = deque([N])
visit = [False] * limit
dist = [0] * limit

while q:
    pos = q.popleft()   
    if pos == K:
        break
    if pos*2 <= limit-1 and visit[pos*2] == False:
        q.appendleft(pos*2)
        visit[pos*2] = True
        dist[pos*2] = dist[pos]
    if pos+1 <= limit-1 and visit[pos+1] == False:
        q.append(pos+1)
        visit[pos+1] = True
        dist[pos+1] = dist[pos] + 1
    if pos-1 >= 0 and visit[pos-1] == False:
        q.append(pos-1)
        visit[pos-1] = True
        dist[pos-1] = dist[pos] + 1

print(dist[K])

