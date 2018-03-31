class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        ### exception !!
        if not nums: return None
        MAX = max(nums)
        node = TreeNode(MAX)
        left = nums[:nums.index(MAX)]
        right = nums[nums.index(MAX)+1:] ### index increments by 1
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node