class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        y = 0
        if (n < 0):
            return 1.0/self.myPow(x,-n)

        if (n == 0):
            y = 1
        else:
            y = self.myPow(x,n//2) ##
            y = y*y
            if (n%2 != 0):
                y = x*y
        return y

        # if b == 0: return 1
        # if b < 0: return 1.0 / self.myPow(a, -b)
        # half = self.myPow(a, b // 2)
        # if b % 2 == 0:
        #     return half * half
        # else:
        #     return half * half * a