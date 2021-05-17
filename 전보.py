import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
graph = defaultdict(list)
INF = int(1e9)
# 도시개수:n, 통로개수:m, 출발지점:c
n, m, c = map(int, input().split())
# 시작:x, 끝:y, 시간:z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
# 거리 테이블 초기화
distance = [INF] * (n+1)
distance[c] = 0
# 다익스트라 알고리즘
q = []
heapq.heappush(q, (0, c))
while q:
    dist, city = heapq.heappop(q)
    # 처리 된 적 있다면 스킵
    if distance[city] < dist:
        continue
    # 현재 도시와 연결된 다른 도시들을 확인
    for adjacent in graph[city]:
        new_dist = dist + adjacent[1]
        if new_dist < distance[adjacent[0]]:
            distance[adjacent[0]] = new_dist
            heapq.heappush(q, (new_dist, adjacent[0]))

# 출력
total_city = total_time = 0
for i in range(1,n+1):
    if 0<distance[i]<INF:
        total_city += 1
        total_time = max(total_time, distance[i])

print(total_city, total_time)

