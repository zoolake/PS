class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for e in s:
            if len(stack) == 0 or e not in mapping:
                stack.append(e)
            else:
                if mapping[e] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    stack.append(e)

        return not len(stack)