# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            max_ = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                max_ = max(max_, node.val)
                queue.extend([node.left, node.right])
            if max_ != float('-inf'):
                res.append(max_)
        return res