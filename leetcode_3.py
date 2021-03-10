class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        max_length , pointer = 0, 0
        # 순회
        for idx, char in enumerate(s):
            # 중복검사
            if char in table and pointer<=table[char]:
                pointer = table[char] + 1
            # 최대길이갱신
            else:
                max_length = max(max_length, idx - pointer + 1)
            table[char] = idx
        return max_length