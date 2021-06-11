from collections import defaultdict

# 1. 플로이드-워셜 + 최소 비용 계산 => 시간초과 테스트 케이스 5개
# 2. 최적화(합승을 아예 안해도 되는 경우면 최소 비용 계산 생략) => 시간초과 테스트 케이스 2개
# 3. 마지막 최소 비용 계산하는 부분에서 <필요도 없는 3중 for문> 돌려서 시간초과 남

# 후기: 사실상 마지막 최소 비용 계산 부분에서 불필요한 3중 for문만 없었어도 효율성 통과함.
#      근데, 합승을 아예 안해도 되는 경우 최소 비용 계산을 생략하는 최적화가 있으면
#      평균적으로 2배 정도 빠름.

def solution(n, s, a, b, fares):
    answer = 0

    # graph initalization
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    
    # graph initalization with reading fares
    for fare in fares:
        start, end, value = fare
        graph[start][end] = value
        graph[end][start] = value
    
    # floyd warshall
    path = [[[]] * (n+1) for _ in range(n+1)]
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j].append(k)

    # calculate minimum cost
    answer = graph[s][a] + graph[s][b]
    if set(path[s][a]) & set(path[s][b]):
        for hub in range(1, n+1):
            answer = min(answer, graph[s][hub] + graph[hub][a] + graph[hub][b])

    return answer