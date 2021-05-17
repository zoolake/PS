import sys

def find(x) -> int:
    global house
    if house[x] != x:
        house[x] = find(house[x])
    return house[x]

# 일반적으로 union 함수에서 find 함수를 다시 사용해서 최상위 노드를 찾는 작업을 하는데,
# 어차피 사이클이 발생하지 않는 경우를 확인하기 위해서 find 함수를 통해 갱신하기 때문에
# union에서 find 함수를 다시 사용할 필요가 없다고 
# 생각해서 (path-compression을 이미 했기 때문) 코드를 다음과 같이 변경
def union(a, b):
    global house
    parent_a = house[a] # path-compression을 이미 했기때문에 find(a)가 아닌 house[a]로 바로 접근
    parent_b = house[b]
    if parent_a < parent_b:
        house[parent_b] = parent_a  # a의 최상위 노드를 b의 최상위 노드와 이어주기
    else:
        house[parent_a] = parent_b

input = sys.stdin.readline
n, m = map(int, input().split())

# 정점 초기화
house = [0] * (n+1)
for i in range(1, n+1):
    house[i] = i

# 간선 초기화 및 오름차순 정렬
roads = []
for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append((c,a,b))
roads.sort()

result = 0
last = 0    # 마지막에 삽입되는 간선

for road in roads:
    cost, start, end = road
    # 사이클이 발생하지 않는 경우
    if find(start) != find(end):
        union(start, end)
        result += cost
        last = cost

print(result - last)


