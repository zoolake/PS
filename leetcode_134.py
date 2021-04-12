import collections
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]:
                start = i + 1           # 성립되지 않는 지점이 있다면 그 이전은 모두 출발점이 될 수 없음을 이용
                fuel = 0
            
            else:
                fuel += gas[i] - cost[i]

        return start


        
