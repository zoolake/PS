import sys
input = sys.stdin.readline

# 입력 및 그래프 초기화
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start][end] = min(graph[start][end], cost)
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()