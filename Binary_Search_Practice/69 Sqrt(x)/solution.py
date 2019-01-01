class Solution:
    import math
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x<=1):
            return x
        x0 = x/2
        tol = 0.01
        while (abs(x0**2 - x)>tol):
            x0 = (x0+x/x0)/2
        return math.floor(x0) # import math