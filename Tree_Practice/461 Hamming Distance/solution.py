class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        reverse_x = bin_x[::-1]
        reverse_y = bin_y[::-1]
        if len(reverse_x)>len(reverse_y):
            longer = reverse_x
            shorter = reverse_y
        else:
            longer = reverse_y
            shorter = reverse_x
        l = len(longer)
        s = len(shorter)
        for i in range(s):
            if shorter[i]!=longer[i]:
                count+=1
        for k in range(s,l):
            if longer[k]=="1":
                count+=1
        return count