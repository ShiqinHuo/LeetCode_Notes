
```python

class Solution(object):
    
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_perm = [] 
        global all_perm
        nums.sort()
        begin,end = 0,len(nums)
        return self.perm(nums,begin,end)
    
    def perm(self,nums,begin,end):

        if begin>=end:
            n_copy = nums[:]
            all_perm.append(n_copy)
        else:
            j = begin
            for k in range(begin,end):
                nums[k],nums[j] = nums[j], nums[k]
                self.perm(nums,begin+1,end)
                nums[k],nums[j] = nums[j], nums[k]
        return all_perm
```