# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        self.root = root
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
    def insert(self, val: int) -> int:
        node = self.queue[0]
        self.queue.append(TreeNode(val))
        if not node.left:
            node.left = self.queue[-1]
        else:
            node.right = self.queue[-1]
            self.queue.popleft()
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()