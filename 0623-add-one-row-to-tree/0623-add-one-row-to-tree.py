# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1:
            return TreeNode(val,root)
        def dfs(node,height):
            if height == depth-1:
                left = node.left
                right= node.right
                node.left = TreeNode(val,left)
                node.right = TreeNode(val,None,right)
                return
            if node.left:
                dfs(node.left,height + 1)
            if node.right:
                dfs(node.right, height + 1)
        dfs(root,1)
        return root