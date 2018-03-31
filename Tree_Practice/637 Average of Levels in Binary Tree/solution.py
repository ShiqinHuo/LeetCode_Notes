class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        average = []
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
            average.append(sum(val_row) / len(val_row))
            current_row = next_row
        return average
