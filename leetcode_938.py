# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:       
        def dfs(node: TreeNode):
            if not node:
                return
            
            if low <= node.val <= high:
                self.result += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)

            

        dfs(root)
        return self.result

