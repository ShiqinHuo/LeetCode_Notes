# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(mid):
    pass



class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Binary Search:
        # left,right = 1,n
        # while True:
        #     mid = (left + right)/2
        #     if guess(mid) == 0:
        #         return mid
        #     if guess(mid) == -1:
        #         right = mid - 1
        #     if guess(mid) == 1:
        #         left = mid + 1

        # Recursion:
        return self.recursive_guess(1, n)

    def recursive_guess(self,bottom, up):
        mid = (up + bottom)/2
        if guess(mid) == 0: return  mid
        elif guess(mid)==-1:
            return self.recursive_guess(bottom,mid-1)
        else:
            return self.recursive_guess(mid+1,up)
