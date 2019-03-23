class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = []
        for i in range(num+1):
            bin_i = bin(i)
            count = 0
            for x in bin_i:
                if x == "1":
                    count+=1
            l.append(count)
        return l