class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        # 함수 작성
        def cal(left, right, op) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result

        if expression.isdigit():
            return [int(expression)]

        results = []
        # expression 순회
        for index, value in enumerate(expression):
            if value in "*+-":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                results.extend(cal(left,right,value))

        return results
