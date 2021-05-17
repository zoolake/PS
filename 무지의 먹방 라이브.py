import heapq
def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    time = 0 
    previous = 0
    length = len(food_times)

    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    
    while time + ((q[0][0] - previous) * length) <= k:
        food_time = heapq.heappop(q)[0]
        time += (food_time - previous) * length
        length -= 1
        previous = food_time

    result = sorted(q, key= lambda x: x[1])
    return result[(k-time) % length][1]