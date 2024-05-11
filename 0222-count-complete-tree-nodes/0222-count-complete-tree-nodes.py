class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        l = self.leftHeight(root.left)
        r = self.rightHeight(root.right)
        
        if l ==r:
            return (2**(l+1)) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
    def leftHeight(self,node):
        if not node:
            return 0
        return 1 + self.leftHeight(node.left)

    def rightHeight(self,node):
        if not node:
            return 0
        return 1 + self.rightHeight(node.right)