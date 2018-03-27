import math

class Solution(object):
    # s = 0
    # global s
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.recursive_pay(1, n, 0)

    def recursive_pay(self, left, right, s):

        mid = math.floor((left + right) / 2)  ## add floor!
        mid2 = math.ceil((left + right) / 2)  ##
        # for evens:
        # mid1 != mid2
        if (mid != mid2):
            if (right - left) == 2 or (right - left) == 1:
                s += mid
                return int(s)
            elif (right == left):
                return int(s)
            else:
                pass ##### minimax！！！

        # for odds:
        # mid1 == mid2
        if (mid == mid2):
            if (right - left) == 2 or (right - left) == 1:
                s += mid
                return int(s)

            elif (right == left):
                return int(s)
            else:
                s += mid
                left = mid + 1
                return self.recursive_pay(left, right, s)