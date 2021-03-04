class Solution:
    def longestPalindrome(self, s: str) -> str:
        # palidrome 판별 (투 포인터 이용)
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 슬라이딩 윈도우
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result
