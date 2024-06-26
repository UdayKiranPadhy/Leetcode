# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def constructBST(arr,start,end):
            if start > end :
                return None
            mid = (start + end) //2
            
            root = TreeNode(arr[mid],constructBST(arr,start,mid-1),constructBST(arr,mid+1,end))
            
            return root
        
        return constructBST(arr,0,len(arr)-1)