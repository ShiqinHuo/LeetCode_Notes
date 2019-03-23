class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp1,dp2 = 1,1
        for i in range(1,len(s)):
            dp2 = dp1 +self.helper(s[:i+1])
            dp1 = dp2
        return dp2

    def helper(self,s):
        count = 0
        s = s[::-1]
        cur, cur_rev = "",""
        for i in range(len(s)):
            cur = s[:i+1]
            cur_rev = cur[-1]+cur_rev
            if cur == cur_rev:
                count +=1
        return count