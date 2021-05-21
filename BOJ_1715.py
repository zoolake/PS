# <오답 코드>
# import heapq

# n = int(input())
# cards = []
# for _ in range(n):
#     heapq.heappush(cards, int(input()))

# if n == 1:
#     print(0)

# else:
#     prev = heapq.heappop(cards)
#     total = 0
#     while cards:
#         prev += heapq.heappop(cards)
#         total += prev

#     print(total)

# <정답 코드>
import sys, heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))


if N == 1: 
    print(0)
else:
    answer = 0
    while len(cards) > 1: 
        temp_1 = heapq.heappop(cards) 
        temp_2 = heapq.heappop(cards) 
        answer += temp_1 + temp_2
        heapq.heappush(cards, temp_1 + temp_2)
    
    print(answer)

# 간과한 부분: 
# 이전 비교 연산 횟수가 앞으로 해야 할 비교 연산보다 큰 경우가 있을 수도 있기 때문에
# 이전 비교 연산 횟수를 따로 변수에 받는게 아닌 우선순위 큐에 삽입해야한다.
# 예로, ( n=4 / 10 45 50 51 ) 을 테스트 케이스로 돌려보면 차이를 알 수 있다.
