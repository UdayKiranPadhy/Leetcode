# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        result = []
        def dfs(node):
            if node == None:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
            return node
        
        dfs(root)
        
        if root.val not in to_delete:
            result.append(root)

        return result