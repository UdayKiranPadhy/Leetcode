# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        """
        Construct an array using dfs.
        Sort it.
        Apply Binary Search
        """
        nums = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        result = []
        for query in queries:
            l = bisect_left(nums,query)
            if l < len(nums) and nums[l] == query: result.append([query,query])
            else:
                if l == len(nums): result.append([nums[-1],-1])
                elif l == 0: result.append([-1,nums[0]])
                else: result.append([nums[l-1], nums[l]])
        return result