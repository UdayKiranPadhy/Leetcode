class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [[root, -1]]
        seen = set()
        while q:
            new_leaves = []
            total = 0
            for node, parent in q:
                if node.left: new_leaves.append([node.left, node])
                if node.right: new_leaves.append([node.right, node])
                total += node.val
            for node, parent in q:
                if parent in seen:
                    continue
                if parent == -1:
                    node.val = 0
                    continue
                l = r = 0
                if parent.left:
                    l = parent.left.val
                if parent.right:
                    r = parent.right.val
                if parent.left:
                    parent.left.val = total - l -r
                if parent.right:
                    parent.right.val = total - l -r
                seen.add(parent)
            q = new_leaves
        return root