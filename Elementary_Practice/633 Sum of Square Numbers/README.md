```python
class Solution:
    import math
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, math.floor(math.sqrt(c))
        # cur = left**2 + right**2
        while (left<=right):
            cur = left**2 + right**2
            if cur < c:
                left+=1
            elif cur > c:
                right-=1
            else:
                return True
        return False
```