class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if L>root.val:
            return self.trimBST(root.right,L,R)
        elif R<root.val:
            return self.trimBST(root.left,L,R)
        else:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
            return root