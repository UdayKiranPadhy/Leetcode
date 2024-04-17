# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node,path=""):
            if not node.left and not node.right:
                return chr(node.val + ord('a')) + path
            if node.left and node.right:
                return min(dfs(node.left,chr(node.val + ord('a')) + path), dfs(node.right, chr(node.val + ord('a'))+path))
            if node.left:
                return dfs(node.left, chr(node.val + ord('a')) + path)
            else:
                return dfs(node.right, chr(node.val + ord('a')) + path)
        
        return dfs(root,"")
            