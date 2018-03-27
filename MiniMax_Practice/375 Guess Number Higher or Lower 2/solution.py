import math
## http://bookshadow.com/weblog/2016/07/16/leetcode-guess-number-higher-or-lower-ii/
## https://discuss.leetcode.com/topic/51356/two-python-solutions
class Solution(object):
    # s = 0
    # global s
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])
                                   for x in range(lo, hi))
        return dp[1][n]



    #     return self.recursive_pay(1, n, 0)
    #
    # def recursive_pay(self, left, right, s):
    #
    #     mid = math.floor((left + right) / 2)  ## add floor!
    #     mid2 = math.ceil((left + right) / 2)  ##
    #     # for evens:
    #     # mid1 != mid2
    #     if (mid != mid2):
    #         if (right - left) == 2 or (right - left) == 1:
    #             s += mid
    #             return int(s)
    #         elif (right == left):
    #             return int(s)
    #         else:
    #             pass ##### minimax！！！  dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])
    #
    #     # for odds:
    #     # mid1 == mid2
    #     if (mid == mid2):
    #         if (right - left) == 2 or (right - left) == 1:
    #             s += mid
    #             return int(s)
    #
    #         elif (right == left):
    #             return int(s)
    #         else:
    #             s += mid
    #             left = mid + 1
    #             return self.recursive_pay(left, right, s)