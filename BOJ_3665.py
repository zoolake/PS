#   참고:   https://enjoyso.tistory.com/139  ,  https://hellominchan.tistory.com/347
#   "IMPOSSiBLE" => 사이클이 있는 경우
#        "?"     => 순위가 바뀐 모든 팀들의 목록을 주기 때문에 발생하지 않는다. 
#                => 구현 자체는 위상 정렬 수행 중 큐의 길이가 1을 초과하는지 확인하면 된다.

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    rank = list(map(int, input().split()))
    # 그래프 및 진입차수 초기화
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for i in range(n-1):
        graph[rank[i]] = rank[i+1:]
        indegree[rank[i+1]] = i+1

    m = int(input())
    for _ in range(m):
        a, b = map(int,input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[b] += 1
            indegree[a] -= 1
    
    q = deque()
    result = []
    for i in rank:
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")

