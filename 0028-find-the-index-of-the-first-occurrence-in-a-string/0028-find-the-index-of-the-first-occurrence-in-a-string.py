class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def buildLPS(needle:str) -> List:
            N = len(needle)
            lps = [0] * N
            j = 0
            for i in range(1,N):
                while needle[i]!=needle[j] and j > 0:
                    j = lps[j-1]
                if needle[i] == needle[j]:
                    j+=1
                    lps[i]= j
            return lps
        
        lps = buildLPS(needle)
        i = j = 0
        N, M = len(haystack), len(needle)
        while i < N:
            while haystack[i] != needle[j] and j > 0:
                j = lps[j-1]
            if haystack[i] == needle[j]:
                j += 1
                if j == M:
                    return i - M + 1
            i += 1
        return -1