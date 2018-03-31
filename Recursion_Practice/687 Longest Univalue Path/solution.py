class Solution:
    def recursion(self, node):
        if node == None: return 0
        l = self.recursion(node.left) if node.left != None else -1
        r = self.recursion(node.right) if node.right != None else -1
        pl = l + 1 if l >= 0 and node.val == node.left.val else 0
        pr = r + 1 if r >= 0 and node.val == node.right.val else 0
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        Max = self.recursion(root)
        return self.ans
