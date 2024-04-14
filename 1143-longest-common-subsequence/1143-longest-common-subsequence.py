class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def LCS(string1,string2,m,n):
            if m == 0:
                return 0
            elif n == 0:
                return 0
            elif string1[m-1] == string2[n-1]:
                return 1 + LCS(string1,string2,m-1,n-1)
            else:
                return max(LCS(string1,string2,m-1,n),LCS(string1,string2,m,n-1))
        
        return LCS(text1,text2,len(text1),len(text2))