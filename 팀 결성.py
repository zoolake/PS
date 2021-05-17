import sys

def find_parent(parent, x) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a_parent, b_parent = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a_parent
    else:
        parent[a] = b_parent

input = sys.stdin.readline
n, m = map(int, input().split())
# 초기화
parent = [0] * (n+1)
for i in range(0,n+1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    # union
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')