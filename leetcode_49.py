class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary 이용, strs의 각 요소를 정렬해서 그 값을 키로 삽입
        anagram = collections.defaultdict(list)

        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        
        return anagram.values()