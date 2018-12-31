class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        no_0 = list(filter(lambda x: x != 0,nums))
        for i in nums:
            if i == 0:
                no_0.append(i)
        nums[:] = no_0