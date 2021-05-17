import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
# 그래프 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0
# 간선 입력
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = 1
# 도착지:x 및 경유지:k 입력
x, k = map(int, input().split())
# 플로이드-와샬
for i in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end] = min(graph[start][end], graph[start][i] + graph[i][end])
# 출력
if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])