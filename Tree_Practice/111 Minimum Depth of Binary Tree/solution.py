class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left and not root.right:
            return self.minDepth(root.left)+1
        if root.right and not root.left:
            return self.minDepth(root.right)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1