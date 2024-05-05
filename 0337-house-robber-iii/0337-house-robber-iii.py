# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def go(node,robbed):
            if not node:
                return 0
            if robbed:
                return go(node.left,False) + go(node.right, False)
            op1 = node.val + go(node.left,True) + go(node.right, True)
            op2 = go(node.left,robbed) + go(node.right,robbed)
            return max(op1,op2)
        
        return go(root, False)