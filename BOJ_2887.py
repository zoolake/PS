# 풀이 방법
# 최소 신장 트리_크루스칼 알고리즘 사용
# 행성 간 간선의 길이를 구하는 부분이 중요
# 1. 각 행성 간 모든 간선을 구하면 시간초과 발생 가능
# 2. 위의 문제를 해결하기 위해서, 행성의 x, y, z 좌표 별 오름차순 정렬을 수행 후 
#    현재 행성과 다음 행성간의 거리를 구하고 저장 (거리, 현재행성id, 다음행성id)
#    모든 간선을 구하는게 아닌 필요한 간선들만 구한다.
import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
planets = []
for id in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, id))
# 부모 테이블, 간선을 담을 테이블, 결과 변수 생성
parents = [i for i in range(n)]
tunnels = []
result = 0
# 터널 정보 입력 후 오름차순 정렬
for i in range(3):
    planets.sort(key = lambda x: x[i])
    for j in range(1,n):
        tunnels.append((abs(planets[j-1][i] - planets[j][i]), planets[j-1][3], planets[j][3]))
tunnels.sort()
# 최소 신장 트리 생성
for tunnel in tunnels:
    cost, a, b = tunnel
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost
print(result)