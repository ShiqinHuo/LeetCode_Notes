```python

# output = heapq.nlargest(k, d.iteritems(), operator.itemgetter(1))

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        temp = []
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        output = heapq.nlargest(k, d.iteritems(), operator.itemgetter(1))
        for k,v in output:
            temp.append(k)
        return temp
```