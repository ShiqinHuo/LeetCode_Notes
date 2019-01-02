class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue: # cur level
            level = []
            nextQ = []
            for node in queue: # cur level traversal
                level.append(node.val) # current level appended
                if node.left: # if l branch not null, next level append
                    nextQ.append(node.left)
                if node.right: # if r branch not null, next level append
                    nextQ.append(node.right)
            queue = nextQ # switch to the next level
            res.append(level) # nested list returned
        return res