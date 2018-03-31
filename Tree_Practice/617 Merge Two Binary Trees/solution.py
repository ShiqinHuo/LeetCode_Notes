class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:  # t1 none & t2 none
            return None
        elif not t1:  # t1 none t2 true
            t = t2
            # t = TreeNode(t2.val)
            # t.left = t2.left
            # t.right = t2.right
        elif not t2:  # t1 true t2 none
            t = t1
            # t = TreeNode(t1.val)
            # # t.left = t1.left
            # # t.right = t1.right
        else:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
        return t


