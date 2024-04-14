# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def dfs(root,left):
            if root == None:
                return
            if root.left == None and root.right == None:
                if left:
                    nonlocal total
                    total += root.val
                    return
            dfs(root.left,True)
            dfs(root.right,False)
        dfs(root,False)
        return total