import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()

        if not s:
            return 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_char = counts.most_common(1)[0][1]  ## 가장 많이 나온 문자의 개수
            
            if (right - left + 1) - max_char > k:
                counts[s[left]] -= 1
                left += 1

        return right - left + 1
