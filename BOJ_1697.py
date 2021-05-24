import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    visited = [0] * 100001
    visited[n] = 0
    q = deque([n])
    # BFS
    while q:
        subin = q.popleft()
        time = visited[subin]
        pos1, pos2, pos3 = subin-1, subin+1, subin*2
        # 동생을 찾을경우 종료
        if pos1 == k or pos2 == k or pos3 == k:
            print(time + 1)
            break

        if 0<= pos1 <= 100000 and not visited[pos1]:
            q.append(pos1)
            visited[pos1] = time + 1
        if 0<= pos2 <= 100000 and not visited[pos2]:
            q.append(pos2)
            visited[pos2] = time + 1
        if 0<= pos3 <= 100000 and not visited[pos3]:
            q.append(pos3)
            visited[pos3] = time + 1
