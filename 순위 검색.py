from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, queries):
    answer = []

    # infos 읽어서 추출
    table = defaultdict(list)
    for info in infos:
        info_list = info.split()
        key, value = info_list[:-1], int(info_list[-1])
        # 조합 생성후 딕셔너리에 저장
        for i in range(5):
            for combi in combinations(key,i):
                new_key = ''.join(combi)
                table[new_key].append(value)
    
    # binary_search를 해야하므로, value 오름차순 정렬
    for v in table.values():
        v.sort()
    
    # queries를 읽어서 형식 변형하기
    for query in queries:
        for ch in ['-','and']:
            query = query.replace(ch,'')
        query = query.split()
        query_key, query_value = ''.join(query[:-1]), int(query[-1])
        
        # binary_search
        if query_key in table:
        # 풀이 1) bisect 사용
            # index = bisect_left(table[query_key], query_value)
            # answer.append(len(table[query_key]) - index)
        # 풀이 2) binary_search 구현
            value_list = table[query_key]
            left = 0
            right = len(value_list) - 1
            while left <= right:
                mid = (left+right)//2
                if value_list[mid] >= query_value:
                    right = mid - 1
                else:
                    left = mid + 1
            answer.append(len(value_list) - left)
        else:
            answer.append(0)
    
    return answer