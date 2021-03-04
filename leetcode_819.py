import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ## paragraph에서 구두점 공백 처리, 소문자화 후 공백 기준 리스트화
        words = [word for word in re.sub('[^\w]',' ',paragraph)
            .lower().split()
                if word not in banned]
        
        counter = collections.defaultdict(int)  ## 일반 dict로 하면 초기 key값이 존재하지 않아서 에러 발생한다.
        for word in words:
            counter[word] += 1
        
        return max(counter.keys(), key=(lambda x: counter[x]))