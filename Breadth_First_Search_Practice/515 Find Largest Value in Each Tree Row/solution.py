# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        largest = []
        current_row = [root]
        while len(current_row) != 0 and None not in current_row:
            next_row = []
            val_row = []
            for node in current_row:
                val_row.append(node.val)
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            largest.append(max(val_row))
            current_row = next_row
        return  largest
