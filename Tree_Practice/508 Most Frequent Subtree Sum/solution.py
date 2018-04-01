# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
import copy


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sumValue(root)  ## add it here to modify the value
        current = [root]
        val_all = []
        while len(current) != 0 and None not in current:
            next_row = []
            for node in current:
                # node.val = self.sumValue(node)
                val_all.append(node.val)
                if node.left is not None:
                    next_row.append(node.left)
                if node.right is not None:
                    next_row.append(node.right)
            current = next_row
        # items, nums = Counter(val_all).most_common(1)
        # return Counter(val_all).most_common()
        count = {}
        for i in val_all:
            count[i] = count.get(i, 0) + 1
        v = list(count.values())  # return k[v.index(max(v))]
        return [k for k in count if count[k] == max(v)]

    def sumValue(self, node):
        if not node: return 0
        # if node.left is not None and node.right is not None:
        #     node.val = node.val + self.sumValue(node.left) + self.sumValue(node.right)
        # node = copy.copy(root)  ## timeout!!!
        if node.left is not None:
            node.val = node.val + self.sumValue(node.left)
        if node.right is not None:
            node.val = node.val + self.sumValue(node.right)
        return node.val
# https://www.jianshu.com/p/c861361dc20f
