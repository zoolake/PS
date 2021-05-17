import sys

def dfs(node):
    tree[node] = -2
    for i in range(len(tree)):
        if tree[i] == node:
            dfs(i)

input = sys.stdin.readline
N = int(input())
tree = list(map(int, input().split()))
target = int(input())

dfs(target)
result = 0

for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        result += 1

print(result)