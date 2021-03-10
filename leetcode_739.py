class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 인덱스를 스택에 삽입
        stack = []
        result = [0 for i in range(len(T))]
        for idx, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                top = stack.pop()
                result[top] = idx-top
            stack.append(idx)
        return result
            