import math
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x0 = num/2
        tol = 0.0000001
        while (abs(x0**2-num)>0.01):
            x0 = (x0+num/x0)/2

        return math.floor(x0)**2 == num*1.0
