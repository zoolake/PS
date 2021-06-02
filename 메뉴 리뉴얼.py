# 내 풀이
# from itertools import combinations
# from collections import defaultdict
# def solution(orders, course):
#     answer = []
#     table = defaultdict(int)
#     for order in orders:
#         for i in course:
#             combi = combinations(order,i)
#             for temp in combi:
#                 table[''.join(sorted(temp))] += 1

#     len_count = [0]*11
#     candidates_list = [[] for _ in range(12)]
#     for menu, count in table.items():
#         if count >= 2 and count >= len_count[len(menu)]:
#             if count > len_count[len(menu)]:
#                 candidates_list[len(menu)] = []
#                 len_count[len(menu)] = count
#             candidates_list[len(menu)].append(menu)
    
#     for candidates in candidates_list:
#         for candidate in candidates:
#             answer.append(candidate)

#     answer.sort()
#     return answer

# 참고할 만한 좋은 풀이 (Counter, most_common 사용)
from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v >= 2 and v == most_ordered[0][1] ]
    return [ ''.join(v) for v in sorted(result) ]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])