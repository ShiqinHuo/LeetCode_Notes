# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        temp = []
        current_row = [root]
        while len(current_row)!=0 and None not in current_row:
        # and None not in current_row: BUG once!
        # [None] as an exception!
            val_row = []
            # temp.append()
            next_row = []
            for node in current_row:
                val_row.append(node.val)
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            temp.append(val_row)
            current_row = next_row
        temp.reverse()
        return temp

# reference:
# https://github.com/WuLC/LeetCode/blob/master/Algorithm/Python/513.%20Find%20Bottom%20Left%20Tree%20Value.py
# similar reasoning method