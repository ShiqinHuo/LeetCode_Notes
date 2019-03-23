class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []

        ## forward
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]

        ## backword
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


#         temp = []
#         p = reduce((lambda x, y: x * y), nums)
#         for i in nums:
#             if (i != 0): temp.append(int(p/i))
#             else:
#                 l = nums[:]
#                 l.remove(i)
#                 k = reduce((lambda x, y: x * y),l)
#                 temp.append(k)
#         return temp

# TIME LIMIT EXCEEDED

        # temp = []
        # for i in nums:
        #     l = nums[:]
        #     l.remove(i)
        #     p = reduce((lambda x, y: x * y), l)
        #     temp.append(p)
        # return temp
        #