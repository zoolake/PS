# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            if node.left and node.val == node.left.val:
                left_len += 1
            else:
                left_len = 0
            if node.right and node.val == node.right.val:
                right_len += 1
            else:
                right_len = 0

            self.result = max(self.result, left_len + right_len)
            return max(left_len, right_len)
        dfs(root)
        return self.result
