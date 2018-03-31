# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root.left is not None and root.right is not None:
            pre_l = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(pre_l)
        elif root.left is not None:
            root.right = self.invertTree(root.left)
            root.left = None
        else:
            root.left = self.invertTree(root.right)
            root.right = None
        return root

        ## misunderstanding the quetion description
        # if root.left is not None and root.right is not None:
        #     if root.left.val < root.right.val:
        #         pre_l = root.left
        #         root.left = self.invertTree(root.right)
        #         root.right = self.invertTree(pre_l)
        # elif root.left is not None:
        #     root.right = self.invertTree(root.left)
        #     root.left = None
        # else:
        #     root.left = self.invertTree(root.right)
        #     root.right = None
        # return root

