# 1. 행의 맨끝에서부터 탐색
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

#         if not matrix:
#             return False

#         row, col = 0, len(matrix[0]) - 1

#         while row < len(matrix) and col >= 0:
#             if target == matrix[row][col]:
#                 return True
#             elif target < matrix[row][col]:
#                 col -= 1
#             else:
#                 row += 1

#         return False
# 2. any 이용
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)