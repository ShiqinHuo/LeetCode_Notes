class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left: # left not None
            if root.left.val == root.val: # left == root
                if not root.right: # right None -> check leftTree
                    return self.isUnivalTree(root.left)
                elif root.val == root.right.val: # right not None -> both check
                    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
                else:
                    return False
            else: # left != root -> False
                return False
        else: # left None
            if not root.right: # right None
                return True
            elif root.val == root.right.val: # right == root -> check rightTree
                return self.isUnivalTree(root.right)
            else:
                return False