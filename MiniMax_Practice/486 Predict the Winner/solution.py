# http://bookshadow.com/weblog/2017/01/22/leetcode-predict-the-winner/

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = dict()
        def solve(nums):
            if len(nums) <=1: return sum(nums)
            tnums = tuple(nums) ## convert list to tuple
            if tnums in dic:
                return dic[tnums]
            dic[tnums] = max(nums[0]-solve(nums[1:]),nums[-1]-solve(nums[:-1]))
            # recursion : max of solve()
            return dic[tnums]
        return solve(nums) >= 0

    # learn by heart