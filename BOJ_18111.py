import sys
import collections

# 높이 0~256 전부 탐색
input = sys.stdin.readline
N, M, B = map(int, input().split())
result_time = float('inf')
result_height = 0

ground = collections.defaultdict(int)
for _ in range(N):
    line = list(map(int, input().split()))
    for elem in line:
        ground[elem] += 1

total = 0
for key, value in ground.items():
        total += key * value
        
for h in range(257):   
    cnt = N * M
    time = 0
    # 만들수없는 높이에 도달한 경우 멈추기
    if total + B < h * cnt:
        break

    for key, value in ground.items():
        # 쌓아야 하는 경우
        if h > key:
            time += 1 * (h - key) * value
        # 지워야 하는 경우
        if h < key:
            time += 2 * (key - h) * value
    
    if result_time >= time:
        if result_time == time:
            result_height = max(result_height, h)
            continue
        result_time = time
        result_height = h

print(result_time, result_height)

