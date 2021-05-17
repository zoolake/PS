import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())

board = [0]*101
dist = [-1]*101

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

q = collections.deque([1])
dist[1] = 0

while q:
    pos = q.popleft()
    if dist[100] != -1:
        break

    for i in range(1,7):
        npos = pos + i
        # 사다리 또는 뱀
        if npos <= 100 and board[npos] != 0:
            npos = board[npos]

        # 범위 내 이면서 방문하지 않은 경우
        if npos <= 100 and dist[npos] == -1:
            dist[npos] = dist[pos] + 1
            q.append(npos)

print(dist[100])
