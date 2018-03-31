class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0
        len_last_row = 2**(N-1)/2
        if K <= len_last_row: return self.kthGrammar(N-1,K)
        else: return 1 - self.kthGrammar(N-1,K-len_last_row)