import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. 재귀
# class Solution:
#     result = sys.maxsize
#     prev = -sys.maxsize
#     def minDiffInBST(self, root: TreeNode) -> int:
#         if not root:
#             return

#         self.minDiffInBST(root.left)
#         self.result = min(self.result, abs(root.val - self.prev))
#         self.prev = root.val
#         self.minDiffInBST(root.right)

#         return self.result

# 2. 반복(스택)
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        result = sys.maxsize
        prev = -sys.maxsize
        node = root

        while stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            result = min(result, abs(node.val-prev))
            prev = node.val

            node = node.right
        
        return result


        