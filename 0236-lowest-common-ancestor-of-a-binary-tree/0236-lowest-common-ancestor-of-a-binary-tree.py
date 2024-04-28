

class Solution:
    def findnode(root, p, array1):
        if root == None:
            return False
        if root.val == p.val:
            array1.append(root)
            return True
        if Solution.findnode(root.left, p, array1):
            array1.append(root)
            return True
        if Solution.findnode(root.right,p,array1):
            array1.append(root)
            return True

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        array1 = []
        Solution.findnode(root, p, array1)
        array1.reverse()
        array2 = []
        Solution.findnode(root,q,array2)
        array2.reverse()
        for i in range(1,len(array1) if len(array1) < len(array2) else len(array2)):
            if array1[i].val == array2[i].val:
                continue
            else:
                return array1[i-1]
        return array1[-1] if len(array1) < len(array2) else array2[-1]
        