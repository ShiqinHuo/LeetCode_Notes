```python
# solution 2:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        p = reduce((lambda x, y: x * y), nums)
        for i in nums:
            if (i != 0): temp.append(int(p/i))
            else:
                l = nums[:]
                l.remove(i)
                k = reduce((lambda x, y: x * y),l)
                temp.append(k)
        return temp
        
## TIME LIMIT EXCEEDED

        # temp = []
        # for i in nums:
        #     l = nums[:]
        #     l.remove(i)
        #     p = reduce((lambda x, y: x * y), l)
        #     temp.append(p)
        # return temp
        #            

```

