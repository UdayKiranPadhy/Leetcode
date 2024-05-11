# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(node):
            if node == None: return None
            if node and (startValue == node.val or destValue == node.val):
                return node
            left = lca(node.left)
            right= lca(node.right)
            
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        
        def dfs(node,required,path):
            if not node : return False
            if node.val == required:
                return True
            path.append("L")
            if(dfs(node.left,required,path)):
                return True
            path.pop()
            
            path.append("R")
            if(dfs(node.right,required,path)):
                return True
            path.pop()
            
            return False
        common = lca(root)
        path1 = []
        dfs(common,startValue,path1)
        path2 =[]
        dfs(common,destValue,path2)
        for i in range(len(path1)):
            path1[i] = "U"
        return "".join(path1) + "".join(path2)