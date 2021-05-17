import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(M):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))
