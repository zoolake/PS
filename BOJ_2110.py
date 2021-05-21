# ##  이분탐색 직접 구현한 풀이_560ms
# import sys
# input = sys.stdin.readline

# # 입력 및 초기화
# n, c = map(int, input().split())
# houses = []
# for _ in range(n):  houses.append(int(input()))
# # 정렬 후 이분탐색을 위한 초기 조건
# houses.sort()
# left = 1
# right = houses[-1] - houses[0]
# result = 1
# # 이분탐색
# while left <= right:
#     count = 1
#     mid = (left + right) // 2
#     # 설치 가능 공유기 개수
#     prev = houses[0]
#     for i in range(1,n):
#         if houses[i] - prev >= mid:
#             count += 1
#             prev = houses[i]
#     # 설치 가능 공유기 개수 기반 범위 재조정
#     if count < c:
#         right = mid - 1
#     elif count >= c:
#         left = mid + 1
#         result = max(result, mid)

# print(result)

##  bisect를 활용한 풀이_336ms
import sys, bisect
input = sys.stdin.readline

# 입력 및 초기화
n, c = map(int, input().split())
houses = []
for _ in range(n):  houses.append(int(input()))
# 정렬 후 이분탐색을 위한 초기 조건
houses.sort()
left = 1
right = houses[-1] - houses[0]
result = 1
# 이분탐색
while left <= right:
    count = 1
    mid = (left + right) // 2
    # 설치 가능 공유기 개수
    prev_index = 0
    while True:
        prev_index = bisect.bisect_left(houses, houses[prev_index]+mid)
        if prev_index < n:
            count += 1
        else:
            break
    # 설치 가능 공유기 개수 기반 범위 재조정
    if count < c:
        right = mid - 1
    elif count >= c:
        left = mid + 1
        result = max(result, mid)

print(result)