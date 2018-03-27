class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        if len(nums1) == 0: return temp
        else:
            for i in nums1:
                if i in nums2 and i not in temp:
                    temp.append(i)
            return temp