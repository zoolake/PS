# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    temp = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return TreeNode(0)
        
        self.bstToGst(root.right)
        self.temp += root.val
        root.val = self.temp
        self.bstToGst(root.left)
        
        return root