class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
    # 1. Counter를 활용한 풀이
        # counter = collections.Counter(stones)
        # result = 0
        # for jewels in jewels:
        #     result += counter[jewels]
        # return result
        
    # 2. 리스트 컴프리헨션을 활용한 풀이
        return sum(stone in jewels for stone in stones)
